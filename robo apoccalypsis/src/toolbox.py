import pygame
import math


# get rotated
def get_rotated_image(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    new_rect = new_image.get_rect(center=rect.center)
    return new_image, new_rect
    # do the angle
def angle_between_points(x1, y1, x2, y2):
    x_difference = x2 - x1
    y_difference = y2 - y1
    angle = math.degrees(math.atan2(-y_difference, x_difference))
    return angle
