"""
calendar_program.py

Prints a calendar for a given month, where the month number and the
day of the week that the 1st falls on are passed in as command-line
arguments.

Usage:
    python3 calendar_program.py <month 1-12> <starting_day 0-6>

    Weekday numbering: 0=Sunday, 1=Monday, 2=Tuesday, 3=Wednesday,
                        4=Thursday, 5=Friday, 6=Saturday

Example:
    python3 calendar_program.py 6 3      (June, starting on Wednesday)

Note: no year is supplied, so this assumes a common (non-leap) year,
meaning February is treated as having 28 days.
"""

import sys

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def parse_month(month_arg):
    """Accept a month number (1-12) and return its 0-based index."""
    if not month_arg.isdigit():
        raise ValueError("Month must be a number from 1 to 12.")
    month_num = int(month_arg)
    if not 1 <= month_num <= 12:
        raise ValueError("Month must be a number from 1 to 12.")
    return month_num - 1


def parse_weekday(day_arg):
    """Accept a weekday number (0=Sunday..6=Saturday) and return it."""
    if not day_arg.isdigit():
        raise ValueError("Starting day must be a number from 0 to 6.")
    day_num = int(day_arg)
    if not 0 <= day_num <= 6:
        raise ValueError("Starting day must be a number from 0 to 6.")
    return day_num


def print_calendar(month_index, start_weekday):
    """Print a calendar for the given month (0-11), where the 1st
    falls on start_weekday (0=Sunday..6=Saturday)."""
    month_name = MONTH_NAMES[month_index]
    days_total = DAYS_IN_MONTH[month_index]

    print(f"\n{month_name}")
    print("Su Mo Tu We Th Fr Sa")

    # Print blank spaces for the days of the week before the 1st.
    line = "   " * start_weekday

    day = 1
    weekday = start_weekday
    while day <= days_total:
        line += f"{day:2} "
        weekday += 1
        if weekday == 7:
            print(line.rstrip())
            line = ""
            weekday = 0
        day += 1

    if line:
        print(line.rstrip())


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 calendar_program.py <month 1-12> <starting_day 0-6>")
        sys.exit(1)

    try:
        month_index = parse_month(sys.argv[1])
        start_weekday = parse_weekday(sys.argv[2])
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print_calendar(month_index, start_weekday)


if __name__ == "__main__":
    main()