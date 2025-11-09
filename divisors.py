import sys

def count_divisors(n: int) -> int:
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(count_divisors(n))

