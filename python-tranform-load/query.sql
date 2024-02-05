SELECT  name,
        `Non-Elderly Population` AS Non_Elderly,
        `Non-Elderly Uninsured Population` AS Non_Elderly_Uninsured,
        `Age 19-34`+`Age 35-49`+`Age 50-64` AS `Age 19-64`,
        a.Male,
        b.Male `Male Non-Elderly`,
        a.Female,
        b.Female `Female-Non-Elderly`,
        c.confirmed_cases AS cases_covid19,
        deaths
FROM censo_2020 a
LEFT JOIN uninsurance_2021 b
    ON b.`State Name` = a.name 
LEFT JOIN covid19 c 
    ON a.name = c.state_name;


WITH tmp AS
(SELECT state_name state_name_1, MAX(date) date_1 FROM `claroinsurance.covid19.us_states`
GROUP BY state_name)
SELECT * EXCEPT (state_name_1,date_1) FROM `claroinsurance.covid19.us_states` a
INNER JOIN tmp b
  ON a.state_name = b.state_name_1 AND a.date = b.date_1