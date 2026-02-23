import streamlit as st
import json

# Configuração da Página
st.set_page_config(layout="wide", page_title="Editor Dockyard Ultimate | Sttack", page_icon="⚙️")

def render_configurator():
    # --- CSS PARA INSTRUÇÕES E ESTILO ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&family=Oswald:wght@700&display=swap');
        
        .instruction-box {
            background-color: #e3f2fd;
            padding: 25px;
            border-left: 6px solid #1976d2;
            border-radius: 8px;
            margin-bottom: 30px;
            font-family: 'Inter', sans-serif;
            color: #0d47a1;
        }
        
        [data-testid="stHeader"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # --- 1. AVISO INICIAL DE VENDAS ---
    st.markdown(f"""
    <div class="instruction-box">
        <h3 style="margin-top:0;">🚀 Instruções de Customização</h3>
        Estas são as alterações básicas para colocar seu site no ar rapidamente. 
        Qualquer <strong>customização mais complexa</strong> pode ser detalhada no campo de 
        <em>'Observações'</em> na barra lateral ou no corpo do e-mail. 
        Nós aplicamos para você (desde que não seja estrutural).
    </div>
    """, unsafe_allow_html=True)

    # --- BARRA LATERAL (PAINEL DE CONTROLE COMPLETO) ---
    st.sidebar.title("🎨 CONFIGURADOR MASTER")
    
    config = {}

    # NOVO: Seção de URL
    st.sidebar.subheader("🌐 Link do seu Site")
    url_nome = st.sidebar.text_input("Nome da URL desejada:", placeholder="ex: myplace")
    config['url_planejada'] = f"https://{url_nome}.streamlit.app" if url_nome else "https://...streamlit.app"
    st.sidebar.caption(f"Seu site será: {config['url_planejada']}")

    # 1. Identidade Visual
    with st.sidebar.expander("📌 1. Identidade e Cores", expanded=True):
        config['cor_destaque'] = st.color_picker("Cor Destaque (Amarelo)", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal (Preto)", "#111111")
        config['cor_fundo'] = st.color_picker("Cor Fundo (Cinza/Branco)", "#f4f4f4")
        config['nome_site'] = st.text_input("Nome da Marca/Logo", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Aviso da Faixa Preta", "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO")

    # 2. Hero Section
    with st.sidebar.expander("🚀 2. Topo do Site (Hero)", expanded=False):
        config['hero_titulo'] = st.text_area("Título Grande (use <br> para pular linha)", "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.")
        config['hero_subtitulo'] = st.text_input("Subtítulo", "O melhor mercado de comida de rua de Glasgow, agora na sua tela.")

    # 3. Cards Dinâmicos
    st.sidebar.markdown("### 🍔 3. Gerenciar Cards")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "CRAFT BEER & COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"},
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic", key="editor_cards")

    # 4. Seção Sobre
    with st.sidebar.expander("📖 4. Seção 'Sobre'", expanded=False):
        config['sobre_titulo'] = st.text_input("Título da Seção", "MAIS QUE UM MERCADO.")
        config['sobre_texto'] = st.text_area("Texto Descritivo", "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos.")

    # 5. CTAs e Botões
    st.sidebar.markdown("### 🔗 5. Botões de Ação")
    config['cta_titulo_secao'] = st.sidebar.text_input("Título da Seção de Botões", "PRONTO PARA VIVER A EXPERIÊNCIA?")
    default_buttons = [{"texto": "RESERVAR AGORA", "link": "https://google.com"}]
    config['botoes'] = st.sidebar.data_editor(default_buttons, num_rows="dynamic", key="editor_btns")

    # 6. Rodapé (Footer)
    with st.sidebar.expander("📍 6. Rodapé e Contatos", expanded=False):
        config['footer_endereco'] = st.text_input("Endereço", "952 South St, Glasgow G14 0BX")
        config['footer_email'] = st.text_input("E-mail", "hello@dockyardsocial.com")
        config['link_instagram'] = st.text_input("Link Instagram", "https://instagram.com")
        config['link_facebook'] = st.text_input("Link Facebook", "https://facebook.com")
        config['link_tiktok'] = st.text_input("Link TikTok", "https://tiktok.com")
        config['footer_copyright'] = st.text_input("Copyright", "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO.")

    # NOVO: Observações
    st.sidebar.markdown("### 📝 7. Observações")
    config['observacoes'] = st.sidebar.text_area("Detalhe aqui outras customizações desejadas:")

    # FINALIZAÇÃO
    st.sidebar.markdown("---")
    st.sidebar.error("⚠️ **IMPORTANTE:**\n\nBaixe o arquivo JSON e envie para **sttacksite@gmail.com** para aplicarmos seu site!")
    
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR CONFIGURAÇÃO", json_export, "meu_site_sttack.json", "application/json")

    # =========================================================
    # RENDERIZAÇÃO DO SITE (ESTILO FIEL AO ORIGINAL)
    # =========================================================
    
    st.markdown(f"""
    <style>
        :root {{
            --dock-yellow: {config['cor_destaque']};
            --dock-black: {config['cor_principal']};
            --dock-white: {config['cor_fundo']};
        }}
        .stApp {{ background-color: var(--dock-white); }}
        .main .block-container {{ padding: 0 !important; max-width: 100% !important; }}

        .announcement {{
            background: var(--dock-black); color: white; padding: 12px;
            font-weight: bold; text-align: center; letter-spacing: 2px;
            font-family: 'Inter', sans-serif; font-size: 14px;
        }}
        .nav-dock {{
            background-color: var(--dock-black); color: var(--dock-yellow);
            padding: 20px 5%; display: flex; justify-content: space-between;
            align-items: center; font-family: 'Oswald', sans-serif;
        }}
        .hero-dock {{
            background-color: var(--dock-yellow); padding: 80px 5%;
            border-bottom: 8px solid var(--dock-black);
        }}
        .hero-h1 {{
            font-family: 'Oswald', sans-serif; font-size: clamp(50px, 10vw, 130px);
            color: var(--dock-black); line-height: 0.9; text-transform: uppercase; margin: 0;
        }}
        .dock-card {{
            background: var(--dock-black); color: white; border: 4px solid var(--dock-black);
            transition: 0.3s; margin-bottom: 25px;
        }}
        .card-content {{ padding: 25px; }}
        h2 {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; margin: 0; }}

        .action-button {{
            display: inline-block !important; background: var(--dock-black) !important;
            color: var(--dock-yellow) !important; padding: 18px 45px !important;
            font-family: 'Oswald', sans-serif !important; font-size: 20px !important;
            text-transform: uppercase !important; text-decoration: none !important;
            font-weight: bold !important; transition: 0.2s !important; border: none !important;
        }}
        .action-button:hover {{ background: #333 !important; color: white !important; transform: scale(1.05); }}
    </style>
    """, unsafe_allow_html=True)

    # 1. Header e Nav
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="nav-dock"><div style="font-size: 32px; font-weight: 700;">{config["nome_site"]}</div><div style="font-size:12px; border: 1px solid; padding: 5px;">MODO EDITOR</div></div>', unsafe_allow_html=True)
    
    # 2. Hero
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">{config['hero_titulo']}</h1>
    </div>
    """, unsafe_allow_html=True)

    # 3. Grid de Cards
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
                            <h2 style="font-size: 40px; line-height: 1;">{c['titulo']}</h2>
                            <p style="color: var(--dock-yellow); font-weight: bold;">{c['sub']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # 4. Sobre
    st.markdown(f"""
    <div style="background-color: var(--dock-black); color: white; padding: 100px 5%; margin-top: 50px;">
        <h2 style="font-size: 60px; color: var(--dock-yellow); margin-bottom: 30px;">{config['sobre_titulo']}</h2>
        <p style="font-size: 24px; line-height: 1.4; font-weight: 300; max-width: 800px;">{config['sobre_texto']}</p>
    </div>
    """, unsafe_allow_html=True)

    # 5. CTA
    st.markdown(f"""
    <div style="background-color: var(--dock-yellow); padding: 120px 5%; text-align: center; border-top: 8px solid var(--dock-black);">
        <h2 style="font-size: 60px; margin-bottom: 40px; color: var(--dock-black);">{config['cta_titulo_secao']}</h2>
    """, unsafe_allow_html=True)
    for btn in config['botoes']:
        st.markdown(f'<a href="{btn["link"]}" target="_blank" class="action-button">{btn["texto"]}</a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 6. Footer
    st.markdown(f"""
    <div style="padding: 80px 5%; background: var(--dock-yellow); color: #111; border-top: 2px solid var(--dock-black);">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 40px;">
            <div><h2 style="font-size: 45px;">{config['nome_site']}.</h2><p style="font-weight: bold;">{config['footer_endereco']}</p></div>
            <div style="text-align: right; font-weight: bold; font-size: 16px;">
                {config['footer_email']}<br>
                INSTAGRAM / FACEBOOK / TIKTOK
            </div>
        </div>
        <div style="margin-top: 60px; border-top: 3px solid #111; padding-top: 20px; font-size: 13px; font-weight: 900;">
            {config['footer_copyright']}
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_configurator()
