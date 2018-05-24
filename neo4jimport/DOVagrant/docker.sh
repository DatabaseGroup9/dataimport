docker run \
    -d --name neo4j \
    --rm \
    --publish=7474:7474 \
    --publish=7687:7687 \
    -v $(pwd):/data/databases \
    --volume=$(pwd)/import:/import \
    --volume=$(pwd)/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/class \
    --env=NEO4J_dbms_security_procedures_unrestricted=apoc.\\\*,algo.\\\* \
    neo4j
    
    
    
    

docker exec neo4j sh -c 'neo4j stop'
docker exec neo4j sh -c 'rm -rf data/databases/graph.db'    

docker exec neo4j sh -c 'neo4j-admin import \
    --nodes:Book /import/books_cleaned.csv \
    --nodes:Author /import/authors_cleaned.csv \    
    --relationships:AUTHORED /import/wrote_cleaned.csv \    
    --nodes:City /import/city_cleaned.csv \
    --relationships:MENTIONS /import/mentioned_cleaned.csv \
    --ignore-missing-nodes=true \
    --ignore-duplicate-nodes=true \
    --id-type=INTEGER'

docker restart neo4j



####--env=NEO4J_dbms_memory_pagecache_size=10G \
####--env=NEO4J_dbms_memory_heap_initial__size=10G \
####--env=NEO4J_dbms_memory_heap_max__size=10G \
