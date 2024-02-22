# 헬스 운동 순서 프로그램
#1. 운동 추가
#2. 운동 순서 변경[a <-> b 자리바꿈]
#3. 운동 삭제
#4. 운동 순서 보기
#5. 종료
def addExercise(list):
    exerciseName = input("추가 할 운동의 이름 입력:")
    list.append(exerciseName)
    print(f"{exerciseName}가 추가되었습니다.")

exercises=[]
while True:
    print("헬스 운동 순서 프로그램!")
    pa=int(input("1. 운동 추가, 2. 운동 순서 변경, 3. 운동 삭제, 4. 운동 순서 보기, 5. 종료:"))
    if pa == 1:
       addExercise(exercises)
    elif pa == 2:
        if len(exercises) <=1:
            print("운동 개수가 부족하므로 순서를 바꿀 수 없습니다.")
        else:
            firstIdx = int(input(f"운동{exercises}에서 변경하고 싶은 운동 번호:")) - 1
            secondIdx = int(input(f"운동{exercises}에서 변경하고 싶은 운동 번호:")) - 1
            temp=exercises[firstIdx]
            exercises[firstIdx] = exercsies[secondIdx]
            exercises[secondIdx] = temp
            print(f"운동 {exercises[firstIdx]} <-> {exercises[secondIdx]}변경 완료")
    elif pa ==3:
        if len(exercises)==0:
            print("삭제할 운동이 없습니다.")
        else:
            deleteIdx = input(f"{exercises}삭제 하고 싶은 운동:")
            exercises.remove(deleteIdx)
    elif pa==4:
        for idx,exe in enumerate(exercises):
            if idx != len(exercises) -1:
                print(f"{exe} ->")
            else:
                print(f"{exe}")
    elif pa == 5:
        print("종료")
        break
    else:
        print("숫자입력오류!")