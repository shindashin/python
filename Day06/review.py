#1. 유저에게 설날에 먹은 음식 3개를 묻고,
# 설날에 먹은 음식 리스트 나타내기
sulFood = []
food1=input("설날에 먹은 음식1을 작성해주세요:")
food2=input("설날에 먹은 음식2을 작성해주세요:")
food3=input("설날에 먹은 음식3을 작성해주세요:")
sulFood.append(food1)
sulFood.append(food2)
sulFood.append(food3)
print(f"설날에 먹은 음식 리스트: {sulFood} 입니다")

#2. 유저에게 좋아하는 커피 프랜차이즈 영어로 입력받고 대문자화하기
coffee=input("좋아하는 커피 프랜차이즈:")
coffee1=coffee.upper()
print(coffee1)

#3. 유저에게 이메일 주소를 입력받고, 도메인만 출력하기
#ex) megastudy@naver.com - > naver
domain=input("이메일 입력:")
a=domain.split("@")
b=a[1].split(".")
print(b[0])

#4. 영어 기사를 스크랩하여서 단어별로 리스트화해서 오름차순으로 출력하기
article="""By Julia Ainsley and Monica Alba
The Biden administration is considering taking executive action to deter illegal migration across the southern border, according to two U.S. officials.
As passing legislation on border security in Congress appears unlikely, the plans under consideration signal that the White House wants to take action before numbers at the border, which have dropped in the past month, rise again as expected.
The plans have been under consideration for months, the officials said. In December, as Congress prepared to leave town for the holidays with no border solution, illegal crossings of the southwest border hit records at more than 10,000 per day.
Senate vote on bipartisan border and national security bill fails
FEB. 8, 202402:05
The unilateral measures under consideration might upset some progressives in Congress, the officials said, but they noted that Democratic mayors who have asked for more help from the federal government to handle the influx of migrants in their cities would be pleased. The measures are still being drafted and are not expected to take place any time soon.
On Wednesday, Senate Republicans blocked a bipartisan border bill that they had negotiated with Democrats and the Biden administration over the preceding months.
In a statement, a White House spokesperson said, “The administration spent months negotiating in good faith to deliver the toughest and fairest bipartisan border security bill in decades because we need Congress to make significant policy reforms and to provide additional funding to secure our border.”
Today, Congressional Republicans chose to put partisan politics ahead of our national security and voted against what border agents have said they need. No regulatory actions would accomplish what the bipartisan national security agreement would have done for border security and the immigration system at large.”
GOP Sen. Lankford urges Congress to pass bipartisan border bill in floor speech
FEB. 8, 202401:39
Regardless of how much any executive action might appear to increase immigration enforcement both on the border and in the interior of the U.S., the officials said, it would pale in comparison to the effects that would arise if Congress had passed the border security bill.
It’s a plan B,” an official said. Both officials said doing nothing is not an option.
Recommended
TRUMP INVESTIGATIONS
Marjorie Taylor Greene files second ethics complaint against Georgia prosecutor who charged Trump

2024 ELECTION
Marianne Williamson ends long-shot presidential bid as Democratic challenger
On Tuesday, President Joe Biden argued the bipartisan bill would have “made important fixes to our broken immigration system,” calling it “the toughest, fairest law” on the border ever proposed.

Biden faces growing political backlash, some of it from members of his own party, over his handling of the border as he campaigns for re-election. He plans to cite the Republican turnabout on the bipartisan border legislation as proof that for political reasons the GOP does not really want to solve the problem. But he is still vulnerable on the issue, trailing his likely 2024 opponent, former President Donald Trump, by more than 30 points on securing the border and controlling immigration, according to a new NBC News poll released this week.

The Biden administration has already taken multiple unilateral actions to try to stem the flow of migrants.

In May, when Covid restrictions were set to lift at the border, the Department of Homeland Security introduced restrictions that would make more migrants eligible for speedy deportations. But overwhelming numbers meant the vast majority of migrants apprehended by border agents were still released into the U.S.


Julia Ainsley
"""
wordlist=article.split(" ")
wordlist.sort()
print(wordlist)