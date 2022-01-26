
# 挿入ソート
# ==========================================================================================================================


# 速度
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
# 1
def main(l):
    n = len(l)
    for i in range(n):
        a = l[i];j = i - 1
        while j >= 0 and l[j] > a:l[j+1] = l[j];j = j - 1
        l[j+1] = a
    return l

test_data = [5,8,3,2,1]
ancer_data = main(
    l = test_data
)
print(ancer_data)

# 2
def main(l):
    for i in range(1, len(l)):
        tmp = l[i];j = i - 1
        while (j >= 0) & (l[j] > tmp):l[j + 1] = l[j];j -= 1
        l[j + 1] = tmp
    return l

test_data = [5,8,3,2,1]
ancer_data = main(
    l = test_data
)
print(ancer_data)



# コード節約
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
# 3
def main(l):
    for i in range(1,len(l)+1):l[:i]=sorted(l[:i])
    return l

test_data = [5,8,3,2,1]
ancer_data = main(
    l = test_data
)
print(ancer_data)


