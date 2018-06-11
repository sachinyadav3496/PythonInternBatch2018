class Even:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        self.n += 2
        return self.n

