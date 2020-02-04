CREATE DATABASE IF NOT EXISTS user_manager;
USE user_manager;

CREATE TABLE ADDRESS (id bigint(20) primary key auto_increment, street varchar(255) not null,  zip_code varchar(255) not null, district varchar(255) not null, city varchar(255) not null, state varchar(255) not null);

CREATE TABLE TELEPHONE(id bigint(20) primary key auto_increment, tel_number int(9) unique not null);

CREATE TABLE USER (id bigint(20) primary key auto_increment, name varchar(255) not null, id_document int(12) unique not null, email varchar(255) unique not null, birth_date date, register_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE USER_TEL(id bigint(20) primary key auto_increment, user_id bigint, tel_id bigint, foreign key (user_id) references USER(id), foreign key (tel_id) references TELEPHONE(id));

CREATE TABLE USER_ADDRESS(user_id bigint, address_id bigint, foreign key (user_id) references USER(id), foreign key (address_id) references ADDRESS(id));
