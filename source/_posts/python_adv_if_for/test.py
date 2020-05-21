seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = {k:str(v) for k, v in enumerate(seq) if v % 2 == 0}
print(res)
