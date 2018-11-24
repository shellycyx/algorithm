def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]


def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_1 = i
        for j in range(i+1, n):

            if lst[j] < lst[min_1]:
                min_1 = j
        lst[i], lst[min_1] = lst[min_1], lst[i]


def insert_sort(lst):
    n = len(lst)
    for i in range(n-1):
        j = i+1
        while (lst[j] < lst[j-1]) and (j-1 >= 0):
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j=j-1


def quick_sort(lst, start, end):
    if start >= end:
        return
    left = start
    right = end
    mid = lst[left]
    while left < right:
        while (left < right) and (lst[right] >= mid):
            right -= 1
        lst[left] = lst[right]

        while (left < right) and (lst[left] < mid):
            left += 1
        lst[right] = lst[left]
    lst[left] = mid

    quick_sort(lst, start, left - 1)
    quick_sort(lst, left + 1, end)




if __name__ == "__main__":
    ll = [45, 13, 5, 50, 57, 10, 6, 3]
    print(ll)
    # bubble_sort(ll)
    # selection_sort(ll)
    # insert_sort(ll)
    quick_sort(ll, 0, len(ll) - 1)
    print(ll)


