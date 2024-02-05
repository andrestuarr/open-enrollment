use db;

CREATE TABLE censo_2020(
    stateID int not null AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    Total int(9) NOT NULL,
    Male int(9) NOT NULL,
    Female int(9) NOT NULL,
    PRIMARY KEY (stateID)
);

CREATE TABLE open_enrollment(
    name varchar(100) NOT NULL,
    Non_Elderly int(9) NOT NULL,
    Non_Elderly_Uninsured int(9) NOT NULL,
    Age_19_64 int(9) NOT NULL,
    Male int(9) NOT NULL,
    Male_Non_Elderly int(9) NOT NULL,
    Female int(9) NOT NULL,
    Female_Non_Elderly int(9) NOT NULL,
    cases_covid19 int(9) NOT NULL,
    deaths int(9) NOT NULL,
    PRIMARY KEY (name)
);