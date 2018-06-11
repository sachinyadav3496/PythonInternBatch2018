class PowNum(object):
    def __init__(self,n=2,m=0):
        self.n = n
        self.m = m
    def __iter__(self):
        self.c = 0
        return self
    def __next__(self):
        if self.c <= self.m :
            self.c = self.c + 1
            r = self.n**self.c
            return r
        else :
            raise StopIteration("you have used all powers")

def main():
    p = PowNum(int(input("Number : ")),int(input("Max. Power : ")))
    p = iter(p)
    while input("Do want next Power then press something : ") :
        try : 
            n = next(p)
            print(n)
        except StopIteration as e :
            print("Error!",e)
            print("Do you want another number's power : ",end='\t')
            if input() :
                main()
if __name__ == "__main__":
    main()

