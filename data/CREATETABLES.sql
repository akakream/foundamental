CREATE DATABASE [IF NOT EXISTS] mydb;
use mydb;
 
CREATE TABLE if not exists companies(
id VARCHAR(100),
name VARCHAR(200),
country VARCHAR(200),
founding_date VARCHAR(200),
description VARCHAR(200),
company_id INTEGER
);

CREATE TABLE if not exists deals(
id VARCHAR(100),
date VARCHAR(200),
funding_amount VARCHAR(200),
funding_round VARCHAR(200),
company_id INTEGER
);

LOAD DATA INFILE '/var/lib/mysql-files/challenge_companies.csv'
INTO TABLE companies
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/var/lib/mysql-files/challenge_deals.csv'
INTO TABLE deals
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;