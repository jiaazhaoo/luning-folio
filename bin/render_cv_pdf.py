#!/usr/bin/env python3
"""Render assets/pdf/Luning_Li_CV.pdf from _data/cv.yml with RenderCV.

_data/cv.yml also feeds the al-folio CV page, which uses a few keys
(label, summary) that RenderCV's schema rejects, so they are dropped
from a temporary copy before rendering.
"""
import pathlib
import shutil
import subprocess
import tempfile

import yaml

root = pathlib.Path(__file__).resolve().parent.parent
data = yaml.safe_load((root / "_data" / "cv.yml").read_text())
for key in ("label", "summary"):
    data["cv"].pop(key, None)
data["design"] = yaml.safe_load((root / "assets" / "rendercv" / "design.yaml").read_text())["design"]

with tempfile.TemporaryDirectory() as tmp:
    src = pathlib.Path(tmp) / "cv.yml"
    src.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False))
    pdf = pathlib.Path(tmp) / "cv.pdf"
    subprocess.run(
        ["rendercv", "render", str(src), "--pdf-path", str(pdf), "--dont-generate-markdown", "--dont-generate-html", "--dont-generate-png"],
        check=True,
        cwd=tmp,
    )
    (root / "assets" / "pdf").mkdir(parents=True, exist_ok=True)
    shutil.copy(pdf, root / "assets" / "pdf" / "Luning_Li_CV.pdf")
print("wrote assets/pdf/Luning_Li_CV.pdf")
