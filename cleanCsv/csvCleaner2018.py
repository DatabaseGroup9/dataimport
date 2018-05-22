import pandas as pd
import numpy as np


def cleanCSV():
	df_authors = pd.read_csv('authors.csv',delimiter=", ",encoding='utf-8',error_bad_lines=False, names=['authorID','fullName','firstName','surName','titel'],skiprows=1)
	df_cities = pd.read_csv('cities.csv',delimiter=", ",error_bad_lines=False, names=['cityID','name','lat','lon'],skiprows=1)
	print(df_authors)
	print(df_cities)

	df_author_cleaned = df_authors[['authorID','firstName','titel']]
	df_author_cleaned['titel'] = df_author_cleaned['titel'].map(lambda x: str(x)[:-1])
	df_author_cleaned["fullName"] = df_author_cleaned["firstName"].map(str) + ", " + df_author_cleaned["titel"]
	df_author_cleaned = df_author_cleaned[['authorID','fullName']]
	df_author_cleaned.to_csv("authors_cleaned.csv",sep=",",encoding='utf-8',index=False);
	df_cities.to_csv("cities_cleaned.csv",sep=",",index=False);

cleanCSV()