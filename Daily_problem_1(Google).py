
def validate():
    data =  [10, 15, 3, 7]
    k = 17
    for i in data:
        data.remove(i)
        if (k -i) in data:
            return True
    return False

if __name__ == "__main__":
    if validate():
        print("Present")
    else:
        print("Not Present")