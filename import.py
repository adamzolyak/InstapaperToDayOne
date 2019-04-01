import re
import subprocess
from pathlib import Path
import datetime

now = datetime.datetime.now()

# import the journal export
path = Path("import.txt")
file = path.read_text()

path2 = Path("export.txt")

# get each entry
# escape characters in body
matcher = re.compile('.*\n\n(".*")\n\n.*\n\n.*\n\n.*\nvia Instapaper (.*)\n\n')
matches = matcher.finditer(file)

i = 0

cleaned = f"# Weekly Instapaper Highlights {now.strftime('%m/%d/%Y')}\n\n"

for match in matches:
    cleaned += f"*{match[1]}* via {match[2]}\n\n"
    i += 1

path2.write_text(cleaned)

entry = cleaned

result = subprocess.call(['dayone2', 'new',
                          entry,
                          '--journal', "Daily Life",
                          '--time-zone', "America/Denver",
                          '--tags', "Instapaper"])

if result == 0:
    print(f"Summary: Created new journal entry with {i} highlights...")
else:
    print("Summary: Error...")
