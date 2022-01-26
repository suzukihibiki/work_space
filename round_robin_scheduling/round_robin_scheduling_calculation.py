from collections import deque

def main(q, t_w):
    t_w = deque(t_w);add_t_w = t_w.append;l = [];time = 0
    while t_w:
        k,v = t_w.popleft();v = int(v)
        if v > q:
            v -= q;time += q;add_t_w([k,v])
        else:time += v;l += [f'{k} {time}']
    return l


q = 50 # cpu クオンタイム
task_name_weight = (["p1",100],["p2",200],["p3",300])

ancer_data = main(
    q = q,
    t_w = task_name_weight
)
print(ancer_data)