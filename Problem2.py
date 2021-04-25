from collections import Counter

#suppose l1 is input array
l1 = [1,3,4,8,2,9,4,1,0]

rev = sorted(l1, reverse= True)

if l1 == rev:
    print("No Higher number possible")
else:
    # l1 = [1,2,3,3,7]
    count1 = Counter(l1)
    int1 = sum(d * 10**i for i, d in enumerate(l1[::-1]))
    # print((int1))
    def increment (integer):
        x = integer + 1
        l = [int(i) for i in str(x)]
        c = Counter(l)
        return x, c
    int2, count2 = increment(int1)
    # l2 = [int(i) for i in str(int2)]
    # count2 = Counter(l2)
    while( count1!= count2 ):
        int2, count2 = increment(int2)

    print(list(str(int2)))