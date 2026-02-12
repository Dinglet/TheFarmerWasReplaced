import utils


def plant_column(x):
    utils.move_to(x, 0)
    for y in range(get_world_size()):
        if get_entity_type() != Entities.Cactus:
            harvest()
        utils.plant_cactus()
        move(North)
    return


def harvest_cactus():
    for x in range(get_world_size()):
        plant_column(x)
    for x in range(get_world_size()):
        cocktail_sort(x)
    for y in range(get_world_size()):
        cocktail_sort(y, False)
    harvest()
    return


def cocktail_sort(x, north_south=True):
    def move_to_yx(x, y):
        utils.move_to(y, x)

    if north_south:
        move_fn = utils.move_to
        direction = North
    else:
        move_fn = move_to_yx
        direction = East

    start = 0
    end = get_world_size() - 1
    while start < end:
        swapped = False
        for j in range(start, end):
            move_fn(x, j)
            if measure() > measure(direction):
                swap(direction)
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for j in range(end - 1, start - 1, -1):
            move_fn(x, j)
            if measure() > measure(direction):
                swap(direction)
                swapped = True
        if not swapped:
            break
        start += 1
    return


def gnome_sort(x, north_south=True):
    def move_to_yx(x, y):
        utils.move_to(y, x)

    if north_south:
        move_fn = utils.move_to
        direction = North
    else:
        move_fn = move_to_yx
        direction = East

    y = 0
    progress = 0
    # cacti[0], ..., cacti[progress] are non-decreasing
    end = get_world_size() - 1
    while progress < end:
        move_fn(x, y)
        if measure() > measure(direction):
            swap(direction)
            if y:
                y = y - 1
            else:
                progress = progress + 1
                y = progress
        else:
            progress = progress + 1
            y = progress
    return


if __name__ == "__main__":
    set_world_size(4)
    harvest_cactus()
