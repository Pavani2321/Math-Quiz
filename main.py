def add_numbers(a,index_nums):
    total = 0
    length = len(index_nums)
    for i in range(length):
        if index_nums[i] in a:
            num_count = a.count(index_nums[i])
            total+=index_nums[i]*num_count
    return total
a=list(map(int,input().split()))
a.sort()
t=int(input())
for p in range(t):
    m,n = input().split()
    m,n = int(m),int(n)
    index_nums = []
    for i in range(m,n+1):
        index_nums.append(i)
    result = add_numbers(a,index_nums)
    print(result)
