x = input().upper()

if 0 < len(list(x)) <= 1000000:

    if len(list(x)) == 1:
        print(x)

    else:
        y = list(x)

        count = {}
        for i in range(len(y)):
            if y[i] in count:
                count[y[i]] += 1
            else:
                count[y[i]] = 1

        total = list(count.values())
        total.sort(reverse=True)

        same = 0
        for i in range(1, len(total)):
            if total[i] == total[0]:
                same += 1

        if same == 0:
            end = [key for key, value in count.items() if value == total[0]]
            print(end[0])
        else:
            print("?")