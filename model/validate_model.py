import os

model_file = "model_build/model.bin"

if not os.path.exists(model_file):
    print("ERROR: Model file not found!")
    exit(1)

# Simulare "inference" simplă: verificăm că fișierul nu e gol
size = os.path.getsize(model_file)
if size == 0:
    print("ERROR: Model file is empty!")
    exit(1)

# Dummy inference: calculăm checksum
checksum = sum(bytearray(open(model_file, "rb").read()))
print(f"Model validation passed. Size: {size} bytes, Checksum: {checksum}")
