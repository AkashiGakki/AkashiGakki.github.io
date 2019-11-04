def count():
    x = 1
    while x:
        if 50 + x * 15 <= 30 * x:
            return x
        x = x + 1

if __name__ == "__main__":
    res = count()
    print(res)