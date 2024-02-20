# 1. 리스트 요소의 제곱
# 문제: 정수 리스트 [1, 3, 5, 7, 9]의 각 요소를 제곱하여 새로운 리스트를 만드세요.
# 예상 답안: [1, 9, 25, 49, 81]
numList = [1, 3, 5, 7, 9]
numList1 = []
for x in numList:
    numList1.append(x**2)
print(numList1)

#for_comprehension 사용하기
numList2=([(i**2) for i in numList])
print(numList2)

# 2. 문자열 길이 변환
# 문자열 리스트 ["hello", "world", "python", "programming"]에서 각 단어의 길이를 구하여 새로운 리스트를 만드세요.
# 예상 답안: [5, 5, 6, 11]
wordList =  ["hello", "world", "python", "programming"]
wordList1 = []
for x in wordList:
    wordList1.append(len(x))
print(wordList1)

#3. 문자열 처리를 위한 리스트 1
# 문제: 문자열 리스트 ["apple", "banana", "cherry", "date"]에서 각 단어의 첫 글자만을 추출하여 새로운 리스트를 만드세요.
# 예상 답안: ['a', 'b', 'c', 'd']
otherWordList = ["apple", "banana", "cherry", "date"]
otherWordList1 = []
for x in otherWordList:
    otherWordList1.append(x[0])
print(otherWordList1)
