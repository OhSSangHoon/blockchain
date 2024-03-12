import string

# Auto Key 암호화
def autokey_cipher(plain_text, key):
    # A=00, B=01, ..., Z=25로 매핑
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = {char: str(i).zfill(2) for i, char in enumerate(alphabet)}
    reverse_mapping = {v: k for k, v in mapping.items()}

    # P's value 계산
    p_values = [mapping[char] for char in plain_text.upper()]

    # Key stream 계산
    key_stream = [str(key).zfill(2)] + p_values[:-1]

    # C's value 계산
    c_values = [(int(p) + int(k)) % 26 for p, k in zip(p_values, key_stream)]
    c_values = [str(c).zfill(2) for c in c_values]

    # 암호문 생성
    cipher_text = ''.join([reverse_mapping[c] for c in c_values])

    return cipher_text


# 비즈네르 암호화
def vigenere_cipher(plain_text, key):
    cipher_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plain_text_int = [ord(i) for i in plain_text]

    for i in range(len(plain_text_int)):
        value = (plain_text_int[i] + key_as_int[i % key_length]) % 26
        cipher_text += chr(value + 65)
    return cipher_text


plain_text = input("평문 입력: ").replace(" ", "").upper()
key = input("암호? ").upper()

if key.isdigit():
    cipher_text = autokey_cipher(plain_text, int(key))
else:
    cipher_text = vigenere_cipher(plain_text, key)

print("암호문: ", cipher_text)
print("평문: ", plain_text)
