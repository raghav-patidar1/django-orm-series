from random import choice

from django.db.models.functions import Lower
from core.models import Course, Student

def run():

    # Create 5 Course objects
    courses = ['Python', 'C++', 'C', 'Java', 'MERN']
    for course in courses:
        Course.objects.get_or_create(name=course)

    # Create 3 Student objects
    students = ['Rahul', 'Alice', 'Ananya']
    for student in students:
        Student.objects.get_or_create(name=student)

    courses = Course.objects.all()
    students = Student.objects.all()

    # ============= Add & Retrieve Relationships ============

    # Assign one course to each student
    for student in students:
        student.course.add(choice(courses))

    # Assign multiple courses to a student
    student = Student.objects.first()
    student.course.add(courses[0], courses[1])

    # Assign all courses to one student
    student = Student.objects.last()
    student.course.add(*courses)

    # Check how many courses a student is enrolled in
    student.course.count()

    # Retreive all courses of a particular student
    Student.objects.last().course.all()

    # check if a specific course is in the student's course list
    student.course.filter(name__iexact='mern').exists()


    # ============= Remove & Clear Relationships ============

    # Remove one course from a student
    student = Student.objects.first()
    course = Course.objects.first()
    if student.course.exists():
        student.course.remove(course)

    # Remove multiple courses a student is enrolled in
    student = Student.objects.last()
    courses = Course.objects.filter(name__in=['Python', 'C'])
    student.course.remove(*courses)

    # Remove all courses in which first student is enrolled in
    student = Student.objects.first()
    student.course.clear()

    # Add all courses to a student, then clear them all
    shivam, created = Student.objects.get_or_create(name='shivam')
    courses = Course.objects.all()
    shivam.course.add(*courses)
    shivam.course.clear()

    # Count how many student are enrolled in Python
    python = Course.objects.get(name='Python')
    python.enrolled_by_students.count()


    # ============= Replace Course Using set() ============

    # Use set() to remove all courses in which first student is enrolled in
    student = Student.objects.first()
    courses = Course.objects.all()
    student.course.add(*courses)
    student.course.set([])

    # Use set() to assign only selected courses [C++, MERN]
    c_plus_plus = Course.objects.get(name='C++')
    mern = Course.objects.get(name='MERN')
    student.course.set([c_plus_plus, mern])

    # Replace all courses of first student with a new one
    django, created = Course.objects.get_or_create(name='Django')
    student.course.set([django])


    # ============= Reverse Relation ============

    # Get all students enrolled in Java course
    java = Course.objects.get(name='Java')
    java.enrolled_by_students.all()

    # Count students per course
    courses = Course.objects.all()
    for course in courses:
        print(course.name, course.enrolled_by_students.count())

    # Remove Alice from Python course using reverse relation
    python = Course.objects.get(name='Python')
    alice = Student.objects.get(name='Alice')
    python.enrolled_by_students.remove(alice)

    # Enroll all students to django course
    django = Course.objects.get(name='Django')
    students = Student.objects.all()
    django.enrolled_by_students.add(*students)

    # Clear all students enrolled in django course
    django.enrolled_by_students.clear()

    # Enroll only specific students to django course
    rahul = Student.objects.get(name='Rahul')
    ananya = Student.objects.get(name='Ananya')
    django.enrolled_by_students.set([rahul, ananya])    


    # ============= Filter + Order ============

    # Filter all students whose name begins with 'A' and enroll them to a new course 'nodejs'
    nodejs, created = Course.objects.get_or_create(name='Nodejs')
    students = Student.objects.filter(name__startswith='A')
    nodejs.enrolled_by_students.add(*students)

    # For a given course, list student names alphabetically
    course = Course.objects.get(name='Java')
    students = course.enrolled_by_students.order_by(Lower('name'))

    