import streamlit as st
import json

# Configuração da Página
st.set_page_config(layout="wide", page_title="Dockyard Configurator Pro", page_icon="🛠️")

def render_configurator():
    # --- BARRA LATERAL: CONFIGURAÇÕES ---
    st.sidebar.title("🛠️ EDITOR DINÂMICO")
    
    config = {}

    # 1. Identidade e Cores
    with st.sidebar.expander("🎨 Cores e Identidade", expanded=True):
        config['cor_destaque'] = st.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal (Preto)", "#111111")
        config['cor_fundo'] = st.color_picker("Cor Fundo (Branco)", "#f4f4f4")
        config['nome_site'] = st.text_input("Nome da Marca", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Aviso do Topo", "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO")

    # 2. Hero Section
    with st.sidebar.expander("🚀 Seção Principal (Hero)", expanded=False):
        config['hero_titulo'] = st.text_area("Título (use <br> para quebrar linha)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
        config['hero_subtitulo'] = st.text_input("Subtítulo", "O melhor mercado de comida de rua de Glasgow, agora na sua tela.")

    # 3. Cards Dinâmicos
    st.sidebar.markdown("### 🍔 Gerenciar Cards")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "CRAFT BEER", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"},
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic", key="editor_cards")

    # 4. Botões de Chamada
    st.sidebar.markdown("### 🔗 Botões de Ação")
    default_buttons = [
        {"texto": "RESERVAR AGORA", "link": "https://google.com"}
    ]
    config['botoes'] = st.sidebar.data_editor(default_buttons, num_rows="dynamic", key="editor_btns")

    # Botão de Download do JSON
    st.sidebar.markdown("---")
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR CONFIGURAÇÃO", json_export, "meu_site.json", "application/json")

    # =========================================================
    # VISUALIZAÇÃO (PREVIEW) - RESTAURANDO O DESIGN ORIGINAL
    # =========================================================
    
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');

        :root {{
            --dock-yellow: {config['cor_destaque']};
            --dock-black: {config['cor_principal']};
            --dock-white: {config['cor_fundo']};
        }}

        .stApp {{ background-color: var(--dock-white); }}

        /* Estilos Originais */
        .announcement {{
            background: var(--dock-black);
            color: white;
            padding: 10px;
            font-weight: bold;
            text-align: center;
            letter-spacing: 2px;
            font-family: 'Inter', sans-serif;
            margin-top: -70px; /* Compensa o padding do streamlit */
        }}

        .nav-dock {{
            background-color: var(--dock-black);
            color: var(--dock-yellow);
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .hero-dock {{
            background-color: var(--dock-yellow);
            padding: 80px 5%;
            border-bottom: 8px solid var(--dock-black);
        }}

        .hero-h1 {{
            font-family: 'Oswald', sans-serif;
            font-size: clamp(50px, 8vw, 100px);
            color: var(--dock-black);
            line-height: 0.9;
            text-transform: uppercase;
        }}

        .dock-card {{
            background: var(--dock-black);
            color: white;
            border: 4px solid var(--dock-black);
            transition: 0.3s;
            margin-bottom: 20px;
        }}

        .card-content {{ padding: 20px; }}
        
        h2 {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; margin: 0; }}

        .action-button {{
            display: inline-block;
            background: var(--dock-black);
            color: var(--dock-yellow);
            padding: 15px 40px;
            font-family: 'Oswald', sans-serif;
            text-decoration: none;
            text-transform: uppercase;
            font-weight: bold;
            margin: 10px;
        }}

        [data-testid="stHeader"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

    # Renderização do Topo
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="nav-dock">
        <div style="font-size: 32px; font-family: 'Oswald'; font-weight: 700;">{config['nome_site']}</div>
        <div style="font-size: 12px; opacity: 0.8;">MODO EDIÇÃO ATIVO</div>
    </div>
    """, unsafe_allow_html=True)

    # Renderização Hero
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">{config['hero_titulo']}</h1>
        <p style="font-size: 20px; font-weight: 900; color: #111; margin-top: 20px;">{config['hero_subtitulo']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Grid de Cards Dinâmico
    st.write("")
    cols_per_row = 3
    cards = config['cards']
    
    for i in range(0, len(cards), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(cards):
                c = cards[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="dock-card">
                        <img src="{c['img']}" style="width:100%; height:250px; object-fit:cover;">
                        <div class="card-content">
                            <h2 style="font-size: 35px;">{c['titulo']}</h2>
                            <p style="color: var(--dock-yellow); font-weight: bold;">{c['sub']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # Seção de Botões Dinâmica
    st.markdown(f"<div style='text-align: center; padding: 80px 5%; background: {config['cor_destaque']}'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 50px; color: #111; margin-bottom: 30px;'>PRONTO?</h2>", unsafe_allow_html=True)
    
    for btn in config['botoes']:
        st.markdown(f'<a href="{btn["link"]}" target="_blank" class="action-button">{btn["texto"]}</a>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_configurator()
