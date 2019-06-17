def getremove_last(l):
    assert len(l) > 0, "AssertionError"
    longitud = len(l)
    val = l[longitud -1]
    rest_list = l[:-1]
    return val, rest_list
