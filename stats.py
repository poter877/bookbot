def get_num_words(text: str):
    return len(text.split(" "))


def get_char_count(texts: str):
    result = {}
    for text in texts:
        if text in result:
            result[text] += 1
        else:
            result[text] = 1
    return result


def sort_words(texts: str):
    texts_dict = get_char_count(texts=texts)
    result = []
    for text in texts_dict:
        result.append({"num": texts_dict[text], "name": text})
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(items):
    return items["num"]
