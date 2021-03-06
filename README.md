# py-students-classrooms
Useful library made in python to handle students and classrooms

student_clusters_in_classes(students, rooms)

This function returns a list of students which are physically in any classroom with more than 2 students (using UTM projection to convert latitude and longitude coord to x and y expressed in meters)

<p>Assumptions<p>

- Each classroom has the a square or rectangular shape, every classroom has its dimensions.
- None of the classrooms intersect.
- Students are dimensionless outside of their latitude / longitude point
- Height is not a concern for either the student nor the classroom
- It does not matter which student was in which classroom, we only care about the list of students found
- This is intended to be performed in memory where you don’t have the usage of a database of some sort.
- This function uses UTM projection which has a deformation using high latitudes

Params:

students: list of students
classrooms list of classrooms

Return: list of students inside a classroom with more than two students

<p>Tests<p>

To run test go to root folder and execute nose2 (nose2 lib required)
