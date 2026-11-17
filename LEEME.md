# Carta v12 interactiva (el árbol) – Le Centre de réfugiés

- `index.html`  → el archivo que editas (CSS + HTML + JS; fuentes e imágenes enlazadas).
- `fonts/`, `img/` → Nunito 500/700/900 y logos.
- `build.py`    → `python3 build.py` crea `dist/…html`, el archivo único para enviar por correo.

## Dónde tocar (Ctrl+F)
- Textos FR/EN y firma: `const T=` (firma = `sname` y `stitle`).
- Árbol: `const FIGS=` (posición x, y, color y fila de cada una de las 44 personitas), `COLS` (paleta), `PERSON` (tamaño).
- Colores de marca: variables en `:root` al inicio del `<style>`.
- Proporción de la carta: `--ratio` en `:root`. Todo escala con `cqw` (% del ancho de la carta).
- Nieve: bloque `/* ====== flakes ====== */` en el `<script>`.

Vista previa en vivo: extensión "Live Server" (clic derecho en index.html → Open with Live Server).
