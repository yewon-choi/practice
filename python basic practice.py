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

# lst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# total = 0
# while len(lst) > 0:
#     if lst[-1] >= 80:
#         total += lst[-1]
#         lst.pop()
# print(total)

"""
9. 내장함수
01.수치 연
abs() : 인자로 숫자를 전달하면, 그 숫자의 절댓값을 반환하는 함수
divmod() : 첫 번째 인자를 두 번째 인자로 나눴을 때의 몫과 나머지를 튜플 객체로 반환하는 함수
pow() : 첫 번쨰로 전달된 인자 값에 대해 두 번째로 전달된 인자 값으로 제곱한 결과를 반환하는 함수
enumerate() : list, tuple, 문자열과 같은 시퀀스형을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 
            enumerate 객체를 반환하는 함수

filter() : 조건에 해당하는 함수는 걸러내는 함수
map() : 두 번째 인자로 반복 가능한 자료형을 전달 받아
        자료형의 각 항목에 대해 첫 번째 인자로 전달 받은 함수를
        적용한 결과를 맵 객체로 변환하는 함수

zip() : 둘 이상의 반복 가능한 자료형을 인자로 전달받아,
        동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성하는 함수

chr() : 정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환하는 함수
ord() : 문자를 인자로 전달 받아 유니코드 값(10진 정수)을 반환하는 함수
hex() : 10진 정수 값을 인자로 전달 받아 16진수로 변환된 값을 반환하는 함수
int() : 인자로 전달된 숫자 형식의 문자열, 부동소수점 숫자를 정수로 변환한 값을 반환하는 함수
float() : 인자로 전달된 숫자 형식의 문자열, 정수를 부동 소수점 숫자로 변환하는 값을 반한하는 함수
str() : 인자로 전달된 객체에 대한 문자열 변환 값을 반환하는 함수

globals() : 현재 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 전역변수와 함수, 클래스의 정보 포함
locals() : 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 -> 매개변수를 포함한 지역변수와 중첩함수의 정보 포함
"""
# #divmod()
# val1, val2 = 9, 5
# result_tuple = divmod(val1,val2)
# print(result_tuple)

# print('divmod({},{}) => 몫:{},나머지:{}'.format(val1,val2,*result_tuple))

# #pow()
# data_list = [1,2,3,4,5]
# print('pow({}, 3) => {}'.format(data_list[3], pow(data_list[3],3)))

# #enumerate

# data_list = [1,2,3,4,5]
# for idx, val in enumerate(data_list):
#     print('{}:{}'.format(idx,val))

#
# data_str = 'Hello'
# data_list = list(data_str)
# data_tuple = tuple(data_list)
# data_set = set(data_list)

# print(data_list)
# print(data_tuple)
# print(data_set)

# data_list = list('abcde')
# result = list(map(lambda x: x.upper(), data_list))
# print(result)

# data_list = [10, 24, 35, 46, 3, 4]
# data_sorted = sorted(data_list))
# print(data_sorted)
# data_sorted

# data_list1 = [1,2,3]
# data_list2 = [4,5,6]
# data_list3 = ['a','b','c']
# print(list(zip(data_list1,data_list3)))

#globals()

class Myclass:
    pass

def test_fn(param):
    def inner_fn():
        pass
    val