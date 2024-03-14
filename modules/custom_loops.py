from modules import button_presser

RAT = (173, 154, 90)
BIRD = (231, 219, 0)

ROUTE1 = [RAT, BIRD]


def shiny_test(self, target_window):
    loop_keys = ['z', 'return', 'down', 'x', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys)


def route1_loop(self, target_window):
    button_presser.wild_loop_combination(self, target_window, ROUTE1)


def starter_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'x', 'x', 'x', 'z', 'x', 'x', 'x', 'return', 'x', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys)


def eevee_loop(self, target_window):
    loop_keys = ['z', 'x', 'z', 'return', 'down', 'x', 'down', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys)


def aero_loop(self, target_window):
    loop_keys = ['z', 'x', 'x', 'z', 'z', 'return', 'down', 'x', 'down', 'x', 'x']

    button_presser.stationary_loop_combination(self, target_window, loop_keys)
