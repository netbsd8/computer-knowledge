"""
Basic Patterns: The most basic patterns are ordinary characters (e.g., A, a, 0) which match themselves exactly.

Special Characters: There are some characters that have special meanings:

.: Matches any character except a newline.
^: Matches the start of the string.
$: Matches the end of the string.
*: Matches 0 or more repetitions of the preceding character.
+: Matches 1 or more repetitions of the preceding character.
?: Matches 0 or 1 repetition of the preceding character.
{m,n}: Matches from m to n repetitions of the preceding character.
\\: Escapes a character.
[]: Indicates a set of characters. E.g., [abc] will match any of a, b, or c.
|: Acts like an OR operator. E.g., a|b matches either a or b.
(): Groups patterns together.
Special Sequences:

\\d: Matches any digit. Equivalent to [0-9].
\\D: Matches any non-digit.
\\s: Matches any whitespace character.
\\S: Matches any non-whitespace character.
\\w: Matches any alphanumeric character or underscore. Equivalent to [a-zA-Z0-9_].
\\W: Matches any non-alphanumeric character.
Using the re module in Python:

Searching:

python
Copy code
import re

text = "Python is fun!"
match = re.search("Python", text)
if match:
    print("Found Python!")
Find All:

python
Copy code
text = "a, b, c, a, b, c"
matches = re.findall("a", text)
print(matches)  # ['a', 'a']
Substitution:

text = "Hello, John!"
new_text = re.sub("John", "Doe", text)
print(new_text)  # Hello, Doe!
Compilation (for repeated use):

pattern = re.compile("\\d+")  # matches one or more digits
result = pattern.findall("Phone: 1234, Age: 25")
print(result)  # ['1234', '25']
Grouping:

text = "Email me at email@example.com"
match = re.search("(\\w+)@(\\w+).(\\w+)", text)
if match:
    print(match.group())   # email@example.com
    print(match.group(1))  # email
    print(match.group(2))  # example
    print(match.group(3))  # com
"""

import re

text = "Python is fun!"
match = re.search("Python", text)
if match:
    print("Found Python")

new_text = re.sub("fun", "cool", text)
print(new_text)

pattern = re.compile("\\d+")
result = pattern.findall("Phone: 1234, Age: 25")
print(result)

text = "Email me at email@example.com"
match = re.search("(\\w+)@(\\w+).(\\w+)", text)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

text = "Here are some IPs: 192.168.1.1, 10.0.0.1 and 256.256.256.256"

"""
Capturing groups (enclosed by ()): These capture a matched substring for use elsewhere. In re.findall(), if a pattern contains capturing groups, the function returns those groups rather than the entire match. So, if your regex has capturing groups, the output will be based on those groups.

Non-capturing groups (starting with ?: and enclosed by (?:...)): These are used to group part of a pattern, but they don't capture the matched substring. As a result, they don't affect the output of re.findall(). You'll get the entire match rather than just the groups.
"""
# Using the more accurate regex pattern with non-capturing groups
pattern = r"((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
matches = re.finditer(pattern, text)

ip_addresses = [match.group() for match in matches]

print(ip_addresses)

# extracting URLs
text = "Visit https://www.example.com or http://example.net for more info."
pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

match = re.search(pattern, text)

if match:
    print(f"URL found at index {match.start()} to {match.end()}")
    print("URL:", match.group())

# output
# URL found at index 6 to 27
# URL: https://www.example.com


# Splitting text by multiple delimiters
delimiters = r"[;,\s]"
text = "apple,banana;orange grape"

fruits = re.split(delimiters, text)
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# checking password strength
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
password = "Password123!"

if re.match(password_pattern, password):
    print("Password is strong.")
else:
    print("Password is weak.")

# match email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}"
text = "Contact us at contact@example.com or support@example.net"

matches = re.findall(email_pattern, text)
print(matches)  # ['contact@example.com', 'support@example.net']

# extracting dates:
date_pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"
text = "Today's date is 10-13-2023 and the event is on 11/15/2023."

dates = re.findall(date_pattern, text)
print(dates)  # ['10-13-2023', '11/15/2023']

# replace text
phone_pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
text = "Call 123-456-7890 or 987 654 3210 for details."

replaced_text = re.sub(phone_pattern, "[REDACTED]", text)
print(replaced_text)  # Call [REDACTED] or [REDACTED] for details.
