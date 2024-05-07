import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
def load_data():
    data = pd.read_csv("dashboard/main_data.csv")
    return data

bike_data = load_data()

# Title
st.title('Dashboard Analisis Data: Bike Sharing Dataset')

#Make tabs
tab1, tab2 = st.tabs(["Question 1", "Question 2"])

with tab1:
   #Make text
   st.subheader("Bagaimana Suhu Lingkungan Berpengaruh Pada Jumlah Penggunaan Sepeda")
   st.markdown("Suhu mempengaruhi jumlah penggunaan sepeda dimana ditunjukkan dengan nilai korelasi :blue-background[0.4]. ")
   
   #Transform column to numpy array
   temp = bike_data[:]['temp'].to_numpy()
   cnt = bike_data[:]['cnt'].to_numpy()
   
   #Get slope and intercept from coefficient to make regression line
   coefficients = np.polyfit(temp, cnt, 1)
   slope, intercept = coefficients

   # Generate y values for the regression line
   regression_line = slope * temp + intercept
   
   #Make plot
   fig, ax = plt.subplots()
   ax.scatter(bike_data['temp'], bike_data['cnt'], label='Data Points')
   ax.plot(temp, regression_line, label='Regression Line', color='red')

   # Adding Title dan label
   ax.set_title('Jumlah Pengguna Sepeda berdasarkan Suhu')
   ax.set_xlabel('Suhu (by temp)')
   ax.set_ylabel('Jumlah Pengguna Sepeda (by cnt)')
   
   #Show plot
   st.pyplot(fig)
   
   #Make Text
   st.markdown('''Berdasarkan visualisasi data yang dilakukan juga diketahui bahwa, 
               semakin tinggi suhu maka akan semakin meningkat jumlah pesepeda. 
               Hal tersebut bersesuaian dengan nilai **Korelasi** yang **Positif**''')
   

with tab2:
   #Make text
   st.subheader("Bagaimana Suhu Lingkungan Berpengaruh Pada Jumlah Penggunaan Sepeda")
   st.markdown("Waktu memiliki korelasi positif dengan jumlah pengguna sepeda dengan nilai :blue-background[0.39]. ")
   
   
   fig, ax = plt.subplots()
   
   #Make Bar plot
   ax.bar(bike_data['hr'], bike_data['cnt'], color ='maroon', 
         width = 0.4)

   # Adding title and label
   ax.set_title('Jumlah Pengguna Sepeda berdasarkan Waktu')
   ax.set_xlabel('Waktu (by hr)')
   ax.set_ylabel('Jumlah Pengguna Sepeda (by cnt)')

   #Show plot
   st.pyplot(fig)
   
   #Make Text
   st.markdown('''Berdasarkan visualisasi data yang dilakukan juga diketahui bahwa, 
               jumlah pengguna sepeda menigkat pada waktu tertentu dimana waktu tersebut merupakan waktu berangkat kerja dan juga pulang kerja. 
               dapat dilihat juga pada diagram bar diatas dimana semakin sore maka semakin banyak pengguna sepeda.
               Hal tersebut bersesuaian dengan nilai **Korelasi** yang **Positif**''')
