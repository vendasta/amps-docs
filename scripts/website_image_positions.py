# Image positions for Website Support doc
import re, os
base = os.path.join(os.path.dirname(__file__), '..', 'website-support-extract', 'word')
with open(os.path.join(base, '_rels', 'document.xml.rels'), 'r', encoding='utf-8') as f:
    rels = f.read()
rid_to_image = {}
for m in re.finditer(r'Id="(rId\d+)"[^>]*Target="media/(image\d+\.png)"', rels):
    rid_to_image[m.group(1)] = m.group(2).replace('.png', '')
with open(os.path.join(base, 'document.xml'), 'r', encoding='utf-8') as f:
    doc = f.read()
pattern = re.compile(r'<w:p[^>]*>(.*?)</w:p>', re.DOTALL)
blip_pattern = re.compile(r'embed="(rId\d+)"')
text_pattern = re.compile(r'<w:t[^>]*>([^<]*)</w:t>')
results = []
for i, p_match in enumerate(pattern.finditer(doc)):
    para = p_match.group(1)
    texts = text_pattern.findall(para)
    text = ' '.join(texts).strip().replace('\n', ' ')[:100]
    blips = blip_pattern.findall(para)
    for rid in blips:
        if rid in rid_to_image:
            results.append((rid_to_image[rid], text))
for idx, (img, text) in enumerate(results):
    print(str(idx+1) + '. ' + img + ' | ' + repr(text[:70]))
