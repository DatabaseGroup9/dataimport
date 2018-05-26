# dataimport


## Editing Integration of Two Live Databases
### USEFUL COMMANDS

There is 76 zip files from Kristjan parser
I concat all the files into one fullbooks.csv .. the tail n +2 suppose to not take the header

```
sed 's/^/aW/' ./data37000-500.zip/authors.csv | tail -n +2 >> fullauthors_pre.csv
sed 's/^/aW/' ./data37000-500.zip/wrote.csv | tail -n +2 >> fullwrote_pre.csv
sed 's/^/aX/' ./data37500-500.zip/authors.csv | tail -n +2 >> fullauthors_pre.csv
sed 's/^/aX/' ./data37500-500.zip/wrote.csv | tail -n +2 >> fullwrote_pre.csv

cat ./data*/books.csv | tail -n +2  >> fullbooks.csv
cat ./data*/cities.csv | tail -n +2  >> fullcities.csv
cat ./data*/mentioned.csv | tail -n +2 >> fullmentioned.csv
```

_Secure copies from this ip address to the current folder you are standing in locally._

```
scp root@178.62.239.18:~/tmp/finished/unzipped/*.csv  ./ 
```
