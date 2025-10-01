import streamlit as st

st.set_page_config(layout="wide")
st.title('A TRANSPARÊNCIA DOS ALGORÍTIMOS')

rede = st.selectbox('Escolha a rede social:', ['InstaX', 'TokVid'])

post = [
    {"autor": "Amigo 1", "conteudo": "Feliz aniversário!", "tipo": "amigo"},
    {"autor": "Marca X", "conteudo": "Compre agora com 50% OFF!", "tipo": "anuncio"},
    {"autor": "Amigo 2", "conteudo": "Estudando para prova...", "tipo": "amigo"},
    {"autor": "Página Polêmica", "conteudo": "Veja essa notícia chocante!", "tipo": "polemico"},
    {"autor": "Amigo 3", "conteudo": "Foto da viagem 🚀", "tipo": "amigo"}
    ]

feed_algoritimo = sorted(post, key=lambda x: {'anuncio':0, 'polemico':1, 'amigo':2}[x['tipo']])
feed_cronologico = post

col1, col2 = st.columns(2)

with col2:
    st.subheader('Feed Cronológico')
    for p in feed_cronologico:
        st.write(f"**{p['autor']}**: {p['conteudo']}")

st.markdown('---')
st.subheader('Resumo de Transparência')
st.write("""No feed algorítmico, anúncios e conteúdos polêmicos aparecem no topo, 
enquanto no cronológico os posts seguem a ordem real""")