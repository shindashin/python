#1. 영화 예매 프로그램(자료 구조 사용)
# 사용자로부터 영화 종류와 팝콘 종류를 입력받습니다.
# 각 영화, 팝콘의 가격은 다음과 같이 설정합니다.
#1:액션영화 - 10000원
#2:로맨틱 코미디 - 8000원
#3: 공포영화 - 9000원
#팝콘 종류
#1: 치즈 팝콘: 6000원
#2: 캬라멜 팝콘: 5000원
#3: 일반팝콘: 5000원

theater={
      'movie': {
            'movieList': ['액션영화', '로맨틱 코미디', '공포영화'],
            'price': [10000, 8000, 9000]
       },
      'popcorn': {
            'popcornList': ['일반 팝콘', '카라멜 팝콘', '치즈 팝콘'],
            'price': [6000, 5000, 5000]
      }
}
movie=int(input(f"{theater['movie']['movieList']} 중 선택하세요(0-2번):"))
popcorn=int(input(f"{theater['popcorn']['popcornList']} 중 선택하세요(0-2번):"))

print(f"영화:{theater['movie']['movieList'][movie]} 팝콘:{theater['popcorn']['popcornList'][popcorn]}")
print(f"총가격:{theater['movie']['price'][movie] + theater['popcorn']['price'][popcorn]}")