# Calculăm hash-urile și le punem în manifest
#lucrul cu dicționare nested, hashing real folosit în firmware release pipelines, generare manifest real (folosit în OTA, CI/CD, deployment)

import json
import hashlib

#1. Citim binarul
with open("model_build/model.bin", "rb") as f:
    data = f.read()

#2. Calculam hash-uri
md5 = hashlib.md5(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()

#3. Construim manifestul complet

manifest = {
    "file": "model.bin",
    "size": len(data),
    "hashes": {
        "md5":md5,
        "sha256": sha256
    }
}

#4. Scriem JSON-ul
with open("manifest_full.json", "w") as f:
    json.dump(manifest, f, indent=4)

print(":Manifest complet generat")
