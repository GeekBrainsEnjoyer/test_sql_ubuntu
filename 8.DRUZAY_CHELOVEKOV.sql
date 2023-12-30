-- SQLBook: Code
-- Active: 1703496572033@@127.0.0.1@3306@druzya_chelovekov

DROP DATABASE IF EXISTS druzya_chelovekov;

CREATE DATABASE druzya_chelovekov;

USE druzya_chelovekov;

CREATE TABLE
    animal_type (
        id INT PRIMARY KEY AUTO_INCREMENT,
        type_name VARCHAR(30)
    );

CREATE TABLE
    pet_types (
        id INT PRIMARY KEY AUTO_INCREMENT,
        pet_type_name VARCHAR(30) NOT NULL
    );

CREATE TABLE
    pack_animal_types (
        id INT PRIMARY KEY AUTO_INCREMENT,
        pack_animal_type_name VARCHAR(30) NOT NULL
    );

CREATE TABLE
    cats (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pet_types INT NOT NULL
    );

CREATE TABLE
    dogs (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pet_types INT NOT NULL
    );

CREATE TABLE
    hamsters (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pet_types INT NOT NULL
    );

CREATE TABLE
    donkeys (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pack_animal_types INT NOT NULL
    );

CREATE TABLE
    horses (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pack_animal_types INT NOT NULL
    );

CREATE TABLE
    camels (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR (30) NOT NULL,
        birthday DATE NOT NULL,
        executed_commands VARCHAR (150),
        pack_animal_types INT NOT NULL
    );