def add(x,y):
    return x + y

c = add(10,20)
print(c)

def subtraction(x,y):
    return x - y

def multiply(x,y):
    return x*y

d=subtraction(20,10)
print(d)
e=multiply(20,10)
print(e)

# 토마토를 만들어주는 함수
def makeTomato():
    return '🍅'

# x의 정수에 따라서 홀수 짝수 문자열을 돌려주는 함수
def sniffling(x):
    if x % 2 == 0:
        return '짝수'
    elif x % 2 == 1:
        return '홀수'

#n개가 들어오면 n개가 담긴 밭 리스트 돌려주기
n=int(input("토마토의 개수를 입력하세요:"))
field =[makeTomato() for i in range(n)]
print(field)



