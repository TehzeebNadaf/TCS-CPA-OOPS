class Item:
    def __init__(self, ilist, idict):
        self.ilist = ilist
        self.idict = idict
    def cal_price(self):
        l1 = []
        t = 0
        for i in self.idict:
            for j in self.ilist:
                if i==j[0]:
                    if j[2]>self.idict[i] or j[2]==self.idict[i]:
                        j[2] = j[2] - self.idict[i]
                        t = j[1]*self.idict[i]
                        l1.append(t)
                    else:
                        return 0
        return l1

class Store(Item):
    def __init__(self, ilist, idict):
        Item.__init__(self, ilist, idict)
    def gen_bill(self):
        a = Item(self.ilist, self.idict).cal_price()
        bill = 0
        l2 = []
        for i in a:
            bill += i 
            l2.append(bill)
        return l2
          
if __name__ == '__main__':
    n = int(input())
    il = []
    ilist = []
    for x in range(n):
        iid = int(input())
        iname = input()
        iprice = int(input())
        iq = int(input())
        il = [iname, iprice, iq] 
        ilist.append(il)

    m = int(input())
    idict = {}
    for y in range(m):
        rname = input()
        rq = int(input())
        idict[rname] = rq

    res = Store(ilist, idict).gen_bill()
    for num in res:
        print(num)
