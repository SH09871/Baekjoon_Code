# 1. 테스트 실행할 횟수 입력 받기
# 2. 입력된 실행할 횟수에 맞춰 동전 40번 던진 결과 출력
# 3. 각 테스트마다 3-동전수열이 몇 번 나타났는지 출력 (뒤뒤뒤, 뒤뒤앞, 뒤앞뒤, 뒤앞앞, 앞뒤뒤, 앞뒤앞, 앞앞뒤, 앞앞앞 순서대로 공백으로 구분해서 출력)

import random

test_list = []

def count_check(list):
    global a, b, c, d, e, f, g
    a += list.count("TTT")
    b += list.count("TTH")
    c += list.count("THT")
    d += list.count("THH")
    e += list.count("HTT")
    e += list.count("HTH")
    f += list.count("HHT")
    g += list.count("HHH")


y = int(input("테스트를 실행할 횟수를 입력하시오: "))
z = int(input("동전을 던질 횟수를 입력하시오: "))


for i in range(y):
    for k in range(z):
        x = random.randint(0, 1)
        if x == 0:
            test_list.append("H")  # 앞면은 H로 표기
        else:
            test_list.append("T")  # 뒷면은 T로 표기

    print(*test_list)  # 리스트 내의 값을 []괄호 없이 출력

    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0   #전역변수값 초기화

    for k in range(z - 2):
        x = test_list[k:k + 3]  # 리스트 내의 값을 앞에서부터 3개씩 분할
        count_check(''.join(x))  # 분할한 값을 하나의 문자열로 바꿔서 앞에서 생성한 함수로 비교

    print("%d %d %d %d %d %d %d" % (a, b, c, d, e, f, g))

    test_list = []  # 리스트 초기화
