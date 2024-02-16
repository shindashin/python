#for_adv
#for 문자열

for x in "megastudy":
    print(x)

# 영어 단어를 대소문자를 섞어서 넣으면 반대로 출력하기
# MegA -> mEGa, aPPLE -> Apple
word=input("단어 입력:")
newWord=""
for x in word:
    print(x)
    if x.isupper():
        newWord += x.lower()
    else:
        newWord += x.upper()
print(newWord)

# for 리스트
for x in ['사과','딸기','포도']:
    print(x)

# ['apple','banana','watermelon','mango','orange']
# 6글자 이상 그리고 알파벳 e포함 과일리스트 새로 뽑기
fruits = ['apple','banana','watermelon','mango','orange']
newfruits = []
for x in fruits:
    if len(x)>=6 and 'e' in x:
        newfruits.append(x)
print(newfruits)

# 뉴스기사를 가져와서 유저에게 n개의 길이를 물어보고, 어떠한 알파벳을 반드시 포함하는 것을 물어보고
# 어떠한 알파벳을 반드시 포함하는 것을 물어보고 해당 일치하는 단어들만 나열해서 오름차순으로 보여주기
article="""If you are preparing to take the Registration Examination for Dietitians, get prepared for test day with eatrightPREP® for the RDN Exam, developed by the Academy of Nutrition and Dietetics. You will have access to a state-of-the-art learning platform offering flashcards, pretest questions, and practice and simulated tests to help you build and gain confidence in your test-taking skills. All flashcards and questions contain a complete rationale and cited reference to explain the correct answer. eatrightPREP® also offers performance statistics that will help you identify your strengths and weaknesses for targeting and monitoring areas of improvement before test day.

The course includes 3 practice tests and 2 simulated tests with multiple-choice questions based on the test specifications for the Registration Examination for Dietitians. The simulated tests are timed to help you practice taking a test in 2.5 hours. You have unlimited access to these practice and simulated tests with your subscription to eatrightPREP®.

Pricing
90-day access is $199.99 for members and nonmembers; access begins the day you purchase. Access is for one person only and is not to be shared. 30-day renewals are available for $49.99 members and nonmembers.

Free Demo
Want to try before you buy? Go to eatrightPREP® and click "RDN Course Demo" to access your 7-day demo!

Educators
Program pricing is now available. Review discount rates, ask a question or place an order for your program. For more information about how to how to use eatrightPREP® in your program, contact our sales team.
"""
a=article.split(" ")
print(a)
length=int(input("문자의 길이는:"))
alphabet=input("포함할 알파벳:")
searchwordlist=[]
for x in a:
    if len(x)>=length and alphabet in x:
        searchwordlist.append(x)
searchwordlist.sort()
print(searchwordlist)

for x in range(100):
    if x==50:
      break
    print(x)

# for range, 문자열, list
for index,item in enumerate("megastudy"):
    print(f"{index},{item}")

#1. 유저에게 영단어를 입력받고, 짝수번째만 뽑고 이어붙인 단어 만들기
# coffee -> cfe
word=input("영단어 입력: ")
newWord=[]
for index,item in enumerate(word):
    if index % 2 == 0:
        newWord += item
print(newWord)

#맨 처음, 맨 마지막
word=input("영단어 입력: ")
newWord=""
for index,item in enumerate(word):
    if index == 0 or len(word) - 1 == index:
        newWord += item
print(newWord)
