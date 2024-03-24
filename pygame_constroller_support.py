
import pygame

class Controller():
    def __init__(self) -> None:
        pygame.joystick.init()
        
    def left_joystick(self, controller : pygame.joystick.JoystickType) -> dict:
        return  {
            "hor": controller.get_axis(0),
            "vert": controller.get_axis(1)
        }
    
    def right_joystick(self, controller : pygame.joystick.JoystickType) -> dict:
        return  {
            "hor": controller.get_axis(3),
            "vert": controller.get_axis(4)
        }

    def triggers(self, controller : pygame.joystick.JoystickType) -> dict:
        return  {
            "RT": controller.get_axis(2),
            "LT": controller.get_axis(5)
        }

    def buttons(self, controller : pygame.joystick.JoystickType) -> dict:
        return  {
            "A": controller.get_button(0),
            "B": controller.get_button(1),
            "X": controller.get_button(2),
            "Y": controller.get_button(3),
            "LB": controller.get_button(4),
            "RB": controller.get_button(5),
            "BACK": controller.get_button(6),
            "START": controller.get_button(7),
            "HOME": controller.get_button(8),
            "L_STICK_IN": controller.get_button(9),
            "R_STICK_IN": controller.get_button(10)
        }

    def d_pad(self, controller : pygame.joystick.JoystickType) -> dict:
        hat_x, hat_y = controller.get_hat(0)
        return  {
            "hor": hat_y,
            "vert": hat_x
        }