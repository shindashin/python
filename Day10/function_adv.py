# year -> '개'
# 1992 -> '원숭이'

def zodiac(year):
    zodiac = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀','말, '양']'
    return zodiac[year % 12]

#핸드폰 번호 가리기 01012345678 -> *******5678
def masking(number):
    masked = ""
    for idx,num in enumerate(number):
        if len(number) - idx > 4:
            maksed += "*"
        else:
            maksed += num
    return masked
b = masking("01012341234")
print(b)

def masking1(number):
    return '*'  * (len(number) -4) + number[-4:]


