from utils import get_data_lines


def parse_nanobot(data_line):
    # sample record pos=<1,3,1>, r=1
    tokens = data_line.split(' ')
    radius = int(tokens[1][2:])
    char_coords = tokens[0][5:][:-2].split(',')
    coords = [int(x) for x in char_coords]
    return (coords, radius)


def find_strongest(data):
    cur_max = 0
    cur_idx = -1
    for idx, bot in enumerate(data):
        if bot[1] > cur_max:
            cur_idx = idx
            cur_max = bot[1]
    print(f'{cur_idx=} {cur_max=}')
    return data[cur_idx]


def manhattan_distance(p1, p2):
    return sum([abs(p1[x] - p2[x]) for x in range(len(p1))])


def in_range(bot, origin, distance):
    return distance <= manhattan_distance(bot[0], origin[0])


if __name__ == '__main__':
    sample, full = get_data_lines(23)
    data = []
    for line in sample:
        data.append(parse_nanobot(line))

    find_strongest(data)
    # full_data = []
    # for line in full:
    #     full_data.append(parse_nanobot(line))
    print(data)
    # print(full_data)