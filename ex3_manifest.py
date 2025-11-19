# Citește dimensiunea unui fișier binar și o salveaza în manifest.json

import json
import os
# 1. citim binarul modelului

with open("model_build/model.bin", "rb") as f:
    data = f.read()

size = len(data)

manifest = {
    "file": "model.bin",
    "size": size
}

with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=4)

print("manifest.json generated") 
