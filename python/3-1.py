N = int(input())
if N < 1 or N > 100:
    print("입력 오류")
else:
    numbers = input().strip()
    total = sum(int(x) for x in numbers)
    print(total)
