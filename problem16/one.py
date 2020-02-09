class Log:
    def __init__(self,n):
        self.maxsize = n
        self.log = list()

    def __repr__(self):
        return str(self.log)

    def record(self,data):
        self.log.append(data)
        if len(self.log) > self.maxsize:
            self.log = self.log[1:]

    def get_last(self,i) -> int:
        return self.log[-i]



if __name__ == "__main__":
    log = Log(5)
    log.record(1)
    log.record(2)
    assert log.log == [1, 2]
    log.record(3)
    log.record(4)
    log.record(5)
    assert log.log == [1, 2, 3, 4, 5]
    log.record(6)
    log.record(7)
    log.record(8)
    assert log.get_last(4) == 5
    assert log.get_last(1) == 8