import pygame
key = pygame.key.get_pressed()

k_left = "K_LEFT"
k_right = "K_RIGHT"
k_up = "K_UP"
k_down = "K_DOWN"
k_a = "K_a"
k_b = "K_b"
k_c = "K_c"
k_d = "K_d"
k_e = "K_e"
k_f = "K_f"
k_g = "K_g"
k_h = "K_h"
k_i = "K_i"
k_j = "K_j"
k_k = "K_k"
k_l = "K_l"
k_m = "K_m"
k_n = "K_n"
k_o = "K_o"
k_p = "K_p"
k_q = "K_q"
k_r = "K_r"
k_s = "K_s"
k_t = "K_t"
k_u = "K_u"
k_v = "K_v"
k_x = "K_x"
k_y = "K_y"
k_z = "K_z"
esc = "K_ESCAPE"
f1 = "K_F1"
f2 = "K_F2"
f3 = "K_F3"
f4 = "K_F4"
f5 = "K_F5"
f6 = "K_F6"
f7 = "K_F7"
f8 = "K_F8"
f9 = "K_F9"
f10 = "K_F10"
f11 = "K_F11"
f12 = "K_F12"
alt_left = "K_LALT"
alt_right = "K_RALT"
k_enter = "K_ENTER"
alt_F4 = alt_left + f4
alt_enter = "K_RETURN"

if key[alt_F4]:
    quit()

if key[alt_enter]:
    pygame.display.set_fullscreen(True)
