word=input("문자열을 넣으세요:")
word1=word.upper()
print(word1)

lyrics="""Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind what you gon do now?
Ever since the d-day y-you went away no, I dont know how
How to erase your body from out my brain what you gon do now?
Maybe I should just focus on me instead but all I think about
Are the nights we were tangled up in your bed
Oh no oh no
Oh no oh no
You're goin' 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind what you gon' do now?
Ever since the d-day y-you went away someone tell me how
How much more do I gotta drink for the pain what you gon' do now?
You did things to me that I just can't forget now all I think about
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're going 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind of my mind
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind what you gon' do now?
Did you know you're the one that got away?
And even now, baby, I'm still not okay
Did you know that my dreams, they're all the same
Every time I close my eyes?
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind what you gon' do now?
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind what you gon' do now?
(Whoa)
I can feel you over here I can feel you over here
You take up every corner of my mind what you gon' do now?
"""
right=lyrics.count('right')
left=lyrics.count('left')
print(f"가사에서 right은 {right}개 left는 {left}개 있습니다.")

article="""
Decide where you stand
You won’t hear anyone disputing that L.A. has a housing affordability crisis, or that we need to “cut red tape” to fix it. But candidates tend to show their differences when it comes to actual housing proposals in their districts, or specific measures to address the crisis. Ask yourself a few questions to see if a candidate’s approach matches yours:

Do you support more housing being built in your neighborhood? 
How much, and what kind? Market-rate condos? Apartments for very low-income tenants? All of the above and everything in between? 
If there’s a specific housing project being proposed near you, how do you feel about it?
What do you think are the main reasons for the housing affordability crisis? This can get in the weeds pretty fast, but generally:
Candidates who say it’s mainly a supply problem focus on finding ways to build more housing, such as fast-tracking approvals for certain types of housing, changing the zoning code to allow developers to build more housing in a given area, or making better use of vacant land and empty buildings. 
Those who say it’s largely a lack of tenant protections problem emphasize expanded rent control, vacancy taxes on units that stay empty for long periods of time, or more protections against evictions. 
Plenty of candidates support combinations of these measures, but knowing what they think is the main source of the problem will give you a better understanding of their approach.
If you’re new to housing policy, start with this explainer.

Before you keep reading…
Dear voter, we're asking you to help us keep local election news widely available for all today. Your financial support allows our reporters to research candidates and provide you and your neighbors the tools you need to make informed decisions when casting your ballot. When reliable local election reporting is widely available, the entire community benefits. Thank you for investing in your neighborhood.
  Monthly Donation   One-Time Donation

$5/mo
$10/mo
$15/mo
$20/mo

$ other amount /month

CONTINUE
The offices that matter most on the 2024 ballot
The Board of Supervisors and City Council have the most direct impact on housing affordability in your neighborhood. They’re particularly powerful in deciding how land is used. Most of the time, a major housing development will need a city council member to sign off before the project moves ahead. These officials can also approve new rules that can determine how much housing is allowed to be built in any given area. This past year, the L.A. City Council passed two plans that allow up to 135,000 additional housing units in downtown L.A. and Hollywood over the next two decades. County and city elected officials also vote on rent stabilization ordinances that limit how much landlords can raise rents every year.

These decisions won’t just affect your neighborhood, but they’ll also have ripple effects on surrounding neighborhoods and general housing affordability across L.A.

Your State Assemblymember and State Senator set the rules for what cities can and can’t do on housing. For instance, the California legislature passed a law in 2023 that allowed for new housing to be fast-tracked if it was built on church-owned land — something that religious groups couldn’t ordinarily do because cities and counties wouldn’t change local zoning laws. In 2017, it also cut restrictions on building accessory dwelling units (ADUs) — also known as converted garages or standalone living units on the same lot as the main house. After that law passed, ADU construction skyrocketed in L.A. and across the entire state.
"""
word=input("찾고 싶은 단어:")
result=article.count(word)
print(f"찾으시는 {word}단어는 총{result}개 있습니다")

replace=article.replace("the", "❤")
print(replace)