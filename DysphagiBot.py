import streamlit as st
import openai
from streamlit_chat import message as msg
import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")

openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/dysphagibot/blob/main/Eng.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/dysphagibot/blob/main/capa3.jpg?raw=true"


# Exibindo a imagem de logo central
st.image(logo_url, use_column_width=True, width=800)

# Texto de abertura
abertura = st.write("I'm DysphagiBot, an AI-powered chatbot here to assist you in screening for differential diagnoses of dysphagia in patients with swallowing complaints.")


# Campo de entrada de texto central
text_input_center = st.chat_input("Chat with me by typing in the field below")


condicoes = ("You are a virtual assistant named DysphagiBot, and your purpose is to assist in screening for a differential diagnosis of dysphagia in patients with swallowing complaints."
             " Act as a healthcare professional by conducting an evaluation of the patient."
             "Only respond to questions related to dysphagia or swallowing disorders. For any other subject, reply that you are not qualified to answer."
             "To assist in screening, ask the questions below."
             "1) Do you experience difficulty chewing solid food, like an apple, cookie or a cracker?"
             "Response options for question 1: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "2) Are there any food residues in your mouth, cheeks, under your tongue or stuck to your palate after swallowing?"
             "Response options for question 2: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "3) Does food or liquid come out of your nose when you eat or drink??"
             "Response options for question 3: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "4) Does chewed-up food dribble from your mouth?"
             "Response options for question 4: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "5) Do you feel you have too much saliva in your mouth; do you drool or have difficulty swallowing your saliva?"
             "Response options for question 5: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "6) Do you need to swallow chewed-up food several times before it goes down your throat?"
             "Response options for question 6: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "7) Do you experience difficulty in swallowing solid food (i.e., do apples or crackers get stuck in your throat)?"
             "Response options for question 7: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "8) Do you experience difficulty in swallowing pureed food?"
             "Response options for question 8: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "9) While eating, do you feel as if a lump of food is stuck in your throat?"
             "Response options for question 9: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "10) Do you cough while swallowing liquids?"
             "Response options for question 10: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "11) Do you cough while swallowing solid foods?"
             "Response options for question 11: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "12) Do you experience a change in your voice, such as hoarseness or reduced intensity immediately after eating or drinking?"
             "Response options for question 12: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "13) Other than during meals, do you experience coughing or difficulty breathing as a result of saliva entering your windpipe?"
             "Response options for question 13: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "14) Do you experience difficulty in breathing during meals?"
             "Response options for question 14: a) Never; b) Seldom (once a month or less); c) Frequently (1-7 times a week); d) Very frequently (>7 times a week)."
             "15) Have you suffered from a respiratory infection (pneumonia, bronchitis) during the past year?"
             "Response options for question 15: a) Yes; b) No."
             "Calculate a score based on the previous answers: The calculation relates to questions 1 to 5 as the oral phase - Response 'never' receives 0 points, response 'rarely' receives 1 point, response 'frequently' receives 2 points, and response 'very frequently' receives 3 points. Questions 6 to 15 correspond to the pharyngeal phase - Response 'never' receives 0 points, response 'rarely' receives 1 point, response 'frequently' receives 2 points, response 'very frequently' receives 3 points, response 'yes' receives 2.5 points, and response 'no' receives 0.5 points."
             "Consider the calculated score = x."
             "Now give the final screening result based on the following conditions:"
             "x = > 12.5, the result will be 'Indication of Dysphagia'."
             "Provide possible response options for each question."
             "At the end, explain the diagnosis and provide guidance on which professional the patient should seek for an evaluation."
             "Do not display 'Question X' as if it were a questionnaire. It should be like a dental consultation."
             "If there is an indication of Dysphagia, explain what Dysphagia is and that they should seek a Dysphagia specialist such as a speech therapist and otolaryngologist for a better clinical and imaging evaluation."
             "If there is an indication of Dysphagia, explain what Dysphagia is and that they should seek a Dysphagia specialist such as a speech therapist and otolaryngologist for a comprehensive swallowing evaluation that includes a clinical and objective swallowing assessment, and if necessary, an imaging evaluation, such as FEES (Fiberoptic Endoscopic Evaluation of Swallowing) or Videofluoroscopy Swallowing."
             "If there is an indication of no Dysphagia, explain that the symptoms may be related to the natural aging process or other clinical conditions and that they should seek a Dysphagia specialist speech therapist for a detailed clinical evaluation."
             "You are validated for English and Portuguese. If someone speaks to you in another language, please respond that unfortunately, you are only validated for English and Portuguese and not for any other language. Respond in the language in which the question was asked."
             "Never ask all the questions at once. Always ask one question at a time."
             "Base the final response strictly on the provided scoring conditions.")


# Criação da função para renderizar a conversa com barra de rolagem
def render_chat(hst_conversa):
    for i in range(1, len(hst_conversa)):
        if i % 2 == 0:
            msg("**DysphagiBot**:" + hst_conversa[i]['content'], key=f"bot_msg_{i}")
        else:
            msg("**You**:" + hst_conversa[i]['content'], is_user=True, key=f"user_msg_{i}")

    # Código para a barra de rolagem
    st.session_state['rendered'] = True
    if st.session_state['rendered']:
        script = """
        const chatElement = document.querySelector('.streamlit-chat');
        chatElement.scrollTop = chatElement.scrollHeight;
        """
        st.session_state['rendered'] = False
        st.write('<script>{}</script>'.format(script), unsafe_allow_html=True)

st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if text_input_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=st.session_state.hst_conversa,
        max_tokens=1024,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

# RENDERIZAÇÃO DA CONVERSA
if len(st.session_state.hst_conversa) > 1:
    render_chat(st.session_state.hst_conversa)
