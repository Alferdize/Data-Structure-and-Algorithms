class Solution:
    pass
#     def numDecodings(self, code: str) -> int:
#         code_str = str(code)
#         if len(code_str) == 1:
#             count = 1
#         elif len(code_str) == 2:
#             count = 1 + self.is_char(code)
#         else:
#             count = self.numDecodings(int(code_str[1:]))
#             if self.is_char(int(code_str[:2])):
#                 count += self.numDecodings(int(code[2:]))
#         return count

#     def is_char(self, code):
#         code = int(code)
#         return 0 if code > 26 or code < 1 else 1


# if __name__ == "__main__":
#     solve = Solution()
#     print(solve.numDecodings('2277'))



def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def get_message_count(code):
    code_str = str(code)
    if len(code_str) == 1:
        count = 1
    elif len(code_str) == 2:
        count = 1 + is_char(code)
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
