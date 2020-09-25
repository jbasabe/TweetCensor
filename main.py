import re
import io

d = {
    'a': 'а',
    'A': 'А',
    'b': '𝖻',
    'B': 'В',
    'c': 'с',
    'C': 'С',
    'd': 'ԁ',
    'D': 'Ꭰ',
    'e': 'е',
    'E': 'Е',
    # 'f': '?',
    'F': 'ᖴ',
    'g': 'ɡ',
    'G': 'Ԍ',
    'h': 'հ',
    'H': 'Н',
    'i': 'і',
    'I': 'І',
    'j': 'ј',
    'J': 'Ј',
    # 'k': '?',
    'K': 'К',
    # 'l': '?',
    'L': 'Ꮮ',
    # 'm': '?',
    'M': 'М',
    'n': 'ո',
    'N': 'Ν',
    'o': 'о',
    'O': 'О',
    'p': 'р',
    'P': 'Р',
    # 'q': 'ԛ',
    # 'Q': 'ⵕ',
    # 'r': 'г',
    # 'R': 'ʀ',
    's': 'ѕ',
    'S': 'Ѕ',
    # 't': '?',
    'T': 'Т',
    'u': 'ᴜ',
    'U': '∪',
    'v': 'ᴠ',
    'V': 'ⴸ',
    'w': 'ᴡ',
    'W': 'Ꮃ',
    'x': 'х',
    'X': 'Х',
    'y': 'у',
    'Y': 'Ү',
    'z': 'ᴢ',
    'Z': 'Ζ'
}

with io.open("message.txt", 'r', encoding="utf8") as f:
    message = f.read()
with io.open("censored.txt", 'w', encoding="utf8") as f:
    for k in d:
        message = re.sub(k, d[k], message)
    f.write(message)