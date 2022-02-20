# By Joshua O
# For the COVID-19 Infographic
# I am a part of Group 7.
# Yes I used Python, satasifying the requirement.
from flask import Flask, request, send_from_directory, url_for
import pandas;
import os;

client_script_fd = os.open("resources/index.html", os.O_RDONLY);
client_script = os.read(client_script_fd, 20*8*1000);
os.close(client_script_fd);

vaccine_data = pandas.read_csv("data/vaccinationData.csv", sep=',', header=0);

columns_to_remove = ["iso_code","continent","total_cases","new_cases","new_cases_smoothed","total_deaths","new_deaths","new_deaths_smoothed","total_cases_per_million","new_cases_per_million","new_cases_smoothed_per_million","total_deaths_per_million","new_deaths_per_million","new_deaths_smoothed_per_million","reproduction_rate","icu_patients","icu_patients_per_million","hosp_patients","hosp_patients_per_million","weekly_icu_admissions","weekly_icu_admissions_per_million","weekly_hosp_admissions","weekly_hosp_admissions_per_million","new_tests","total_tests","total_tests_per_thousand","new_tests_per_thousand","new_tests_smoothed","new_tests_smoothed_per_thousand","positive_rate","tests_per_case","tests_units","total_vaccinations","people_fully_vaccinated","total_boosters","new_vaccinations","new_vaccinations_smoothed","total_vaccinations_per_hundred","people_vaccinated_per_hundred","people_fully_vaccinated_per_hundred","total_boosters_per_hundred","new_vaccinations_smoothed_per_million","new_people_vaccinated_smoothed","new_people_vaccinated_smoothed_per_hundred","stringency_index","population","population_density","median_age","aged_65_older","aged_70_older","gdp_per_capita","extreme_poverty","cardiovasc_death_rate","diabetes_prevalence","female_smokers","male_smokers","handwashing_facilities","hospital_beds_per_thousand","life_expectancy","human_development_index","excess_mortality_cumulative_absolute","excess_mortality_cumulative","excess_mortality","excess_mortality_cumulative_per_million"]

vaccine_data.drop(columns=columns_to_remove, inplace=True);

vaccine_data["people_vaccinated"] = pandas.to_numeric(vaccine_data["people_vaccinated"]);
vaccine_data["date"] = pandas.to_datetime(vaccine_data["date"]);



casesData = pandas.read_csv("data/casesData.csv", sep=',', header=0);

columns_to_remove = ["iso_code","continent","total_cases","new_cases","new_cases_smoothed","total_deaths","new_deaths","new_deaths_smoothed","total_cases_per_million","new_cases_smoothed_per_million","total_deaths_per_million","new_deaths_per_million","new_deaths_smoothed_per_million","reproduction_rate","icu_patients","icu_patients_per_million","hosp_patients","hosp_patients_per_million","weekly_icu_admissions","weekly_icu_admissions_per_million","weekly_hosp_admissions","weekly_hosp_admissions_per_million","new_tests","total_tests","total_tests_per_thousand","new_tests_per_thousand","new_tests_smoothed","new_tests_smoothed_per_thousand","positive_rate","tests_per_case","tests_units","total_vaccinations","people_vaccinated","people_fully_vaccinated","total_boosters","new_vaccinations","new_vaccinations_smoothed","total_vaccinations_per_hundred","people_vaccinated_per_hundred","people_fully_vaccinated_per_hundred","total_boosters_per_hundred","new_vaccinations_smoothed_per_million","new_people_vaccinated_smoothed","new_people_vaccinated_smoothed_per_hundred","stringency_index","population","population_density","median_age","aged_65_older","aged_70_older","gdp_per_capita","extreme_poverty","cardiovasc_death_rate","diabetes_prevalence","female_smokers","male_smokers","handwashing_facilities","hospital_beds_per_thousand","life_expectancy","human_development_index","excess_mortality_cumulative_absolute","excess_mortality_cumulative","excess_mortality","excess_mortality_cumulative_per_million"]

casesData.drop(columns=columns_to_remove, inplace=True);

casesData["new_cases_per_million"] = pandas.to_numeric(casesData["new_cases_per_million"]);
casesData["date"] = pandas.to_datetime(casesData["date"]);


lockdownData = pandas.read_csv("data/lockdownData.csv", sep=',', header=0);

lockdownData["date"] = pandas.to_datetime(casesData["date"]);

populationData = pandas.read_csv("data/populationData.csv", sep=',', header=0);

app = Flask(__name__);

@app.route("/get_vaccine_data/", methods=["GET"])
def get_vaccine_data():
    return vaccine_data.to_json();

@app.route("/get_cases_data/", methods=["GET"])
def get_cases_data():
    return casesData.to_json();

@app.route("/get_population_data/", methods=["GET"])
def get_population_data():
    return populationData.to_json();

@app.route("/get_lockdown_data/", methods=["GET"])
def get_lockdown_data():
    return lockdownData.to_json();

@app.route("/infographic/", methods=["GET"])
def infographic():
    return client_script;

@app.route("/<path:path>", methods=["GET"])
def resources(path):
    return send_from_directory('resources/', path);

if (__name__ == "__main__"):
    app.run(host="0.0.0.0",port=10000);