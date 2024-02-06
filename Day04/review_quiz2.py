#1 정수 분리기 프로그램
# 사용자로부터 10000부터 99999 정수를 입력받아 각자리 분리하세요.

num=input("10000부터 99999 사이의 정수를 입력하세요: ")
num1=num[0]
num2=num[1]
num3=num[2]
num4=num[3]
num5=num[4]

print(f"입력 값이 {num}이라면, 각 자리수는 {num1}만 {num2}천 {num3}백 {num4}십 {num5}")

num=input("10000부터 99999 사이의 정수를 입력하세요: ")
ten_thousands = num // 10000

thousands = (num % 10000) // 1000
hundred = (num % 1000) // 100
ten = (num % 100) // 10
one = (num % 10)

print(f"{ten_thousands}만 {thousands}천 {hundred}백 {ten}십 {원})


#2 시간 변환 프로그램(양의 정수(초단위)
time=int(input("양의 정수: "))
hour = time//3600
min = (time % 3600) // 60
sec = time % 60
print(f"{hour}시 {min}분 {sec}초")