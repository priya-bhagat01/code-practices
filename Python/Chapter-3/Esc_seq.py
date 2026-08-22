#a = "Priya is a good girl
#but not a good student"
#print(a)  # Output: error for undetermind string literal

#To fix the error, we can use escape sequences to include the newline character in the string. The corrected code is as follows:
#\n is an escape sequence that represents a newline character. When the string is printed, it will be displayed on multiple lines as follows:
a = "Priya is a good girl\nbut not a\ngood student"
print(a)

#\t is an escape sequence that represents a tab character. When the string is printed, it will be displayed with a tab space as follows:
b = "Priya is a good girl\tbut not a good student"
print(b)

#\' is an escape sequence that represents a single quote character. When the string is printed, it will be displayed with a single quote as follows:
c = 'Priya is a good girl but not a good student. She said, \'I am a good girl.\''
print(c)

#\\ is an escape sequence that represents a backslash character. When the string is printed, it will be displayed with a backslash as follows:
d = "Priya is a good girl but not a good student. She said, \\I am a good girl."
print(d)
