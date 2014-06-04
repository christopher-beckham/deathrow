corpus:
	tar -zxvf links.tar.gz
	python get-statements.py > R/wordcloud/statements.txt
	python im-innocent.py > quotes.txt