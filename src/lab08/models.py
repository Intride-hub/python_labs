from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str     
    group: str
    gpa: float         

    def __post_init__(self):
        
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")

    
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa должно быть в диапазоне 0–5, получено: {self.gpa}")

    # -------------------------------------------------------

    def age(self) -> int:
        
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    # -------------------------------------------------------

    def to_dict(self) -> dict:
        
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    # -------------------------------------------------------

    @classmethod
    def from_dict(cls, d: dict):
        """Создание объекта Student из словаря."""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"]),
        )

    # -------------------------------------------------------

    def __str__(self):
        return f"{self.fio} ({self.group}), GPA={self.gpa}"
