# 출력화면
# 첫번째 실수를 입력하세요: 1.23
# 두번째 실수를 입력하세요: 2.34
# 두 값을 더한다:
# 1.23 + 2.34의 합은 3.57입니다.
#외부상수 출력방식으로 출력

#2. 10-99 사이의 두 자리 정수를 입력받아 십의자리와 일의 자리로 분리하여 출력하는 프로그램
#십의자리와(//) 일의자리(%)로 분리하여 출력하는 프로그램
#출력화면
#10-99 사이의 정수 입력: 45
#십의 자리:4
#일의 자리:5
#%연산자를 이용한 출력

#사용자로부터 2개의 실수를 입력받아 합계를 구하는 프로그램 구현

#1. 실습
num1 = float(input("첫번째 실수를 입력하세요 : "))
num2 = float(input("두번째 실수를 입력하세요 : "))
result=num1+num2
print("첫번째 실수 {}와 두번째 실수 {} 합은 {} 이다".format(num1, num2, result))

#2. 실습
num3=int(input("10-99 사이의 정수를 입력하세요: "))
tens=num3 // 10
units=num3 % 10
print("십의자리:%d" %tens)
print("일의자리:%d" %units)

print("십의자리:%d, 일의자리:%d" %(tens, units))