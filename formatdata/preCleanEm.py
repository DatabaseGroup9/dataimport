import sys
import csv
import re


def main():
	inputfile = sys.argv[1]
	tempfile = sys.argv[2]

	w=open(tempfile,"w+")
	print(tempfile)
	with open(inputfile) as f:
		read_data = f.read()
		read_data = read_data.strip()
		replaced = "|".join(read_data.split("\\n"))
		replaced = "|".join(replaced.split("\\r"))
		replaced = "|".join(replaced.split(";"))
		replaced = "|".join(replaced.split("||"))

	w.write(replaced)
	w.close()
	f.close()

def doShortTitles():

	outList = []

	if 'books' in sys.argv[1]:
		with open("./tmp.csv", 'r') as file:
			reader = csv.DictReader(file, fieldnames = ( "bookID","title"))

			for row in reader:
				row['short_title'] = row['title'].split('|', 1)[0]
				outList.append(row)

			for row in outList:
				print(row)

		with open('books_cleaned.csv', 'w') as csvfile:
			fieldnames = ['bookID', 'title', 'short_title']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",", quotechar='"')

			writer.writeheader()
			for row in outList:
				writer.writerow(row)
	

if __name__ == "__main__":
	main() 
	doShortTitles()
