# 123, "123", True,
starbucks = ['아메라카노','아이스라떼','바닐라']
numlist = [5,1,'121',582,'30',True,['아메리카노','라떼']]
print(f"starbucks menu is {starbucks}")
print(numlist)
print(starbucks[0])

coffee = ['아메리카노','라떼','바닐라','모카','민트']
price = [2000, 2500, 3000, 3000, 3500]
print(f"메뉴:{coffee}, 가격:{price}")
number=int(input("커피 두 메뉴를 고르세요(0-4): "))
number1=int(input("커피 두 메뉴를 고르세요(0-4): "))
print(f"고르신 메뉴:{coffee[number],coffee[number1]} 총 가격:{price[number]+price[number1]}")

#팝콘과 음료 정해서 가격 구하기

popcorn = ['일반 팝콘', '캬라멜 팝콘', '치즈 팝콘', '어니언 팝콘']
popcornprice = [5000,6000,6000,5500]
beverage = ['콜라', '제로콜라', '스프라이트', '에이드']
beverageprice = [2000,2500,2000,3000]
print(f"팝콘 메뉴{popcorn} 팝콘 가격{popcornprice}")
pnumber=int(input("팝콘 메뉴를 고르세요(0-3): "))

print(f"음료 메뉴{beverage} 음료 가격{beverageprice}")
bnumber=int(input("음료 메뉴를 고르세요(0-3): "))
print(f"고르신 콤보:{popcorn[pnumber],beverage[bnumber]} 총 가격:{popcornprice[pnumber]+beverageprice[bnumber]}")