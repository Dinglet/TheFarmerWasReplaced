# This script makes the "Pumpkin Master" achievement.
# A constraint to the achievement is that the water level of grounds must be maintained high enough.
import utils
import pumpkin


def main():
    n_pumpkins = num_items(Items.Pumpkin)
    start_time = get_time()
    pumpkin_master()
    elapsed_time = get_time() - start_time
    harvested_pumpkins = num_items(Items.Pumpkin) - n_pumpkins
    quick_print("Elapsed time:", elapsed_time, "seconds")
    quick_print("Harvested pumpkins:", harvested_pumpkins)
    quick_print("Rate:", harvested_pumpkins / elapsed_time * 60, "pumpkins/minute")
    return


def pumpkin_master(time_limit=60):
    start_time = get_time()
    def handle():
        while get_time() - start_time < time_limit:
            plant_a_pumpkin()
            harvest()

    SIZE = get_world_size()
    positions = []
    for y in range(0, SIZE - 6, 7):
        for x in range(0, SIZE - 6, 7):
            positions.append((x, y))
    positions = positions[:max_drones()//2]

    for position in positions:
        utils.move_to(position)
        if position == positions[-1] or not spawn_drone(handle):
            handle()
    return


def plant_a_pumpkin():
    x, y = get_pos_x(), get_pos_y()
    orig_x = (x // 7) * 7
    orig_y = (y // 7) * 7

    utils.move_to(orig_x + 3, orig_y)
    other = spawn_drone(plant_half_pumpkin)

    utils.move_to(orig_x, orig_y)
    plant_half_pumpkin()

    wait_for(other)
    return


def plant_half_pumpkin():
    orig_x, orig_y = get_pos_x(), get_pos_y()

    positions = []
    for x in range(orig_x, orig_x + 3):
        for y in range(orig_y, orig_y + 6):
            positions.append((x, y))
    pumpkin.plant_pumpkins(positions)
    return


if __name__ == "__main__":
    main()