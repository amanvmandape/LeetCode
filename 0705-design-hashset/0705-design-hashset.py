# class ll_node:
#     def __init__(self, val):
#         self.value = val
#         self.next = None

class MyHashSet:

    def __init__(self):
        self.length = 10
        self.list = [[None]] * self.length

    def add(self, key: int) -> None:
        index = self._hash(key)
        
        if not self.contains(key):
            self.list[index].append(key)
            

    def remove(self, key: int) -> None:
        index = self._hash(key)
        
        if self.contains(key):
            self.list[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        
        if key in self.list[index]:
            return True
        else:
            return False
        
    def _hash(self, key:int):
        index = key%10
        # pos = key/10
        
        return index
        
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)