#set형 변수
#{}안에 서로 다른 자료형의 값을 , 로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
#순서의 개념이 존재하지 않아, 인덱스를 사용할 수 없다
#중복이 허용되지 않음

student = {'홍길동','이순신','강감찬','홍길동'}
print(student)
print(len(student))
# print(student[0])

student = {'임꺽정',30}
print(student)


#dictionary형 변수
dogs = {1:'골든리트리버',2:'진돗개',3:'보더콜리'}
print(dogs)
print(dogs[1])
print(dogs[2])

dogs[2] = '레브라도리트리버'
print(dogs)

dogs[4] = '알래스카말라뮤트'
print(dogs)

#none 변수선언
obj = None #False로 평가!