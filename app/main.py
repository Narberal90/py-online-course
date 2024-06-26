import math


class OnlineClass:
    course_dict = {
        "name": "",
        "description": "",
        "days": 0,
    }

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return math.ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineClass":
        return OnlineClass(
            course_dict["name"],
            course_dict["description"],
            OnlineClass.days_to_weeks(course_dict["days"])
        )
