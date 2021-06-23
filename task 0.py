from random import randint


def rand_arr():
    RArr = []
    for i in range(0, 30):
        RArr.append(randint(-100, 100))
    return RArr


def max_in_arr(arr):

    arr_a = list(enumerate(arr, 0))
    max_a = max(arr_i, key=lambda i: i[1])

    return max_a[1], max_a[0]


def unpaired_arr(arr):
    un_p_arr = []
    for a in arr:
        if a % 2 != 0:
            un_p_arr.append(a)
    if len(un_p_arr) == 0:
        return "there are no unpaired numbers"
    else:
        return un_p_arr


arr = rand_arr()
print("initial random list :\n", arr)
print("max num > ", max_in_arr(arr)[0], "\nposition of max num > ", max_in_arr(arr)[a]+1)


if isinstance(unpaired_arr(arr), list):
    print("list of unpaired numbers sorted from highest to lowest :\n",
          sorted(unpaired_arr(arr), reverse=True))
else:
    print(unpaired_arr(arr))
