class MyHashMap(dict):
    def put(self, key: int, value: int) -> None:
        self[key] = value

    def get(self, key: int) -> int:
        if key in self:
            return self[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self:
            del self[key]
