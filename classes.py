import sys
from datetime import datetime
from dataclasses import dataclass


import requests

# from database import DatabaseManager

# module scope
# db = DatabaseManager("bookmarks.db")


class Command(ABC):
    pass


@dataclass
class Course(Command):
    """
    This command is a dataclass that encapsulates a bookmark
    This uses type hints: https://docs.python.org/3/library/typing.html
    """

    Course_id: int
    CourseName: str
    # data["date_added"] = datetime.utcnow().isoformat()
    date_start: str
    date_end: str
    notes: Optional[str] = None


@dataclass
class Student(Command):
    Student_id: int
    FirstName: str
    LastName: str
    # data["date_added"] = datetime.utcnow().isoformat()
    notes: Optional[str] = None


@dataclass
class Instructor(Command):
    Instructor_id: int
    FirstName: str
    LastName: str
    # data["date_added"] = datetime.utcnow().isoformat()
    date_start: str
    date_end: str
    notes: Optional[str] = None

