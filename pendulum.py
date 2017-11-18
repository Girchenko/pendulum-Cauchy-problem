import numpy as np
import pygame
from pygame.locals import *

# 1 - Euler method; 2 - Runge–Kutta method
method = 2
x = 75 * np.pi / 180
h = 0.05
pen_l = 100 * 0.02
pen_g = 9.81
penLength = pen_l * 150


def get_f(t, angle, v):
    return - pen_g * np.sin(angle)/ pen_l


def Euler(t, x, v):
    y_new = v + h * get_f(t, x, v)
    x_new = x + h * y_new
    return x_new, y_new


def RK4(t, x, v):
    kx1 = v
    kv1 = get_f(t, x, v)

    kx2 = v + h * kv1 / 2
    kv2 = get_f(t + h / 2, x + h * kx1 / 2, v + h * kv1 / 2)

    kx3 = v + h * kv2 / 2
    kv3 = get_f(t + h / 2, x + h * kx2 / 2, v + h * kv2 / 2)

    kx4 = v + h * kv3
    kv4 = get_f(t + h, x + h * kx3, v + h * kv3)

    dx = h * (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
    dv = h * (kv1 + 2 * kv2 + 2 * kv3 + kv4) / 6

    return x + dx, v + dv


def main():
    global x, method
    t = v = 0
    surface_w = 600
    surface_h = 600
    line_beginning_x_coordinate = surface_w /2
    line_beginning_y_coordinate = surface_h /10
    pygame.init()
    srf = pygame.display.set_mode((surface_w, surface_h))
    loop_flag = True
    #print(x, v)
    while loop_flag:
        for event in pygame.event.get(QUIT):
            loop_flag = False
        srf.fill((255, 255, 255))
        t += h
        if method == 1:
            [x, v] = Euler(t, x, v)
        else:
            [x, v] = RK4(t, x, v)
        #print(x, v)
        #print t
        updated_x = line_beginning_x_coordinate + penLength * np.sin(x)
        updated_y = line_beginning_y_coordinate + penLength * np.cos(x)

        # drawing line: surface, color, start_pos_coords, end_pos_coords, width

        pygame.draw.line(srf, (100, 100, 100), (10, surface_h /10), (surface_w - 30, surface_h / 10), 5)


        pygame.draw.line(srf, (255, 100, 100), (line_beginning_x_coordinate, line_beginning_y_coordinate),
                         (updated_x, updated_y), 3)
        # drawing circle: surface, color, x, y, r, width
        pygame.draw.circle(srf, (255, 100, 100), (int(updated_x), int(updated_y)), 20, 0)

        pygame.time.delay(30)
        pygame.display.flip()




if __name__ == "__main__":
    main()
