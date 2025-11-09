import sys

number = int(sys.argv[1])

for i in range(1, number + 1):   # 1부터 number까지 반복
    if number % i == 0:           # 나누어떨어지면 약수
        print(i, end=" ")

print()  # 마지막 줄바꿈
