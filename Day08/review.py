#1. 점심 메뉴를 4개를 입력하고, 디저트 4개를 입력하고, 커피메뉴를 4개 입력하고,
# 여기서 랜덤으로 조합해서 각각 점심, 디저트, 커피를 뽑는 점메추 프로그램 만들기!
lunchmenu = []
lunch1=input("점심 메뉴1 입력하세요: ")
lunch2=input("점심 메뉴2 입력하세요: ")
lunch3=input("점심 메뉴3 입력하세요: ")
lunch4=input("점심 메뉴4 입력하세요: ")
lunchmenu.append(lunch1)
lunchmenu.append(lunch2)
lunchmenu.append(lunch3)
lunchmenu.append(lunch4)

dessertmenu = []
dessert1=input("디저트 메뉴1 입력하세요: ")
dessert2=input("디저트 메뉴2 입력하세요: ")
dessert3=input("디저트 메뉴3 입력하세요: ")
dessert4=input("디저트 메뉴4 입력하세요: ")
dessertmenu.append(dessert1)
dessertmenu.append(dessert2)
dessertmenu.append(dessert3)
dessertmenu.append(dessert4)

coffeemenu = []
coffee1=input("디저트 메뉴1 입력하세요: ")
coffee2=input("디저트 메뉴2 입력하세요: ")
coffee3=input("디저트 메뉴3 입력하세요: ")
coffee4=input("디저트 메뉴4 입력하세요: ")
coffeemenu.append(coffee1)
coffeemenu.append(coffee2)
coffeemenu.append(coffee3)
coffeemenu.append(coffee4)

import random
print(f"점심메뉴: {random.choice(lunchmenu)}, 디저트: {random.choice(dessertmenu)} 커피메뉴: {random.choice(coffeemenu)}")

#2. 유저에게 각도를 입력받고 0-90도 예각, 90도 직각, 90-180도 둔가, 180도 평각을 나타내주는 프로램
angle=int(input("각도 입력:"))

if 0<angle<90:
    print("예각")
elif angle==90:
    print("직각")
elif 90<angle<180:
    print("둔각")
elif angle==180:
    print("평각")
else:
    print("입력오류")

#3. 유저에게 x, y를 입력받고 좌표 평면 구하기
# ex) (1,4)=> 1사분면, (-2, 3) => 2사분면
x=int(input("X를 입력하세요:"))
y=int(input("Y를 입력하세요:"))

if x>0 and y>0:
    print("1사분면")
elif x<0 and y>0:
    print("2사분면")
elif x<0 and y<0:
    print("3사분면")
elif x>0 and y<0:
    print("4사분면")
else:
    print("x축 or y축 or 원점")