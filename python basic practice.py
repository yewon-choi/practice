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

"""
객체지향 프로그래밍(object-oriendted Programming)

객체 형성(상태와 행위로 이루어짐) -> 객체 조립 -> 프로그램 형성
객체를 이용해 문제를 해결하려는 프로그래밍 방법

객체: 변수 + 메서드 연관된 것 들끼리 묶어 만든 것

클래스 
1. 부품 객체를 만들기 위한 청사진, 설계도, 템플릿
2. 추상화의 과정을 통해 만들어짐

메서드
-메시지라고도 부름
-한 객체의 속성을 조작할 목적으로 사용
-객체 간의 통신은 메시지 전달을 통해 이루어짐
-클래스로부터 생성된 객체 사용 시 객체에 명령을 내리는 행위
-> 객체가 가지고 있는 메서드를 호출한다. 객체에 메시지를 전달한다.

특징
-추상화 : 객체에서 공통된 속성과 행위를 추출하는 것
 -> 추상 데이터 타입 (클래스)
-상속 : 상위 클래스의 속성, 행위를 하위 클래스가 물려받는 것
 ->재사용으로 인해 코드가 줄어듦
 ->범용적인 사용 가능, 물려받은 자료의 자유로운 사용 및 추가 가능
 -다형성 : 다양한 형태로 나타날 수 있음

생성자 메서드 - __init__ 

class 클래스명:
    def __init__(self,매개변수 목록):


소멸자 메서드 - __del__

class 클래스명:
    def __del__(self):

** 메서드 오버라이딩
-> 부모 클래스에 있는 메서드와 동일한 서명을 가진 메서드를
자식 클래스에서 다시 정의해 사용하는 것


"""

# #딕셔너리 및 리스트 객체를 이용한 코드 생성
# members = [
#     {'name' : '홍길동', 'age': 20},
#     {'name' : '이순신', 'age': 45},
#     {'name' : '강감찬', 'age': 35}
# ]

# for member in members:
#     print(member)

# def create(name, age):
#     return {'name': name, 'age':age}

# def to_str(person):
#     return '{}\t{}'.format(person['name'],person['age'])

# members = [
#     {'name' : '홍길동', 'age': 20},
#     {'name' : '이순신', 'age': 45},
#     {'name' : '강감찬', 'age': 35}
# ]

# for member in members:
#     print(to_str(member))


# class Person:
#     pass

# member = Person()

# if isinstance(member, Person):
#     print('member는 Person 클래스의 인스턴스입니다.')

#객체의 생성과 소멸, self
# class Person:
#     def __init__(self, name, age): #self가 가리키는 객체공간에 name, age 필드 생성
#         self.name = name
#         self.age = age
#         print('{} 객체가 생성되었습니다'.format(self, name))

#     def __del__(self):
#         print('{} 객체가 제거되었습니다.'.format(self.name))

# member = Person('홍길동',20)
# print('{}\t{}'.format(member.name, member.age))
# print(dir(member))

#클래스 메서드 사용
# class Person:
#     count = 0

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Person.count +=1
#         print('{} 객체가 생성되었습니다.'.format(self.__name))

#     def __del__(self):
#         print('{} 객체개 제거되었습니다.'.format(self.__name))

#     def to_str(self):
#         return '{}\t{}'.format(self.__name, self.__age)


#__str()__메서드
#str()함수에 객체를 전달해 문자열로 변환

# class Person:
#     count = 0

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Person.count += 1
#         print('{} 객체가 생성되었습니다.'.format(self.__name))

#     def __del__(self):
#         print('{} 객체가 제거되었습니다.'.format(self.__name))

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self,age):
#         if age < 0:
#             raise TypeError('나이는 0이상의 값만 허용합니다.')
#         self.__age = age

    
#     @classmethod
#     def get_info(cls):
#         return '현재 Person 클래스의 인스턴스는 총 {} 개입니다.'.format(cls.count)

#     def __gt__(self, other):
#         return self.__age > other.__age
    
#     def __ge__(self, other):
#         return self.__age >= other.__age
    
#     def __lt__(self, other):
#         return self.__age < other.__age
    
#     def __le__(self, other):
#         return self.__age <= other.__age

#     def __eq__(self,other):
#         return self.__age == other.__age

#     def __ne__(self, other):
#         return self.__age != other.__age

#     def __str__(self):
#         return '{}\n{}'.format(self.__name, self.__age)

# members = [
#     Person('홍길동',20),
#     Person('이순신',45),
#     Person('강감찬',35)
# ]

# for member in members:
#     print(str(member)) #Person 클래스의 객체 전달하면 __Str__메서드 호출


#클래스 상속(부모 클래스 -> 자식 클래스)

# class Parent:
#     def __init__(self, family_name):
#         self.__family_name = family_name
#         print('Parent 클래스의 __init__()...')

#     @property
#     def family_name(self):
#         return self.__family_name

# class Child(Parent):
#     def __init__(self, first_name, last_name):
#         Parent.__init__(self, last_name)
#         #super().__init__(last_name)
#         self.__first_name = first_name
#         print('Child 클래스의 __init__()...')


#메소드 오버라이딩
#super() 기반 클래스의 메서드 호출

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 배우는 학생입니다.')

james = Student()
james.greeting()
























