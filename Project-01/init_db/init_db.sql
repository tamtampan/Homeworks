CREATE USER 'tamtampan'@'localhost' IDENTIFIED BY 'tamtampan_pass';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD
on *.* TO 'tamtampan'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS shop;