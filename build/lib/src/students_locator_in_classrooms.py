# @author Yassir Aguila
# @version $Revision: 1.0 $ $Date: 2017-04-05


def students_in_classes(students, rooms):
    # students_in_classes(List(Student), List(Classroom))
    # returns: List(Student)
    # This function determines which students are physically in any classroom.
    
    student_in_classrooms = []
    for student in students:
        if is_student_in_any_room(student, rooms):
            student_in_classrooms.append(student)

    return student_in_classrooms


def student_clusters_in_classes(students, rooms):
    # student_clusters_in_classes(List(Student), List(Classroom))
    # returns: List(Student)
    # This function determines which students are physically in any classroom with two or more students in it.

    student_clusters_in_classrooms = []
    for student in students_in_classes(students, rooms):
        if student.classroom.no_students >= 2:
            student_clusters_in_classrooms.append(student)

    return student_clusters_in_classrooms


def is_student_in_any_room(student, rooms):
    # is_student_in_any_room(student, List(Classroom))
    # returns: List(Student)
    # This function determines if student is physically in any classroom.

    res = False
    for room in rooms:
        if room.is_inside(student.position):
            student.classroom = room
            room.no_students += 1
            res = True
            break
    return res
