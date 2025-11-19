# Unit test cu pytest

import os

def test_model_exists():
    assert os.path.exists("model_build/model.bin")

def test_model_size():
    size = os.path.getsize("model_build/model.bin")
    assert size > 0

