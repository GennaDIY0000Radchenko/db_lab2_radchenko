-- Кількість самогубств серед жінок/чоловіків в різні роки в Україні

-- select concat(trim(name_country), ' ', year) as country_year, case sex when 0 then 'male' when 1 then 'female' end, suicide, population from suicide_data
-- join country on country.id_country = suicide_data.id_country
-- where suicide_data.id_country = (select id_country from country where name_country = 'Ukraine')

-- Кількість самогубств серед чоловіків та жінок

-- select sum(male.suicide) as male_suicide, sum(female.suicide) as female_suicide from
-- (select * from suicide_data where sex = 0) as male join
-- (select * from suicide_data where sex = 1) as female
-- on male.id_country = female.id_country and male.year = female.year

-- Залежність кіл-ті самогубств від ВВП на душу населення та ІЛР

-- select concat(trim(country.name_country), ' ', country_data.year) as country_year, male.suicide as male_suicide, female.suicide as female_suicide,
--        gdp/(male.population + female.population) as GDP_per_capita, HDI from country_data
-- join (select * from suicide_data where sex = 0) as male   on male.id_country = country_data.id_country and male.year = country_data.year
-- join (select * from suicide_data where sex = 1) as female on female.id_country = country_data.id_country and female.year = country_data.year
-- join country on country.id_country = country_data.id_country

-- Ім'я людей, тривалість життя, тип смерті

-- select
-- concat(l_name, ' ', f_name, ' ', m_name) as name,
-- concat((COALESCE(d_death, CURRENT_DATE) - d_birth)/365, ' years') as alive_time,
-- COALESCE(definition, 'stayin alive') as type_death
-- from people left join type_death ON type_death.type_death = people.type_death
-- ORDER by people.d_birth