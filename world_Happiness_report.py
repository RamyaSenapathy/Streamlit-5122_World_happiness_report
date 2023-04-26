import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import seaborn as sns

st.title(f"World Happiness Report")

#data   #year>2010 data
df = pd.read_csv("C:/Ramya/Streamlit/world_happiness/world_happiness_data.csv")
df = df[df['year'] > 2010] 
#nordic data
nordic= ['Sweden','Denmark','Iceland','Norway','Finland']
nordic_df = df[df['Country_name'].isin(nordic)] 
#o/p :  entire df with country filtered

#list of nordic country names
country2 = nordic_df['Country_name'].drop_duplicates().sort_values()                                                  
country3=country2.copy().to_list()                                                                                      
#o/p : ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']

#to get a list of year values
year_values = df['year'].drop_duplicates().sort_values()
year_list=year_values.copy().to_list()
#o/p: [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

##sidebar with year      #o/p: year (default 2022)
all = st.sidebar.checkbox("Select all", value=True)
if all:
    Year_select = st.sidebar.multiselect("Select one or more Country of origin:",   year_list, year_list)
else:
    Year_select =  st.sidebar.multiselect("Select one or more Country of origin:", year_list, default = 2022)

#passing year_select
df_year = df[(df.year).isin(Year_select)] #o/p : entire df since no group by used



#df grouped by year 
avg_happiness_score = df_year.groupby('year')['Happiness_score'].mean().round(2) 
avg_happiness_score = avg_happiness_score.reset_index() #to convert it to df 
#O/P : 	year	Happiness_score

#df grouped by year & country
top10_country = df_year.groupby(['Country_name'])['Happiness_score'].mean().round(2) 
top10_country = top10_country.reset_index() #to convert it to df 
#O/P : 		Country_name	Happiness_score

avg_happiness_score_asc = top10_country.groupby('Country_name')['Happiness_score'].mean().sort_values(ascending=False).round(2).head(5)
avg_happiness_score_desc = top10_country.groupby('Country_name')['Happiness_score'].mean().sort_values(ascending=True).round(2).head(5)
# o/p: Columns : Country_name  Happiness_score


#3 tabs for display
tab1, tab2, tab3 = st.tabs(['Most/Least happy countries','Correlation of factors', 'Nordic region analysis'])

with tab1:
            #Fig1
            figpx = px.line(avg_happiness_score, x = 'year', y = 'Happiness_score',title='Happiness Trend across the world',text="Happiness_score")
            figpx.update_traces(textposition="top center")
            st.plotly_chart(figpx)

            #fig2
            col1, col2 = st.columns(2)
            with col1:
                st.text('Most happy countries')
                st.write(avg_happiness_score_asc)
            with col2:
                st.text('Least happy countries')
                st.write(avg_happiness_score_desc)
          
with tab2:
            corr1 = df[['Social_support','Freedom', 'GDP_per_capita', 'Life_expectancy',  'Generosity', 'Corruption']].corrwith(df['Happiness_score'])
            df_corr = corr1.reset_index() # changing series into df
            df_corr.columns = ['Factors', 'pearson_coefficient']  #changing column name
            df_corr['pearson_coefficient'] =df_corr['pearson_coefficient'] .round(3)

            #barchart 
            corr_fig =alt.Chart(df_corr).mark_bar(color="teal").encode(
                x='pearson_coefficient:Q', y= 'Factors').properties(width=600,height=400).properties(title='Correlation of happiness score against 6 factors')

            text = corr_fig.mark_text(
                align='left',  baseline='middle',  dx=3, color='black'
            ).encode(text='pearson_coefficient:Q' )

            corr_fig + text

with tab3:    
        options = st.radio("Select", ('All','One/more countries'),horizontal=True,label_visibility="collapsed")
        if options == 'All':
            country_select = st.multiselect("Selected countries",country3, country3,label_visibility="collapsed")
        else:
            country_select =  st.multiselect("Selected countries",country3, default = 'Finland',label_visibility="collapsed")

#passing country select
        filtered_nordic_country = nordic_df[(nordic_df.Country_name).isin(country_select)] 
        
        line = alt.Chart(filtered_nordic_country).mark_line().encode(
            x='year:O', y=alt.Y('mean(Happiness_score):Q',scale=alt.Scale(domain=[7, 8.5])),
            color='Country_name:N'
        ).properties(title='Nordic countries happiness trend over the years').properties(
        width=400,height=200)

        rank = alt.Chart(filtered_nordic_country).mark_bar().encode(
            x=alt.X('mean(Happiness_score):Q',scale=alt.Scale(domain=[7.3, 7.6])),
            y=alt.Y('Country_name:N',sort='-x'),
            color=alt.Color('Country_name',scale=alt.Scale(scheme='category20')),
        ).properties(title='Ranking of Nordic countries based on happiness score')
        line & rank
