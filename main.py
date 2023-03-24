import sys


def main():
    n = int(input().strip())
    predefined = {}

    for i in range(n):
        s = int(input().strip())
        bits = 1 << i
        predefined[bits] = s

    m = int(input().strip())

    for i in range(m):
        data = list(map(int, input().split()))
        s = data[0]
        bits = 0
        for j in data[2:]:
            bits |= 1 << (j - 1)

        if bits in predefined:
            predefined[bits] = min(predefined[bits], s)
        else:
            predefined[bits] = s

    data = list(map(int, input().split()))
    to_by = 0
    for i in data[1:]:
        to_by |= 1 << (i - 1)

    dp = [sys.maxsize for _ in range(1 << n)]

    for key, value in predefined.items():
        dp[key] = value

    for i in range(1, 1 << n):
        if dp[i] == sys.maxsize:
            continue

        if i in predefined:
            for j in range(1, i):
                if dp[j] == sys.maxsize:
                    continue

                dp[i | j] = min(dp[i | j], dp[j] + dp[i])
        else:
            for key, value in predefined.items():
                if key > i:
                    break

                dp[i | key] = min(dp[i | key], dp[i] + value)

    result = sys.maxsize

    for i in range(1, 1 << n):
        if (i & to_by) != to_by:
            continue

        result = min(result, dp[i])

    print(result)


if __name__ == '__main__':
    main()
