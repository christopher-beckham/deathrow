f = open("dr_executed_offenders.html")
body = []
for line in f:
    body.append( line.rstrip() )
f.close()

for line in body:
    if "Last Statement" in line and "no_last_statement.html" not in line:
        print "http://www.tdcj.state.tx.us/death_row/" + line[ line.find("dr_info") : line.find(".html")+5]
