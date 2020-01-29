def is_char(code):
    code = int(code)
    return 0 if code > 26 or code < 1 else 1


def get_message_count(code_str):
    code_str = str(code_str)
    if len(code_str) == 1:
        count = is_char(code_str)
    elif len(code_str) == 2:
        count = 1 + is_char(code_str)
    else:
        count = get_message_count(int(code_str[1:]))
        if is_char(int(code_str[:2])):
            count += get_message_count(int(code_str[2:]))

    return count



assert get_message_count(81) == 1
assert get_message_count(11) == 2
assert get_message_count(111) == 3
assert get_message_count(1111) == 5
assert get_message_count(1311) == 4