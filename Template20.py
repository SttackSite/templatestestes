import streamlit as st
import json

# Configuração inicial da página (Isso aqui o cliente não muda na hora, só você)
st.set_page_config(layout="wide", page_title="Dockyard Configurator", page_icon="⚙️")

def render_configurator():
    st.sidebar.title("🎨 Personalize seu Site")
    st.sidebar.markdown("Altere os campos abaixo e veja o resultado ao lado.")

    #Dict que guardará todas as configs
    config = {}

    # ==============================
    # 1. CORES E ESTILO (Sidebar)
    # ==============================
    st.sidebar.header("1. Cores da Marca")
    config['cor_destaque'] = st.sidebar.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
    config['cor_principal'] = st.sidebar.color_picker("Cor Principal (Preto)", "#111111")
    config['cor_fundo'] = st.sidebar.color_picker("Cor Fundo (Branco/Cinza)", "#f4f4f4")

    # ==============================
    # 2. CONTEÚDO HERO (Sidebar)
    # ==============================
    st.sidebar.header("2. Topo do Site (Hero)")
    config['titulo_aba'] = st.sidebar.text_input("Título da Aba do Navegador", "Dockyard Social | Comida & Vibe")
    config['aviso_topo'] = st.sidebar.text_input("Texto do Aviso (Faixa Preta)", "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO")
    config['nome_site'] = st.sidebar.text_input("Nome/Logo do Site", "DOCKYARD SOCIAL")
    
    config['hero_titulo'] = st.sidebar.text_area("Título Principal (Use <br> para pular linha)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
    config['hero_subtitulo'] = st.sidebar.text_area("Subtítulo", "O melhor mercado de comida de rua de Glasgow, agora na sua tela.")

    # ==============================
    # 3. CARDS (Sidebar)
    # ==============================
    st.sidebar.header("3. Destaques (Cards)")
    
    # Card 1
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Card 1 (Esquerda)**")
    config['c1_titulo'] = st.sidebar.text_input("Card 1 - Título", "COMIDA")
    config['c1_sub'] = st.sidebar.text_input("Card 1 - Subtítulo", "10+ VENDEDORES")
    config['c1_img'] = st.sidebar.text_input("Card 1 - URL Imagem", "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600")
    
    # Card 2
    st.sidebar.markdown("**Card 2 (Centro)**")
    config['c2_titulo'] = st.sidebar.text_input("Card 2 - Título", "BEBIDA")
    config['c2_sub'] = st.sidebar.text_input("Card 2 - Subtítulo", "CRAFT BEER & COCKTAILS")
    config['c2_img'] = st.sidebar.text_input("Card 2 - URL Imagem", "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600")

    # Card 3
    st.sidebar.markdown("**Card 3 (Direita)**")
    config['c3_titulo'] = st.sidebar.text_input("Card 3 - Título", "EVENTOS")
    config['c3_sub'] = st.sidebar.text_input("Card 3 - Subtítulo", "MÚSICA AO VIVO")
    config['c3_img'] = st.sidebar.text_input("Card 3 - URL Imagem", "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600")

    # ==============================
    # 4. BOTÃO DE AÇÃO (Sidebar)
    # ==============================
    st.sidebar.header("4. Chamada para Ação")
    config['cta_titulo'] = st.sidebar.text_input("Título CTA", "PRONTO PARA VIVER A EXPERIÊNCIA?")
    config['cta_texto'] = st.sidebar.text_input("Texto CTA", "Garanta seu ingresso agora e venha fazer parte da melhor vibe.")
    config['cta_btn_texto'] = st.sidebar.text_input("Texto do Botão", "RESERVAR AGORA")
    config['cta_link'] = st.sidebar.text_input("Link do Botão", "https://www.google.com/")

    # ==============================
    # 5. GERAR JSON (Sidebar Final)
    # ==============================
    st.sidebar.markdown("---")
    st.sidebar.success("Tudo pronto?")
    json_string = json.dumps(config, indent=4, ensure_ascii=False)
    
    st.sidebar.download_button(
        label="📥 BAIXAR ARQUIVO DE CONFIGURAÇÃO",
        data=json_string,
        file_name="meu_site_config.json",
        mime="application/json"
    )

    # ==============================================================================
    # AREA DE PREVIEW (O TEMPLATE ORIGINAL APLICANDO AS VARIÁVEIS)
    # ==============================================================================
    
    # Injeção de CSS Dinâmico
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Oswald:wght@700&display=swap');

        :root {{
            --dock-yellow: {config['cor_destaque']}; 
            --dock-black: {config['cor_principal']};
            --dock-white: {config['cor_fundo']};
        }}

        .stApp {{ background-color: var(--dock-white); }}

        h1, h2, h3, .impact-font {{
            font-family: 'Oswald', sans-serif;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: -1px;
            line-height: 0.9;
        }}

        .nav-dock {{
            background-color: var(--dock-black);
            color: var(--dock-yellow);
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
        
        /* ... (O resto do CSS original pode ficar aqui, omiti para não ficar gigante) ... */
        
        .hero-dock {{
            background-color: var(--dock-yellow);
            padding: 80px 5%;
            border-bottom: 8px solid var(--dock-black);
            text-align: left;
        }}

        .hero-h1 {{
            font-size: clamp(60px, 12vw, 150px);
            color: var(--dock-black);
        }}

        .dock-card {{
            background: var(--dock-black);
            color: white;
            padding: 0;
            border-radius: 0px;
            transition: 0.3s;
            height: 100%;
            border: 4px solid var(--dock-black);
        }}
        
        .card-content {{ padding: 25px; }}
        
        .announcement {{
            background: var(--dock-black);
            color: white;
            padding: 10px;
            font-weight: bold;
            text-align: center;
            letter-spacing: 2px;
        }}

        .action-button {{
            display: inline-block !important;
            background: var(--dock-black) !important;
            color: var(--dock-yellow) !important;
            border: none !important;
            padding: 15px 40px !important;
            font-family: 'Oswald', sans-serif !important;
            font-size: 14px !important;
            text-transform: uppercase !important;
            text-decoration: none !important;
            transition: 0.3s !important;
            cursor: pointer !important;
        }}
        
        [data-testid="stHeader"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

    # Renderização HTML usando as variáveis do config
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="nav-dock">
        <div style="font-size: 32px; font-family: 'Oswald'; font-weight: 700;">{config['nome_site']}</div>
        <div style="display: flex; gap: 30px;">
            <span style="font-size:12px;">PREVIEW MODE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hero-dock">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-h1">{config["hero_titulo"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; font-weight: 900; color: #111; margin-top: 20px;">{config["hero_subtitulo"]}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns(3)

    def render_dock_card(col, title, subtitle, img_url):
        with col:
            st.markdown(f"""
            <div class="dock-card">
                <img src="{img_url}" style="width:100%; filter: grayscale(20%); object-fit: cover; height: 300px;">
                <div class="card-content">
                    <h2 style="font-size: 40px; margin-bottom: 5px;">{title}</h2>
                    <p style="color: var(--dock-yellow); font-weight: bold; letter-spacing: 1px;">{subtitle}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    render_dock_card(col1, config['c1_titulo'], config['c1_sub'], config['c1_img'])
    render_dock_card(col2, config['c2_titulo'], config['c2_sub'], config['c2_img'])
    render_dock_card(col3, config['c3_titulo'], config['c3_sub'], config['c3_img'])

    st.markdown(f"""
    <div id="reservar" style="background-color: var(--dock-yellow); color: #111; padding: 100px 5%; text-align: center;">
        <h2 style="font-size: 60px; margin-bottom: 30px;">{config['cta_titulo']}</h2>
        <p style="font-size: 20px; margin-bottom: 40px;">{config['cta_texto']}</p>
        <a href="{config['cta_link']}" target="_blank" class="action-button" style="background: #111; color: var(--dock-yellow);">{config['cta_btn_texto']}</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_configurator()
