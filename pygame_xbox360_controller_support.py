
import pygame
import sys

LINUX = 0
WINDOWS = 1

if sys.platform == "linux":
    platform = LINUX
elif sys.platform == "win32":
    platform = WINDOWS

if platform == LINUX:
    L_JOYSCTICK_HOR = 0
    L_JOYSCTICK_VERT = 1
    R_JOYSCTICK_HOR = 3
    R_JOYSCTICK_VERT = 4
    LT = 2
    RT = 5
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    HOME = 8
    L_STICK_IN = 9
    R_STICK_IN = 10
    D_PAD_HOR = 0
    D_PAD_VERT = 1
elif platform == WINDOWS:
    L_JOYSCTICK_HOR = 0
    L_JOYSCTICK_VERT = 1
    R_JOYSCTICK_HOR = 2
    R_JOYSCTICK_VERT = 3
    LT = 4
    RT = 5
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    HOME = 10
    L_STICK_IN = 8
    R_STICK_IN = 9
    D_PAD_HOR = 0
    D_PAD_VERT = 1


class Controller():
    def __init__(self):
        pygame.joystick.init()
        
    def joysticks(self, controller: pygame.joystick.JoystickType) -> dict:
        return {
            "L_HOR": controller.get_axis(L_JOYSCTICK_HOR),
            "L_VERT": controller.get_axis(L_JOYSCTICK_VERT),
            "R_HOR": controller.get_axis(R_JOYSCTICK_HOR),
            "R_VERT": controller.get_axis(R_JOYSCTICK_VERT)
        }
    
    def triggers(self, controller: pygame.joystick.JoystickType) -> dict:
        return {
            "RT": controller.get_axis(RT),
            "LT": controller.get_axis(LT)
        }

    def buttons(self, controller: pygame.joystick.JoystickType) -> dict:
        return {
            "A": controller.get_button(A),
            "B": controller.get_button(B),
            "X": controller.get_button(X),
            "Y": controller.get_button(Y),
            "LB": controller.get_button(LB),
            "RB": controller.get_button(RB),
            "BACK": controller.get_button(BACK),
            "START": controller.get_button(START),
            "HOME": controller.get_button(HOME),
            "L_STICK_IN": controller.get_button(L_STICK_IN),
            "R_STICK_IN": controller.get_button(R_STICK_IN)
        }

    def d_pad(self, controller: pygame.joystick.JoystickType) -> dict:
        hat = controller.get_hat(0)
        
        return  {
            "hor": hat[D_PAD_HOR],
            "vert": hat[D_PAD_VERT]
        }