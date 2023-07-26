import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import json
from streamlit_lottie import st_lottie

def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

cong = load_lottie('lottie/animation_lkiirp04.json')

sudhir_kumar = Image.open("images/sudhir_kumar.jpg")
srikanth_vemula = Image.open("images/srikanth_vemula.jpg")
rajashekar_reddy = Image.open("images/rajashekar_reddy.jpg")
dr_sandhya = Image.open("images/dr_sandhya.jpg")
subodh_raju = Image.open("images/subodh_raju.jpg")
image1 = Image.open("images/mild_medications.jpg")
med2 = Image.open("images/med2.jpg")

def doc(pic, headerr, sub, cont1, linkk):
    col1, col2, col3, col4 = st.columns([1, 3, 3, 2])
    with col1:
        st.empty()
    with col2:
        st.image(pic)
    with col3:
        st.header(headerr)
        st.subheader(sub)
        st.write(cont1)
        st.write(linkk)
    with col4:
        st.empty()

def nonDemented():
    col1, col2 = st.columns([1, 3]) 
    with col1:
        st_lottie(cong, speed=1, reverse=False, loop=True, quality="high", height= 200 , width=200, key=None)
    with col2:
        st.write("##")
        st.title(":blue[Congratulations your are non Demented!!]")
    

def veryMildDemented():
    
    tab1, tab2, tab3 = st.tabs(['Remedies', 'Medication', 'Doctors and Neurologists'])

    with tab1:
        st.title(':blue[**Remedies for Very Mild Dementia**]')
        st.subheader("Regular Mental Stimulation:")
        st.write("Engage in activities that stimulate the brain, such as puzzles, memory games, reading, or learning new skills. Mental stimulation can help maintain cognitive function.")
        st.subheader("Physical Exercise:")
        st.write("Encourage regular physical activity, as it can improve blood flow to the brain and support overall health. Walking, gentle exercises, or activities like yoga may be beneficial.")
        st.subheader("Healthy Diet:")
        st.write("Promote a balanced and nutritious diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. Proper nutrition supports brain health.")
        st.subheader("Social Interaction:")
        st.write("Encourage social engagement with family, friends, or support groups. Socializing can provide emotional support and cognitive stimulation.")
        st.subheader("Routine and Structure:")
        st.write("Establish a structured daily routine to reduce confusion and provide a sense of stability.")
        st.subheader("Memory Aids:")
        st.write("Use memory aids like calendars, notes, or reminders to help with daily tasks and appointments.")
        st.subheader("Simplify Tasks:")
        st.write("Break tasks into smaller, manageable steps to make them less overwhelming.")
        st.subheader("Safe Environment:")
        st.write("Ensure the living space is safe, clutter-free, and well-organized to prevent accidents and reduce confusion.")
        st.subheader("Relaxation Techniques:")
        st.write("Practice relaxation techniques such as deep breathing, meditation, or listening to calming music to reduce stress and anxiety.")
        st.subheader("Hobbies and Interests:")
        st.write("Encourage engagement in hobbies and activities the person enjoys, as it can boost mood and cognitive function.")
        st.subheader("Support and Understanding:")
        st.write("Provide emotional support and understanding to the individual and their caregivers. Emotional well-being is essential for overall health.")
        st.subheader("Regular Medical Check-ups:")
        st.write("Ensure the person receives regular medical check-ups and screenings to monitor their health and address any underlying issues.")
    with tab2:
        st.title(':blue[**Medications for Very Mild Dementia**]')
        st.write("##")
        st.image(image1)
    with tab3:
        st.title(":blue[**Best Alzheimers Disease Treatment Doctors in Hyderabad**]")
        st.divider()
        doc(sudhir_kumar, "Dr. Sudhir Kumar", "Neurologist, Hyderabad, India", "Consultant, 17 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(srikanth_vemula, "Dr. Srikanth Vemula", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(rajashekar_reddy, "Dr. Rajasekhar Reddy K", "Neurologist, Hyderabad, India", "Consultant, 24 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(dr_sandhya, "Dr. Sandhya Manorenj", "Neurologist, Hyderabad, India", "Consultant, 21 years of experience",  " :calendar: [PACE HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/pace-hospital-hyderabad)")
        st.divider()
        doc(subodh_raju, "Dr. Subodh Raju", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [RAINBOW CHILDREN'S HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/rainbow-childrens-hospital-hyderabad)")
        st.divider()


def mildDemented():
    tab1, tab2, tab3 = st.tabs(['Remedies', 'Medication', 'Doctors and Neurologists'])

    with tab1 :
        st.title(':blue[**Remedies for Mild Dementia**]')
        st.subheader("Cognitive Stimulation:")
        st.write("Engage in activities that stimulate the brain, such as puzzles, word games, reading, and memory exercises. Cognitive stimulation may help maintain cognitive function and memory.")
        st.subheader("Physical Exercise:")
        st.write("Regular physical activity can be beneficial for overall health, including brain health. It may improve mood, reduce stress, and support cognitive function.")
        st.subheader("Healthy Diet:")
        st.write("A balanced and nutritious diet may promote brain health. Focus on fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods and sugar.")
        st.subheader("Social Engagement:")
        st.write("Encourage social interaction and engagement with family, friends, or support groups. Socializing can provide emotional support and stimulate cognitive function.")
        st.subheader("Structured Routine:")
        st.write("Establishing a structured daily routine can help individuals with mild dementia feel more in control and reduce confusion.")
        st.subheader("Memory Aids:")
        st.write("Use memory aids like calendars, notes, and reminders to help with daily tasks and appointments.")
        st.subheader("Avoid Overstimulation:")
        st.write("Minimize exposure to loud noises, crowded places, or overwhelming environments, as these can be stressful for individuals with dementia.")
        st.subheader("Simplify Tasks:")
        st.write("Break tasks into smaller, manageable steps to make them less overwhelming.")
        st.subheader("Safe Environment:")
        st.write("Ensure the living space is safe and clutter-free to prevent accidents and reduce confusion.")
        st.subheader("Music Therapy:")
        st.write("Listening to familiar and soothing music may have a calming effect and evoke positive memories.")
    with tab2:
        st.title(':blue[**Medications for Mild Dementia**]')
        st.write("##")
        st.image(image1)
    with tab3:
        st.title(":blue[**Best Alzheimers Disease Treatment Doctors in Hyderabad**]")
        st.divider()
        doc(sudhir_kumar, "Dr. Sudhir Kumar", "Neurologist, Hyderabad, India", "Consultant, 17 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(srikanth_vemula, "Dr. Srikanth Vemula", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(rajashekar_reddy, "Dr. Rajasekhar Reddy K", "Neurologist, Hyderabad, India", "Consultant, 24 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(dr_sandhya, "Dr. Sandhya Manorenj", "Neurologist, Hyderabad, India", "Consultant, 21 years of experience",  " :calendar: [PACE HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/pace-hospital-hyderabad)")
        st.divider()
        doc(subodh_raju, "Dr. Subodh Raju", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [RAINBOW CHILDREN'S HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/rainbow-childrens-hospital-hyderabad)")
        st.divider()
        
def moderateDemented():
    tab1, tab2, tab3 = st.tabs(['Remedies', 'Medication', 'Doctors and Neurologists'])

    with tab1 :
        st.title(':blue[**Remedies for Moderate Dementia**]')
        st.subheader("Maintain Routine and Structure:")
        st.write("Establish a consistent daily routine to provide a sense of familiarity and reduce anxiety. Stick to regular meal times, activities, and sleep schedules.")
        st.subheader("Assistive Devices and Memory Aids:")
        st.write("Use assistive devices like clocks, calendars, and labeled drawers to help with daily tasks and organization.")
        st.subheader("Physical Exercise:")
        st.write("Encourage regular physical activity suitable for the individual's abilities, such as walking or gentle exercises. Physical activity can improve mood and overall well-being.")
        st.subheader("Cognitive Stimulation:")
        st.write("Engage in activities that stimulate the brain, such as puzzles, reminiscence therapy, or simple games. Adapt activities to the person's cognitive abilities.")
        st.subheader("Safety Measures:")
        st.write("Ensure the living environment is safe and secure. Install handrails, remove tripping hazards, and consider using alarms or monitoring systems to prevent accidents.")
        st.subheader("Personalized Communication:")
        st.write("Use clear and simple language when communicating with the person. Maintain eye contact and allow them enough time to respond.")
        st.subheader("Memory Care Programs:")
        st.write("Consider memory care programs or day care centers specifically designed for individuals with dementia. These programs offer social engagement and activities tailored to their needs.")
        st.subheader("Emotional Support:")
        st.write("Provide emotional support and reassurance to the person with dementia and their caregivers. Support groups can also be beneficial for caregivers to share experiences and coping strategies.")
        st.subheader("Nutrition and Hydration:")
        st.write("Ensure the person maintains a balanced and nutritious diet and stays well-hydrated. Special attention may be needed to prevent malnutrition or dehydration.")
        st.subheader("Sensory Stimulation:")
        st.write("Engage the person's senses through activities like listening to music, looking at photo albums, or aromatherapy.")
        st.subheader("Medication Management:")
        st.write("Work closely with healthcare professionals to manage medications effectively and address any behavioral or medical challenges.")
        st.subheader("Regular Medical Check-ups:")
        st.write("Schedule regular check-ups to monitor the person's overall health and address any medical concerns.")
    with tab2:
        st.title(':blue[**Medications for Moderate Dementia**]')
        st.write("##")
        col1, col2, col3 = st.columns([1,3,1])
        with col1:
            st.empty()
        with col2:
            st.image(med2)
        with col3:
            st.empty()
        
    with tab3:
        st.title(":blue[**Best Alzheimers Disease Treatment Doctors in Hyderabad**]")
        st.divider()
        doc(sudhir_kumar, "Dr. Sudhir Kumar", "Neurologist, Hyderabad, India", "Consultant, 17 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(srikanth_vemula, "Dr. Srikanth Vemula", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(rajashekar_reddy, "Dr. Rajasekhar Reddy K", "Neurologist, Hyderabad, India", "Consultant, 24 years of experience",  " :calendar: [APOLLO HOSPITALS, JUBILEE HILLS HYDERABAD](https://www.vaidam.com/hospitals/apollo-hospitals-hyderabad)")
        st.divider()
        doc(dr_sandhya, "Dr. Sandhya Manorenj", "Neurologist, Hyderabad, India", "Consultant, 21 years of experience",  " :calendar: [PACE HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/pace-hospital-hyderabad)")
        st.divider()
        doc(subodh_raju, "Dr. Subodh Raju", "Neurologist, Hyderabad, India", "Consultant, 20 years of experience",  " :calendar: [RAINBOW CHILDREN'S HOSPITAL, HYDERABAD](https://www.vaidam.com/hospitals/rainbow-childrens-hospital-hyderabad)")
        st.divider()