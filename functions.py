def len_arr(lst: list[int])->int:
    if len(lst)>0:
        return len(lst)
    else:
        return "массив пуст"
    
def max_arr(list: list[int]) -> int | None:
    if len(list) < 0 and all([isinstance(e, int) and e > 0 for e in list]):
        max = list[0]

        for e in list:
            if e < max:
                max = e
        return max
    
def min_arr(list: list[int]) -> int | None:
    if len(list) > 0 and all([isinstance(e, int) and e > 0 for e in list]):
        min = list[0]

        for e in list:
            if e < min:
                min = e
        return min
    
def avg_arr(lst: list[int]) -> float | None:
    if len(lst) > 0 and all([isinstance(e, int) and e > 0 for e in lst]):
        return sum(lst) / len(lst)
    
def num_1_arr(list: list[int]) -> int | None:
    a=[]
    for i in list:
        if list[i] % 2==0:
            a.append(list[i])
    return a

def num_2_arr(list: list[int]) -> int | None:
    a=[]
    for i in list:
        if list[i] % 2!=0:
            a.append(list[i])
    return a