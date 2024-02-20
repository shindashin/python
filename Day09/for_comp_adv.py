#조건부 리스트 for comprehension
# 1. 필터링(걸르기) 2. 맵핑(바꾸기)
# [for i in rnage(n) 조건문]
evenList = [i for i in range(100) if i % 2 == 0]
print(evenList)

words = ['apple', 'banana', 'pineapple', 'mango', 'kiwi', 'blueberry', 'avocado']
wordsList = [i for i in words if len(i)>=6]
print(wordsList)

wordsList2 = [i.upper() for i in words if 'e' in i]
print(wordsList2)

#2. 맵핑(바꾸기)
# [a if 조건 else b for i in range(n)/list/str ]
ice = ['🍦' if i % 2 ==0 else i for i in range(100)]
print(ice)

words = ['apple', 'banana', 'pineapple', 'mango', 'kiwi', 'blueberry', 'avocado']
wordList3 = [i.upper() if len(i)>=5 else i for i in words]
print(wordList3)

# 3 6 9 게임
# [1~100] '👏' 아니면 숫자
game=['👏' if str(i%10) in '369' or str(i//10) in '369' else i for i in range(1,101)]
print(game)
print(str(23%10))