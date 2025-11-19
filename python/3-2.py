N = int(input())

numbers = list(map(int, input().split()))

if len(numbers) != N:
    print("입력 오류")
else:
    min_val = min(numbers)
    max_val = max(numbers)

    print(min_val, max_val)
