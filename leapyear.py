import streamlit as st
import matplotlib.pyplot as plt

def is_(leap_year):
 if leap_year %4!=0:
        return False
 elif leap_year % 100 !=0:
        return True 
 elif leap_year %400!=0:
        return False
 else:
     return leap_year(start_year,end_year)
st.title(" Bar Graph")
st.write("This program generates a bar graph of leap years ")

        
start_year = st.number_input("Enter the start year:", value=1000)
end_year = st.number_input("Enter the end year:", value=2023)

leap_years= (start_year, end_year)

if len(leap_years) == 0:
        st.write("No leap years found in the given range.")
else:
        st.write("Leap years found:", leap_years)

        year_labels = [str(year) for year in leap_years]
        year_counts = [1] * len(leap_years)

        fig, ax = plt.subplots()
        ax.bar(year_labels, year_counts)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        ax.set_title("Leap Years")

        st.pyplot(fig)
