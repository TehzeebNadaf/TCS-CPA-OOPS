class Book:
    def __init__(self, bl):
        self.bl = bl

class Lib(Book):
    def __init__(self, bl, ml):
        self.ml = ml
        Book.__init__(self, bl)
    def cb(self, c):
        self.c = c 
        count = 0
        for i in bl:
            if i[0]==c:
                count+=1
        return count 
    def rb(self):
        l = []
        for i in bl:
            if i not in ml:
                l.append(i)
        return l

if __name__ == '__main__':
    n = int(input())
    bl = []
    for x in range(n):
        bid = int(input())
        bname = input()
        bl.append(bname)
    c = input()
    m = int(input())
    ml = []
    for y in range(m):
        m1 = input()
        ml.append(m1)

    res = Lib(bl, ml).rb()
    print(Lib(bl, ml).cb(c), res[0], res[1])
