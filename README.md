# Streamlit-5122_World_happiness_report
## WORLD HAPPINESS REPORT - STREAMLIT DASHBOARD
[STREAMLIT APP](https://ramyasenapathy-streamlit-5122-wor-world-happiness-report-mv4ees.streamlit.app/)


* Tab1: WORLD HAPPINESS TREND and RANKING
  * For nine years in a row, Finland has been ranked No. 1 as the happiest 
  * Afganistan as the least happy country in the world.
  * Filter : to add/edit years, the trend line and the ranking changes accordingly
  * The filter is defaulted to all years, must be unchecked to add/edit years

* Tab2: CORRELATION 
  * We have compared 6 factors of happiness, using pearson coefficient
  * Social support has the highest correlation, that explains that people are happy with high social support, high freedom to make life choices and high GDP.
  * Corruption has the negative correlation

* Tab3: NORDIC REGION ANALYSIS
  * As a region with high levels of societal trust, that goes some way to explaining why all the Nordic countries held on to high positions despite the impact of the COVID-19 pandemic (year: 2019-2021). 
  * But other things must explain the consistently high rankings of the Nordic countries over so many years. 
  * There is a filter to add/edit countries, the trend line and the ranking changes accordingly
  * The filter is defaulted to all 5 nordic countries

----
## DATA PREPARATION
* The data is available in the form of excel sheets for year 2008-2021 and year 2022. <br />
[link for data]( https://worldhappiness.report/ed/2022/#appendices-and-data)<br />
Under Appendices & Data :
  * _Year 2022 data  : Data for Figure 2.1_
  * _Year 2008- 2021  : Data for Table 2.1_
* I have merged the data from both the excel sheets and also have added regional information based on countries.
* The world_happiness_data.csv file has the following information: **<br />**

Country_name | Region | year | Happiness_score | GDP_per_capita | Social_support | Life_expectancy | Freedom | Generosity | Corruption

----
## PYTHON FILE
* world_Happiness_report.py
* [Github link for python file](https://github.com/RamyaSenapathy/Streamlit-5122_World_happiness_report/blob/main/world_Happiness_report.py)
----
## FUTURE WORK
* Will be adding the data for the coming years
* Will be considering other factors influencing happiness such as age, population or weather.



