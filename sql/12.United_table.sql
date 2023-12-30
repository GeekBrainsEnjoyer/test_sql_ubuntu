-- SQLBook: Code
USE druzya_chelovekov;

DROP TABLE IF EXISTS united_table;

CREATE TABLE
    united_table (
        id_in_type INT NOT NULL,
        name VARCHAR(30) NOT NULL,
        birthday DATE NOT NUll,
        executed_commands VARCHAR(100) NOT NULL,
        pet_types VARCHAR(30),
        pack_animal_types VARCHAR(30)
    );

INSERT INTO
    united_table (
        id_in_type,
        name,
        birthday,
        executed_commands,
        pet_types,
        pack_animal_types
    )
SELECT
    *,
    NULL AS pack_animal_types
FROM cats
UNION ALL
SELECT
    *,
    NULL AS pack_animal_types
FROM dogs
UNION ALL
SELECT
    *,
    NULL AS pack_animal_types
FROM hamsters
UNION ALL
SELECT
    id,
    name,
    birthday,
    executed_commands,
    NULL AS pet_types,
    pack_animal_types
FROM donkeys
UNION ALL
SELECT
    id,
    name,
    birthday,
    executed_commands,
    NULL AS pet_types,
    pack_animal_types
FROM horses
UNION ALL
SELECT
    id,
    name,
    birthday,
    executed_commands,
    NULL AS pet_types,
    pack_animal_types
FROM camels;