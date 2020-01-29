def is_char(code):
    code = int(code)
    return 0 if code > 26 or code < 1 else 1

def get_message(code):
    code = str(code)
    if len(code) == 1:
        count = is_char(code)
    elif len(code) == 2:
        count = 1 + is_char(code)
    else:
        count = get_message(code[1:])
        if is_char(code[:2]):
            count += get_message(code[2:])
    return count



assert get_message(81) == 1
assert get_message(11) == 2
assert get_message(111) == 3
assert get_message(1111) == 5
assert get_message(1311) == 4