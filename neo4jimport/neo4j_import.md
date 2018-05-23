# Import Data to Neo4J 

##### Import data into Neo4J via the GUI Interface



```USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/cleanCsv/books.csv" AS row
MERGE (:Book {bookID: row.bookID, bookTitle: row.title, bookShortTitle: row.short_title});


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/cleanCsv/authors_cleaned.csv" AS row
MERGE (:Author {authorID: row.authorID, fullName: row.fullName});


USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/cleanCsv/cities_cleaned.csv" AS row
MERGE (:City {cityID: row.cityID, name: row.name, lat: row.lat,  lon: row.lon});

CREATE INDEX ON :Book(bookID)
CREATE INDEX ON :City(cityID)


USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/cleanCsv/wrote.csv" AS row
MATCH (b:Book {bookID: toString(row.bookID)}), 
                      (a:Author {authorID :toString(row.authorID)})
CREATE (a)-[:AUTHORED]->(b);



USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/cleanCsv/mentioned.csv" AS row
MATCH (b:Book {bookID: replace(toString(row.bookID), " ", "") }),(c:City {cityID: replace(toString(row.cityID), " ", "")})
CREATE (b)-[:MENTIONS {mentions: row.count}]->(c);
```