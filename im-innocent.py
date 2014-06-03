f = open("statements.txt")
body = ""

for line in f:
    line = line.rstrip()
    body += line
f.close()

body = body.split()

for k in range(0, len(body)):
    if body[k] == "innocent":
        print "..."+" ".join(body[k-10 : k+10])+"..."
