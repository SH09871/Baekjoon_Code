#입력: 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력

#알파벳 대소문자로 된 단어 입력 받기
x = input()

#알파벳 전부 대문자로 변경
x = x.upper()

#입력 받은 알파벳 분할해서 리스트에 저장
y = list(x)

if len(y) == 1: #입력 받은 알파벳이 하나일 경우
    print(x)
else: 
    #알파벳 갯수 세기
    count = {} #갯수 저장할 딕셔너리 저장

    for i in range(len(y)):
        if y[i] in count:
            count[y[i]] += 1
        else:
            count[y[i]] = 1

    #갯수 비교
    total = list(count.values()) #count에 있는 모든 value값 추출 후 리스트로 저장
    total.sort(reverse=True) #내림차순으로 정렬

    #최종 출력
    if total[0] != total[1]:  #가장 많이 사용된 알파벳 갯수가 동일한 게 없다면
        end = [key for key, value in count.items() if value == total[0]]
        print(end[0])
    else:  #갯수가 동일한 게 있다면
        print("?")