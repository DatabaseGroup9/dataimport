# Import Data to Neo4J 

##### Import data into Neo4J via the GUI Interface


```
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/books_cleaned.csv" AS row
MERGE (:Book {bookID: row.bookID, bookTitle: row.title, bookShortTitle: row.short_title});



LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/authors_cleaned.csv" AS row
MERGE (a:Author {authorID: row.authorID, fullName: row.fullName, firstName: row.firstName, surName: row.surName })
ON CREATE SET a.title = row.title
ON MATCH SET a.title = row.title

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/cities_cleaned.csv" AS row
MERGE (:City {cityID: row.cityID, name: row.name, location: point({longitude: row.lon, latitude: row.lat})});

CREATE INDEX ON :Book(bookID)
CREATE INDEX ON :City(cityID)
CREATE INDEX ON:Author(authorID)


USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/wrote_cleaned.csv" AS row
MATCH (b:Book {bookID: toString(row.bookID)}), 
                      (a:Author {authorID :toString(row.authorID)})
CREATE (a)-[:AUTHORED]->(b);



USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/mentioned_cleaned.csv" AS row
MATCH (b:Book {bookID: replace(toString(row.bookID), " ", "") }),(c:City {cityID: replace(toString(row.cityID), " ", "")})
CREATE (b)-[:MENTIONS {mentions: row.count}]->(c);
```


Useful commands

```MATCH (n) DETACH DELETE n
CALL db.indexes

DROP INDEX ON :Book(bookID)

MATCH ()-[r:AUTHORED]-() 
DELETE r
MATCH ()-[r:WROTE]-() 
DELETE r```
