#!/bin/bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo systemctl status docker
sudo usermod -aG docker ${USER}
sudo apt-get install unzip
sudo apt-get install python3-pip
pip3 install riak
mkdir -p /vagrant
mkdir -p /vagrant/import

echo "Downloading authors_cleaned.csv"
wget https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/authors_cleaned.csv
echo "Downloading wrote_cleaned.csv"
wget https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/wrote_cleaned.csv
echo "Downloading books_cleaned.csv"
wget https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/books_cleaned.csv
echo "Downloading mentioned_cleaned.csv"
wget https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/mentioned_cleaned.csv
echo "Downloading cities_cleaned.csv"
wget https://raw.githubusercontent.com/DatabaseGroup9/dataimport/master/data/cities_cleaned.csv

mkdir -p /vagrant/plugins
cd /vagrant/plugins
echo "Downloading APOC plugin"
wget https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.3.0.1/apoc-3.3.0.1-all.jar
echo "Downloading algorithms plugin"
wget https://github.com/neo4j-contrib/neo4j-graph-algorithms/releases/download/3.3.2.0/graph-algorithms-algo-3.3.2.0.jar
echo "Downloading Neo4J-Spatial plugin"
wget https://github.com/neo4j-contrib/spatial/releases/download/0.25.5-neo4j-3.3.5/neo4j-spatial-0.25.5-neo4j-3.3.5-server-plugin.jar

cd /vagrant
rm secret.noup.sh
chmod u+x docker.sh
./docker.sh