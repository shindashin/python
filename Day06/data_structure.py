# data_structure
# [](list), {}(set), {}(dict), ()(tuple)

# set(집합, 중복 허용 안됨(제일 중요함))
a = {1,2,3,1,2,3}
b = set([1,2,3,4,1,2,3,4])
print(a)
print(b)
a.add(10)
print(a)

starbucks = ["아메리카노", "라떼", "오늘의커피", "아이스커피"]
megacoffee = ["아메리카노", "라떼", "딸기라떼", "메가리카노"]
a = set(starbucks)
b = set(megacoffee)
print(a)
a.update(b)
print(a)

# 모든 단어를 중복없이 출력
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
wordlist = article.split(" ")
no_dup_words=set(wordlist)
print(no_dup_words)

wordlist1=list(no_dup_words)
wordlist1.sort()
print(wordlist1)

# 데이터가 추가/삭제되지 않으면 그대로 한 줄
# 위 사항이 아니면 새로운 변수에 넣기

# 중복된 단어만 보여주세요.
wordlist = article.split(" ")
wordlist1 = article.split(" ")
setWord = set(wordlist)
setWord1 = set(wordlist1)
inter=setWord.intersection(setWord1)
print(inter)
