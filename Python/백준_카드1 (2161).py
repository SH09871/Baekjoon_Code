#1. 몇 번째의 카드까지 생성할지 자연수 입력 받기
#2. 입력 받은 숫자까지의 카드 만들기
#3. 반복문 작성 - 맨 위의 카드 버리고, 맨 위에 위치하게 된 카드를 맨 밑으로 옮기기 (카드가 한 장이 남을 때까지 반복)
#4. 카드를 버린 순서대로 결과 출력

card_list = []

a = int(input("몇 번째 카드까지 생성할까요? "))

for i in range(a):
    card_list.append(i+1)

while len(card_list) != 1:
    print(card_list[0], end=' ')
    card_list.remove(card_list[0])
    card_list.append(card_list[0])
    card_list.remove(card_list[0])

print(card_list[0])