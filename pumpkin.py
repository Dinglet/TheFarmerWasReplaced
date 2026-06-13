import utils


def main():
    harvest_a_pumpkin()
    return


def harvest_a_pumpkin(size=1):
    utils.move_to(0, 0)
    positions = []
    for x in range(size):
        for y in range(size):
            positions.append((x, y))
    plant_pumpkins(positions)
    harvest()


def plant_pumpkins(positions):
    while positions:
        utils.move_to(positions[0])
        entity_type = get_entity_type()
        if entity_type == Entities.Pumpkin:
            if can_harvest():
                positions.pop(0)
        elif entity_type == Entities.Dead_Pumpkin:
            utils.plant_pumpkin()
            positions.append(positions.pop(0))
        else:
            if entity_type != None:
                while not can_harvest():
                    pass
                harvest()
            utils.plant_pumpkin()
            positions.append(positions.pop(0))
    return


if __name__ == "__main__":
    main()
