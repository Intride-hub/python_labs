<h1>Лабораторная работа 9</h1>


```python
import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

 

    def _ensure_storage_exists(self):
       
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> List[Student]:
        
        students = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError("Некорректный заголовок CSV")

            for row in reader:
                student = Student(
                    fio=row["fio"],
                    birthdate=row["birthdate"],
                    group=row["group"],
                    gpa=float(row["gpa"]),
                )
                students.append(student)
        return students

    def _write_all(self, students: List[Student]):
        
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            for s in students:
                writer.writerow({
                    "fio": s.fio,
                    "birthdate": s.birthdate,
                    "group": s.group,
                    "gpa": s.gpa,
                })

   

    def list(self) -> List[Student]:
        
        return self._read_all()

    def add(self, student: Student):
        
        students = self._read_all()
        students.append(student)
        self._write_all(students)

    def find(self, substr: str) -> List[Student]:
        
        substr = substr.lower()
        return [s for s in self._read_all() if substr in s.fio.lower()]

    def remove(self, fio: str):
        
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        self._write_all(students)

    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False

        for s in students:
            if s.fio == fio:
                for key, value in fields.items():
                    if hasattr(s, key):
                        setattr(s, key, value)
                updated = True
                break

        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")

        self._write_all(students)


    def stats(self) -> dict:
        students = self._read_all()
        if not students:
            return {}

        gpas = [s.gpa for s in students]

        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        top_5 = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": round(sum(gpas) / len(gpas), 2),
            "groups": groups,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} for s in top_5
            ],
        }
```

<h3>fio,birthdate,group,gpa
Иванов Иван,2003-10-10,БИВТ-21-1,4.6
Сидоров Алексей,2003-01-15,БИВТ-21-1,4.7</h3>
