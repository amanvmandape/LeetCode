class OrderedStream:

    def __init__(self, n: int):
        self.length = n
        self.counter = 1
        self.table = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.table[idKey] = value
        self.return_list = []
        
        while self.counter <= self.length:
            if self.counter in self.table:
                self.return_list.append(self.table[self.counter])
                self.counter+=1
            else:
                break
                
        return self.return_list
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)