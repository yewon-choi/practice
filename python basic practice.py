# #set형 변수
# #{}안에 서로 다른 자료형의 값을 , 로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
# #순서의 개념이 존재하지 않아, 인덱스를 사용할 수 없다
# #중복이 허용되지 않음

# student = {'홍길동','이순신','강감찬','홍길동'}
# print(student)
# print(len(student))
# # print(student[0])

# student = {'임꺽정',30}
# print(student)


# #dictionary형 변수
# dogs = {1:'골든리트리버',2:'진돗개',3:'보더콜리'}
# print(dogs)
# print(dogs[1])
# print(dogs[2])

# dogs[2] = '레브라도리트리버'
# print(dogs)

# dogs[4] = '알래스카말라뮤트'
# print(dogs)

# #none 변수선언
# obj = None #False로 평가!

# #변수를 생성하고 초기화하는 다양한 방법
# x = y = 10
# print(x)
# print(y)

# x, y = (10, 20)
# print(x)
# print(y)

# #6. 흐름과 제어 -if

# score = 80
# if score >= 60:
#     print('{}점'.format(score))
#     print('합격입니다')

# #출력을 위한 result에 기본값을 설정하는 것!
# result = '불합격입니다'
# score = 80
# if score >= 60:
#     result = '합격입니다.'
# print(result)

# score = 50
# if score >= 60:
#     print('합격입니다.')
# else:
#     print('불합격입니다.')


# #7.흐름과 제어 - 반복
# #2단 구구단
# dan = int(input())
# for i in range(1,10):
#     print('{} x {} = {:>2}'.format(dan, i, dan*i))


# dogs = {1:'골든리트리버', 2:'진돗개', 3:'보더콜리'}
# for key in dogs:
#     print('{} : {}'.format(key, dogs[key]))

# for key, value in dogs.items():
#     print('{} : {}'.format(key,value))

# #총점구하기
# scores = [100, 95, 88, 98]
# total = 0

# for score in scores:
#     total += score
# print('총점: {}'.format(total))


# #중첩된 for문을 활용한 구구단 출력 코드
# for i in range(2,10):
#     for j in range(1,10):
#         print('{} x {} = {:>2}'.format(i,j,i*j))

#while문
#bool 값을 반환하는 조건식
#true 면 while 문 값을 반복, false는 while문 나가기

# dan = int(input())
# i = 1

# while i < 10:
#     print('{} x {} = {}'.format(dan, i, dan*i))
#     i += 1

# scores = [100, 95, 88, 98]
# total = 0
# cnt = len(scores)
# i = 0

# while i < cnt:
#     total += scores[i]
#     i += 1

# print('총점: {}'.format(total))

# #break 문, answer의 값이 q이면 break
# answer = ''

# while True:
#     answer = input()
#     if answer =='q':
#         break
#     print('{}을 입력하셨습니다.'.format(answer))


# #반복문 실습
# cnt = 1
# while cnt < 5:
#     print('*'*cnt)
#     cnt +=1

# for i in range(1,5):
#     print('*'*i)

# for i in range(2):
#     for j in range(1,5):
#         print('*'*j)

# i, k = 1, 1
# while i <= 2:
#     while k <= 4:
#         print("*"*k)
#         k += 1
#     i += 1
#     k = 1


# #공백문자와 '*'을 이용해서 만드는 것
# i, k = 5,1
# while i >= 0:
#     print('{}{}'.format(' '*i,'*'*(2*k-1)))
#     i -= 1
#     k += 1

lst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0
while len(lst) > 0:
    if lst[-1] >= 80:
        total += lst[-1]
        lst.pop()
print(total)