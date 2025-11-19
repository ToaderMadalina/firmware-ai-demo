import os
import hashlib


original = "model_build/model.bin"
modified = "model_build/model_modified.bin"

def get_hash(file_path):
    with open(file_path, "rb") as fi:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def test_files_exist():
    assert os.path.exists(original), f"{original} does not exist!"
    assert os.path.exists(modified), f"{modified} does not exist!"

def test_files_size():
    size_orig = os.path.getsize(original)
    size_mod = os.path.getsize(modified)
    assert size_orig == size_mod, "Sizes should be equal for this test"

def _test_files_hash_differ():
    hash_orig = get_hash(original)
    hash_mod = get_hash(modified)
    assert hash_orig != hash_mod, "Sizes should differ after modification"

    