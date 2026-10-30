"""index.html parçasını tek başına açılabilen tam bir HTML belgesine sarar.

Kullanım: python3 demo/build_standalone.py  ->  demo/kader-kismet.html
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")

head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]
head = head.replace('<meta charset="utf-8">\n', "", 1)

out = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Kader & Kısmet: Alanya'da bir yaz villasında geçen flört ve eleme oyunu.">
<meta name="theme-color" content="#0C0C0E">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 fill=%27%230C0C0E%27/%3E%3Ctext x=%2716%27 y=%2723%27 font-size=%2720%27 text-anchor=%27middle%27 fill=%27%23FF2E7E%27 font-family=%27Arial%27 font-weight=%27bold%27%3E%26amp;%3C/text%3E%3C/svg%3E">
<style>html, body {{ margin: 0; }} body {{ font-size: 14px; }}</style>
{head}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(here / "kader-kismet.html").write_text(out, encoding="utf-8")
print("yazıldı:", here / "kader-kismet.html")
