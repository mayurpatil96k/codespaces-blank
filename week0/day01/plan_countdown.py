"""Countdown for the AI Engineer study plan (Oct 2026 – Jan 2027)."""
import datetime as dt
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")
START = dt.date(2026, 10, 1)
END = dt.date(2027, 1, 31)
WEEK0_DAYS = 4  # Days 1–4 (Thu–Sun) are Week 0; Week 1 starts Monday (Day 5)


def week_number(day: int) -> int:
    if day <= WEEK0_DAYS:
        return 0
    return (day - WEEK0_DAYS - 1) // 7 + 1


def main() -> None:
    today = dt.datetime.now(IST).date()
    total_days = (END - START).days + 1  # inclusive -> 123
    day_number = (today - START).days + 1
    days_left = (END - today).days

    print(f"Start:      {START}")
    print(f"End:        {END}")
    print(f"Total days: {total_days}")

    if today < START:
        print(f"Plan starts in {(START - today).days} day(s).")
    elif today > END:
        print("Plan complete!")
    else:
        print(f"Today:      {today} (Day {day_number})")
        print(f"Days left:  {days_left}")
        print(f"Week:       {week_number(day_number)}")


if __name__ == "__main__":
    main()