-- SQLBook: Code
USE druzya_chelovekov;

DROP TABLE IF EXISTS young_animals;

CREATE TABLE
    young_animals (
        id INT NOT NULL,
        name VARCHAR(30) NOT NULL,
        birthday DATE NOT NUll,
        executed_commands VARCHAR(100),
        age INT NOT NULL
    )

INSERT INTO
    young_animals (
        id,
        name,
        birthday,
        executed_commands,
        age
    )
SELECT
    id_in_type,
    name,
    birthday,
    executed_commands,
    TIMESTAMPDIFF(MONTH, birthday, curdate())
FROM united_table
WHERE
    TIMESTAMPDIFF(MONTH, birthday, curdate()) BETWEEN 12 and 36;