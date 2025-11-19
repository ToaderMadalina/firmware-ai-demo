# manifest “release-ready”, cu versiune și momentul generării 

import json
import hashlib
import argparse
from datetime import datetime, timezone

# 1. CLI arguments

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
parser.add_argument("--version", required=True)
args = parser.parse_args()

#2. Citim binarul

with open(args.file, "rb") as f:
    data = f.read()

#3. calculam hash-uri
md5 = hashlib.md5(data).hexdigest()
sha256 = hashlib.sha256(data).hexdigest()

# 4.Construim manifest

manifest = {
    "file": args.file,
    "size": len(data),
    "hashes": {
        "md5": md5,
        "sha256": sha256
    },
    "version": args.version,
    "timestamp": datetime.now(timezone.utc).isoformat(),
}


# 5.Scriem manifest
output_file = "manifest_release.json"
with open(output_file, "w") as f:
    json.dump(manifest, f, indent=4)

print(f"Manifest {output_file} generat cu succes!")
