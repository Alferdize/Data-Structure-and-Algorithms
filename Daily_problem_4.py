"""
Dailyproblem4.py
"""
import random 


def min_missing(data):
    mini = min(i for i in data if i > 0)
    maxi = max(data)
    for i in range(mini,maxi):
        if i not in data:
            return i
    return maxi + 1










if __name__ == "__main__":
    data = [1, 2, 0]
    # data.remove(random.randint(1,10000))
    print(min_missing(data))