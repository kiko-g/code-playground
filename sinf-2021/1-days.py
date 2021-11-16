from sys import maxsize

if __name__ == '__main__':
    days = int(input())
    pf_array = [int(elem) for elem in input().split()]

    max_global = -maxsize - 1
    max_current = 0

    for i in range(0, days):
        max_current = max_current + pf_array[i]
        if max_global < max_current:
            max_global = max_current

        if max_current < 0:
            max_current = 0

    print(max_global)
