import random
import time

d = []
for _ in range(10000):
    a = (random.choice([True, False]))
    b = (random.choice([True, False]))
    c = (random.choice([True, False]))
    d.append([a,b,c])

# 検証１
# Falseとnot
# =======================================================================================================
def v1():
    def main():
        s_time = time.time()
        e = []
        for id,i in enumerate(d):
            if all(i[0:3]) == True:
                e.append("ttt")
            if all(i[0:3]) == False:
                if (all(i[0:2]) == True) and (i[2] == False):
                    e.append("ttf")
                else:
                    e.append("oot")
        e_time = time.time()
        a =  e_time - s_time
        return a
    tt = []
    for _ in range(10000):
        tt.append(main())
    print("False仕様",sum(tt)/10000)

    def main2():
        s_time = time.time()
        e = []
        for id,i in enumerate(d):
            if all(i[0:3]) == True:
                e.append("ttt")
            if not all(i[0:3]) == True:
                if (all(i[0:2]) == True) and (i[2] == False):
                    e.append("ttf")
                else:
                    e.append("oot")
        e_time = time.time()
        a =  e_time - s_time
        return a
    tt = []
    for _ in range(10000):
        tt.append(main2())
    print("not仕様",sum(tt)/10000)

# 1回目=======================================================================================================
# not仕様 0.0036163734674453736
# False仕様 0.003610470366477966
# 2回目=======================================================================================================
# False仕様 0.003633445930480957
# not仕様 0.0036186809062957763
# =======================================================================================================


# 検証
# elseとif(明示的に条件を決める)
# =======================================================================================================
def v2():
    def main4():
        s_time = time.time()
        e = []
        for id,i in enumerate(d):
            if all(i[0:3])==True:
                e.append("a")
            if all(i[0:3]) == False:
                e.append("a")
        e_time = time.time()
        a =  e_time - s_time
        return a
    tt = []
    for _ in range(10000):
        tt.append(main4())
    print("ifのみ仕様",sum(tt)/10000)

    def main3():
        s_time = time.time()
        e = []
        for id,i in enumerate(d):
            if all(i[0:3])==True:
                e.append("a")
            else:
                e.append("a")
        e_time = time.time()
        a =  e_time - s_time
        return a
    tt = []
    for _ in range(10000):
        tt.append(main3())
    print("else有仕様",sum(tt)/10000)

# 1回目=======================================================================================================
# else有仕様 0.0016804442405700683
# ifのみ仕様 0.0026821977615356443
# 2回目=======================================================================================================
# else有仕様 0.0017045347213745117
# ifのみ仕様 0.0026985381841659545
# 3回目=======================================================================================================
# ifのみ仕様 0.002721876859664917
# else有仕様 0.0016976391315460205
# =======================================================================================================

# 検証
# if ...==True and ...==True and ...==True and 
# if all([...,...,...])
# =======================================================================================================
aaa = [True,False]
import random
import time

data1 = random.choice(aaa)
data2 = random.choice(aaa)
data3 = random.choice(aaa)
def v3():
    def main(data_1_,data_2_,data_3_):
        start = time.time()
        if data_1_ == True and data_2_ ==True and data_3_ ==True:
            anser = "a"
        else:
            anser = "b"
        end = time.time()
        how = end - start
        return how,anser
    toral_time= []
    toral_elem = []
    for i in range(100000):
        how_time,elem = main(data1,data2,data3)
        toral_time.append(how_time)
        toral_elem.append(elem)
    print(sum(toral_time)*1000000/len(toral_elem))
    print(len(toral_elem))

def v4():
    def main_2(data_1_,data_2_,data_3_):
        start = time.time()
        if all([data_1_,data_2_,data_3_]):
            anser = "a"
        else:
            anser = "b"
        end = time.time()
        how = end - start
        return how,anser
    toral_time= []
    toral_elem = []
    for i in range(100000):
        how_time,elem = main_2(data1,data2,data3)
        toral_time.append(how_time)
        toral_elem.append(elem)
    print(sum(toral_time)*1000000/len(toral_elem))
    print(len(toral_elem))
# 1回目=======================================================================================================
# 0.019619464874267578
# 100000
# 0.08985519409179688
# 100000
# 2回目=======================================================================================================
# 0.009968280792236328
# 100000
# 0.08083105087280273
# 100000
# 3回目=======================================================================================================
# 0.07004737854003906
# 100000
# 0.14616727828979492
# 100000
# =======================================================================================================
# 結果
# if ...Trueと明示的に指定した方が早いことが多い。=======================================================================================================


# 検証
# パターン１
# if (可能性が高い):
# if (可能性が低い):
# パターン２
# if (可能性が高い):
# elif(可能性が低い):
# パターン３
# if (可能性が高い):
# else (可能性が低い):
# パターン４
# if (可能性が低い):
# if (可能性が高い):
# パターン５
# if (可能性が低い):
# elif (可能性が低い):
# パターン６
# if (可能性が低い)
# else (可能性が高い)
# =======================================================================================================
aaa = [0,1,2,3,4,5,6,7,8,9]
x = []
for _ in range(1000000):
    x.append(random.choice(aaa))

def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        how = end - start
        print((how/1000000) * 100000000)
    return wrapper

@my_decorator
def v5():
    v_list = []
    for _x in x:
        if _x != 3:
            v_list.append(_x)
        if _x == 3:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v6():
    v_list = []
    for _x in x:
        if _x != 3:
            v_list.append(_x)
        elif _x == 3:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v7():
    v_list = []
    for _x in x:
        if _x != 3:
            v_list.append(_x)
        else:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v8():
    v_list = []
    for _x in x:
        if _x == 3:
            v_list.append(_x)
        if _x != 3:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v9():
    v_list = []
    for _x in x:
        if _x == 3:
            v_list.append(_x)
        elif _x != 3:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v10():
    v_list = []
    for _x in x:
        if _x == 3:
            v_list.append(_x)
        else:
            v_list.append(_x)
    print(len(v_list))

# 結果
# 検証1=======================================================================================================
# 7.702946662902832 4
# 6.896519660949707 3
# 6.579136848449707 1
# 7.937192916870117 5
# 8.196544647216797 6
# 6.799983978271485 2
# 検証２=======================================================================================================
# 7.422637939453125 4
# 6.674933433532716 3
# 6.449818611145019 1
# 7.902073860168457 6
# 7.601714134216309 5
# 6.531286239624024 2
# 検証３=======================================================================================================
# 8.629322052001953 5
# 7.216095924377441 1
# 7.231497764587402 2
# 8.705306053161621 6
# 8.028221130371094 4
# 7.30419158935547 3
# 検証４=======================================================================================================
# 8.183503150939941 6
# 6.543135643005371 2
# 6.499791145324707 1
# 7.961583137512206 4
# 8.121156692504883 5
# 6.801295280456543 3
# 検証５=======================================================================================================
# 7.5008392333984375 4
# 6.549072265625 3
# 6.453323364257813 2
# 7.899785041809082 6
# 7.596778869628907 5
# 6.365966796875001 1
# 考察=======================================================================================================
# 順位のまとめ
# パターン１：4 4 5 6 4：平均：4.6
# パターン２：3 3 1 2 3：平均：2.4
# パターン３：1 1 2 1 2：平均：1.4
# パターン４：5 6 6 4 6：平均：5.4
# パターン５：6 5 4 5 5：平均：5
# パターン６：2 2 3 3 1：平均：2.2
# パターン１、パターン４、パターン５が順不同だが、固定で下位にある。
# 逆説的にパターン２、パターン３、パターン６が、上位にあると言える。
# パターン４とパターン５は(可能性が低い),(可能性が高い)一度目で計算を終える確率が低く、余分に計算する確率が高いと言える。また、パターン６においては、if→elseの順番であるため、１度目に(可能性が低いもの)と、(それ以外)として、構文の順序とelseの強みを最大限に生かしているといえる。
# しかしながら、パターン６に比べて、パターン３(if(可能性高い),else(可能性低い))の方が早いことが多いという結果より、出現確立の低いものでも、出現確立の高いものでも必ず1度目の計算を通るためだと思われる。
# また、elseを用いたものが1位と2位であることより、elseを用いる方法がスピードに関しては得策であると言える。
# また、パターン３とパターン１を比べた際、結果に開きがある理由として、パターン３の方は最初で完結する確率が高く、パターン６では最初で完結する確率が低いからであると予想する。

# v5~v10の追加検証=======================================================================================================
# 判断基準が多い場合
# パターン１
# if if if if(可能性が高い):
# else (可能性が低い):
# パターン２
# if (可能性低い):
# else(可能性高い)

aaa = [0,1,2,3,4,5,6,7,8,9,10]
x = []
for _ in range(1000000):
    x.append([
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),
        random.choice(aaa),])

def my_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        how = end - start
        print((how/1000000) * 100000000)
    return wrapper

@my_decorator
def v11():
    v_list = []
    for _x in x:
        if (
            0 in _x) and (
            1 in _x) and (
            2 in _x) and (
            3 in _x) and (
            4 in _x) and (
            5 in _x) and (
            6 in _x) and (
            7 in _x) and (
            8 in _x) and (
            9 in _x):
            v_list.append(_x)
        else:
            v_list.append(_x)
    print(len(v_list))

@my_decorator
def v12():
    v_list = []
    for _x in x:
        if 10 in _x:
            v_list.append(_x)
        else:
            v_list.append(_x)
    print(len(v_list))

# 結果１=======================================================================================================
# 27.10099220275879
# 12.862873077392578
# 結果２=======================================================================================================
# 26.839208602905273
# 13.002705574035645
# 考察=======================================================================================================
# 以上の結果より条件式が多い場合には、1度目に出現確立が高いものを持ってくるアルゴリズムは最適な方法であるとは言えない。



# 検証
# 直接append,間接append,累算代入演算子(+=)で追加,内包表記
# =======================================================================================================
import time

def add_data():
    start = time.time()
    a = []
    for i in range(10000000):
        a.append(i)
    print(a[-1])
    end = time.time()
    print(end - start)

def add_data_1():
    start = time.time()
    a = []
    b = a.append
    for i in range(10000000):
        b(i)
    print(a[-1])
    end = time.time()
    print(end - start)

def add_data_2():
    start = time.time()
    a = []
    for i in range(10000000):
        a += [i]
    print(a[-1])
    end = time.time()
    print(end - start)

def add_data_3():
    start = time.time()
    a = [i for i in range(10000000)]
    print(a[-1])
    end = time.time()
    print(end - start)

# =======================================================================================================
# 結果
# 1回目
    # 0.5680763721466064
    # 0.4709484577178955
    # 0.6271297931671143
    # 0.3468317985534668
# 2回目
    # 0.5680763721466064
    # 0.4529397487640381
    # 0.631026029586792
    # 0.3501298427581787
# 3回目
    # 0.5680763721466064
    # 0.4525601863861084
    # 0.6775646209716797
    # 0.35092997550964355

# 結論=======================================================================================================
# 1位：内包表記
# 2位：間接append
# 3位：直接append
# 4位：累算代入演算子(+=)
# 内包表記が最も早いと言える。
# 考察=======================================================================================================
# 間接appendはappend先が固定されていて探す必要がないため直接appendするよりも早い結果になったと思われる。

# 累計計算速度
# ==========================================================================================================================
import time


def add_data():
    start = time.time()
    a = []
    b = a.append
    for i in range(10000000):
        b(i)
    a = sum(a)
    print(a)
    end = time.time()
    print(end - start)

def add_data():
    start = time.time()
    a = 0
    for i in range(10000000):
        a += i
    print(a)
    end = time.time()
    print(end - start)

def add_data():
    start = time.time()
    a = sum([i for i in range(10000000)])
    print(a)
    end = time.time()
    print(end - start)

add_data()

# =======================================================================================================
# 結果
# 1回目
    # 0.6285028457641602
    # 0.3616516590118408
    # 0.5719165802001953
# 2回目
    # 0.6369533538818359
    # 0.3695688247680664
    # 0.5650923252105713
# 3回目
    # 0.6414132118225098
    # 0.3649587631225586
    # 0.5574371814727783



# 検証
# bool式の判定
# =======================================================================================================
import time
import random

def bool_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if bool(a):
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

def bool_equal_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if bool(a) == True:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

def bool_equal2_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if bool(a) == False:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

def equal3_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if a:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

def equal4_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if a == True:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

# =======================================================================================================
# 結果
# 1回目
    # 0.4136819839477539
    # 0.43216419219970703
    # 0.43302464485168457
    # 0.3750326633453369
    # 0.38503122329711914
# 2回目
    # 0.4231569766998291
    # 0.43770313262939453
    # 0.4369978904724121
    # 0.3721184730529785
    # 0.3833475112915039
# 3回目
    # 0.41472601890563965
    # 0.4227614402770996
    # 0.42883944511413574
    # 0.3642427921295166
    # 0.3783540725708008
# 3回目
    # 0.42380237579345703
    # 0.42767858505249023
    # 0.4334132671356201
    # 0.3706667423248291
    # 0.38379454612731934

# 結論=======================================================================================================
# 無印が最も早い。

# 考察=======================================================================================================
# また、関数の実行順序を変えても速度が変わらないことより、関数の実行順序が結果に及ぼす可能性が低いことがうかがえる。
# 無印の方が早いことが結果よりわかるが、可読性的に、==Trueなどとした方が、保守性は優れているように思える



# 検証
# not　と　!=
# =======================================================================================================
def equal5_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True,False]))
        if not a:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)


def equal6_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([True, False]))
        if a != True:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)

def equal7_time():
    _lists = []
    _b = _lists.append
    start = time.time()
    for _ in range(1000000):
        a = (random.choice([0, 1]))
        if a == 1:
            _b(a)
    print(_lists[-1])
    end = time.time()
    print(end - start)
# =======================================================================================================
# 結果
# 1回目
    # 0.37717366218566895
    # 0.390270471572876
    # 0.3946988582611084
# 2回目
    # 0.3710291385650635
    # 0.3737306594848633
    # 0.38002729415893555
# 3回目
    # 0.38296079635620117
    # 0.3901543617248535
    # 0.3708674907684326

# 結論=======================================================================================================
# notがわずかに早い

# 考察=======================================================================================================


