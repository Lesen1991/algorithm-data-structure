origin = [8, 3, 5, 4, 6]


def insert_sort(ls):
    sort_list = []

    while len(ls) > 0:
        item = ls.pop()
        insert_index = 0
        for i in range(len(sort_list)):
            if item > sort_list[i]:
                insert_index = i + 1
        sort_list.insert(insert_index, item)
    return sort_list


print(insert_sort(origin))
