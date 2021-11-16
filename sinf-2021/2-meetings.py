def merge_ranges(minutes):
    minutes.sort(key=lambda x: x[0])
    merged_list = [(minutes[0])]

    for current_start_time, current_end_time in minutes[1:]:
        last_merged_start, last_merged_end = merged_list[-1]
        if current_start_time <= last_merged_end:
            merged_list[-1] = (last_merged_start, max(current_end_time, last_merged_end))
        else:
            merged_list.append((current_start_time, current_end_time))

    return merged_list

if __name__ == '__main__':
    n = int(input())
    minutes_array = []
    for i in range(0, n):
        a = [int(elem) for elem in input().split()]
        minutes_array.append((a[0], a[1]))

    print(len(merge_ranges(minutes_array)))
