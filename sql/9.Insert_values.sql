-- SQLBook: Code
USE druzya_chelovekov;

INSERT INTO
    animal_type (type_name)
VALUES ("pet"), ("pack_animal");

INSERT INTO
    pet_types (pet_type_name)
VALUES ("cat"), ("dog"), ("hamster");

INSERT INTO
    pack_animal_types (pack_animal_type_name)
VALUES ("donkey"), ("horse"), ("camel");

INSERT INTO
    cats (
        name,
        birthday,
        executed_commands,
        pet_types
    )
VALUES (
        "Васька",
        "2007-01-24",
        "Лает, кусает",
        1
    ), (
        "Барсик",
        "2007-01-24",
        "Лает, кусает",
        1
    );

INSERT INTO
    dogs (
        name,
        birthday,
        executed_commands,
        pet_types
    )
VALUES (
        "Шарик",
        "2012-01-24",
        "Лает, дать лапу",
        2
    ), (
        "Барсик",
        "2001-01-24",
        "лежать, голос",
        2
    );

INSERT INTO
    hamsters (
        name,
        birthday,
        executed_commands,
        pet_types
    )
VALUES (
        "Маша",
        "2022-01-24",
        "Лает, кусает",
        3
    ), (
        "Саша",
        "2023-01-24",
        "Лает, кусает",
        3
    );

INSERT INTO
    donkeys (
        name,
        birthday,
        executed_commands,
        pack_animal_types
    )
VALUES (
        "Шрек",
        "2007-01-24",
        "Лает, кусает",
        1
    ), (
        "Фиона",
        "2007-01-24",
        "Лает, кусает",
        1
    );

INSERT INTO
    horses (
        name,
        birthday,
        executed_commands,
        pack_animal_types
    )
VALUES (
        "Белка",
        "2021-01-24",
        "Лает, кусает",
        2
    ), (
        "Блек",
        "2022-01-24",
        "Лает, кусает",
        2
    );

INSERT INTO
    camels (
        name,
        birthday,
        executed_commands,
        pack_animal_types
    )
VALUES (
        "Горбатый",
        "2014-01-24",
        "Лает, кусает",
        3
    ), (
        "Усатый",
        "2021-01-24",
        "Лает, кусает",
        3
    );