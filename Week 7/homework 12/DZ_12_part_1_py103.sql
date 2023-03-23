-- part 1

-- DROP DATABASE IF EXISTS record;
CREATE DATABASE IF NOT EXISTS record;
USE record;

CREATE TABLE IF NOT EXISTS customer(
customer_name VARCHAR(50) NOT NULL,
customer_surname VARCHAR(50) NOT NULL,
customer_jmbg VARCHAR(13) NOT NULL UNIQUE,
address VARCHAR(50) NOT NULL,
phone VARCHAR(20) UNIQUE,
place_name VARCHAR(50)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS place(
place_name VARCHAR(50) NOT NULL,
zip VARCHAR(8) UNIQUE,
state VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS material(
material_name VARCHAR(50) NOT NULL,
material_description VARCHAR(500) NOT NULL,
material_picture BLOB
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS product(
product_name VARCHAR(50) NOT NULL,
product_description VARCHAR(500) NOT NULL,
product_picture BLOB,
price INT NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS component_product(
product_name VARCHAR(50) NOT NULL,
material_name VARCHAR(50) NOT NULL,
quantity INT
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS buy_product(
product_name VARCHAR(50) NOT NULL,
place_name VARCHAR(50) NOT NULL,
customer_name VARCHAR(50) NOT NULL,
quantity_buy INT NOT NULL,
total_price INT NOT NULL,
date_buy DATE NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 auto_increment=1000;

-- ADDING PRIMARY KEY

ALTER TABLE customer ADD PRIMARY KEY (customer_jmbg);
ALTER TABLE place ADD PRIMARY KEY (zip);
ALTER TABLE material ADD PRIMARY KEY (material_name);
ALTER TABLE product ADD PRIMARY KEY (product_name);
ALTER TABLE component_product ADD PRIMARY KEY (product_name);
ALTER TABLE buy_product ADD PRIMARY KEY (product_name);

-- DROPPING PRIMARY KEYS

ALTER TABLE customer DROP PRIMARY KEY;
ALTER TABLE place DROP PRIMARY KEY;
ALTER TABLE material DROP PRIMARY KEY;
ALTER TABLE product DROP PRIMARY KEY;
ALTER TABLE component_product DROP PRIMARY KEY;
ALTER TABLE buy_product DROP PRIMARY KEY;

-- ADDING COLUMNS AND PRIMARY KEYS

ALTER TABLE customer ADD COLUMN id_customer INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE place ADD COLUMN id_place INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE material ADD COLUMN id_material INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE product ADD COLUMN id_product INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE component_product ADD COLUMN id_component_product INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE buy_product ADD COLUMN id_buy_product INT PRIMARY KEY AUTO_INCREMENT FIRST;


-- ADDING FOREIGN KEYS
-- CUSTOMER
ALTER TABLE customer ADD COLUMN id_place INT;
ALTER TABLE customer ADD CONSTRAINT fk_place FOREIGN KEY (id_place) references place(id_place)
ON UPDATE SET NULL ON DELETE SET NULL;

-- COMPONENT PRODUCT
ALTER TABLE component_product ADD COLUMN id_product INT;
ALTER TABLE component_product ADD CONSTRAINT fk_product FOREIGN KEY (id_product) references product(id_product)
ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE component_product ADD COLUMN id_material INT;
ALTER TABLE component_product ADD CONSTRAINT fk_material FOREIGN KEY (id_material) references material(id_material)
ON UPDATE SET NULL ON DELETE SET NULL;

-- BUY PRODUCT
ALTER TABLE buy_product ADD COLUMN id_product INT;
ALTER TABLE buy_product ADD CONSTRAINT fk_product2 FOREIGN KEY (id_product) references product(id_product);

ALTER TABLE buy_product ADD COLUMN id_place INT;
ALTER TABLE buy_product ADD CONSTRAINT fk_place2 FOREIGN KEY (id_place) references place(id_place)
ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE buy_product ADD COLUMN id_customer INT;
ALTER TABLE buy_product ADD CONSTRAINT fk_customer2 FOREIGN KEY (id_customer) references customer(id_customer)
ON UPDATE SET NULL ON DELETE SET NULL;

-- DROPPING COLUMNS
ALTER TABLE customer DROP COLUMN place_name;
ALTER TABLE component_product DROP COLUMN product_name;
ALTER TABLE component_product DROP COLUMN material_name;
ALTER TABLE buy_product DROP COLUMN product_name;
ALTER TABLE buy_product DROP COLUMN place_name;
ALTER TABLE buy_product DROP COLUMN customer_name;

-- DROPPING PICTURES
ALTER TABLE material DROP COLUMN material_picture;
ALTER TABLE product DROP COLUMN product_picture;

-- RENAME
ALTER TABLE customer RENAME COLUMN phone TO phone_number;


-- CREATING NEW TABLE
CREATE TABLE IF NOT EXISTS bill_item (
id_bill_item INT PRIMARY KEY AUTO_INCREMENT,
id_product_bill_item INT,
id_place_bill_item INT,
CONSTRAINT fk_id_product_bill_item FOREIGN KEY (id_product_bill_item) references product(id_product) ON UPDATE SET NULL ON DELETE SET NULL,
CONSTRAINT fk_id_place_bill_item FOREIGN KEY (id_place_bill_item) references place(id_place) ON UPDATE SET NULL ON DELETE SET NULL
) ENGINE=InnoDB;

-- INSERTNG ROWS
INSERT INTO place (id_place, place_name, zip, state) VALUES (NULL, 'Smederevo', '11300', 'Srbija');
INSERT INTO place (id_place, place_name, zip, state) VALUES (NULL, 'Beograd', '11000', 'Srbija');

INSERT INTO customer (id_customer, customer_name, customer_surname, customer_jmbg, address, phone_number, id_place)
VALUES (NULL, 'Tamara', 'Pantic', '0304998765020', 'Srbina 46', '0644770562', 1);
INSERT INTO customer (id_customer, customer_name, customer_surname, customer_jmbg, address, phone_number, id_place)
VALUES (NULL, 'Daki', 'Pantic', '2009992765020', 'Karadjordjeva 3', '0644333362', 2);

INSERT INTO material (id_material, material_name, material_description) VALUES (NULL, 'Kakao', 'Kakao iz juzne Afrike...');
INSERT INTO material (id_material, material_name, material_description) VALUES (NULL, 'Maslac', 'Visokomasni...');

INSERT INTO product (id_product, product_name, product_description, price) VALUES (NULL, 'Cokolada', 'Cokolada sa 70% kakaoa...', 160);
INSERT INTO product (id_product, product_name, product_description, price) VALUES (NULL, 'Torta', 'Vocna torta sa plazmom i ...', 1400);

INSERT INTO component_product (id_component_product, quantity, id_product, id_material) VALUES (NULL, 100, 1, 1);
INSERT INTO component_product (id_component_product, quantity, id_product, id_material) VALUES (NULL, 10, 2, 2);

INSERT INTO buy_product (id_buy_product, quantity_buy, total_price, date_buy, id_product, id_place, id_customer)
VALUES (NULL, 3, 580, '2023-01-01', 1, 1, 1);
INSERT INTO buy_product (id_buy_product, quantity_buy, total_price, date_buy, id_product, id_place, id_customer)
VALUES (NULL, 2, 1850, '2023-03-02', 2, 2, 2);

INSERT INTO bill_item (id_bill_item, id_product_bill_item, id_place_bill_item) VALUES (NULL, 1, 1);
INSERT INTO bill_item (id_bill_item, id_product_bill_item, id_place_bill_item) VALUES (NULL, 2, 2);

-- DELETING ROWS AND TABLES

DELETE FROM bill_item WHERE id_bill_item=1;
DELETE FROM bill_item WHERE id_bill_item=2;
DROP TABLE bill_item;

DELETE FROM buy_product WHERE id_buy_product=1;
DELETE FROM buy_product WHERE id_buy_product=2;
DROP TABLE buy_product;

DELETE FROM customer WHERE id_customer=1;
DELETE FROM customer WHERE id_customer=2;
DROP TABLE customer;

DELETE FROM place WHERE id_place=1;
DELETE FROM place WHERE id_place=2;
DROP TABLE place;

DELETE FROM component_product WHERE id_component_product=1;
DELETE FROM component_product WHERE id_component_product=2;
DROP TABLE component_product;


DELETE FROM material WHERE id_material=1;
DELETE FROM material WHERE id_material=2;
DROP TABLE material;

DELETE FROM product WHERE id_product=1;
DELETE FROM product WHERE id_product=2;
DROP TABLE product;

DROP DATABASE IF EXISTS record
