with open('input_day1.txt') as f:
    ids = f.read().split()


def add_to_sorted_list(sorted_list: list, new_element: int):
    counter = 0
    for element in sorted_list:
        if new_element >= element:
            counter += 1
        else:
            break
    sorted_list.insert(counter, new_element)


def count_occurrences(sorted_list: list, new_element: int) -> int:
    counter = 0
    stop = False
    for element in sorted_list:
        if new_element == element:
            counter += 1
            stop = True
        else:  # once we find a match and the next is different, we can stop
            if stop:
                break
    return counter


# part 1
ids_sorted_first, ids_sorted_second = [], []
for i_first in range(0, len(ids), 2):
    id_first, id_second = int(ids[i_first]), int(ids[i_first + 1])

    add_to_sorted_list(ids_sorted_first, id_first)
    add_to_sorted_list(ids_sorted_second, id_second)

# sum diffs between elements
total_dist = 0
for i in range(len(ids_sorted_first)):
    total_dist += abs(ids_sorted_first[i] - ids_sorted_second[i])


print(total_dist)

# part 2
similarity_score = 0
for id_first in ids_sorted_first:
    count = count_occurrences(ids_sorted_second, id_first)
    similarity_score += id_first * count

print(similarity_score)
