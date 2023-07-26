import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import json
from streamlit_lottie import st_lottie


def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

cong = load_lottie('lottie/animation_lkjf2v5r.json')

def homee():
    st.title(
        "NeuroWise: Your AI Guide to Alzheimer's Detection")

    with st.container():
        st.write("---")
        st.header("Introduction")
        
            
    #st.markdown('<div style="text-align: justify;">Alzheimer\'s disease is a complex and progressive neurological disorder that primarily affects the memory and cognitive abilities of individuals. It is the most common form of dementia, a term used to describe a group of conditions characterized by a decline in cognitive function severe enough to interfere with daily life. In this article, we delve into the key aspects of Alzheimer\'s disease, including its causes, risk factors, symptoms, diagnosis, stages, and available treatments.</div>', unsafe_allow_html=True)
        
        st.write("Discover the enigma of Alzheimer's disease, impacting millions worldwide. This progressive neurological disorder disrupts lives, targeting the elderly and straining families. We dive deep into the intricate factors shaping Alzheimer's—genetics, environment, lifestyle—shedding light on its manifestations, risks, and diagnostics. Amidst the elusive cure, explore emerging treatments that improve lives. The brain's mysterious decline, sparked by abnormal proteins, forms our focus. With advancing research and compassionate care, we envision a future where Alzheimer's shadow vanishes, liberating countless lives from its grip. Join the mission, unite researchers, healthcare, and society—forge a path to conquer Alzheimer's together! 🌟")


    image1 = Image.open("images/image1.png")
    image2 = Image.open("images/symp1.jpg")


    with st.container():
        st.write("---")
        st.header("What is Alzheimer's Disease?")
        image, content = st.columns([1.5,2])    


        with image:
            st.video("https://youtu.be/zTd0-A5yDZI")
            #   st.write("##")
        with content:
            
            st.write("Alzheimer's disease is a progressive neurological disorder affecting the brain, leading to a gradual and irreversible decline in cognitive function and memory. It is the most common cause of dementia in older adults, impacting millions globally. The disease is characterized by the accumulation of abnormal protein deposits, amyloid plaques, and neurofibrillary tangles in the brain, disrupting cell communication and triggering inflammation. As Alzheimer's progresses, individuals experience memory loss, difficulties in daily tasks, confusion, mood swings, and dependency on caregivers. While the exact cause remains unknown, advancing age, genetics, and certain risk factors contribute to its development. Although there is no cure, treatments exist to manage symptoms and improve quality of life. Alzheimer's imposes emotional, financial, and societal burdens, underscoring the need for research, support, and awareness efforts to combat this profound healthcare challenge.")


    with st.container():
        st.write("---")
        st.header("Symptoms")

        image, content = st.columns(2)

        with image:
            st.image(image2)
        with content:
            st.write("Alzheimer's disease manifests through a wide range of symptoms that progress gradually over time. These symptoms can significantly impact an individual's cognitive abilities, behavior, and daily functioning. Some key points to consider regarding Alzheimer's symptoms include:")
            st.write(""":blue[**Memory Loss:**] One of the hallmark symptoms of Alzheimer's is memory loss, particularly in the early stages. Individuals may have difficulty remembering recent events, names, and conversations.

:blue[**Cognitive Decline:**] As the disease advances, cognitive decline becomes more pronounced. Individuals may struggle with problem-solving, decision-making, and abstract thinking.

:blue[**Disorientation and Confusion:**] People with Alzheimer's often experience confusion about time, place, and people. They may get lost in familiar settings and have trouble recognizing loved ones.

:blue[**Language Difficulties:**] Expressing oneself and understanding language can become challenging. Finding the right words and following conversations may be difficult.

:blue[**Mood Swings and Behavioral Changes:**] Alzheimer's can lead to mood swings, irritability, anxiety, and agitation. Individuals may withdraw from social interactions and display uncharacteristic behaviors.

""")
        
    with st.container():
        st.write('---')
        st.header("Causes and Risk Factors")
        col1, col2 = st.columns([2,2])

        with col1:
            st.write("##")
            st.write("##")
            st_lottie(cong, speed=1, reverse=False, loop=True, quality="high", height= None , width = None, key=None)
        with col2:
            st.write("Alzheimer's disease is a complex neurological condition influenced by a combination of genetic, environmental, and lifestyle factors. While the exact cause remains elusive, researchers have identified several significant causes and risk factors associated with the development of Alzheimer's. Some key points to consider include:")
            st.write(""":blue[**Genetics:**] Family history plays a crucial role in Alzheimer's risk. Individuals with a first-degree relative (parent or sibling) who had Alzheimer's are at a higher risk of developing the disease themselves. Specific genes, such as the APOE gene variants (particularly APOE ε4), are linked to an increased risk of Alzheimer's.

:blue[**Age:**] Advancing age is the most significant risk factor for Alzheimer's disease. The likelihood of developing the condition increases dramatically after the age of 65, and the risk continues to rise with each decade of life.

:blue[**Abnormal Protein Accumulation:**] The accumulation of abnormal proteins, including beta-amyloid plaques and tau tangles, in the brain is a hallmark feature of Alzheimer's. These protein deposits disrupt brain cell communication and contribute to neurological damage.

:blue[**Family History and Heredity:**] People with a family history of Alzheimer's are at a higher risk, suggesting a genetic predisposition to the disease.

:blue[**Gender:**] Women are generally at a slightly higher risk of developing Alzheimer's compared to men, although the reasons for this difference are not fully understood.

""")

    with st.container():
        st.write('---')
        st.header('Diagnosis')
        st.write("Diagnosing Alzheimer's disease involves a comprehensive evaluation of an individual's medical history, physical and neurological examinations, and cognitive assessments. Medical professionals may also employ imaging techniques, such as magnetic resonance imaging (MRI) and positron emission tomography (PET), to assess brain structure and function. While there is currently no definitive test for Alzheimer's disease, these evaluations can help rule out other potential causes of cognitive decline.")

        st.header('Stages')
        st.write("Alzheimer's disease is typically divided into four stages:")
        st.write(":blue[**Non Demented:**] The term non-demented stage typically refers to the early stage of a neurodegenerative disease, such as Alzheimer's disease or other forms of dementia, where individuals do not exhibit significant cognitive impairment or dementia-related symptoms. During this stage, individuals may not experience noticeable memory loss or cognitive decline that interferes with their daily activities.")
        st.write(":blue[**Early stage (very mild):**] Memory lapses and subtle cognitive difficulties become noticeable. Individuals can still function independently but may experience challenges with organization and concentration.")
        st.write(":blue[**Middle stage (mild):**] Memory loss and cognitive decline worsen, affecting language, reasoning, and problem-solving. Assistance with daily activities becomes necessary.")
        st.write(":blue[**Late stage (moderate):**] Individuals lose the ability to communicate coherently, recognize loved ones, and carry out basic self-care tasks. They require round-the-clock assistance and care.")

        st.header("Treatment and Management")
        st.write("While there is no known cure for Alzheimer's disease, various approaches can help manage the symptoms and improve the quality of life for affected individuals:")
        st.write(":blue[**Medications:**] Cholinesterase inhibitors (such as donepezil, rivastigmine, and galantamine) and memantine are commonly prescribed to temporarily alleviate cognitive symptoms.")
        st.write(":blue[**Non-pharmacological interventions:**] Cognitive stimulation, physical exercise, social engagement, and a healthy diet may provide supportive benefits and help slow disease progression.")
        st.write(":blue[**Supportive care:**] Creating a safe and structured environment, implementing routines, and providing emotional support to individuals and their caregivers are crucial aspects of managing Alzheimer's disease.")

        st.write(":red[More detailed treatment and diagnosis information will be provided in the classification section, after getting the classified output.]")