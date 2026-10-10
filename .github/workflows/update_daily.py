import json
import datetime
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
examples = json.loads((ROOT / "examples.json").read_text(encoding="utf-8"))
today = datetime.date.today()
idx = today.toordinal() % len(examples)
daily = {"date": today.isoformat(), "title": "Today's example", "example": examples[idx], "challenge": "Say this sentence aloud three times, then change one detail to make it true for you."}
(ROOT / "daily.json").write_text(json.dumps(daily, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated daily.json for {today.isoformat()} from {len(examples)} examples.")
