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
    data = [i for i in range(1,1000000)]
    data.remove(random.randint(1,1000000))
    print(min_missing(data))