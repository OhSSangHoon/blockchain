#1. Dictionary E를 이용한 입력받은 문장 암호화
   - key는 영어 알파벳, value는 알파벳을 random.shuffling한 문자
   - 평문을 입력받은 다음, 알파벳을 value로 대치한 암호문 출력  
#2. Vigenere cipher와 auto key cipher
   - 영어 문장을 평문으로 입력받은 후, 2가지 방법으로 암호화/복호화
   - 단, 단어 사이의 띄어쓰기는 무시하고, 소문자는 모두 대문자로 변경
   - key값이 영어 단어이면 vigenere, 숫자이면 auto key  
#3. Fernet 라이브러리를 사용한 암호화
   - data.txt 파일을 읽어서 암호화
   - 암호화 한 문자를 encrypted.txt 파일에 저장
   - encrypted.txt 파일을 읽어서 복호화한 후 출력
