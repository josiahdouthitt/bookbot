def get_num_words(contents):
    count = len(contents.split())
    return count


def get_word_count(contents):
    result = {}
    for i in contents.lower():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    
    return result

def sort_on(dict):
    return dict["num"]

def make_count_list(counts):
    result = []
    for i in counts:
        result.append({"char": i, "num": counts[i]})
    
    result.sort(reverse=True, key=sort_on)
    return result