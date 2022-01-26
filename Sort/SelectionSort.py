


# 選択ソート
# ==========================================================================================================================

# コード節約
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def main(l):
    for i in range(len(l)-1):
        m=l.index(min(l[i:]),i)
        l[i],l[m]=l[m],l[i]
    return l

test_data = [5,2,4,6,1,3]
ancer_data = main(
    l = test_data
)

print(ancer_data)


# 汎用モデル : 速度優先
# ==========================================================================================================================

def main(l):
    n = len(l)
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            if l[min_i] > l[j]:min_i = j
        if min_i != i : l[min_i], l[i] = l[i], l[min_i]
    return l

test_data = [5,2,4,6,1,3]
ancer_data = main(
    l = test_data
)

print(ancer_data)





