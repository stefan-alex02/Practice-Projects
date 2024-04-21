def find_sum_of_solutions(p, a, b):
    MOD = 10 ** 9 + 7
    sum_of_solutions = 0

    for y in range(max(1, int(b - abs(p))), int(b + abs(p)) + 1):
        x = a + p / (y - b) if y != b else float('inf')

        if x.is_integer() and x >= 1:
            sum_of_solutions = (sum_of_solutions + int(x)) % MOD

    return sum_of_solutions


a, b, n = map(int, input().split())

p = 1
for _ in range(n):
    p *= int(input())

print(find_sum_of_solutions(p, a, b))
