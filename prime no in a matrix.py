#prints prime numbers in the matrix:
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(m)
cols = len(m[0])
for i in range(rows):
    for j in range(cols):
        num = m[i][j]
        if num > 1:
            is_prime = True
            for k in range(2, int(num**0.5) + 1):
                if num % k == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"Prime number: {num}")


