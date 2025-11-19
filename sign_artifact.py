from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def sign_file(private_key_path, input_path, output_sig_path):
    private_key = serialization.load_pem_private_key(
        Path(private_key_path).read_bytes(),
        password=None
    )

    data = Path(input_path).read_bytes()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    Path(output_sig_path).write_bytes(signature)
    print("Signature written to", output_sig_path)

if __name__ == "__main__":
    import sys
    sign_file(sys.argv[1], sys.argv[2], sys.argv[3])
