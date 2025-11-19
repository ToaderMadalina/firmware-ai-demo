import subprocess
import os
import sys
def run(cmd, cwd=None):
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print("Error: Command failed!")
        sys.exit(result.returncode)

def check_file(path):
    if not os.path.exists(path):
        print(f"Missing file: {path}")
        sys.exit(1)
    else:
         print(f"Found: {path}")


def main():
    print("=== FULL PIPELINE START ===")

    # build model
    print("\n=== STEP 1: Build AI model ===")
    run("python3 model/build_model.py")

    #check model is created
    check_file("model_build/model.bin")

    #modify model
    print("\n=== STEP 2:Modify model artefact ===")
    run("python3 ex1_bin_io.py")

    #check modified files exists
    check_file("model_build/model_modified.bin")

    #compute checksums
    print("\n=== STEP 3: Compute checksums ===")
    run("python3 ex2_checksum.py")

    print("\n=== STEP 4: Sign artefacts ===")

    # Creăm folderul signed dacă nu există
    run("mkdir -p signed")

    # Semnăm model.bin
    run("python3 sign_artifact.py keys/private_key.pem model_build/model.bin signed/model.bin.sig")

    # Semnăm main.bin (firmware)
    run("python3 sign_artifact.py keys/private_key.pem build/main.bin signed/main.bin.sig")

    print("\n=== STEP 5: Verify signatures ===")

    # Verificăm model.bin
    run("python3 verify_signature.py keys/public_key.pem model_build/model.bin signed/model.bin.sig")

    # Verificăm main.bin
    run("python3 verify_signature.py keys/public_key.pem build/main.bin signed/main.bin.sig")

    #run tests
    print("\n=== STEP 6: Run automates tests ===")
    run("pytest -q")

    print("\n=== PIPELINE CREATED SUCCESSFULLY ===")
    print("All artefcts generated, validated and tests passed!")

if __name__ == "__main__":
    main()