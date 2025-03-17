import random

def fisher_yates(lst):
    n = len(lst)
    for i in range(n-1, -1, -1):
        #print(i, end=' ')
        r = random.randint(0, i)
        lst[i], lst[r] = lst[r], lst[i]
    return lst


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    random.seed(1234)
    for i in range(20):
        fisher_yates(lst)
        #print(f'i={i} ')
        print(lst)
