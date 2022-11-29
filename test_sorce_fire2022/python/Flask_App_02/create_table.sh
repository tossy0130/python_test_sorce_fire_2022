#!/bin/bash
psql -U postgres -d postgres -h localhost << "EOSQL"
CREATE TABLE ppp_users (
        id SERIAL NOT NULL, 
        name VARCHAR(200), 
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id)
);
EOSQL
