import json
from pathlib import Path
from .models import Student


def students_to_json(students: list[Student], path: str | Path):
    
    path = Path(path)
    data = [s.to_dict() for s in students]

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> list[Student]:
   
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    return [Student.from_dict(item) for item in raw_list]
