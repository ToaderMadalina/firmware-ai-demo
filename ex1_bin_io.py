# Simulam citirea si scrierea unui artefact binar

input_file = "model_build/model.bin"
output_file = "model_build/model_modified.bin"

with open(input_file, "rb") as f:
    data = bytearray(f.read())

#Exemplu de transformare : inversam fiecare byte
data = bytearray([255 -b for b in data])

with open(output_file, "wb") as f:
    f.write(data)

print(f"Modified model saved to {output_file}")
