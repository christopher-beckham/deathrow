from cz import cz

import glob

htmls = glob.glob("links/*.html")

for html in htmls:
    f = open(html)
    body = []
    for line in f:
        body.append( line.rstrip() )
    f.close()

    c = 0
    for line in body:
        if "text_bold" in line and "Last Statement" in line:
            break
        c += 1

    for line in body[c+1::]:
        if "<!-- InstanceEndEditable -->" in line:
            break
        line = "".join( cz.striphtml(line,unescape=True) ).encode('ascii', 'ignore')
        line = line.replace("This offender declined to make a last statement.", "")
        print line
