var1 = "HelloPython"
print(var1) #문자열 객체 출력
print(id(var1)) #객체의 주소를 반환해주는 내장함수

var1=100
print(var1)
print(id(var1))

var2=150.25
print(var2)
print(id(var2))

var3=True
print(var3)
print(id(var3))

#실수>정수
a=int(10.5) #a=10
b=int(20.42) #b=20
add=a+b
print('add =', add)


#논리형>정수
print(int(True))
print(int(False))

#문자형>정수
st= '10'
print(int(st)**2)

#이름,나이,주소 등과 같은 개인정보를 변수에 저장하고 출력하는 프로그램-->동적 타이핑
name='Alice'
age=25
address='''우편번호 12345
           서울시 영등포구
           서울빌딩 501호'''
friend=None
height=178.3

print("이름:", name)
print("나이:", age)
print("주소:", address)
print("friend:", friend)
print("키:", height)
