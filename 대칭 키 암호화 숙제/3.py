from cryptography.fernet import Fernet

# 키 생성
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# data.txt 파일 읽기
with open('data.txt', 'rb') as file:
    data = file.read()

# 데이터 암호화
cipher_text = cipher_suite.encrypt(data)

# 암호화된 데이터를 encrypted.txt 파일에 저장
with open('encrypted.txt', 'wb') as file:
    file.write(cipher_text)

# encrypted.txt 파일 읽기
with open('encrypted.txt', 'rb') as file:
    encrypted_data = file.read()

# 데이터 복호화
plain_text = cipher_suite.decrypt(encrypted_data)

# 복호화된 데이터 출력
print(plain_text.decode())
