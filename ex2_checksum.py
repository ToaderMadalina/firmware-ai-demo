# Generare checksum → util pentru CI/CD și semnare artefacte

import hashlib

file_path = "model_build/model.bin"

with open(file_path, "rb") as f:
    data = f.read()

checksum_md5 = hashlib.md5(data).hexdigest()
checksum_sha256 = hashlib.sha256(data).hexdigest()

print(f"MD5: {checksum_md5}")
print(f"SHA256: {checksum_sha256}")

