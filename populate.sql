insert into country (id_country, name_country)
values
(0, 'Albania'),
(6, 'Austria'),
(35, 'Germany'),
(75, 'Russian federation'),
(95, 'Ukraine'),
(98, 'United States'),
(100, 'Uzbekistan');

insert into Country_data (id_country, year, hdi, gdp)
values
(95, 1987, Null, 64087694038),
(95, 1988, Null, 74703517903),
(95, 1989, Null, 82709161099),
(95, 1990, 0.705, 81456918679),
(95, 1991, Null, 77464561150),
(95, 1992, Null, 73942235330),
(95, 1993, Null, 65648559903),
(95, 1994, Null, 52549555149),
(95, 1995, 0.662, 48213868178),
(95, 1996, Null, 44558077827),
(95, 1997, Null, 50150399792),
(95, 1998, Null, 41883241472),
(95, 1999, Null, 31580639045),
(95, 2000, 0.668, 31261527363),
(95, 2001, Null, 38009344577),
(95, 2002, Null, 42392896031),
(95, 2003, Null, 50132953288),
(95, 2004, Null, 64883060726),
(95, 2005, 0.713, 86142018069),
(95, 2006, Null, 107753069307),
(95, 2007, Null, 142719009901),
(95, 2008, Null, 179992405832),
(95, 2009, Null, 117227769792),
(95, 2010, 0.732, 136013155905),
(95, 2011, 0.738, 163159671670),
(95, 2012, 0.743, 175781379051),
(95, 2013, Null, Null),
(95, 2014, 0.747, 133503411376),
(95, 2015, Null, 91030959455);

insert into Suicide_data (id_country, year, sex, suicide, population)
values
(95, 1987, 0, 7457, 21632300),
(95, 1987, 1, 2593, 25741900),
(95, 1988, 0, 7243, 21742900),
(95, 1988, 1, 2508, 25807000),
(95, 1989, 0, 8296, 21877300),
(95, 1989, 1, 2591, 25884400),
(95, 1990, 0, 8229, 22011600),
(95, 1990, 1, 2416, 25960000),
(95, 1991, 0, 8338, 22149700),
(95, 1991, 1, 2362, 26050900),
(95, 1992, 0, 9128, 22316200),
(95, 1992, 1, 2538, 26171100),
(95, 1993, 0, 9864, 22434800),
(95, 1993, 1, 2605, 26245700),
(95, 1994, 0, 11063, 22427600),
(95, 1994, 1, 2763, 26191400),
(95, 1995, 0, 11909, 22348600),
(95, 1995, 1, 2632, 26066700),
(95, 1996, 0, 12495, 22246800),
(95, 1996, 1, 2665, 25927700),
(95, 1997, 0, 12110, 22138700),
(95, 1997, 1, 2793, 25784300),
(95, 1998, 0, 11948, 22034100),
(95, 1998, 1, 2841, 25641300),
(95, 1999, 0, 11726, 21921200),
(95, 1999, 1, 2637, 25494200),
(95, 2000, 0, 11834, 21786300),
(95, 2000, 1, 2633, 25339100),
(95, 2001, 0, 10939, 21633783),
(95, 2001, 1, 2192, 25172186),
(95, 2002, 0, 10367, 21203082),
(95, 2002, 1, 2169, 24856935),
(95, 2003, 0, 10163, 21024802),
(95, 2003, 1, 2150, 24672581),
(95, 2004, 0, 9391, 20838059),
(95, 2004, 1, 1865, 24484767),
(95, 2005, 0, 8860, 20642726),
(95, 2005, 1, 1761, 24296544),
(95, 2006, 0, 8300, 20451715),
(95, 2006, 1, 1713, 24108319),
(95, 2007, 0, 8403, 20271460),
(95, 2007, 1, 1629, 23927212),
(95, 2008, 0, 7779, 20099461),
(95, 2008, 1, 1675, 23756662),
(95, 2009, 0, 7991, 19955090),
(95, 2009, 1, 1724, 23602854),
(95, 2010, 0, 7510, 19837828),
(95, 2010, 1, 1579, 23458981),
(95, 2011, 0, 7309, 19742243),
(95, 2011, 1, 1664, 23332548),
(95, 2012, 0, 7361, 19682379),
(95, 2012, 1, 1697, 23233556),
(95, 2013, 0, Null, Null),
(95, 2013, 1, Null, Null),
(95, 2014, 0, 6412, 18595916),
(95, 2014, 1, 1556, 21868249),
(95, 2015, 0, 6148, 18552231),
(95, 2015, 1, 1426, 21793215);

insert into Type_death (type_death, definition)
values
(0, 'suicide'),
(1, 'murder'),
(2, 'accident'),
(3, 'cancer'),
(4, 'heart'),
(-1, 'other');

insert into People (passport, id_country, sex, f_name, l_name, m_name, d_birth, d_death, type_death)
values
(00642678, 95, 0 , 'Hennadii', 'Radchenko', 'Anatoliiovych', '2003-07-11', null, null) ,
(00571584, 75, 0 , 'Bikhner', 'Yevhenii', 'Aleksandrovych', '1861-05-20', '1913-05-20', 0) ,
(00125954, 98, 0 ,  'Bruce', 'Patrik', 'Genri', '1880-04-02', '1936-10-12', 0) ,
(00248921, 35, 0 ,  'Vahner', 'Moritz', 'Friedrich', '1813-03-10', '1887-05-31', 0) ,
(01548911, 74, 0 ,  'Sandor', 'Zold', null, '1913-05-19', '1951-04-20', 0) ,
(03259546, 98, 0 ,  'John', 'Fitzgerald', 'Kennedy', '1917-05-29', '1963-11-22', 1) ,
(05478949, 98, 0 ,  'Chadwick', 'Boseman', 'Aaron', '1976-11-29', '2020-08-28', 3) ,
(02573914, 98, 0 ,  'Frank', 'Maxwell', 'Andrews', '1884-02-03', '1943-05-03', 2) ;
