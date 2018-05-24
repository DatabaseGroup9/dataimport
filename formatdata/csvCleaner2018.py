import pandas as pd
import numpy as np


def cleanCSV():
	df_authors = pd.read_csv('fullauthors_pre.csv',delimiter=",",quotechar='"',error_bad_lines=False,keep_default_na=False,names=['authorID','fullName','firstName','surName','title'],skiprows=1)
	df_books = pd.read_csv('books_cleaned.csv',delimiter=",",quotechar='"',error_bad_lines=False,keep_default_na=False,names=['bookID','title','short_title'],skiprows=1)
	df_cities = pd.read_csv('fullcities.csv',delimiter=",",quotechar='"',error_bad_lines=False,keep_default_na=False,names=['cityID','name','lat', 'lon'],skiprows=1)
	


#df_cities = pd.read_csv('cities.csv',delimiter=",",error_bad_lines=False, names=['cityID','name','lat','lon'],skiprows=1)
	#print(df_books)
	#print(df_cities)

	#df_author_cleaned = df_authors[['authorID','firstName','titel']]
	#df_author_cleaned['titel'] = df_author_cleaned['titel'].map(lambda x: str(x)[:-1])
	#df_author_cleaned["fullName"] = df_author_cleaned["firstName"].map(str) + ", " + df_author_cleaned["titel"]
	#df_author_cleaned = df_author_cleaned[['authorID','fullName']]
	#df_author_cleaned.to_csv("authors_cleaned.csv",sep=",",encoding='utf-8',index=False);
	#df_cities.to_csv("cities_cleaned.csv",sep=",", quote,index=False);
	#doShortTitles(df_books)

		#df_books['title'] = df_books['title'].apply(lambda s: fixUnicode(s) if isinstance(s, str) and not (not s) else s)
		#df_books['short_title'] = df_books['short_title'].apply(lambda s: fixUnicode(s) if isinstance(s, str) and not (not s) else s)

	df_authors = df_authors.applymap(lambda s: fixUnicode(s) if isinstance(s, str) and not (not str(s)) else s)

	df_books = df_books.applymap(lambda s: fixUnicode(s) if isinstance(s, str) and not (not str(s)) else s)

	df_cities = df_cities.applymap(lambda s: fixUnicode(s) if isinstance(s, str) and not (not str(s)) else s)

	#df_authors['title'] = df_books['title'].apply(lambda s: fixUnicode(s))
        #df_books['short_title'] = df_books['short_title'].apply(lambda s: fixUnicode(s))

	print(df_cities)

	df_books.to_csv("books_cleaned.csv", sep=",", quotechar='"', encoding="utf-8", index=False)
	df_authors.to_csv("authors_cleaned.csv", sep=",", quotechar='"', encoding="utf-8", index=False)
	df_cities.to_csv("cities_cleaned.csv", sep=",", quotechar='"', encoding="utf-8", index=False)

def fixUnicode(col):
	col = col.replace("\\xc9", "É") # hexadecimal
	col = col.replace("\\xe7", "ç") # hexadecimal
	col = col.replace("\\xe9", "é") # hexadecimal
	col = col.replace("\\xeb", "ë") # hexadecimal
	col = col.replace("\\xf3", "ó") # hexadecimal
	col = col.replace("\\xe1", "á") # hexadecimal

	col = col.replace("\\xf8", "ø") # hexadecimal
	col = col.replace("\\u017", "ž") # hexadecimal
	col = col.replace("\\u012", "Ī") # hexadecimal	
	col = col.replace("\\u0301", "́́`") # hexadecimal
	col = col.replace("\\u0142", "ł") # hexadecimal
	col = col.replace("\\xed", "í") # hexadecimal
	col = col.replace("\\u2014", "-") # hexadecimal

	col = col.replace("\\xe8", "è") # hexadecimal
	col = col.replace("\\xfc", "ü") # hexadecimal
	col = col.replace("\\xde", "Þ") #     Þ
	col = col.replace("\\xe3", "ã") # hexadecimal
	col = col.replace("\\xf6", "a") # hexadecimal
	col = col.replace("\\xef", "ï") # hexadecimal
	col = col.replace("\\u0100", "Ā") # hexadecimal
	col = col.replace("\\u0101", "ā") # hexadecimal
	col = col.replace("\\u0113", "ē") # hexadecimal
	col = col.replace("\\u011f", "ğ") # hexadecimal
	col = col.replace("\\xf1", "ñ") # hexadecimal
	col = col.replace("\\xc1", "Á") # hexadecimal
	return col

cleanCSV()
