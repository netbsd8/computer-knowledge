import subprocess

res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# removing leading and trailing whitespaces by default
# removing customized: data.strip('-')
# The decode() method is used to convert these bytes back into a string. 
uname = res.stdout.read().strip().decode('utf-8')

print(uname)

print("next")
print("Linux index is {}".format(uname.index("Linux")))
first_occurrence = uname.find("Ubuntu")
print(first_occurrence) # return the index of first occurrence
# search the second occurrence
second_occurrence = uname.find("world", first_occurrence + 1)
print(second_occurrence) # return the index of second occurrence

print(uname.startswith('Linux'))
print(uname.lower())

test_str = "hello-world"
test_str_list = test_str.split('-')
print(test_str_list)

new_test_str = ','.join(test_str_list)
print(new_test_str)

replaced_test_str = test_str.replace("world", "world!!")
print(replaced_test_str)
