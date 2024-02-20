#for_comprehension: for문 간결한 버전
#list for_comprehension
newList = [i for i in range(100)]
appleList = ['😂' for i in range(100)]
print(newList)
print(appleList)
#25-75
aList = [i for i in range(25,76)]
print(aList)
fruits=['🍎','🍒','🍋']
fruitslist = [fruits[i % 3] for i in range(100)]
print(fruitslist)

# 기본 구조
helloworldList = [i.upper() for i in "helloworld"]
print(helloworldList)

coffee = ['americano', 'latte', 'mint', 'mocha', 'cocoa']
coffeelenlist = ([len(i) for i in coffee])
print(coffeelenlist)

res=[i ** 2 for i in range(1,10,2)]
print(res)

