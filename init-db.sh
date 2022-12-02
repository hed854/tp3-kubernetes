#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER docker;
	CREATE DATABASE docker;
	GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
        \c docker;
	CREATE TABLE test(
		id INT PRIMARY KEY NOT NULL,
                country TEXT NOT NULL,
                capital TEXT NOT NULL
	);
        INSERT INTO test(country,capital) VALUES('france','paris');
EOSQL
