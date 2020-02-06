class LogDataStructure:
    def __init__(self,n):
        self.maxsize = n
        self.log = list()

    def __repr__(self):
        return str(self.log)

    def record(self, orderId):
        self.log.append(orderId)
        if len(self.log) > self.maxsize:
            self.log = self.log[1:]

    def getLast(self,i) -> int:
        return self.log[-i]



if __name__ == "__main__":
    log = LogDataStructure(5)
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
    print(log.log)
    assert log.getLast(4) == 5
    assert log.getLast(1) == 8
    