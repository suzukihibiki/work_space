def solution(x):
    string = str(x)
    if string[0] == '-':return '-'+string[:0:-1]
    else:return string[::-1]

print(solution(-231)) # => -123
print(solution("suzuki hibiki")) # => 543
print(solution(795))