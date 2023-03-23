-- part 2

-- DROP DATABASE IF EXISTS medical_record;
CREATE DATABASE IF NOT EXISTS medical_record;
USE medical_record;


CREATE TABLE IF NOT EXISTS patient(
patient_name VARCHAR(20) NOT NULL,
patient_surname VARCHAR(20) NOT NULL,
patient_jmbg VARCHAR(13) NOT NULL UNIQUE,
address VARCHAR(50) NOT NULL,
phone VARCHAR(20) NOT NULL,
doctor_licence_num VARCHAR(20)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS doctor(
doctor_name VARCHAR(20) NOT NULL,
doctor_surname VARCHAR(20) NOT NULL,
doctor_jmbg VARCHAR(13) NOT NULL UNIQUE,
specialization BOOL,
licence_number VARCHAR(20) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS medicine(
medicine_name VARCHAR(50) NOT NULL,
medicine_id VARCHAR(50) NOT NULL UNIQUE,
producer_name VARCHAR(30) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS disease(
disease_name VARCHAR(30) NOT NULL,
disease_description VARCHAR(100) NOT NULL,
picture BLOB
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS producer(
producer_name VARCHAR(50) NOT NULL,
producer_address VARCHAR(50) NOT NULL,
producer_phone VARCHAR(20) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS suffers_from(
patient_name_carton VARCHAR(30) NOT NULL,
doctor_name_carton VARCHAR(30) NOT NULL,
disease_name_carton VARCHAR(30) NOT NULL,
diagnosis_date DATE NOT NULL
)ENGINE=InnoDB;

-- ADDING PRIMARY KEY

ALTER TABLE patient ADD PRIMARY KEY (patient_jmbg);
ALTER TABLE doctor ADD PRIMARY KEY (doctor_jmbg);
ALTER TABLE medicine ADD PRIMARY KEY (medicine_id);
ALTER TABLE disease ADD PRIMARY KEY (disease_name);
ALTER TABLE producer ADD PRIMARY KEY (producer_name);
ALTER TABLE suffers_from ADD PRIMARY KEY (diagnosis_date);

-- DROPPING PRIMARY KEYS

ALTER TABLE patient DROP PRIMARY KEY;
ALTER TABLE doctor DROP PRIMARY KEY;
ALTER TABLE medicine DROP PRIMARY KEY;
ALTER TABLE disease DROP PRIMARY KEY;
ALTER TABLE producer DROP PRIMARY KEY;
ALTER TABLE suffers_from DROP PRIMARY KEY;

-- ADDING COLUMNS AND PRIMARY KEYS

ALTER TABLE patient ADD COLUMN id_patient INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE doctor ADD COLUMN id_doctor INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE medicine ADD COLUMN id_medicine INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE disease ADD COLUMN id_disease INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE producer ADD COLUMN id_producer INT PRIMARY KEY AUTO_INCREMENT FIRST;
ALTER TABLE suffers_from ADD COLUMN id_suffers_from INT PRIMARY KEY AUTO_INCREMENT FIRST;


-- ADDING FOREIGN KEYS 

ALTER TABLE patient ADD COLUMN id_doctor INT;
ALTER TABLE patient ADD CONSTRAINT fk_id_doctor FOREIGN KEY (id_doctor) references doctor(id_doctor)
ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE medicine ADD COLUMN id_producer INT;
ALTER TABLE medicine ADD CONSTRAINT fk_id_producer FOREIGN KEY (id_producer) references producer(id_producer)
ON UPDATE SET NULL ON DELETE SET NULL;

ALTER TABLE suffers_from ADD COLUMN id_patient INT;
ALTER TABLE suffers_from ADD COLUMN id_doctor INT;
ALTER TABLE suffers_from ADD COLUMN id_disease INT;
ALTER TABLE suffers_from ADD CONSTRAINT fk_id_patient FOREIGN KEY (id_patient) references patient(id_patient)
ON UPDATE SET NULL ON DELETE SET NULL;
ALTER TABLE suffers_from ADD CONSTRAINT fk_id_doctor2 FOREIGN KEY (id_doctor) references doctor(id_doctor)
ON UPDATE SET NULL ON DELETE SET NULL;
ALTER TABLE suffers_from ADD CONSTRAINT fk_id_disease FOREIGN KEY (id_disease) references disease(id_disease)
ON UPDATE SET NULL ON DELETE SET NULL;

-- DROPPING FORMER FOREIGN KEYS
ALTER TABLE patient DROP COLUMN doctor_licence_num;
ALTER TABLE medicine DROP COLUMN producer_name;
ALTER TABLE suffers_from DROP COLUMN patient_name_carton;
ALTER TABLE suffers_from DROP COLUMN doctor_name_carton;
ALTER TABLE suffers_from DROP COLUMN disease_name_carton;


-- DROPPING PICTURES
ALTER TABLE disease DROP COLUMN picture;

-- RENAME
ALTER TABLE patient RENAME COLUMN phone TO phone_number;

-- CREATING NEW TABLE
CREATE TABLE IF NOT EXISTS new_table (
id_new_table INT PRIMARY KEY AUTO_INCREMENT,
id_patient INT,
id_doctor INT,
CONSTRAINT fk_id_patient2 FOREIGN KEY (id_patient) REFERENCES patient(id_patient) ON UPDATE SET NULL ON DELETE SET NULL,
CONSTRAINT fk_id_doctor3 FOREIGN KEY (id_doctor) REFERENCES doctor(id_doctor) ON UPDATE SET NULL ON DELETE SET NULL
)ENGINE=InnoDB;

-- INSERTNG ROWS
INSERT INTO doctor(id_doctor, doctor_name, doctor_surname, doctor_jmbg, specialization, licence_number)
VALUES (NULL, 'Pera', 'Peric', '1112223334445', 1, '1568');
INSERT INTO doctor(id_doctor, doctor_name, doctor_surname, doctor_jmbg, specialization, licence_number)
VALUES (NULL, 'Zika', 'Zikic', '1112223334448', 1, '2235');

INSERT INTO disease(id_disease, disease_name, disease_description)
VALUES (NULL, 'Bronhitis', 'Zapaljenje pluca...');
INSERT INTO disease(id_disease, disease_name, disease_description)
VALUES (NULL, 'Grip', 'Temperatura, kasalj...');

INSERT INTO patient(id_patient, patient_name, patient_surname, patient_jmbg, address, phone_number, id_doctor)
VALUES (NULL, 'Miki', 'Mikic', '9998887776661', 'Karadjordjeva 5', '0648876065', 1);
INSERT INTO patient(id_patient, patient_name, patient_surname, patient_jmbg, address, phone_number, id_doctor)
VALUES (NULL, 'Saki', 'Sakic', '9998885556661', 'Karadjordjeva 8', '0648876333', 2);

INSERT INTO producer (id_producer, producer_name, producer_address, producer_phone)
VALUES (NULL, 'Belafarm', 'Goricka 45', '0116564422');
INSERT INTO producer (id_producer, producer_name, producer_address, producer_phone)
VALUES (NULL, 'Medikafarm', 'Knez Milosa 5', '0115554040');

INSERT INTO medicine (id_medicine, medicine_name, medicine_id, id_producer)
VALUES(NULL, 'Brufen', '654312', 1);
INSERT INTO medicine (id_medicine, medicine_name, medicine_id, id_producer)
VALUES(NULL, 'Fervex', '655552', 2);

INSERT INTO new_table (id_new_table, id_patient, id_doctor)
VALUES(NULL, 1, 1);
INSERT INTO new_table (id_new_table, id_patient, id_doctor)
VALUES(NULL, 2, 2);

INSERT INTO suffers_from (id_suffers_from, diagnosis_date, id_patient, id_doctor, id_disease)
VALUES (NULL, '2023-06-06', 1, 1, 1);
INSERT INTO suffers_from (id_suffers_from, diagnosis_date, id_patient, id_doctor, id_disease)
VALUES (NULL, '2023-08-08', 2, 2, 2);


-- DELETING ROWS AND TABLES

DELETE FROM suffers_from WHERE id_suffers_from=1;
DELETE FROM suffers_from WHERE id_suffers_from=2;
DROP TABLE suffers_from;

DELETE FROM new_table WHERE id_new_table=1;
DELETE FROM new_table WHERE id_new_table=2;
DROP TABLE new_table;

DELETE FROM patient WHERE id_patient=1;
DELETE FROM patient WHERE id_patient=2;
DROP TABLE patient;

DELETE FROM medicine WHERE id_medicine=1;
DELETE FROM medicine WHERE id_medicine=2;
DROP TABLE medicine;

DELETE FROM disease WHERE id_disease=1;
DELETE FROM disease WHERE id_disease=2;
DROP TABLE disease;

DELETE FROM doctor WHERE id_doctor=1;
DELETE FROM doctor WHERE id_doctor=2;
DROP TABLE doctor;

DELETE FROM producer WHERE id_producer=1;
DELETE FROM producer WHERE id_producer=2;
DROP TABLE producer;

DROP DATABASE IF EXISTS medical_record

