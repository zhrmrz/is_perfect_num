from math import log2
class Sol:
    def is_perfect_num(self,num):
        list=[]
        for i in range(1,int(log2(num)+2)):
            if num%i==0:
                list.append(i)
                list.append(num//i)
        print(sum(set(list)))
        if sum(set(list))==2*num:
            return True
        return False
