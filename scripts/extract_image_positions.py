# Extract image positions from Word document.xml - for each image, get the preceding paragraph text
import re
import sys
import os

doc_path = os.path.join(os.path.dirname(__file__), '..', 'listings-src-extract', 'word', 'document.xml')
rels_path = os.path.join(os.path.dirname(__file__), '..', 'listings-src-extract', 'word', '_rels', 'document.xml.rels')

with open(rels_path, 'r', encoding='utf-8') as f:
    rels = f.read()
# rId8 -> image16.png etc (only image type)
rid_to_image = {}
for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="media/(image\d+\.png)"', rels):
    rid_to_image[m.group(1)] = m.group(2).replace('.png', '')  # image16

with open(doc_path, 'r', encoding='utf-8') as f:
    doc = f.read()

# Split by <w:p (paragraph start) - get each paragraph as a chunk
# We need to find all blip/embed to get rId in document order, and for each get preceding text
# In Word XML: <w:p>...<w:r>...<w:t>text</w:t>... or <w:drawing>...<a:blip r:embed="rId8"/>
from xml.etree import ElementTree as ET
# Use regex instead - namespace issues with ET
# Find all rId that are image refs (embed) in order of appearance
pattern = re.compile(r'<w:p[^>]*>(.*?)</w:p>', re.DOTALL)
blip_pattern = re.compile(r'embed="(rId\d+)"')
text_pattern = re.compile(r'<w:t[^>]*>([^<]*)</w:t>')

results = []
for i, p_match in enumerate(pattern.finditer(doc)):
    para = p_match.group(1)
    texts = text_pattern.findall(para)
    text = ' '.join(texts).strip().replace('\n', ' ')[:120]
    blips = blip_pattern.findall(para)
    for rid in blips:
        if rid in rid_to_image:
            img = rid_to_image[rid]
            results.append((i, rid, img, text))

for i, (para_idx, rid, img, text) in enumerate(results):
    print(f"{i+1}. {img} (para ~{para_idx}) | preceding: {repr(text[:80])}")
