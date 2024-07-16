NoSQL DATABASES.

NOSQL - an approach to databases that represents a shift away from traditional relational database managemtnt systems.
SQL-  A query langueage used bty RDBMS.
Relational databases rely on table, columns and rows, or schemas to organize and retrieve data.
NoSQL - don't rely on these structures and usemore flexible data models.  
not SQL or Not only SQL - As RDBMS have failed to meet the performance, scalability and flexibility needs that next generation, data intesive apps need.
NoSQL - useful for storing unstructured data which is growing far more rapidly than structured data. and does not fit in RDBMS.
Types of unstrucutred data
    user
    session data
    chat 
    messaging 
    log data
    time series data
    video
    images


TYPES OF NOSQL DATABASES
Key-value data stores: Key-value NoSQL databases emphasize simplicity and are very useful in accelerating an application to support high-speed read and write processing of non-transactional data. Stored values can be any type of binary object (text, video, JSON document, etc.) and are accessed via a key. The application has complete control over what is stored in the value, making this the most flexible NoSQL model. Data is partitioned and replicated across a cluster to get scalability and availability. For this reason, key value stores often do not support transactions. However, they are highly effective at scaling applications that deal with high-velocity, non-transactional data.
Document stores: Document databases typically store self-describing JSON, XML, and BSON documents. They are similar to key-value stores, but in this case, a value is a single document that stores all data related to a specific key. Popular fields in the document can be indexed to provide fast retrieval without knowing the key. Each document can have the same or a different structure.
Wide-column stores: Wide-column NoSQL databases store data in tables with rows and columns similar to RDBMS, but names and formats of columns can vary from row to row across the table. Wide-column databases group columns of related data together. A query can retrieve related data in a single operation because only the columns associated with the query are retrieved. In an RDBMS, the data would be in different rows stored in different places on disk, requiring multiple disk operations for retrieval.
Graph stores: A graph database uses graph structures to store, map, and query relationships. They provide index-free adjacency, so that adjacent elements are linked together without using an index.
BENEFITS OF NOSQL
Scalability
Performance
High Availability
Global Availability
Flexible Data Modelling
