import streamlit as st
import googletrans as  gt




st.header('w h i s p e r     w o r d s')



# 
with st.sidebar:
    st.info(
        'this application is created for the basic purpose of eleminating the conversational barriers'
        )
    




# creating the input box for writing
myText=st.text_area('')


#declaring the list for the languages
myLanguages=['select language','Marathi','Japanese','Korean','German','Russian']
st.selectbox('',myLanguages)


#the outut set to the input string for now on 
# must change it to the translated one 
resultText=myText







translateBtn=st.button('Translate')

def translate(myText):
    
    # implement google translate library

    if myLanguages=='Marathi':
        pass
    if myLanguages=='Japanese':
        pass
    if myLanguages=='Korean':
        pass
    if myLanguages=='German':
        pass
    if myLanguages=='Russian':
        pass




if translateBtn:
    if myText=="":
        pass
    

    # st.info(resultText)
    if myText!="":
        st.text(resultText)



# implementing the talk function
talkBtn=st.button('Talk')

if talkBtn:
    # implement the talk function using python sound
    # st.markdown('this function will help to communicate...')
    st.text('lets talk a bit...')





