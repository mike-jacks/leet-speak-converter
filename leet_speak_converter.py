def convert(text: str) -> str:
    special_chars = {"a": "@", "A": "4", "B": "8", "b": "8", "E":"3", "e":"3", "I":"!", "i":"!", "L":"1", "l":"1", "O":"0", "o":"0", "S":"5", "s":"5"}
    converted_text = ""
    for letter in text:
        if letter in special_chars:
            converted_text += special_chars[letter]
        else:
            converted_text += letter
    return converted_text

