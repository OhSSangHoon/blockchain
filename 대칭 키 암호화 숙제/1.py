import random
import string

# 알파벳 리스트 생성
alphabet = list(string.ascii_lowercase)

# 알파벳을 무작위로 섞은 리스트 생성
shuffled_alphabet = alphabet.copy()
random.shuffle(shuffled_alphabet)

# 암호화 딕셔너리 생성
E = dict(zip(alphabet, shuffled_alphabet))

# 복호화 딕셔너리 생성
D = dict(zip(shuffled_alphabet, alphabet))

def encrypt(message):
    return ''.join(E.get(char, char) for char in message)

def decrypt(message):
    return ''.join(D.get(char, char) for char in message)

# 평문 입력
plain_text = input("평문을 입력하세요: ")
# 암호문 생성
cipher_text = encrypt(plain_text)
print("암호문: ", cipher_text)
# 복호문 생성
decipher_text = decrypt(cipher_text)
print("복호문: ", decipher_text)
