def solution(new_id):
    new_id = change(new_id)
    new_id = deleteChar(new_id)
    new_id = deleteDot(new_id)
    new_id = lengthCtrl(new_id)
    result = deleteDot(new_id)
    result = ''.join(result)
    return result


def change(id):
    id = id.lower()
    return id


def deleteChar(id):
    id = list(id)
    i = 0
    while (i < len(id)):
        if 97 <= ord(id[i]) <= 122 or ord(id[i]) == 46 or ord(id[i]) == 55 or ord(id[i]) == 137 or 48 <= ord(
                id[i]) <= 57 or ord(id[i]) == 95 or ord(id[i]) == 45:
            i += 1
        else:
            id.pop(i)
    return id


def deleteDot(id):
    i = 0
    while (i < len(id)):
        if i == 0:
            if id[i] == '.':
                id.pop(0)
                continue
        if i == len(id) - 1:
            if id[i] == '.':
                id.pop(i)
                continue

        if id[i] == '.':
            if i + 1 < len(id):
                if id[i + 1] == '.':
                    id.pop(i + 1)
                else:
                    i += 1
        else:
            i += 1
    return id


def lengthCtrl(id):
    if len(id) == 0:
        return 'aaa'
    elif len(id) >= 16:
        tmp = id[:15]
        return tmp
    elif len(id) <= 2:
        tmp = id.pop()
        while len(id) < 3:
            id.append(tmp)
        return id
    else:
        return id
