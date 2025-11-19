from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

def verify_file(public_key_path, input_path, sig_path):
    public_key = serialization.load_pem_public_key(
        Path(public_key_path).read_bytes()
    )

    data = Path(input_path).read_bytes()
    signature = Path(sig_path).read_bytes()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

if __name__ == "__main__":
    import sys
    ok = verify_file(sys.argv[1], sys.argv[2], sys.argv[3])
    if ok:
        print("✔ VERIFIED: signature is valid")
    else:
        print("✘ VERIFICATION FAILED")
