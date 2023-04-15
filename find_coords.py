def find_coords(toponym):
    lower = list(map(int, toponym["boundedBy"]["Envelope"]['lowerCorner'].split()))
    upper = list(map(int, toponym["boundedBy"]["Envelope"]['upperCorner'].split()))
    delta_1 = str(upper[0] - lower[0])
    delta_2 = str(upper[1] - lower[1])

    spn = ",".join([delta_1, delta_2])

    return spn
