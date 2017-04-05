def student_clusters_in_classes(students, rooms):
    student_in_classrooms = []
    student_clusters_in_classrooms = []
    for student in students:
        if is_in_any_room(student, rooms):
            student_in_classrooms.append(student)
    for student in student_in_classrooms:
        if student.classroom.no_students >= 2:
            student_clusters_in_classrooms.append(student)

    return student_clusters_in_classrooms


def is_in_any_room(student, rooms):
    res = False
    for room in rooms:
        if is_in_room(student, room):
            student.classroom = room
            room.no_students += 1
            res = True
            break
    return res


def is_in_room(student, room):
    return room.min_x_position < student.position.x < room.max_x_position and \
           room.min_y_position < student.position.y < room.max_y_position
