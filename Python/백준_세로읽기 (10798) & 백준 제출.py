#글자 입력 받기
word = []
length = []
for i in range(5):
    word.append(list(input())) #글자 입력 받기 -> 한 글자씩 분할해서 리스트에 저장
    length.append(len(word[i])) #글자 길이 세기

#가장 긴 단어 길이 확인
length.sort(reverse=True)

#세로로 읽기
col = []
for i in range(length[0]):
    for j in range(5):
        if len(word[j]) >= i+1 :
            col.append(word[j][i])

#가로로 출력
for i in range(len(col)):
    print(col[i], end = '')