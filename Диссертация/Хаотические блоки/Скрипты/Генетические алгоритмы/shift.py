def shift(function, vector):
    vector = int(vector)
    if vector < 0:
        vector = abs(vector);
        for i in range(0, vector):
            function.append(function.pop(0));
    else:
        for i in range(0,vector):
            function.insert(0, function.pop())
    return function