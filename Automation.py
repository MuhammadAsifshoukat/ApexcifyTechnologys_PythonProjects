import re

# File names
input_file = "input.txt"
output_file = "emails.txt"

# Read input file
with open(input_file, "r") as file:
    data = file.read()

# Regex pattern for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract emails
emails = re.findall(email_pattern, data)

# Write emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ Email addresses extracted and saved successfully!")
