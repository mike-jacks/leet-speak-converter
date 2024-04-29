from leet_speak_converter import convert


def test_convert():
    assert convert("a") == "@"
    assert convert("a") != "a"
    assert convert("A") == "4"
    assert convert("aABbEeIiLlOoSs") == "@48833!!110055"
    assert convert("leet speak") == "133t 5p3@k"

