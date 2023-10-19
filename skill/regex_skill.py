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
This is a very basic introduction. Regular expressions are a deep topic and can get very complex. To truly master them, you'll need to study them in depth and practice on a variety of patterns. The Python re documentation provides a more exhaustive look at what's possible.
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