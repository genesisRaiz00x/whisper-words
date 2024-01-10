import streamlit as st
from googletrans import Translator as gt
import pyttsx3 as sp
# make sure to apt install espeak
# from gtts import gTTS 





'''title declared '''
st.header('W h i s p e r     W o r d s')



'''side bar created here'''
with st.sidebar:
    st.info(
        'this application is created for the basic purpose of eleminating the conversational barriers'
    )


myText=st.text_area(label='')


#declaring the list for the languages
myLanguages=('Japanese','french','Russian','Korean','Indonesian','German','Hindi')
lang=st.selectbox('select',myLanguages)



'''
translation functionality implementation
'''

def translate(myText):

    translated_text=myText
    translator = gt()

    if lang=='Japanese':
            translated_text = translator.translate(myText, src='en', dest='ja')
            return translated_text.text
        

      
    if lang=='french':
            translated_text = translator.translate(myText, src='en', dest='fr')
            return translated_text.text

   
    if lang=='German':
            translated_text = translator.translate(myText, src='en', dest='de')
            return translated_text.text
        
 
        
    if lang=='Indonesian':
            translated_text = translator.translate(myText, src='en', dest='ja')
            return translated_text.text
        

        
    if lang=='Korean':
            translated_text = translator.translate(myText, src='en', dest='ko')
            return translated_text.text
        
        
    if lang=='Russian':
            translated_text = translator.translate(myText, src='en', dest='id')
            return translated_text.text
    
    if lang=='Hindi':
            translated_text = translator.translate(myText, src='en', dest='hi')
            return translated_text.text
          
        
    else:

            return 'please select a language'
    



'''
implementing the text to speech functionality
'''

def speak(myText):
      
      st.write(myText)

     
translateBtn=st.button('Translate')

if translateBtn:

    if myText=="":

        
        st.text(translate('Do not leave the text box empty')) 


    if myText!="":
       
        
        st.text(translate(myText))

'''
to implement speech functionality its better to first declare the language codes in advance instead of
declaring it in if statement in the function declaration'''
speakBtn=st.button('Speak')
if speakBtn:
      
      speak('this is speak functionality still needs better implementation.....')




