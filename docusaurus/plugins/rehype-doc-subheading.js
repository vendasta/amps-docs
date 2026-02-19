/**
 * Rehype plugin: add class "doc-subheading" to paragraphs that are only a label ending with ":".
 * Used to style subheadings like "Review Process:", "Key Points:", "Sales Leaders' Requests:" in light green.
 */
function rehypeDocSubheading() {
  return (tree) => {
    visit(tree);
  };

  function getTextContent(node) {
    if (!node) return "";
    if (node.type === "text" && typeof node.value === "string") return node.value;
    if (node.children && Array.isArray(node.children)) {
      return node.children.map(getTextContent).join("");
    }
    return "";
  }

  function visit(node) {
    if (!node) return;
    if (node.type === "element" && node.tagName === "p" && node.children?.length >= 1) {
      const text = getTextContent(node).trim();
      if (text.length > 0 && text.endsWith(":")) {
        node.properties = node.properties || {};
        const cn = node.properties.className;
        const arr = Array.isArray(cn) ? cn : cn ? [cn] : [];
        if (!arr.includes("doc-subheading")) arr.push("doc-subheading");
        node.properties.className = arr;
      }
    }
    if (node.children && Array.isArray(node.children)) {
      for (const child of node.children) visit(child);
    }
  }
}

module.exports = rehypeDocSubheading;
