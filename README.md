# Streamlit-5122_World_happiness_report
## WORLD HAPPINESS REPORT - STREAMLIT DASHBOARD
* under tab1:
  * For nine years in a row, Finland has been ranked No. 1 as the happiest 
  * Afganistan as the least happy country in the world.

The least happy people are mostly from Sub-Saharan Africa and South Asia and they have the world's lowest GDP.
* under tab2 : This has the correlation of 6 factors with happiness score.
  * We have compared 6 factors of happiness, using pearson coefficient
  * Corruption has the negative correlation
  * Social support has the highest correlation, that explains that people are happy with high social support, high freedom to make life choices and high GDP.
* under tab3

----
## DATA PREPARATION
* The data is available in the form of excel sheets for year 2008-2021 and year 2022.  https://worldhappiness.report/ed/2022/#appendices-and-data<br />
Under Appendices & Data :
  * _Year 2022 data  : Data for Figure 2.1_
  * _Year 2008- 2021  : Data for Table 2.1_
* I have merged the data from both the excel sheets and also have added regional information based on countries.
* The world_happiness_data.csv file has the following information: **<br />**

Country_name | Region | year | Happiness_score | GDP_per_capita | Social_support | Life_expectancy | Freedom | Generosity | Corruption

----
## PYTHON FILE
world_Happiness_report.py
[Github](https://github.com/RamyaSenapathy/Streamlit-5122_World_happiness_report/blob/main/world_Happiness_report.py)



