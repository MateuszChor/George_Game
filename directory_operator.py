from os.path import join
from pathlib import Path

BASE_DIR = Path(__file__).absolute().parent


def get_background_image():
    return join(BASE_DIR, "Obiekty", "background_space.jpg")


def get_george_image():
    return join(BASE_DIR, "Obiekty", "George_walk_animation", "gerobe_standing_0.png")


print(get_george_image())
