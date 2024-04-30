#단어의 개수 입력 받기
n = int(input())

#단어 입력 받기
raw_word = []
for i in range(n):
    raw_word.append(input())

#단어 여부 검사
word = []
for i in range(n):
    x = list(raw_word[i])  #입력 받은 알파벳 한 글자씩 분할해서 리스트에 저장

    if len(x) == 1:
        word.append(x[0])

    else:
        check = [] #리스트 초기화
        check.append(x[0])  # 첫 번째 단어는 무조건 추가 (어차피 비교할 거 없음)

        dup = 0
        for j in range(1, len(x)):
            if x[j] != x[j-1]:
                if x[j] not in check:
                    check.append(x[j])
                else:
                    dup += 1

        if dup == 0:
            word.append(raw_word[i])

print(len(word))
