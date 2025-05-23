import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1: Return all columns for planets that have 0 moons
df_no_moons = pd.read_sql("""SELECT * FROM planets WHERE moons = 0;""", conn1)

# STEP 2: Return the name and mass of each planet with a name of exactly 7 letters
df_name_seven = pd.read_sql("""SELECT name, mass FROM planets WHERE LENGTH(name) = 7;""", conn1)

##### Part 2: Advanced Filtering #####

# STEP 3: Return the name and mass for planets with mass <= 1.00
df_mass = pd.read_sql("""SELECT name, mass FROM planets WHERE mass <= 1.00;""", conn1)

# STEP 4: Return all columns for planets with at least 1 moon and mass < 1.00
df_mass_moon = pd.read_sql("""SELECT * FROM planets WHERE moons > 0 AND mass < 1.00;""", conn1)

# STEP 5: Return the name and color of planets with a color containing 'blue'
df_blue = pd.read_sql("""SELECT name, color FROM planets WHERE color LIKE '%blue%';""", conn1)

##### Part 3: Ordering and Limiting #####

conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6: Return name, age, and breed of hungry dogs, sorted youngest to oldest
df_hungry = pd.read_sql("""SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;""", conn2)

# STEP 7: Return name, age, and hungry status for hungry dogs aged 2-7, sorted alphabetically
df_hungry_ages = pd.read_sql("""SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC;""", conn2)

# STEP 8: Return name, age, and breed for 4 oldest dogs, sorted alphabetically by breed
df_4_oldest = pd.read_sql("""SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4;""", conn2)

##### Part 4: Aggregation #####

conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""SELECT * FROM babe_ruth_stats;""", conn3)

# STEP 9: Return total number of years Babe Ruth played professional baseball
df_ruth_years = pd.read_sql("""SELECT COUNT(DISTINCT year) AS total_years FROM babe_ruth_stats;""", conn3)

# STEP 10: Return total number of home runs Babe Ruth hit
df_hr_total = pd.read_sql("""SELECT SUM(home_runs) AS total_home_runs FROM babe_ruth_stats;""", conn3)

##### Part 5: Grouping and Aggregation #####

# STEP 11: Return team name and number of years played on each team
df_teams_years = pd.read_sql("""SELECT team, COUNT(DISTINCT year) AS number_years FROM babe_ruth_stats GROUP BY team;""", conn3)

# STEP 12: Return teams Babe Ruth averaged over 200 at-bats, with average at-bats
df_at_bats = pd.read_sql("""SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200;""", conn3)

# Close connections
conn1.close()
conn2.close()
conn3.close()