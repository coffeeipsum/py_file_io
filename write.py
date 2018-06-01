""""
# Scenario 1
f = open('newfile.txt', 'a')   #File access mode: a for append, w for write, r for read, etc.
f.write("_World")
f.close()
"""


# Scenario 2 - HowTo create files in Python

f = open('newfile.txt', 'a')
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()