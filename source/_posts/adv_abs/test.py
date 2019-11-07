def print_params(**params):
    print(params)

def in_the_middle(x, *y, z):
    print(x, y, z)

def add(x, y):
    print(x+y)

def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1

    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

if __name__ == "__main__":
   seq = [34, 67, 8, 123, 4, 100, 95]
   seq.sort()
   print(seq)
   res = search(seq, 3)
   print(res)
