import matplotlib.pyplot as plt

country_list = [
    'Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
    'Bahamas', 'Bahrain', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bosnia and Herzegovina', 'Brazil',
    'Bulgaria', 'Cabo Verde', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
    'Czech Republic', 'Denmark', 'Dominica', 'Ecuador', 'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France',
    'Georgia', 'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland', 'Ireland', 'Israel',
    'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania',
    'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Norway', 'Oman', 'Panama', 'Paraguay', 'Philippines', 'Poland', 'Portugal',
    'Puerto Rico', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saint Kitts and Nevis',
    'Saint Lucia', 'Saint Vincent and Grenadines', 'San Marino', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia',
    'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland', 'Thailand',
    'Trinidad and Tobago', 'Turkey', 'Turkmenistan', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
    'United States', 'Uruguay', 'Uzbekistan']
age = [
    '5-14', '15-24', '25-34', '35-54', '55-74', '75+']
blue = (5 / 255, 20 / 255, 255 / 255)
pink = (255 / 255, 37 / 255, 209 / 255)
green = (32 / 255, 168 / 255, 72 / 255)
yellow = (241 / 255, 255 / 255, 6 / 255)

country = "Ukraine"

table = []
country_data = []
suicide_data = []

# fill table -s
length = len(country)
file = open("master.csv")
for line in file:
    if line[:length] == country:
        s = line.index('"')
        e = line.index('"', s + 1)
        table.append((line[:s] + line[s + 1:e].replace(",", "") + line[e + 1:]).split(","))
file.close()

for line in table:
    # id_country | year | HDI | GDP
    country_data_line = [f"{country_list.index(line[0]):0>3}", int(line[1]),
                         float(line[8]) if len(line[8]) != 0 else None, int(line[9])]
    if country_data_line not in country_data:
        country_data.append(country_data_line)

    # id_country | year | sex | age | suicide | population
    suicide_data.append([f"{country_list.index(line[0]):0>3}", int(line[1]), 0 if line[2] == "male" else 1,
                         age.index(line[3][:-6]), int(line[4]), int(line[5])])
year_s = suicide_data[0][1]
year_e = suicide_data[-1][1]
r = year_e - year_s + 1
for i in range(r):
    if i + year_s not in [line[1] for line in country_data]:
        country_data.append([f"{country_list.index(country):0>3}", i + year_s, None, None])
country_data.sort()

# for bar : suicides male/female in country
year = [year_s + i for i in range(r)]
array_male = [0 for i in range(r)]
array_female = [0 for i in range(r)]
array_male_pop = [0 for i in range(r)]
array_female_pop = [0 for i in range(r)]

for row in suicide_data:
    if row[2] == 0:
        array_male[row[1] - year_s] += row[4]
        array_male_pop[row[1] - year_s] += row[5]
    else:
        array_female[row[1] - year_s] += row[4]
        array_female_pop[row[1] - year_s] += row[5]

fig_0, ax_0 = plt.subplots()

ax_0.bar(year, array_male, color=blue, width=0.4, label="Women")
year = [i + 0.4 for i in year]
ax_0.bar(year, array_female, color=pink, width=0.4, label="Men")
ax_0.set_title(f"Suicides in {country}")
ax_0.legend()

# for pie : suicide male/female in country
fig_1, ax_1 = plt.subplots()

ax_1.pie([sum(array_male), sum(array_female)], labels=["male", "female"], autopct='%1.1f%%', explode=(0.01, 0.01),
         colors=[blue, pink])
ax_1.set_title(f"Total suicides in {country}")


# for dependency graph
fig_2, ax_2 = plt.subplots()

year, array = [], []
for i in range(r):
    if array_male_pop[i] != 0:
        year.append(i + year_s)
        array.append(array_male[i] / array_male_pop[i])
ax_2.plot(year, array, color=blue, label="Men")

year, array = [], []
for i in range(r):
    if array_female_pop[i] != 0:
        year.append(i + year_s)
        array.append(array_female[i] / array_female_pop[i])
ax_2.plot(year, array, color=pink, label="Women")

year, array = [], []
for i in range(year_e - year_s + 1):
    if country_data[i][3] is not None:
        year.append(country_data[i][1])
        array.append((country_data[i][3] / (array_female_pop[i] + array_male_pop[i])) / 10000000)
ax_2.plot(year, array, color=green, label="GDP per capita / 10^7")

year, array = [], []
for line in country_data:
    if line[2] is not None:
        year.append(line[1])
        array.append(line[2] / 1000 * 1)
ax_2.plot(year, array, color=yellow, label="HDI / 10^3")
ax_2.legend()
fig_2.tight_layout()

plt.show()


# # for creating populate.sql
# for line in country_data:
#     print(f"({int(line[0])}, {line[1]}, {line[2] if line[2] is not None else 'Null'}, {line[3] if line[3] is not None else 'Null'}),")

# for i in range(r):
#     print(f"({95}, {year_s + i}, {0}, {array_male[i] if array_male[i] is not None else 'Null'}, {array_male_pop[i] if array_male_pop[i] is not 0 else 'Null'}),")
#     print(f"({95}, {year_s + i}, {1}, {array_female[i] if array_female[i] is not None else 'Null'}, {array_female_pop[i] if array_female_pop[i] is not 0 else 'Null'}),")
