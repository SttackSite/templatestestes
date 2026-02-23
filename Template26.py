import streamlit as st
import json

def render():
    # --- CSS DE INSTRUÇÕES ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&family=Oswald:wght@700&display=swap');
        .instruction-box {
            background-color: #e3f2fd;
            padding: 20px;
            border-left: 6px solid #1976d2;
            border-radius: 8px;
            margin-bottom: 25px;
            font-family: 'Inter', sans-serif;
            color: #0d47a1;
        }
        [data-testid="stHeader"] { display: none; }
    </style>
    <div class="instruction-box">
        <h3 style="margin-top:0;">🚀 Editor Full: Template 26</h3>
        Tudo o que você alterar no menu ao lado será refletido no site em tempo real.
    </div>
    """, unsafe_allow_html=True)

    # --- CONFIGURADOR NA BARRA LATERAL ---
    st.sidebar.title("🎨 CONTROLE TOTAL")
    config = {}

    # 1. URL E IDENTIDADE
    with st.sidebar.expander("🌐 1. Link e Identidade", expanded=True):
        url_nome = st.sidebar.text_input("Subdomínio desejado:", "meu-negocio")
        config['url_planejada'] = f"https://{url_nome}.streamlit.app"
        config['nome_marca'] = st.text_input("Nome da Marca (Menu)", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Aviso Faixa Superior", "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO")

    # 2. MENU DE NAVEGAÇÃO (BOTÕES SUPERIOR DIREITO)
    with st.sidebar.expander("🔗 2. Menu de Navegação", expanded=False):
        config['nav_1'] = st.text_input("Botão 1", "O QUE ROLA")
        config['nav_2'] = st.text_input("Botão 2", "COMIDA")
        config['nav_3'] = st.text_input("Botão 3", "BEBIDA")
        config['nav_4'] = st.text_input("Botão 4 (Destaque)", "RESERVAR")

    # 3. CORES
    with st.sidebar.expander("🎨 3. Cores do Sistema", expanded=False):
        config['cor_amarelo'] = st.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
        config['cor_preto'] = st.color_picker("Cor Principal (Preto)", "#111111")
        config['cor_fundo'] = st.color_picker("Cor de Fundo", "#f4f4f4")

    # 4. HERO SECTION (TOPO)
    with st.sidebar.expander("🚀 4. Seção de Impacto (Hero)", expanded=False):
        config['hero_titulo'] = st.text_area("Título (use <br> para quebrar linha)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
        config['hero_desc'] = st.text_area("Descrição abaixo do título", "O melhor mercado de comida de rua de Glasgow, agora na sua tela.")

    # 5. GRID DE CONTEÚDO (CARDS)
    st.sidebar.markdown("### 🍔 5. Gerenciar Cards")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "CRAFT BEER & COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"}
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic", key="editor_26")

    # 6. SEÇÃO SOBRE
    with st.sidebar.expander("📖 6. Seção Sobre", expanded=False):
        config['sobre_h2'] = st.text_input("Título Sobre", "MAIS QUE UM MERCADO.")
        config['sobre_txt'] = st.text_area("Texto Sobre", "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos...")

    # 7. CHAMADA PARA AÇÃO (CTA)
    with st.sidebar.expander("🎯 7. Call to Action", expanded=False):
        config['cta_h2'] = st.text_input("Título Chamada", "PRONTO PARA VIVER A EXPERIÊNCIA?")
        config['cta_p'] = st.text_input("Subtítulo Chamada", "Garanta seu ingresso agora e venha fazer parte da melhor vibe.")
        config['cta_btn_txt'] = st.text_input("Texto do Botão", "RESERVAR AGORA")
        config['cta_btn_link'] = st.text_input("Link do Botão", "https://www.google.com/")

    # 8. FOOTER E CONTATOS
    with st.sidebar.expander("📍 8. Rodapé e Contatos", expanded=False):
        config['foot_end'] = st.text_input("Endereço", "952 South St, Glasgow G14 0BX")
        config['foot_email'] = st.text_input("E-mail", "hello@dockyardsocial.com")
        config['foot_insta'] = st.text_input("Link Instagram", "https://instagram.com")
        config['foot_fb'] = st.text_input("Link Facebook", "https://facebook.com")
        config['foot_tt'] = st.text_input("Link TikTok", "https://tiktok.com")
        config['foot_copy'] = st.text_input("Copyright", "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO.")

    # OBSERVACÕES E DOWNLOAD
    st.sidebar.markdown("---")
    config['observacoes'] = st.sidebar.text_area("📝 Alguma observação extra?")
    st.sidebar.error("⚠️ Envie o arquivo para **sttacksite@gmail.com**")
    
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR ARQUIVO DE CONFIGURAÇÃO", json_export, "config_template26.json", "application/json")

    # --- RENDERIZAÇÃO DO SITE (ESTILOS) ---
    st.markdown(f"""
    <style>
        :root {{
            --dock-yellow: {config['cor_amarelo']};
            --dock-black: {config['cor_preto']};
            --dock-white: {config['cor_fundo']};
        }}
        .stApp {{ background-color: var(--dock-white); }}
        .main .block-container {{ padding: 0 !important; max-width: 100% !important; }}
        
        h1, h2, h3, .impact {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; font-weight: 700; line-height: 0.9; }}
        
        .announcement {{ background: var(--dock-black); color: white; padding: 10px; text-align: center; font-weight: bold; letter-spacing: 2px; font-size: 14px; }}
        
        .nav-dock {{
            background-color: var(--dock-black); color: var(--dock-yellow);
            padding: 15px 5%; display: flex; justify-content: space-between;
            align-items: center; position: sticky; top: 0; z-index: 1000;
        }}
        .nav-link {{ color: var(--dock-yellow) !important; text-decoration: none; font-weight: bold; font-family: 'Oswald'; font-size: 14px; margin-left: 25px; text-transform: uppercase; }}

        .hero-dock {{ background-color: var(--dock-yellow); padding: 80px 5%; border-bottom: 8px solid var(--dock-black); }}
        .hero-h1 {{ font-size: clamp(60px, 12vw, 150px); color: var(--dock-black); margin: 0; }}

        .dock-card {{ background: var(--dock-black); color: white; border: 4px solid var(--dock-black); transition: 0.3s; height: 100%; }}
        .dock-card:hover {{ transform: rotate(-1deg); border-color: var(--dock-yellow); }}
        
        .action-button {{
            display: inline-block; background: var(--dock-black); color: var(--dock-yellow);
            padding: 18px 45px; font-family: 'Oswald'; font-size: 18px; text-decoration: none;
            transition: 0.3s; font-weight: bold; border: none; cursor: pointer;
        }}
        .action-button:hover {{ background: #333; color: white; }}
    </style>
    """, unsafe_allow_html=True)

    # --- ESTRUTURA VISUAL (O SITE) ---

    # Faixa aviso
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)

    # Navegação
    st.markdown(f"""
    <div class="nav-dock">
        <div style="font-size: 30px; font-family: 'Oswald'; font-weight: 700;">{config['nome_marca']}</div>
        <div>
            <a class="nav-link">{config['nav_1']}</a>
            <a class="nav-link">{config['nav_2']}</a>
            <a class="nav-link">{config['nav_3']}</a>
            <a class="nav-link" style="border: 2px solid; padding: 5px 15px;">{config['nav_4']}</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">{config['hero_titulo']}</h1>
        <p style="font-size: 22px; font-weight: 900; color: #111; margin-top: 25px; max-width: 800px;">{config['hero_desc']}</p>
        <p style="font-family: 'Inter'; font-weight: bold; background: #111; color: #fff; display: inline-block; padding: 5px 10px; margin-top: 15px;">URL: {config['url_planejada']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Grid de Cards
    st.write("")
    cards = config['cards']
    cols = st.columns(len(cards))
    for i, col in enumerate(cols):
        c = cards[i]
        with col:
            st.markdown(f"""
            <div class="dock-card">
                <img src="{c['img']}" style="width:100%; height:320px; object-fit:cover; filter: grayscale(20%);">
                <div style="padding: 25px;">
                    <h2 style="font-size: 40px; margin: 0;">{c['titulo']}</h2>
                    <p style="color: var(--dock-yellow); font-weight: bold; letter-spacing: 1px; margin: 0;">{c['sub']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Seção Sobre
    st.markdown(f"""
    <div style="background-color: var(--dock-black); color: white; padding: 100px 5%; margin-top: 50px;">
        <h2 style="font-size: 65px; color: var(--dock-yellow); margin-bottom: 30px;">{config['sobre_h2']}</h2>
        <p style="font-size: 24px; line-height: 1.4; font-weight: 300; max-width: 900px;">{config['sobre_txt']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Seção CTA
    st.markdown(f"""
    <div style="background-color: var(--dock-yellow); color: #111; padding: 100px 5%; text-align: center; border-top: 8px solid var(--dock-black);">
        <h2 style="font-size: 60px; margin-bottom: 20px;">{config['cta_h2']}</h2>
        <p style="font-size: 20px; margin-bottom: 40px; font-weight: 600;">{config['cta_p']}</p>
        <a href="{config['cta_btn_link']}" target="_blank" class="action-button">{config['cta_btn_txt']}</a>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown(f"""
    <div style="padding: 80px 5%; background: var(--dock-yellow); color: #111; border-top: 2px solid var(--dock-black);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 30px;">
            <div>
                <h2 style="font-size: 45px; margin: 0;">{config['nome_marca']}.</h2>
                <p style="font-weight: 900;">{config['foot_end']}</p>
            </div>
            <div style="text-align: right; font-weight: 900; font-family: 'Oswald';">
                <a href="{config['foot_insta']}" style="color: #111;">INSTAGRAM</a> / 
                <a href="{config['foot_fb']}" style="color: #111;">FACEBOOK</a> / 
                <a href="{config['foot_tt']}" style="color: #111;">TIKTOK</a><br>
                <a href="mailto:{config['foot_email']}" style="color: #111;">{config['foot_email']}</a>
            </div>
        </div>
        <div style="margin-top: 50px; border-top: 2px solid #111; padding-top: 20px; font-size: 13px; font-weight: 900;">
            {config['foot_copy']}
        </div>
    </div>
    """, unsafe_allow_html=True)
