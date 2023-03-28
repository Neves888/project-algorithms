from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("message", "key")
    assert encrypt_message("abcdef", 3) == "cba_fed"
    assert encrypt_message("cerveja", 8) == "ajevrec"
