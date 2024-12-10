import streamlit as st

st.set_page_config(page_title='BMI Calculator')

st.header('BMI (Body Mass Calculator) Calculator')
st.markdown("""
    **Welcome to the BMI Calculator!**  
    This simple tool helps you calculate your Body Mass Index (BMI) based on your height and weight.
    Enter your height and weight, and you'll get your BMI along with a category.
    """)


#Function to calculate BMI
def calculate_BMI(weight,height):
    BMI = weight / (height**2)
    return BMI

#BMI Range
st.subheader('Range of BMI')

st.markdown('Underweight -- Less than 18.5')
st.markdown('Normal Weight -- 18.5 to 24.9')
st.markdown('Over Weight -- 25 to 29.9')
st.markdown('Obese -- Greater than 29.9')

#Input 
height = st.number_input('Enter your height(in cm):',min_value=50,max_value=300)
weight = st.number_input('Enter your weight(in kg):', format="%.2f", step=0.01, min_value=5.00,max_value=200.00)
height = height/100

#Button
if st.button('Calculate BMI'):
    if height > 0 and weight > 0:
        BMI = calculate_BMI(weight,height)
        # BMI Categories
        if BMI < 18.5:
            st.markdown("You are Underweight")
        elif BMI >= 18.5 and BMI <= 24.9:
            st.markdown("You have a Normal weight")
        elif BMI >= 25 and BMI <= 29.9:
            st.markdown("You are Overweight")
        else:
            st.markdown("You are Obese")

    st.write('Your BMI :',round(BMI,2))

#Purpose of BMI
st.header('Purpose of BMI')

st.markdown('''The purpose of BMI (Body Mass Index) is to provide a simple and quick method to estimate whether an individual's body weight is healthy relative to their height. It acts as a general indicator for categorizing people into weight groups and identifying potential health risks.

**Key Objectives:**

    Health Monitoring:

Assess whether a person is underweight, normal weight, overweight, or obese.

    Risk Identification:

Highlight risks associated with weight-related conditions like heart disease, diabetes, and hypertension.

    Public Health:
    
Serve as a metric in population studies to understand and manage health trends.

Though useful, BMI doesn't directly measure body fat or account for individual factors like muscle mass or bone density.''')

#Health Risks
st.header('Here are the health risks by BMI category:')
st.markdown('''
1. **Underweight (BMI < 18.5)**
 >Malnutrition
 
 >Weakened immune system
 
 >Osteoporosis (bone weakness)
 
 >Fertility issues (especially in women)
 
 >Increased risk of anemia
2. **Normal Weight (BMI 18.5–24.9)**
 >Generally associated with a lower risk of weight-related health problems if paired with a healthy lifestyle.
3. **Overweight (BMI 25–29.9)**
     >Increased risk of:
 
 >High blood pressure (hypertension)
   
   >Type 2 diabetes
   
   >Cardiovascular diseases
   
   >Sleep apnea
4. **Obese (BMI ≥ 30)**
     >Significantly higher risk of:

 >Heart disease and stroke

   >Type 2 diabetes

   >Certain cancers (e.g., breast, colon)

   >Gallbladder disease

   >Osteoarthritis

   >Respiratory issues (e.g., asthma, sleep apnea)''')
