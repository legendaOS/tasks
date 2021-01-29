def goto(coord):
    ret = []
    ret.append([coord[0] - 1, coord[1] - 2])
    ret.append([[coord[0] - 2, coord[1] - 1])
    ret.append([coord[0] - 2, coord[1] + 1])
    ret.append([coord[0] - 1, coord[1] + 2])