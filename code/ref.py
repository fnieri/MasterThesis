import re

# Step 1: Read the malformed CSV from file
with open("displ.csv", "r") as f:
    data = f.read()

# Step 2: Use regex to find all valid "type,obs,calc,time" entries
pattern = r'(comp|gui),\d+,\d+,\d+'
matches = re.finditer(pattern, data)

# Step 3: Write to a new CSV file
with open("formatted.csv", "w") as f:
    f.write("type,obs,calc,time\n")  # Optional header
    for match in matches:
        f.write(match.group(0) + "\n")
