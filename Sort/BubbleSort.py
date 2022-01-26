
# バブルソート
# ==========================================================================================================================

# 分かりやすさ
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
# 1
def main(l):
    n = len(l);flag = 1;sorted_index = 0
    while flag:
        flag = 0
        for i in range(n-1, sorted_index, -1):  # N-1から1まで降順 
            if l[i] < l[i-1]:temp = l[i];l[i] = l[i-1];l[i-1] = temp;flag = 1
        sorted_index += 1
    return l

test_data = [5,3,2,4,1]
ancer_data = main(
    l = test_data
)
print(ancer_data)


# 速度
#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#  2
def main(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:l[j:j+2]=l[j+1],l[j]
    return l
            
            
test_data = [5,2,4,6,1,3]
ancer_data = main(
    l = test_data
)

print(ancer_data)


