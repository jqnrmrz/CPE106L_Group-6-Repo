def mode(numbers):
 
    if not numbers:
        return 0
    number_count = {}
    for num in numbers:
        if num in number_count:
            number_count[num] += 1
        else:
            number_count[num] = 1
    max_count = max(number_count.values())
    mode_list = [num for num, count in number_count.items() if count == max_count]
    if len(mode_list) == 1:
        return mode_list[0]
    else:
        return 0