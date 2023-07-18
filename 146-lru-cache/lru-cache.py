class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.free = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache[key] = self.cache.pop(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.free:
                self.free -= 1
            else:
                self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)