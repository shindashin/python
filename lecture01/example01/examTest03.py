#연습문제3: 두자리정수(10-99)를 입력받아 십의자리와 일의자리로 분리하여 출력하는 프로그램
number=int(input('10-99 사이의 정수: ' ))
tens = number // 10
units = number % 10
print(tens)
print(units)
print('십의자리는',tens, '일의자리는', units, '입니다.')

