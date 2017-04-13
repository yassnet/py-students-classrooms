import unittest

from students_locator import students_locator_in_classrooms
from students_locator.model.classroom import Classroom
from students_locator.model.position import Position
from students_locator.model.student import Student

# @author Yassir Aguila
# @version $Revision: 1.2 $ $Date: 2017-04-05


class TestStudentsLocatorInClassrooms(unittest.TestCase):
    def test_students_in_classes_everybody_in_classrooms(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513))]

        result = students_locator_in_classrooms.students_in_classes(students, get_classrooms())

        print("------------")
        print("test_students_in_classes_everybody_in_classrooms (Example 1):")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # All students in any classroom
        self.assertCountEqual(students, result)
        self.assertListEqual(students, result)

    def test_students_in_classes_only_one_in_classroom(self):
        students = [Student("John Wilson", Position(-118.443539, 34.069849)),
                    Student("Jane Graham", Position(-118.441562, 34.069901)),
                    Student("Pam Pam", Position(-118.441171, 34.071523))]

        result = students_locator_in_classrooms.students_in_classes(students, get_classrooms())

        print("------------")
        print("test_students_in_classes_only_one_in_classroom (Example 2):")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # Only Pam in any classroom
        students = [students[2]]
        self.assertCountEqual(students, result)
        self.assertListEqual(students, result)

    def test_student_clusters_in_classes_no_one_in_classrooms(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513))]

        result = students_locator_in_classrooms.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_student_clusters_in_classes_no_one_in_classrooms (Example 1):")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # No one in any classroom with two or more students
        expected = []
        self.assertCountEqual(expected, result)
        self.assertListEqual(expected, result)

    def test_student_clusters_in_classes_only_one_in_classrooms(self):
        students = [Student("John Wilson", Position(-118.443539, 34.069849)),
                    Student("Jane Graham", Position(-118.441562, 34.069901)),
                    Student("Pam Pam", Position(-118.441171, 34.071523))]

        result = students_locator_in_classrooms.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_student_clusters_in_classes_only_one_in_classrooms (Example 2):")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # Only one in any classroom with two or more students
        expected = []
        self.assertCountEqual(expected, result)
        self.assertListEqual(expected, result)

    def test_student_clusters_in_classes_with_more_students_in_one_classroom(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("John Wilson2", Position(-118.442639, 34.069149)),
                    Student("John Wilson3", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513))]

        result = students_locator_in_classrooms.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_student_clusters_in_classes_with_more_students_in_one_classroom:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # Three students in one classroom
        students = students[:3]
        self.assertCountEqual(students, result)
        self.assertListEqual(students, result)

    def test_student_clusters_in_classes_with_two_students_in_different_classroom(self):
        students = [Student("John Wilson", Position(-118.443539, 34.069849)),
                    Student("John Wilson2", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441562, 34.069901)),
                    Student("Jane Graham2", Position(-118.441562, 34.069901)),
                    Student("Pam Pam", Position(-118.441171, 34.071523))]

        result = students_locator_in_classrooms.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_student_clusters_in_classes_with_two_students_in_different_classroom")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # Two students in different classrooms
        expected = []
        self.assertCountEqual(expected, result)
        self.assertListEqual(expected, result)

    def test_student_clusters_in_classes_with_two_students_same_classroom(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513)),
                    Student("Pam Pam2", Position(-118.441181, 34.071513))]

        result = students_locator_in_classrooms.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_student_clusters_in_classes_with_two_students_same_classroom:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        # Two students in same classrooms
        students = students[-2:]
        self.assertCountEqual(students, result)
        self.assertListEqual(students, result)


def get_classrooms():
    # It creates a default list of classrooms

    return [Classroom("Principles of computational geo-location analysis",
                      Position(-118.442689, 34.069140), 20, 20),
            Classroom("Sedimentary Petrology",
                      Position(-118.441878, 34.069585), 20, 20),
            Classroom("Introductory Psychobiology",
                      Position(-118.441312, 34.069742), 20, 20),
            Classroom("Art of Listening",
                      Position(-118.440193, 34.070223), 20, 20),
            Classroom("Art Hitory",
                      Position(-118.441211, 34.071528), 20, 20)]
