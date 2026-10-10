```python
import json
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

examples = json.loads(
    (ROOT / "examples.json").read_text(encoding="utf-8")
)

if not examples:
    raise ValueError("The examples.json file is empty.")

today = datetime.date.today()
index = today.toordinal() % len(examples)

daily = {
    "date": today.isoformat(),
    "title": "Today's example",
    "example": examples[index],
    "challenge": (
        "Say this sentence aloud three times, "
        "then make it true for you."
    )
}

(ROOT / "daily.json").write_text(
    json.dumps(daily, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

print(f"Daily example updated for {today.isoformat()}.")
```
