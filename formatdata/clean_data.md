# Cleaning The Data  From Parser
``` scp root@178.62.239.18:~/tmp/finished/unzipped/*.csv  ./ ```

*On the server*

```cd ~/tmp/finished

cp ~/tmp/other/PGParser_proper/PGParser/data/data*.zip ~/tmp/finished
mkdir unzipped
find -name  "data*.zip" | while read f ; do unzip "$f" -d unzipped/"${f//.{5}" 

cp ~/tmp/other/PGParser_proper/PGParser/data/unzipped/unicode.py ~/tmp/finished/unzipped/unicode.py
cp ~/tmp/other/PGParser_proper/PGParser/data/unzipped/book_formatter.py ~/tmp/finished/unzipped/book_formatter.py

cp ./unicode.py ~/tmp/finished/unzipped/unicode.py
cp ./book_formatter.py ~/tmp/finished/unzipped/book_formatter.py

cd unzipped ```

#### run the following commands

*Add prefix to authors because the ids will not be unique otherwise.*


```
sed 's/^/a/' ./data0-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/a/' ./data0-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/b/' ./data500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/b/' ./data500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/c/' ./data1000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/c/' ./data1000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/d/' ./data1500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/d/' ./data1500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/e/' ./data2000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/e/' ./data2000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/f/' ./data2500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/f/' ./data2500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/g/' ./data3000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/g/' ./data3000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/h/' ./data3500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/h/' ./data3500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/i/' ./data4000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/i/' ./data4000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/j/' ./data4500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/j/' ./data4500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/k/' ./data5000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/k/' ./data5000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/l/' ./data5500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/l/' ./data5500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/m/' ./data6000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/m/' ./data6000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/n/' ./data6500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/n/' ./data6500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/o/' ./data7000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/o/' ./data7000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/p/' ./data7500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/p/' ./data7500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/q/' ./data8000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/q/' ./data8000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/r/' ./data8500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/r/' ./data8500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/s/' ./data9000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/s/' ./data9000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/t/' ./data9500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/t/' ./data9500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/u/' ./data10000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/u/' ./data10000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/v/' ./data10500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/v/' ./data10500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/w/' ./data11000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/w/' ./data11000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/x/' ./data11500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/x/' ./data11500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/y/' ./data12000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/y/' ./data12000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/z/' ./data12500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/z/' ./data12500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/A/' ./data13000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/A/' ./data13000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/B/' ./data13500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/B/' ./data13500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/C/' ./data14000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/C/' ./data14000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/D/' ./data14500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/D/' ./data14500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/E/' ./data15000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/E/' ./data15000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/F/' ./data15500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/F/' ./data15500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/G/' ./data16000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/G/' ./data16000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/H/' ./data16500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/H/' ./data16500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/I/' ./data17000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/I/' ./data17000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/J/' ./data17500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/J/' ./data17500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/K/' ./data18000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/K/' ./data18000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/L/' ./data18500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/L/' ./data18500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/M/' ./data19000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/M/' ./data19000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/N/' ./data19500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/N/' ./data19500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/O/' ./data20000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/O/' ./data20000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/P/' ./data20500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/P/' ./data20500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/Q/' ./data21000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/Q/' ./data21000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/R/' ./data21500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/R/' ./data21500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/S/' ./data22000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/S/' ./data22000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/T/' ./data22500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/T/' ./data22500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/U/' ./data23000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/U/' ./data23000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/V/' ./data23500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/V/' ./data23500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/W/' ./data24000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/W/' ./data24000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/X/' ./data24500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/X/' ./data24500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/Y/' ./data25000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/Y/' ./data25000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/Z/' ./data25500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/Z/' ./data25500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aA/' ./data26000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aA/' ./data26000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aB/' ./data26500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aB/' ./data26500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aC/' ./data27000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aC/' ./data27000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aD/' ./data27500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aD/' ./data27500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aE/' ./data28000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aE/' ./data28000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aF/' ./data28500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aF/' ./data28500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aG/' ./data29000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aG/' ./data29000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aH/' ./data29500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aH/' ./data29500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aI/' ./data30000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aI/' ./data30000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aJ/' ./data30500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aJ/' ./data30500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aK/' ./data31000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aK/' ./data31000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aL/' ./data31500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aL/' ./data31500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aM/' ./data32000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aM/' ./data32000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aN/' ./data32500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aN/' ./data32500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aO/' ./data33000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aO/' ./data33000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aP/' ./data33500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aP/' ./data33500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aQ/' ./data34000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aQ/' ./data34000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aR/' ./data34500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aR/' ./data34500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aS/' ./data35000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aS/' ./data35000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aT/' ./data35500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aT/' ./data35500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aU/' ./data36000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aU/' ./data36000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aV/' ./data36500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aV/' ./data36500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aW/' ./data37000-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aW/' ./data37000-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv
sed 's/^/aX/' ./data37500-500.zip/authors.csv | tail -n +2 >> fullauthors.csv
sed 's/^/aX/' ./data37500-500.zip/wrote.csv | tail -n +2 >> fullwrote.csv

cat ./data*/books.csv | tail -n +2  >> fullbooks.csv
cat ./data*/cities.csv | tail -n +2  >> fullcities.csv
cat ./data*/mentioned.csv | tail -n +2 >> fullmentioned.csv
cat ./data*/mentioned.csv | tail -n +2 >> fullmentioned.csv

sort fullcities.csv | uniq -d -s1  >> fullcities_d.csv
sort fullcities.csv | uniq -u -s1  >> fullcities_u.csv
cat ./fullcities_d.csv >> fullcities2.csv
cat ./fullcities_u.csv >> fullcities2.csv
rm fullcities_d.csv
rm fullcities_u.csv

```


Run https://github.com/DatabaseGroup9/dataimport/blob/master/cleanCsv/csvCleaner2018.py

