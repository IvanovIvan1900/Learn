import pprint


def subsets_my(array_in: list) -> list:
    array_out = []
    array_out.append({})
    array_in_sort = sorted(array_in)
    len_array = len(array_in)
    for len_subset in range(1, len(array_in_sort)):
        curr_array_index = [x for x in range(len_subset)]
        curr_array_value = [array_in_sort[x] for x in range(len_subset)]
        array_out.append(curr_array_value.copy())
        # get next unical array
        gen_next = True
        index = len_subset- 1
        while(gen_next):
            if curr_array_index[index] == len_array:
                while(index > 0 and curr_array_index[index] == len_array):
                    index -= 1
                if index == 0 and curr_array_index[index] == len_array:
                    gen_next = False
                else:
                    # curr_array_index[index] += 1
                    uniqui = False
                    curr_array_index[index] += 1
                    while(index < len_subset):
                        if curr_array_value[index] != array_in_sort[curr_array_index[index]]:
                            uniqui = True
                            curr_array_value[index] == array_in_sort[curr_array_index[index]]
                        index += 1
                        if index < len_subset-1:
                            curr_array_index[index] = curr_array_index[index-1] + 1
                    index -= 1
                    if uniqui:
                        array_out.append(curr_array_value.copy())
                # while(index > 0 ):
                #     index -= 1
                #     if curr_array_index[index] == len_array:
                #         index -= 1
                #     else:
                #         curr_array_index[index] += 1
                #         while(index < len_subset-1):
                #             curr_array_value[index] != array_in_sort[curr_array_index[index]]
                #             index += 1
                #             if index > 0:
                #                 curr_array_index[index] = curr_array_index[index-1] + 1
                #         array_out.append(curr_array_value.copy())
                # if index == 0:
                #         break
                #     gen_next = False
                    
            else:
                if curr_array_value[index] != array_in_sort[curr_array_index[index]]:
                    curr_array_value[index] = array_in_sort[curr_array_index[index]]
                    array_out.append(curr_array_value.copy())
                curr_array_index[index] += 1

    return array_out


if __name__ == '__main__':
    pprint.pprint(subsets_my([1, 1, 2]))
    pprint.pprint(subsets_my([1, 2, 2]))
    pass
    # subsets([1, 2, 2]) -> [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    # subsets([1, 2, 3]) -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    # subsets([0]) -> [[], [0]]
