class Classroom:
    def __init__(self, name, position, width, height):
        self.name = name
        self.position = position
        self.max_x_position = position.x + height / 2
        self.min_x_position = position.x - height / 2
        self.max_y_position = position.y + width / 2
        self.min_y_position = position.y - width / 2
        self.no_students = 0

