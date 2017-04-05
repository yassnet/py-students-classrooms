import geolocation_util
import unittest
from classroom import Classroom
from student import Student
from src.position import Position


def get_classrooms():
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


class TestGeoLocationUtil(unittest.TestCase):
    def test_example_1(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513))]

        result = geolocation_util.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("Example 1:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        self.assertEquals(0, len(result))

    def test_example_2(self):
        students = [Student("John Wilson", Position(-118.443539, 34.069849)),
                    Student("Jane Graham", Position(-118.441562, 34.069901)),
                    Student("Pam Pam", Position(-118.441171, 34.071523))]

        result = geolocation_util.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("Example 2:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        self.assertEquals(0, len(result))

    def test_with_more_students_in_one_room(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("John Wilson2", Position(-118.442639, 34.069149)),
                    Student("John Wilson3", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513))]

        result = geolocation_util.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_with_more_students_in_one_room:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        self.assertEquals(3, len(result))
        self.assertEquals("John Wilson", result[0].name)
        self.assertEquals("John Wilson2", result[1].name)
        self.assertEquals("John Wilson3", result[2].name)

    def test_with_two_students_in_different_classroom(self):
        students = [Student("John Wilson", Position(-118.443539, 34.069849)),
                    Student("John Wilson2", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441562, 34.069901)),
                    Student("Jane Graham2", Position(-118.441562, 34.069901)),
                    Student("Pam Pam", Position(-118.441171, 34.071523))]

        result = geolocation_util.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_with_two_students_in_different_classroom")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        self.assertEquals(0, len(result))

    def test_with_more_students_in_one_room3(self):
        students = [Student("John Wilson", Position(-118.442639, 34.069149)),
                    Student("Jane Graham", Position(-118.441862, 34.069601)),
                    Student("Pam Pam", Position(-118.441181, 34.071513)),
                    Student("Pam Pam2", Position(-118.441181, 34.071513))]

        result = geolocation_util.student_clusters_in_classes(students, get_classrooms())

        print("------------")
        print("test_with_more_students_in_one_room 3:")
        if len(result) == 0:
            print("(Empty)")
        for res in result:
            print(res.name)

        self.assertEquals(2, len(result))
        self.assertEquals("Pam Pam", result[0].name)
        self.assertEquals("Pam Pam2", result[1].name)
