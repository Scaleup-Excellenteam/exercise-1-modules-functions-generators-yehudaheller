def join(*lists, sep='-'):
    result = []
    for i, lst in enumerate(lists):
        # print(f"index = {i} and list item = {lst} \n")
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(sep)

    print(result)


join([1, 2], [8], [9, 5, 6])
