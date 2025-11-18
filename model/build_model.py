import os

# Folder output
output_dir = "model_build"
os.makedirs(output_dir, exist_ok=True)

# Simulare generare model AI
model_path = os.path.join(output_dir, "model.bin")
with open(model_path, "wb") as f:
    f.write(os.urandom(1024))  # 1KB dummy model

# Metadata
meta_path = os.path.join(output_dir, "model_metadata.txt")
with open(meta_path, "w") as f:
    f.write("model_name: demo_model\n")
    f.write("version: 1.0.0\n")
    f.write("size: 1024 bytes\n")

print(f"Model artefact generated: {model_path}")
print(f"Metadata generated: {meta_path}")
