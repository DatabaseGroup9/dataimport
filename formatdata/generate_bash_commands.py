# This script has only been run in jupyter. 
def main():

	listlower = [chr(i) for i in range(ord('a'),ord('z')+1)]
	listupper = [chr(i) for i in range(ord('A'),ord('Z')+1)]
	listother = ['AA','BB','CC']
	print(len(listlower))

	list = listlower + listupper



	for lower in listlower:
		for upper in listupper:
			list.append(lower+upper)

	print(list)    
	i = 0
	j = 0

	while i < 38000:
		print("sed 's/^/"+list[j]+"/' ./data"+str(i)+"-500.zip/authors.csv | tail -n +2 >> fullauthors_pre.csv")
		print("sed 's/^/"+list[j]+"/' ./data"+str(i)+"-500.zip/wrote.csv | tail -n +2 >> fullwrote_pre.csv")
		j = j +1
		
		i = i+500;
	print(j) 

if __name__ == "__main__":
    main() 