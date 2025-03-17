import random
from collections import defaultdict

def reservoir_sampling(lst, k):
    n = len(lst)
    res = lst[0:k]
    for i in range(k, n):
        r = random.randint(0, i)
        if r < k:
            res[r] = lst[i]
    return res

def test_generator(iterable, k):
    reservoir = []
    for i, item in enumerate(iterable):
        #print(f'i={i} item={item} k={k}')
        if i < k:
            reservoir.append(item)
        else:
            r = random.randint(0, i)
            #print(f'r={r}')
            if r < k:
                reservoir[r] = item
    return reservoir

def my_generator(lst):
    for item in lst:
        yield item


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    freq = defaultdict(int)
    random.seed(124)
    for i in range(100):
        res = reservoir_sampling(lst, 3)
        #print(f'i={i} ')
        #print(res)
        for j in res:
            freq[j] += 1
    print(freq)

    lst2 = ['a', 'b', 'c', 'd', 'e']
    freq2 = defaultdict(int)
    for i in range(2000):
        res = test_generator(my_generator(lst2), 3)
        for j in res:
            freq2[j] += 1
    print(freq2)

