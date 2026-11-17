"""Genera dist/Carte_remerciement_partenaires_v12_interactive.html: UN solo archivo
con fuentes e imágenes incrustadas (el que se adjunta al correo).   Uso:  python3 build.py"""
import base64, re, pathlib
root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
def inline(m):
    p = root / m.group(2)
    mime = {"woff2": "font/woff2", "png": "image/png"}[p.suffix[1:]]
    return m.group(1) + f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode() + m.group(3)
html = re.sub(r'(url\(|src=")((?:fonts|img)/[^)"]+)(\)|")', inline, html)
out = root / "dist" / "Carte_remerciement_partenaires_v12_interactive.html"
out.write_text(html, encoding="utf-8"); print(out.name, len(html) // 1024, "KB")
