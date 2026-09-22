import re
from pathlib import Path


# --------------------------------------------------
# README location
# --------------------------------------------------

readme_path = Path(__file__).parent / "README.md"

if not readme_path.exists():
    print("ERROR: README.md was not found.")
    exit()


# --------------------------------------------------
# Get and validate date
# --------------------------------------------------

date_updated = input("Date updated: ").strip()

if not date_updated:
    print("ERROR: Date cannot be empty.")
    exit()


# --------------------------------------------------
# Get and validate year
# --------------------------------------------------

while True:
    year_input = input("Year: ").strip()

    if not year_input.isdigit():
        print("ERROR: Year must be a number.")
        continue

    year = int(year_input)

    if year < 2015 or year > 2026:
        print("ERROR: AoC years must be between 2015 and 2026.")
        continue

    break


# --------------------------------------------------
# Get and validate day
# --------------------------------------------------

while True:
    day_input = input("Day: ").strip()

    if not day_input.isdigit():
        print("ERROR: Day must be a number.")
        continue

    day = int(day_input)

    if day < 1 or day > 25:
        print("ERROR: Day must be between 1 and 25.")
        continue

    break


# --------------------------------------------------
# Get and validate solved parts
# --------------------------------------------------

while True:
    parts_input = input(
        "Solved parts (e.g. 1,2 or 1): "
    ).strip()

    parts_input = parts_input.replace(" ", "")

    parts = parts_input.split(",")

    if not all(part in ["1", "2"] for part in parts):
        print("ERROR: Parts can only be 1 or 2.")
        continue

    # Remove duplicate parts
    parts = list(dict.fromkeys(parts))

    if len(parts) == 0:
        print("ERROR: You must enter at least one part.")
        continue

    break


# --------------------------------------------------
# Generate puzzle name
# --------------------------------------------------

if len(parts) == 2:
    puzzle_solved = f"{year} Day {day} Part 1 & 2"
else:
    puzzle_solved = f"{year} Day {day} Part {parts[0]}"

stars_added = len(parts)


# --------------------------------------------------
# Read README
# --------------------------------------------------

readme = readme_path.read_text(encoding="utf-8")


# --------------------------------------------------
# Check that the year exists in README
# --------------------------------------------------

year_pattern = (
    rf'(<td align="center">{year}</td>'
    rf'<td align="center">)(\d+)(\*)'
)

year_match = re.search(year_pattern, readme)

if not year_match:
    print(f"ERROR: Year {year} was not found in the README.")
    print("Make sure the year has a row in the Progress table.")
    exit()


# --------------------------------------------------
# Get current stars for the year
# --------------------------------------------------

current_stars = int(year_match.group(2))


# --------------------------------------------------
# Check for duplicate puzzle
# --------------------------------------------------

if re.search(
    rf"Latest Puzzle Solved: {year} Day {day} ",
    readme,
    re.IGNORECASE
):
    print(
        f"WARNING: {year} Day {day} may already be recorded."
    )

    confirm = input("Continue anyway? (y/n): ").strip().lower()

    if confirm != "y":
        print("Update cancelled.")
        exit()


# --------------------------------------------------
# Calculate new stars for the year
# --------------------------------------------------

new_stars = current_stars + stars_added


# --------------------------------------------------
# Update year's star count
# --------------------------------------------------

readme = re.sub(
    year_pattern,
    rf'\g<1>{new_stars}\g<3>',
    readme,
    count=1
)


# --------------------------------------------------
# Calculate total stars
# --------------------------------------------------

year_stars = re.findall(
    r'<tr><td align="center">20\d{2}</td>'
    r'<td align="center">(\d+)\*</td>',
    readme
)

total_stars = sum(int(stars) for stars in year_stars)


# --------------------------------------------------
# Calculate total possible stars
# --------------------------------------------------

year_totals = re.findall(
    r'<tr><td align="center">20\d{2}</td>'
    r'<td align="center">\d+\*</td>'
    r'<td align="center">(\d+)</td></tr>',
    readme
)

total_possible_stars = sum(
    int(total) for total in year_totals
)


# --------------------------------------------------
# Update date
# --------------------------------------------------

readme = re.sub(
    r"> Last updated: .*",
    f"> Last updated: {date_updated}",
    readme,
    count=1
)


# --------------------------------------------------
# Update latest puzzle
# --------------------------------------------------

readme = re.sub(
    r"<br>Lastest Puzzle Solved: .*",
    f"<br>Latest Puzzle Solved: {puzzle_solved}",
    readme,
    count=1
)

# If the README already has the corrected spelling
readme = re.sub(
    r"<br>Latest Puzzle Solved: .*",
    f"<br>Latest Puzzle Solved: {puzzle_solved}",
    readme,
    count=1
)


# --------------------------------------------------
# Update Total Progress
# --------------------------------------------------

readme = re.sub(
    r'(<th align="center">Total Progress:</th>\s*'
    r'<th align="center">)\d+\*/\d+',
    rf'\g<1>{total_stars}*/{total_possible_stars}',
    readme,
    count=1
)


# --------------------------------------------------
# Update Total row
# --------------------------------------------------

readme = re.sub(
    r'(<tr><td align="center">Total</td>'
    r'<td align="center">)\d+\*'
    r'(</td><td align="center">)\d+',
    rf'\g<1>{total_stars}*\g<2>{total_possible_stars}',
    readme,
    count=1
)


# --------------------------------------------------
# Save README
# --------------------------------------------------

readme_path.write_text(
    readme,
    encoding="utf-8"
)


# --------------------------------------------------
# Display result
# --------------------------------------------------

print("\n" + "=" * 40)
print("README UPDATED SUCCESSFULLY")
print("=" * 40)

print(f"Date:           {date_updated}")
print(f"Year:           {year}")
print(f"Day:            {day}")
print(f"Puzzle:         {puzzle_solved}")
print(f"Stars added:    {stars_added}")
print(f"Year progress:  {new_stars}*")
print(f"Total progress: {total_stars}*/{total_possible_stars}")
print("=" * 40)
