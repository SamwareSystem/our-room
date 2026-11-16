#!/usr/bin/env python3
"""Escanea musica/ y escribe musica/lista.js con los archivos de audio."""
import json, pathlib
d = pathlib.Path(__file__).parent / "musica"
ext = {".mp3", ".m4a", ".ogg", ".wav", ".aac", ".opus"}
f = sorted(p.name for p in d.iterdir() if p.suffix.lower() in ext)
(d / "lista.js").write_text("window.CANCIONES = " + json.dumps(f, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
print(f"{len(f)} canciones registradas")
