# for i in [] start and end vs. while unknown

# a = 3
# while a > 1:
#     print("믿을 건 나뿐이다.")
#     a -= 1

# break 문

# while True:
#     num = int(input("숫자 0을 입력하면 탈출!:"))
#     if num == 0:
#         break
#
# while True:
#     print("사칙연산 프로그램")
#     num = int(input("1. 더하기 2. 빼기 3. 종료"))
#     if num == 1:
#         a = int(input("첫 번째 수: "))
#         b = int(input("두 번째 수: "))
#         print(f"두 수의 합은 {a+b}입니다.")
#     elif num == 2:
#         a = int(input("첫 번째 수: "))
#         b = int(input("두 번째 수: "))
#         print(f"두 수의 합은 {a-b}입니다.")
#     elif num == 3:
#         print("프로그램 종료!")
#         break
#     elif num == 1004:
#         print("과장님 제발 퇴근시켜주세요")
#     else:
#         print(f"숫자를 잘못 입력했습니다. 다시 입력하세요!")



# 도형 넓이 구하는 프로그램
# 1. 원의 넓이 2. 정삼각형의 넓이 3. 정사각형의 넓이 4. 프로그램 종료 그 외 숫자 재입력 요구
# while True:
#     print("도형 넓이 구하는 프로그램")
#     option = int(input("1. 원의 넓이 2. 정삼각형의 넓이 3. 정사각형의 넓이 4. 프로그램 종료"))
#     if option == 1:
#         a = int(input("반지름(cm): "))
#         print(f"원의 넓이는 {a * a * 3.14} cm^2 입니다.")
#     elif option == 2:
#         b = int(input("정삼각형의 변의 길이(cm): "))
#         print(f"정삼각형의 넓이는 {b * b * 0.5} cm^2 입니다.")
#     elif option == 3:
#         c = int(input("정사각형의 변의 길이(cm): "))
#         print(f"정사각형의 넓이는 {c * c} cm^2 입니다.")
#     elif option == 4:
#         print("프로그램 종료!")
#         break
#     else:
#         print(f"숫자를 잘못 입력했습니다. 다시 입력하세요!")

# 일본 여행 투두리스트
# 0. 필수 물품 추가하기 1. 갈 곳 등록하기 2. 먹을 것 등록하기 3. 할일 등록하기 4. 모든 투두리스트 보기 5. 종료하기
itemlist=[]
placelist=[]
foodlist=[]
todolist=[]

while True:
    print("일본 여행 투두리스트 프로그램!")
    num = int(input("0. 필수 물품 추가하기 1. 갈 곳 등록하기 2. 먹을 것 등록하기 3. 할일 등록하기 4. 모든 투두리스트 보기 5. 종료하기"))
    if num == 0:
       item = input("필수품:")
       itemlist.append(item)
       print(f"{item}이 추가되었습니다.")
    elif num == 1:
        place = input("갈 곳:")
        placelist.append(place)
        print(f"{place}이 추가되었습니다.")
    elif num == 2:
        food = input("먹을 것:")
        foodlist.append(food)
        print(f"{food}이 추가되었습니다.")
    elif num == 3:
        todo = input("할 것:")
        todolist.append(todo)
        print(f"{todo}이 추가되었습니다.")
    elif num == 4:
        print(f"필수품 리스트:{itemlist}")
        print(f"갈곳 리스트:{placelist}")
        print(f"먹을것 리스트:{foodlist}")
        print(f"할것 리스트:{todolist}")
    elif num == 5:
        print("일본여행 투두리스트 종료")
        #데이터베이스, 엑셀, 핸드폰 저장 장치에 저장하는 코드
        break
    else:
        print("숫자입력오류!")