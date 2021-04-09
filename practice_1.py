#연습문제
# 1)별찍기1
# print('*' * 1)
# print('*' * 2)
# print('*' * 3)
# print('*' * 4)
# print('*' * 5)
# print('*' * 6)
# print('*' * 7)

# for x in range(7):
#     print(x * '*')
#     x+=1

# print('*' * 7)
# print('*' * 6)
# print('*' * 5)
# print('*' * 4)
# print('*' * 3)
# print('*' * 2)
# print('*' * 1)

# 2)별찍기2
# for x in range(6,0,-1):
#     print(x * '*')

# print(' '*5, end='');print('*' * 1)
# print(' '*4, end='');print('*' * 2)
# print(' '*3, end='');print('*' * 3)
# print(' '*2, end='');print('*' * 4)
# print(' '*1, end='');print('*' * 5)
# print(' '*0, end='');print('*' * 6)

# 3)별찍기3 (practice)
# for x in range(7,0):
#     print(" "* x, end='')
#     for y in range(7,0,-1):
#             print("*"* y)


#실습2) 구구단 출력
# for x in range(1,10):
#     print("%d * %d = %d"%(2,x,2*x))
#
# for x in range(1,10):
#     for y in range(1,10):
#         print(x,y)
# 이중반복 구구단
# for x in range(1,10):
#     for y in range(1,10):
#         print("%d * %d = %d"%(x,y,x*y))



#실습3)숫자를 입력받아 0부터 3의 배수를 출력하는 프로그램

# for x in range(0,30):
#     s = x * 3
#     if s > 30:
#         break
#     else:
#         print(s)

# last = int(input('마지막 수는?'))
# for x in  range(0, last+1, 3):
#     print(x, end="\n")

# for x in range(0,last+1):
#     if x%3==0:
#         print(x)


# 실습4)숫자 두개와 기호를 입력 받아 계산기 프로그램 but 사용자가 q 입력하면 계산기 종료
# 두수 기호 입력
# 기호에 따라 계산
# 계속 진행여부

# 입력 정의
# s = input("숫자와 기호를 입력하세요").split() # 두수 입력/리스트화
# a = int(s[0]) # 숫자
# b = s[1] # 기호
# c = int(s[2]) # 두번째 숫자

# #while 문/계산식
# while s == 'q': # 입력한 수가 q
#
#     if b == '+': # 덧셈식
#         print("%d + %d = %d"%(a,c,a+c))
#     elif b == '-': # 뺄셈식
#         print("%d - %d = %d"%(a,c,a-c))
#     elif b == '*': # 곱셈식
#         print("%d * %d = %d"%(a,c,a*c))
#     elif b == '/': # 나누기식
#         print("%d / %d = %d"%(a,c,a/c))
#     else:
#         print("잘못입력하셨습니다.")
# while True:
#     a = int(input('first'))
#     if a == 'q' : break
#     a = int(a)
#     b = int(input('second'))
#     #원하는 기호가 입력 될때까지 계속입력
#     sign = input('기호는?')
#     if sign in ['+','-','*','/']:
#         break
# #     # if sign == 'q': break *
#     if sign =='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign =='*':
#         print(a*b)
#     elif sign =='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')

    # ***
    # if input('종료(y)?')=='y':
    #     break



# while True:
#     a = int(input('first'))
#     if a == 'q':break
#     a =int(a)
#     b = int(input('second'))
#     sign = input('기호는?')
#     # if sign == 'q': break *
#     if sign == '+':
#         print(a + b)
#     elif sign == '-':
#         print(a - b)
#     elif sign == '*':
#         print(a * b)
#     elif sign == '/':
#         print(a / b)
#     else:
#         print('잘못된 기호')



    # ***
    # if input('종료(y)?')=='y':
    #     break

# 실습4)
# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# k = dicA.keys()
# v = dicA.values()
# i = dicA.items()
# # print(k,v,i)
# print("90점 이상 학생은")
# for x,y in i:
#     if int(y) < 90:
#         continue
#     else:
#         print( x,'번')

#실습5)
#사원의 판매수량 입력
#히스토그램 그리기
# 데이터 구조: {'홍길동':10, '이순신':15, '김순희':5, '이철수':7}
# listA = ['홍길동','이순신','김순희','이철수']
# qty = {} #판매수량을 저장할 딕셔너리
# for name in listA:
#     qty[name] = int(input(name + '?'))
#     i = qty.items()
# for x,y in i:
#     print(x,":", "*" * y)





print("당신은 적정 체중입니다.")
print("당신은 너무 말랐네요")
print("당신은 비만입니다.")

















