def rec(param):
    if param == 1:
        return 1
    else:
        new_param = param - 1
        print(new_param)
        return rec(new_param)


rec(5)