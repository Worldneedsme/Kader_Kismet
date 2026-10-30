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
