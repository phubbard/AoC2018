from utils import get_data_lines, manhattan_distance


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


def in_range(bot, origin, distance):
    return distance >= manhattan_distance(bot, origin)


if __name__ == '__main__':
    sample, full = get_data_lines(23)
    for dataset in [sample, full]:
        data = [parse_nanobot(x) for x in dataset]
        main_bot = find_strongest(data)
        in_range_bots = [x for x in data if in_range(x[0], main_bot[0], main_bot[1])]
        print(f'{len(in_range_bots)=}')
