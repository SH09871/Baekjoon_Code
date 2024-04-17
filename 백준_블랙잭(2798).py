import random

#n, m 지정
n = int(input("3~100 사이의 값: ")) #n: 카드 개수
m = int(input("10, 300000 사이의 값: ")) #m: 딜러가 부르는 최고합

#카드에 쓰여 있는 수 정하기
card_num = []
for i in range(n):
    a = int(input("카드의 숫자: "))
    card_num.append(a)

#M에 가장 가까운 수가 되는 카드 숫자 3개 뽑기: 카드 자체가 동일한 숫자가 나올 수는 있으나, 더할 때는 서로 다른 카드끼리만 더한 다는 것을 명심
thr = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            thr.append(card_num[i] + card_num[j] + card_num[k])

thr = list(set(thr)) #중복 제거

cp_thr = []
for i in range(len(thr)):
    cp_thr.append(thr[i]-m)

cp_thr_abs = []
for i in range(len(thr)):
    cp_thr_abs.append(abs(thr[i] - m))

#최종 값
if 0 in cp_thr:
    print(m)
else:
    cp_thr_abs.sort()
    x = cp_thr_abs[0]

    if x in cp_thr:
        k = cp_thr.index(x)
    else:
        k = cp_thr.index(-x)

    print(m+cp_thr[k])
