import subprocess

ret = subprocess.call("ping -c 1 127.0.0.1",
                      shell=True)

if ret == 0:
    print("Success!")
else:
    print("Failure!")

# Using call()
ret_code = subprocess.call(['ls', '-l'])

# Using run()
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

# Using Popen(), the PIPE will prevent the output to terminal directly
process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode())
