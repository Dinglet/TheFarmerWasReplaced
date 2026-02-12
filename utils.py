def plant_grass():
    if get_ground_type() != Grounds.Grassland:
        plant(Entities.Grass)
    return


def plant_bush():
    plant(Entities.Bush)
    maintain_water_level(0.75)
    return


def plant_tree():
    plant(Entities.Tree)
    maintain_water_level(0.8)
    return


def plant_carrot():
    till_to(Grounds.Soil)
    plant(Entities.Carrot)
    maintain_water_level(0.75)
    return


def plant_pumpkin():
    till_to(Grounds.Soil)
    plant(Entities.Pumpkin)
    maintain_water_level(0.25)
    return


def plant_sunflower():
    till_to(Grounds.Soil)
    plant(Entities.Sunflower)
    maintain_water_level(0.75)
    return


def plant_cactus():
    till_to(Grounds.Soil)
    plant(Entities.Cactus)
    return


PLANT_HANDLERS = {
    Entities.Grass: plant_grass,
    Entities.Bush: plant_bush,
    Entities.Tree: plant_tree,
    Entities.Carrot: plant_carrot,
    Entities.Sunflower: plant_sunflower,
    Entities.Pumpkin: plant_pumpkin,
    Entities.Cactus: plant_cactus
}


def harvest_and_plant(type):
    harvest()
    PLANT_HANDLERS[type]()
    return


def till_to(ground):
    if get_ground_type() != ground:
        till()
    return


def move_to(x, y = None):
    if y == None:
        x, y = x[0], x[1]
    world_size = get_world_size()
    right_moves = x - get_pos_x()
    up_moves = y - get_pos_y()

    if 2*right_moves > world_size:
        right_moves -= world_size
    if 2*right_moves < -world_size:
        right_moves += world_size

    if 2*up_moves > world_size:
        up_moves -= world_size
    if 2*up_moves < -world_size:
        up_moves += world_size

    if right_moves >= 0:
        for i in range(right_moves):
            move(East)
    else:
        for i in range(-right_moves):
            move(West)

    if up_moves >= 0:
        for i in range(up_moves):
            move(North)
    else:
        for i in range(-up_moves):
            move(South)
    return


def move_to_next(xlim = get_world_size(), ylim = get_world_size()):
    x, y = get_pos_x(), get_pos_y()
    if x + 1 > xlim or y + 1 > ylim:
        move_to(0, 0)
        return
    if y + 1 == ylim:
        if x + 1 == xlim:
            move_to(0, 0)
            return
        move_to(x+1, 0)
        return
    move(North)


def maintain_water_level(level = 0.25):
    while get_water() < level:
        use_item(Items.Water)
    return


GROWING_TIME = {
    Entities.Grass: 0.5,
    Entities.Bush: 4,
    Entities.Tree: 7,
    Entities.Carrot: 6
}

def predict_harvest_time(type, factor = 1):
    if type not in GROWING_TIME:
        return 0
    return get_time() + GROWING_TIME[type] * factor