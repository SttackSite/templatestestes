import streamlit as st
import json

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Editor Sttack - Template 26", layout="wide")

# --- 2. ESTADO INICIAL (O que o cliente vai editar) ---
if 'db' not in st.session_state:
    st.session_state.db = {
        "cores": {"amarelo": "#ffcc00", "preto": "#111111", "fundo": "#f4f4f4"},
        "aviso": "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO",
        "marca": "DOCKYARD SOCIAL",
        "nav_links": [
            {"label": "O QUE ROLA", "url": "#oque-rola"},
            {"label": "COMIDA", "url": "#comida"},
            {"label": "BEBIDA", "url": "#bebida"},
            {"label": "RESERVAR", "url": "#reservar"}
        ],
        "hero": {
            "titulo": "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.",
            "desc": "O melhor mercado de comida de rua de Glasgow, agora na sua tela."
        },
        "cards": [
            {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
            {"titulo": "BEBIDA", "sub": "CRAFT BEER & COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
            {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"}
        ],
        "sobre": {
            "titulo": "MAIS QUE UM MERCADO.",
            "texto": "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos..."
        },
        "cta": {
            "titulo": "PRONTO PARA VIVER A EXPERIÊNCIA?",
            "sub": "Garanta seu ingresso agora e venha fazer parte da melhor vibe de Glasgow.",
            "botao_txt": "RESERVAR AGORA",
            "botao_url": "https://www.google.com"
        }
    }

# --- 3. SIDEBAR DE EDIÇÃO (CONTROLE TOTAL) ---
with st.sidebar:
    st.title("🛠️ EDITOR TEMPLATE 26")
    
    with st.expander("🎨 Cores e Identidade"):
        st.session_state.db['marca'] = st.text_input("Nome da Marca", st.session_state.db['marca'])
        st.session_state.db['cores']['amarelo'] = st.color_picker("Amarelo Principal", st.session_state.db['cores']['amarelo'])
        st.session_state.db['cores']['preto'] = st.color_picker("Preto Principal", st.session_state.db['cores']['preto'])
        st.session_state.db['aviso'] = st.text_input("Aviso Superior", st.session_state.db['aviso'])

    with st.expander("🚀 Hero (Topo)"):
        st.session_state.db['hero']['titulo'] = st.text_area("Título (HTML aceito)", st.session_state.db['hero']['titulo'])
        st.session_state.db['hero']['desc'] = st.text_area("Descrição", st.session_state.db['hero']['desc'])

    with st.expander("🍔 Gerenciar Cards"):
        # Aqui ele pode adicionar e excluir elementos
        st.session_state.db['cards'] = st.data_editor(st.session_state.db['cards'], num_rows="dynamic")

    with st.expander("🎯 Call to Action (Botão)"):
        st.session_state.db['cta']['titulo'] = st.text_input("Título CTA", st.session_state.db['cta']['titulo'])
        st.session_state.db['cta']['botao_txt'] = st.text_input("Texto do Botão", st.session_state.db['cta']['botao_txt'])
        st.session_state.db['cta']['botao_url'] = st.text_input("Link do Botão", st.session_state.db['cta']['botao_url'])

    st.divider()
    json_data = json.dumps(st.session_state.db, indent=4)
    st.download_button("📥 GERAR JSON PARA GITHUB", json_data, "config_t26.json")

# --- 4. RENDERIZAÇÃO 100% FIEL (INJEÇÃO DE CSS) ---
db = st.session_state.db
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Oswald:wght@700&display=swap');
        :root {{
            --dock-yellow: {db['cores']['amarelo']};
            --dock-black: {db['cores']['preto']};
            --dock-white: {db['cores']['fundo']};
        }}
        .stApp {{ background-color: var(--dock-white); }}
        [data-testid="stHeader"] {{ display: none; }}
        
        h1, h2, h3 {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; font-weight: 700; line-height: 0.9; }}
        .announcement {{ background: var(--dock-black); color: white; padding: 10px; text-align: center; font-weight: bold; letter-spacing: 2px; }}
        
        .nav-dock {{
            background-color: var(--dock-black); color: var(--dock-yellow);
            padding: 15px 5%; display: flex; justify-content: space-between; align-items: center;
            position: sticky; top: 0; z-index: 1000;
        }}
        .nav-link {{ color: var(--dock-yellow) !important; text-decoration: none; font-weight: bold; font-family: 'Oswald'; font-size: 14px; margin-left: 25px; }}

        .hero-dock {{ background-color: var(--dock-yellow); padding: 80px 5%; border-bottom: 8px solid var(--dock-black); }}
        .hero-h1 {{ font-size: clamp(60px, 12vw, 150px); color: var(--dock-black); }}

        .dock-card {{ background: var(--dock-black); color: white; border: 4px solid var(--dock-black); transition: 0.3s; height: 100%; }}
        .dock-card:hover {{ transform: rotate(-1deg); border-color: var(--dock-yellow); }}
        
        .action-button {{
            display: inline-block; background: var(--dock-black); color: var(--dock-yellow);
            padding: 18px 45px; font-family: 'Oswald'; font-size: 18px; text-decoration: none;
            font-weight: bold; transition: 0.3s;
        }}
        .action-button:hover {{ background: #333; color: white; }}
    </style>
""", unsafe_allow_html=True)

# --- 5. ESTRUTURA VISUAL ---
st.markdown(f'<div class="announcement">{db["aviso"]}</div>', unsafe_allow_html=True)

# Nav
links_html = "".join([f'<a class="nav-link" href="{l["url"]}">{l["label"]}</a>' for l in db['nav_links']])
st.markdown(f'<div class="nav-dock"><div style="font-size: 32px; font-family: Oswald;">{db["marca"]}</div><div>{links_html}</div></div>', unsafe_allow_html=True)

# Hero
st.markdown(f'<div class="hero-dock"><h1 class="hero-h1">{db["hero"]["titulo"]}</h1><p style="font-size: 20px; font-weight: 900; margin-top: 20px;">{db["hero"]["desc"]}</p></div>', unsafe_allow_html=True)

# Cards Dinâmicos
st.write("")
cols = st.columns(len(db['cards']))
for i, col in enumerate(cols):
    card = db['cards'][i]
    with col:
        st.markdown(f"""
            <div class="dock-card">
                <img src="{card['img']}" style="width:100%; height:300px; object-fit:cover;">
                <div style="padding: 25px;">
                    <h2 style="font-size: 40px; margin:0;">{card['titulo']}</h2>
                    <p style="color: var(--dock-yellow); font-weight: bold;">{card['sub']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# CTA
st.markdown(f"""
    <div style="background-color: var(--dock-yellow); color: #111; padding: 100px 5%; text-align: center; border-top: 8px solid var(--dock-black);">
        <h2 style="font-size: 60px; margin-bottom: 20px;">{db['cta']['titulo']}</h2>
        <p style="font-size: 20px; margin-bottom: 40px;">{db['cta']['sub']}</p>
        <a href="{db['cta']['botao_url']}" target="_blank" class="action-button">{db['cta']['botao_txt']}</a>
    </div>
""", unsafe_allow_html=True)
