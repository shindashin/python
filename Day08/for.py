#제어문 안에서 조건문[if,elif,else], 반복문[for]
import random

for x in range(10): #0-9까지의 수
    print(x)
print("끝")

#0부터 10까지의 누적 총합을 구하기
a = 0
for x in range(11):
    print(x)
    a += x
print(a)

#0부터 100까지 짝수만 출력하기
for i in range(101):
    if i % 2 == 0:
        print(i)

#3. 유저에게 n을 입력받고
#n단을 보여주기 ex) 5-> 5*0=0 // 5*1=5 // 5*2=10//5*3=15 ...
number=int(input("n을 입력하세요:"))
for i in range(10):
    print(f"{number}*{i}={number*i}")

for x in range(1,10): #1부터 9까지
    print(x)

for x in range(1,10,2): #2번씩 점프하라는 뜻
    print(x)

#1. 로또 리스트 만들기 for문 사용해서
import random
lotto=[]
for i in range(6):
    lotto.append(random.randint(1,46))
lotto.sort()
print(lotto)

#2. 점메추 프로그램
# 점심메뉴를 7개 입력받아서 하나 랜덤으로 출력하는 프로그램[for 이용]
lunch=[]
for x in range(7):
    menu = input("점심 입력:")
    lunch.append(menu)
print(f"오늘의 점심:{random.choice(lunch)}")

#3. 3의 배수인 리스트 [0-99]
num=[]
for i in range(0, 100):
    if i % 3 == 0:
      num.append(i)
print(num)