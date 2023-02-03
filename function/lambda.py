func = lambda x: print(x * 10)
func(9)

names = ['a', 'b', 'c', 'd']
new_names = list(map(lambda x: x + 'さん', names))
print(new_names)

n1 = ['a', 'b', 'c', 'd']
n2 = ['A', 'B', 'C', 'D']
new_n = list(map(lambda x, y: x + y + 'さん', n1, n2))
print(new_n)

nums = [x for x in range(1, 11)]
new_nums  = list(filter(lambda x: x >= 5, nums))
print(new_nums)
