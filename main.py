
import pygame
import pygame_xbox360_controller_support

pygame.init()


screen = pygame.display.set_mode((300, 300))
Controller = pygame_xbox360_controller_support.Controller()
controllers = []
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)

pygame.display.set_caption("controller test")

x = 300
y = 300

def label(text: str, x: int, y: int):
    screen.blit(font.render(text, 1, (255, 255, 255)), (x, y))


run = True
while run:
    clock.tick(60)
    screen.fill(pygame.Color(51, 51, 51))


    for controller in controllers:
        j = Controller.joysticks(controller)
        t = Controller.triggers(controller)
        b = Controller.buttons(controller)
        d = Controller.d_pad(controller)
        label(f"L_HOR: {j['L_HOR']}", 10, 10)
        label(f"L_VERT: {j['L_VERT']}", 10, 25)
        label(f"R_HOR: {j['R_HOR']}", 10, 40)
        label(f"R_VERT: {j['R_VERT']}", 10, 55)
        label(f"RT: {t['RT']}", 10, 70)
        label(f"LT: {t['LT']}", 10, 85)
        label(f"A: {b['A']}", 10, 100)
        label(f"B: {b['B']}", 10, 115)
        label(f"X: {b['X']}", 10, 130)
        label(f"Y: {b['Y']}", 10, 145)
        label(f"LB: {b['LB']}", 10, 160)
        label(f"RB: {b['RB']}", 10, 175)
        label(f"BACK: {b['BACK']}", 10, 190)
        label(f"START: {b['START']}", 10, 205)
        label(f"HOME: {b['HOME']}", 10, 220)
        label(f"L_STICK_IN: {b['L_STICK_IN']}", 10, 235)
        label(f"R_STICK_IN: {b['R_STICK_IN']}", 10, 250)
        label(f"D_HOR: {d['hor']}", 10, 265)
        label(f"D_VERT: {d['vert']}", 10, 280)

                

    for e in pygame.event.get():
        if e.type == pygame.JOYDEVICEADDED:
            controllers.append(pygame.joystick.Joystick(e.device_index))
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    
    pygame.display.flip()

pygame.quit()