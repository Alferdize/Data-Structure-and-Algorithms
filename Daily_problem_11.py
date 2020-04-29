def checking(prefix,set_of_substring):
    substr = []
    for i in set_of_substring:
        if i.startswith(prefix):
            substr.append(i)
    return substr

assert checking("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert checking("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert checking("ae", ["cat", "car", "cer"]) == []
assert checking("ae", []) == []
