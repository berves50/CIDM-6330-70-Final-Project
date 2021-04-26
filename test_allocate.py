from datetime import date, timedelta
import pytest


today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_students():
    first_batch = Batch("FirstName", "StudentID", 100)
    Last_batch = Batch("LastName",  100, )
    StudentID = ID("studentID", 7)

    allocate(line, [first_batch, Last_batch])


def test_faculty():
    First_batch = Batch("FirstName", "facultyID", 100)
    Last_batch = Batch("LastName",  100, )
    StudentID = ID("facultyID", 7)

    allocate(line, [first_batch, Last_batch])


def test_course():
    course_Name = Batch("Name", 100)
    CoursedID = Batch("ID,  12, )
    startDate = Batch("Start", 100)
    endDate = Batch("End", 100)
