#!/usr/bin/env python3

import json
import datetime
from pathlib import Path

# Project root: one folder above scripts/
ROOT = Path(__file__).resolve().parents[1]

EXAMPLES_FILE = ROOT / "examples.json"
DAILY_FILE = ROOT / "daily.json"


def main():
    # Check that the example library exists.
    if not EXAMPLES_FILE.is_file():
        raise SystemExit(
            f"ERROR: examples.json not found at {EXAMPLES_FILE}"
        )

    # Read the example library.
    try:
        with EXAMPLES_FILE.open("r", encoding="utf-8") as file:
            examples = json.load(file)
    except json.JSONDecodeError as error:
        raise SystemExit(
            f"ERROR: examples.json contains invalid JSON: {error}"
        )
    except OSError as error:
        raise SystemExit(
            f"ERROR: Could not read examples.json: {error}"
        )

    # Confirm the library has the expected structure.
    if not isinstance(examples, list) or not examples:
        raise SystemExit(
            "ERROR: examples.json must contain a non-empty JSON list."
        )

    # Keep examples that have the fields used by the website.
    required_fields = ("id", "topic", "family", "en", "ta")

    valid_examples = [
        item
        for item in examples
        if isinstance(item, dict)
        and all(
            isinstance(item.get(field), str) and item[field].strip()
            for field in required_fields
        )
    ]

    if not valid_examples:
        raise SystemExit(
            "ERROR: No valid examples found. "
            "Each example needs id, topic, family, en and ta."
        )

    # Select a repeatable example for today's date.
    today = datetime.date.today()
    index = today.toordinal() % len(valid_examples)
    selected_example = valid_examples[index]

    # Build the daily featured example.
    daily_data = {
        "date": today.isoformat(),
        "title": "Today's example",
        "example": selected_example,
        "challenge": (
            "Say this sentence aloud three times, "
            "then change one detail to make it true for you."
        )
    }

    # Save daily.json while preserving Tamil characters.
    try:
        with DAILY_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                daily_data,
                file,
                ensure_ascii=False,
                indent=2
            )
            file.write("\n")
    except OSError as error:
        raise SystemExit(
            f"ERROR: Could not update daily.json: {error}"
        )

    print("Daily example updated successfully!")
    print(f"Date: {today.isoformat()}")
    print(f"Valid examples: {len(valid_examples):,}")
    print(f"Selected example ID: {selected_example['id']}")
    print(f"Topic: {selected_example['topic']}")
    print(f"English: {selected_example['en']}")
    print("Updated file: daily.json")


if __name__ == "__main__":
    main()
