from modules import button_presser
from config import config


def shiny_test(self, target_window):
    loop_keys = ['z', 'return', 'down', 'x', 'x', 'x']

    button_presser.gift_loop_combination(self, target_window, loop_keys)


def route1_loop(self, target_window):
    button_presser.wild_loop_combination_side(self, target_window, config.ROUTE1)


def route22_loop(self, target_window):
    button_presser.wild_loop_combination_side(self, target_window, config.ROUTE22)


def route8_loop(self, target_window):
    button_presser.wild_loop_combination_vert(self, target_window, config.ROUTE8)


def viridian_forest_loop(self, target_window):
    button_presser.wild_loop_combination_side(self, target_window, config.VIRIDIAN_FOREST)


def snorlax_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys, config.SNORLAX)


def legends_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'x', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys, config.LEGENDS)


def starter_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'x', 'x', 'x', 'z', 'x', 'x', 'x', 'return', 'x', 'x', 'x']

    button_presser.gift_loop_combination(self, target_window, loop_keys)


def eevee_loop(self, target_window):
    loop_keys = ['z', 'x', 'z', 'return', 'down', 'x', 'down', 'x', 'x']

    button_presser.gift_loop_combination(self, target_window, loop_keys)


def fossil_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'z', 'z', 'return', 'down', 'x', 'down', 'x', 'x']

    button_presser.gift_loop_combination(self, target_window, loop_keys)
