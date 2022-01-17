#Pyspark - Postgres - JDBC connector
To use spark jdbc connector:
- download jdbc connector jar, see all versions [here](https://jdbc.postgresql.org/documentation/changelog.html#version_all)
- include in driver and executor class path 
```angular2html
spark-shell --packages org.postgresql:postgresql:42.3.1
```

download the file from [here](https://jdbc.postgresql.org/download.html)

# Track
run postgres check name of container
`docker ps
`

switch the user with following command
`su postgres
`

then to run commands in db
`psql -U test
`
then run the followings
`\d
`
`select * from my_sample_table;
`