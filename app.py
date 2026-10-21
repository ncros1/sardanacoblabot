import streamlit as st
from google import genai

# 1. Configurar l'aspecte visual de la pàgina web per als teus alumnes
st.set_page_config(page_title="App de l'Aula con IA", page_icon="🎓", layout="centered")

st.title("🎓 El teu Assistent de l'Aula amb IA")
st.write("Escriu la teva consulta aquí sota per interactuar amb el model que el teu professor ha preparat.")

# 2. Connectar de forma segura amb la API Key amagada als 'Secrets' de Streamlit
# (Això evita que els alumnes o qualsevol persona pugui veure la teva clau privada)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("🚨 Error de configuració: No s'ha trobat la clau 'GEMINI_API_KEY' als Secrets de Streamlit.")
    st.stop()

# 3. Crear la caixa de text on l'alumne escriu la seva pregunta
user_input = st.text_area(
    label="Què vols preguntar avui?", 
    placeholder="Escriu aquí el teu text o la teva pregunta...",
    height=150
)

# 4. Botó per activar la Intel·ligència Artificial i mostrar la resposta
if st.button("Preguntar a la IA", type="primary"):
    if user_input.strip():
        with st.spinner("🧠 La IA està pensant la resposta..."):
            try:
                # Enviem el text de l'alumne al model recomanat més ràpid i eficient
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                )
                
                # Mostrem el resultat final a la pantalla de l'alumne
                st.success("✨ Resposta del model:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"S'ha produït un error al connectar amb Gemini: {e}")
    else:
        st.warning("⚠️ Si us plau, escriu una pregunta abans de prémer el botó.")
