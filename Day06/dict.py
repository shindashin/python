#

coffee = {
    1: "아메리카노",
    2: "라떼",
    3: "바닐라"
}
print(coffee[1])

cgv = {
    'A': '웡카',
    'B': '시민덕희',
    'C': '귀멸칼날'
}
print(cgv["A"])
print(cgv["C"])

mbti = {
    'e': '외향적',
    'i': '내향적',
    's': '현실적',
    'n': '상상적',
    't': '공감1도 안해주는',
    'f': '감성적',
    'p': '즉흥적',
    'j': '계획적'
}

userMBTI=input("당신의 mbti는: ")
print(f"당신의 유형은 {mbti[userMBTI[0]]} {mbti[userMBTI[1]]} {mbti[userMBTI[2]]} {mbti[userMBTI[3]]}이군요")

 
