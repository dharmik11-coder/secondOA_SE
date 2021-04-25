

find_at = 16
idx = -1
num = 1
while True:
    s = str(num)
    idx += len(s)
    if idx >= find_at:
        idx -= len(s)
        print(f"At index {find_at} is element ->",s[find_at-idx-1])
        break
    # print(num)
    num += 1