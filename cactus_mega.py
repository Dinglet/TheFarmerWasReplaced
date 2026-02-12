import utils
from cactus import plant_column
from cactus import cocktail_sort


def plant_cacti():
    def handle():
        x = get_pos_x()
        while x < get_world_size():
            plant_column(x)
            x += max_drones()

    utils.move_to(0, 0)
    drones = []
    for _ in range(min(max_drones(), get_world_size())):
        drone = spawn_drone(handle)
        if drone:
            drones.append(drone)
        else:
            handle()
        move(East)
    for drone in drones:
        wait_for(drone)
    return


def sort_cacti_by_col():
    def handle():
        x = get_pos_x()
        while x < get_world_size():
            cocktail_sort(x, True)
            x += max_drones()

    utils.move_to(0, 0)
    drones = []
    num_drones = min(max_drones(), get_world_size())
    for _ in range(num_drones):
        drone = spawn_drone(handle)
        if drone:
            drones.append(drone)
        else:
            handle()
        move(East)
    for drone in drones:
        wait_for(drone)
    return


def sort_cacti_by_row():
    def handle():
        y = get_pos_y()
        while y < get_world_size():
            cocktail_sort(y, False)
            y += max_drones()

    utils.move_to(0, 0)
    drones = []
    num_drones = min(max_drones(), get_world_size())
    for _ in range(num_drones):
        drone = spawn_drone(handle)
        if drone:
            drones.append(drone)
        else:
            handle()
        move(North)
    for drone in drones:
        wait_for(drone)
    return


if __name__ == "__main__":
    plant_cacti()
    sort_cacti_by_col()
    sort_cacti_by_row()
    harvest()
