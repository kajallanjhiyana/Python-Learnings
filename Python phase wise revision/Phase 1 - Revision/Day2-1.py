nums = [2, 7, 5, 11, 15, 4]
target = 9
seen = {}
res = []

for i, n in enumerate(nums):
    need = target - n
    print(need)
    if need in seen:
        res.append([seen[need], i])   # save it and keep looping
        print(seen)
    seen[n] = i

print(res)   # [[0, 1], [2, 5]]
print(seen)