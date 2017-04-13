# @author Yassir Aguila
# @version $Revision: 1.0 $ $Date: 2017-04-05
#
# Classroom model class


class Classroom:
    RECTANGLE_DIVIDER = 2

    def __init__(self, name, position, width, height):
        self.name = name
        self.position = position

        # Maximum X position inside classroom
        self.max_x_position = (position.x + (height / self.RECTANGLE_DIVIDER))

        # Minimum X position inside classroom
        self.min_x_position = (position.x - (height / self.RECTANGLE_DIVIDER))

        # Maximum Y position inside classroom
        self.max_y_position = (position.y + (width / self.RECTANGLE_DIVIDER))

        # Minimum Y position inside classroom
        self.min_y_position = (position.y - (width / self.RECTANGLE_DIVIDER))

        # Counter of students inside classroom
        self.no_students = 0

    def is_inside(self, position):
        return self.min_x_position < position.x < self.max_x_position and \
               self.min_y_position < position.y < self.max_y_position

