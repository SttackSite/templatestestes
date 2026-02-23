import streamlit as st
import json

def render():
    # --- 1. AVISO DE INSTRUÇÕES NO TOPO ---
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
        <h3 style="margin-top:0;">🚀 Instruções de Customização</h3>
        Estas são as alterações básicas para colocar seu site no ar rápido. 
        Qualquer customização mais complexa pode ser detalhada no campo de 'Observações' ou no e-mail.
    </div>
    """, unsafe_allow_html=True)

    # --- 2. BARRA LATERAL (CONFIGURADOR) ---
    st.sidebar.title("🎨 CONFIGURADOR MASTER")
    config = {}

    # Campo de URL Personalizada
    st.sidebar.subheader("🌐 Link do Site")
    url_nome = st.sidebar.text_input("Nome da URL desejada:", placeholder="ex: meu-negocio")
    config['url_planejada'] = f"https://{url_nome}.streamlit.app" if url_nome else "https://...streamlit.app"
    st.sidebar.caption(f"Prévia: {config['url_planejada']}")

    # Identidade e Cores
    with st.sidebar.expander("📌 1. Identidade e Cores", expanded=True):
        config['cor_destaque'] = st.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal (Preto)", "#111111")
        config['cor_fundo'] = st.color_picker("Cor Fundo", "#f4f4f4")
        config['nome_site'] = st.text_input("Nome da Marca", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Aviso do Topo", "ABERTO NESTE FINAL DE SEMANA")

    # Conteúdo Hero
    with st.sidebar.expander("🚀 2. Topo (Hero)", expanded=False):
        config['hero_titulo'] = st.text_area("Título (use <br> para pular linha)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
        config['hero_subtitulo'] = st.text_input("Subtítulo", "O melhor mercado de comida de rua de Glasgow.")

    # Cards
    st.sidebar.markdown("### 🍔 3. Gerenciar Conteúdo")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"}
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic", key="editor_cards")

    # Seção Sobre
    with st.sidebar.expander("📖 4. Seção 'Sobre'", expanded=False):
        config['sobre_titulo'] = st.text_input("Título Sobre", "MAIS QUE UM MERCADO.")
        config['sobre_texto'] = st.text_area("Texto Sobre", "Espaço seguro e inclusivo para todos.")

    # Rodapé e Redes
    with st.sidebar.expander("📍 5. Rodapé e Contatos", expanded=False):
        config['footer_email'] = st.text_input("E-mail", "hello@dockyardsocial.com")
        config['link_insta'] = st.text_input("Link Instagram", "https://instagram.com")
        config['footer_copy'] = st.text_input("Copyright", "© 2026 DOCKYARD SOCIAL.")

    # Observações e Finalização
    st.sidebar.markdown("### 📝 6. Pedidos Especiais")
    config['observacoes'] = st.sidebar.text_area("Descreva outras mudanças aqui:")

    st.sidebar.markdown("---")
    st.sidebar.error("⚠️ **COMO FINALIZAR:**\n\nBaixe o arquivo JSON e envie para **sttacksite@gmail.com**")
    
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR CONFIGURAÇÃO", json_export, "meu_site_sttack.json", "application/json")

    # --- 3. RENDERIZAÇÃO VISUAL (O SITE) ---
    st.markdown(f"""
    <style>
        :root {{ --dock-yellow: {config['cor_destaque']}; --dock-black: {config['cor_principal']}; --dock-white: {config['cor_fundo']}; }}
        .stApp {{ background-color: var(--dock-white); }}
        .main .block-container {{ padding: 0 !important; max-width: 100% !important; }}
        .announcement {{ background: var(--dock-black); color: white; padding: 12px; text-align: center; font-weight: bold; font-family: 'Inter'; font-size: 14px; letter-spacing: 2px; }}
        .nav-dock {{ background: var(--dock-black); color: var(--dock-yellow); padding: 20px 5%; display: flex; justify-content: space-between; font-family: 'Oswald'; }}
        .hero-dock {{ background: var(--dock-yellow); padding: 80px 5%; border-bottom: 8px solid var(--dock-black); }}
        .hero-h1 {{ font-family: 'Oswald'; font-size: clamp(50px, 10vw, 130px); color: var(--dock-black); line-height: 0.9; text-transform: uppercase; margin: 0; }}
        .dock-card {{ background: var(--dock-black); color: white; border: 4px solid var(--dock-black); margin-bottom: 25px; }}
        .card-content {{ padding: 25px; }}
    </style>
    """, unsafe_allow_html=True)

    # Conteúdo do Site
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="nav-dock"><div style="font-size: 32px; font-weight: 700;">{config["nome_site"]}</div></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">{config['hero_titulo']}</h1>
        <p style="font-size: 22px; font-weight: 900; color: #111; margin-top: 25px;">URL Planejada: {config['url_planejada']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Grid de Cards
    st.write("")
    cards = config['cards']
    for i in range(0, len(cards), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(cards):
                c = cards[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="dock-card">
                        <img src="{c['img']}" style="width:100%; height:300px; object-fit:cover;">
                        <div class="card-content">
                            <h2 style="font-family: 'Oswald'; font-size: 40px;">{c['titulo']}</h2>
                            <p style="color: var(--dock-yellow); font-weight: bold;">{c['sub']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # Seção Sobre
    st.markdown(f"""
    <div style="background-color: var(--dock-black); color: white; padding: 100px 5%;">
        <h2 style="font-family: 'Oswald'; font-size: 60px; color: var(--dock-yellow);">{config['sobre_titulo']}</h2>
        <p style="font-size: 24px; max-width: 800px;">{config['sobre_texto']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown(f"""
    <div style="padding: 80px 5%; background: var(--dock-yellow); color: #111; border-top: 2px solid var(--dock-black);">
        <h2 style="font-family: 'Oswald'; font-size: 45px;">{config['nome_site']}.</h2>
        <p>E-mail: {config['footer_email']} | <a href="{config['link_insta']}" style="color:#111;">Instagram</a></p>
        <div style="margin-top: 40px; border-top: 2px solid #111; padding-top: 20px; font-size: 13px; font-weight: 900;">
            {config['footer_copy']}
        </div>
    </div>
    """, unsafe_allow_html=True)
