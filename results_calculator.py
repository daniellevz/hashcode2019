


def load_data(filepath, is_data=False):
    f = open(filepath, 'r').read().split('\n')[:-1]
    num_of_photos = int(f.pop(0))
    if is_data:
        data = {i: line.split(' ')[2:] for i, line in enumerate(f)}
    else:
        data = {i: line.split(' ') for i, line in enumerate(f)}
    return num_of_photos, data

def score_couple(item1, item2):
    print ('comparing ' + str(item1) + ' and  ' + str(item2))
    common_tag = list(set(item1) & set(item2))
    unique1 = [item for item in item1 if item not in common_tag]
    unique2 = [item for item in item2 if item not in common_tag]
    print ('common tags are %s, item1 unique tags are %s, item2 unique tags are %s' % (str(common_tag), str(unique1), str(unique2)))
    score = min(len(common_tag), len(unique1), len(unique2))
    print ('score is %s' % (str(score)))
    return score

def get_list(data, index):
    l = data[int(index[0])]
    if len(index) > 1:
        l += data[int(index[1])]
    return list(set(l))

def score_all_chain(data_set_path, items_path):
    data_size, data = load_data(data_set_path, True)
    res_size, res = load_data(items_path)
    score = 0

    for i in res:
        if i+1 == len(res):
            continue

        current = get_list(data, res[i])
        next = get_list(data, res[i+1])

        score += score_couple(current, next)

    return score


