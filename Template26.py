import streamlit as st
import json

def render():
    # --- 1. CONFIGURAÇÕES E INSTRUÇÕES DE VENDA NO TOPO ---
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&family=Oswald:wght@700&display=swap');
        
        .instruction-box {{
            background-color: #e3f2fd;
            padding: 20px;
            border-left: 6px solid #1976d2;
            border-radius: 8px;
            margin-bottom: 25px;
            font-family: 'Inter', sans-serif;
            color: #0d47a1;
        }}
        [data-testid="stHeader"] {{ display: none; }}
    </style>
    <div class="instruction-box">
        <h3 style="margin-top:0;">🚀 Instruções de Customização - Template 26</h3>
        Edite as informações na barra lateral. Para customizações que não encontrar nos campos, 
        use a caixa de <strong>'Observações'</strong> ou detalhe no corpo do e-mail ao enviar o arquivo.
    </div>
    """, unsafe_allow_html=True)

    # --- 2. BARRA LATERAL (PAINEL DE CONTROLE COMPLETO) ---
    st.sidebar.title("🎨 EDITOR DINÂMICO")
    config = {}

    # Seção de URL Planejada
    st.sidebar.subheader("🌐 Link do Site")
    url_nome = st.sidebar.text_input("Subdomínio desejado:", placeholder="ex: minha-marca")
    config['url_planejada'] = f"https://{url_nome}.streamlit.app" if url_nome else "https://...streamlit.app"
    st.sidebar.caption(f"Seu link final será: {config['url_planejada']}")

    # Identidade Visual e Cores
    with st.sidebar.expander("📌 1. Cores e Textos Principais", expanded=True):
        config['cor_destaque'] = st.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal (Preto)", "#111111")
        config['cor_fundo'] = st.color_picker("Cor Fundo (Cinza/Branco)", "#f4f4f4")
        config['nome_site'] = st.text_input("Nome do Site/Marca", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Aviso da Faixa", "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO")

    # Hero Section
    with st.sidebar.expander("🚀 2. Seção de Topo (Hero)", expanded=False):
        config['hero_titulo'] = st.text_area("Título Impactante (HTML <br> aceito)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
        config['hero_subtitulo'] = st.text_input("Subtítulo", "O melhor mercado de comida de rua de Glasgow, agora na sua tela.")

    # Cards de Conteúdo
    st.sidebar.markdown("### 🍔 3. Gerenciar Cards")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "CRAFT BEER & COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"},
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic", key="editor_cards_26")

    # Seção Sobre
    with st.sidebar.expander("📖 4. Seção Sobre", expanded=False):
        config['sobre_titulo'] = st.text_input("Título 'Sobre'", "MAIS QUE UM MERCADO.")
        config['sobre_texto'] = st.text_area("Texto Descritivo", "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos...")

    # Botão de Ação (CTA)
    with st.sidebar.expander("🔗 5. Chamada para Ação", expanded=False):
        config['cta_titulo'] = st.text_input("Título CTA", "PRONTO PARA VIVER A EXPERIÊNCIA?")
        config['cta_sub'] = st.text_input("Subtítulo CTA", "Garanta seu ingresso agora e venha fazer parte da melhor vibe.")
        config['cta_botao_texto'] = st.text_input("Texto do Botão", "RESERVAR AGORA")
        config['cta_botao_link'] = st.text_input("Link do Botão", "https://www.google.com/")

    # Rodapé
    with st.sidebar.expander("📍 6. Rodapé e Social", expanded=False):
        config['footer_endereco'] = st.text_input("Endereço", "952 South St, Glasgow G14 0BX")
        config['footer_email'] = st.text_input("E-mail de Contato", "hello@dockyardsocial.com")
        config['link_insta'] = st.text_input("Link Instagram", "https://instagram.com")
        config['footer_copy'] = st.text_input("Copyright", "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO.")

    # Observações Finais
    st.sidebar.markdown("### 📝 7. Observações")
    config['observacoes'] = st.sidebar.text_area("Explique aqui outras mudanças desejadas:")

    # Exportação
    st.sidebar.markdown("---")
    st.sidebar.error("⚠️ **FINALIZAÇÃO:** Baixe o arquivo e envie para **sttacksite@gmail.com**")
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR CONFIGURAÇÃO", json_export, "template26_config.json", "application/json")

    # --- 3. RENDERIZAÇÃO DO DESIGN ORIGINAL (ESTILOS VISUAIS) ---
    st.markdown(f"""
    <style>
        :root {{
            --dock-yellow: {config['cor_destaque']};
            --dock-black: {config['cor_principal']};
            --dock-white: {config['cor_fundo']};
        }}

        .stApp {{ background-color: var(--dock-white); }}
        .main .block-container {{ padding: 0 !important; max-width: 100% !important; }}

        h1, h2, h3 {{
            font-family: 'Oswald', sans-serif;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: -1px;
            line-height: 0.9;
        }}

        .announcement {{
            background: var(--dock-black); color: white; padding: 10px;
            font-weight: bold; text-align: center; letter-spacing: 2px;
            font-family: 'Inter', sans-serif; font-size: 14px;
        }}

        .nav-dock {{
            background-color: var(--dock-black); color: var(--dock-yellow);
            padding: 15px 5%; display: flex; justify-content: space-between;
            align-items: center; position: sticky; top: 0; z-index: 1000;
        }}

        .hero-dock {{
            background-color: var(--dock-yellow); padding: 80px 5%;
            border-bottom: 8px solid var(--dock-black); text-align: left;
        }}

        .hero-h1 {{ font-size: clamp(60px, 10vw, 150px); color: var(--dock-black); }}

        .dock-card {{
            background: var(--dock-black); color: white; transition: 0.3s;
            border: 4px solid var(--dock-black); height: 100%;
        }}
        
        .dock-card:hover {{ transform: rotate(-1deg); border-color: var(--dock-yellow); }}

        .card-content {{ padding: 25px; }}

        .action-button {{
            display: inline-block !important; background: var(--dock-black) !important;
            color: var(--dock-yellow) !important; padding: 15px 40px !important;
            font-family: 'Oswald', sans-serif !important; font-size: 16px !important;
            text-transform: uppercase !important; text-decoration: none !important;
            transition: 0.3s !important; cursor: pointer !important; font-weight: bold;
        }}
        .action-button:hover {{ background-color: #333 !important; color: white !important; }}
    </style>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 1: AVISO E NAVEGAÇÃO ==========
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="nav-dock">
        <div style="font-size: 32px; font-family: 'Oswald'; font-weight: 700;">{config['nome_site']}</div>
        <div style="display: flex; gap: 30px; font-family: 'Oswald'; font-size: 14px;">
            <span style="cursor:pointer;">O QUE ROLA</span>
            <span style="cursor:pointer;">COMIDA</span>
            <span style="cursor:pointer;">BEBIDA</span>
            <span style="cursor:pointer; border: 1px solid; padding: 0 10px;">MODO EDITOR</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 2: HERO ==========
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">{config['hero_titulo']}</h1>
        <p style="font-size: 22px; font-weight: 900; color: #111; margin-top: 20px; max-width: 700px;">{config['hero_subtitulo']}</p>
        <p style="font-family: 'Inter'; font-size: 14px; font-weight: bold; color: var(--dock-black); margin-top: 10px;">URL SOLICITADA: {config['url_planejada']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 3: GRID DE CARDS ==========
    st.write("")
    cards = config['cards']
    cols = st.columns(len(cards))
    for i, col in enumerate(cols):
        c = cards[i]
        with col:
            st.markdown(f"""
            <div class="dock-card">
                <img src="{c['img']}" style="width:100%; height:300px; object-fit:cover; filter: grayscale(20%);">
                <div class="card-content">
                    <h2 style="font-size: 40px; margin-bottom: 5px;">{c['titulo']}</h2>
                    <p style="color: var(--dock-yellow); font-weight: bold; letter-spacing: 1px;">{c['sub']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ========== SEÇÃO 4: SEÇÃO "SOBRE" ==========
    st.markdown(f"""
    <div style="background-color: var(--dock-black); color: white; padding: 100px 5%; margin-top: 50px;">
        <div style="max-width: 800px;">
            <h2 style="font-size: 60px; color: var(--dock-yellow); margin-bottom: 30px;">{config['sobre_titulo']}</h2>
            <p style="font-size: 24px; line-height: 1.4; font-weight: 300;">{config['sobre_texto']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 5: CHAMADA PARA AÇÃO (CTA) ==========
    st.markdown(f"""
    <div style="background-color: var(--dock-yellow); color: #111; padding: 100px 5%; text-align: center; border-top: 8px solid var(--dock-black);">
        <h2 style="font-size: 60px; margin-bottom: 20px;">{config['cta_titulo']}</h2>
        <p style="font-size: 20px; margin-bottom: 40px;">{config['cta_sub']}</p>
        <a href="{config['cta_botao_link']}" target="_blank" class="action-button">{config['cta_botao_texto']}</a>
    </div>
    """, unsafe_allow_html=True)

    # ========== SEÇÃO 6: FOOTER ==========
    st.markdown(f"""
    <div style="padding: 60px 5%; background: var(--dock-yellow); color: #111; border-top: 2px solid var(--dock-black);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px;">
            <div>
                <h2 style="font-size: 45px; margin: 0;">{config['nome_site']}.</h2>
                <p style="font-weight: bold;">{config['footer_endereco']}</p>
            </div>
            <div style="text-align: right; font-weight: bold;">
                <a href="{config['link_insta']}" target="_blank" style="color: #111; text-decoration: none;">INSTAGRAM</a><br>
                <a href="mailto:{config['footer_email']}" style="color: #111; text-decoration: none;">{config['footer_email']}</a>
            </div>
        </div>
        <div style="margin-top: 40px; border-top: 2px solid #111; padding-top: 20px; font-size: 12px; font-weight: 900;">
            {config['footer_copy']}
        </div>
    </div>
    """, unsafe_allow_html=True)
