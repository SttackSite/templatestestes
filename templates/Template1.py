import streamlit as st

def render():
    # CSS GLOBAL DO EDITOR
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background: #f4f6fb; }
        [data-testid="stHeader"], [data-testid="stToolbarActions"], [data-testid="stDecoration"], footer { display: none !important; }
        .editor-panel { background: #ffffff; border-right: 1px solid #e2e8f0; height: 100vh; overflow-y: auto; padding: 24px 20px; }
        .preview-panel { height: 100vh; overflow-y: auto; background: #f8faff; }
        iframe { border: none !important; width: 100% !important; }
        .panel-title { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
        .panel-subtitle { font-size: 13px; color: #64748b; margin-bottom: 20px; }
        .section-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; margin: 20px 0 8px 0; padding-bottom: 6px; border-bottom: 1px solid #f1f5f9; }
        .stButton > button { background: linear-gradient(135deg, #0066FF, #0052CC) !important; color: white !important; border: none !important; border-radius: 8px !important; font-weight: 600 !important; width: 100% !important; }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="small")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-subtitle">Template 1 — Agência Digital</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        page_title = st.text_input("Título da aba", "Agência Digital - Transforme seu Negócio")
        page_icon = st.text_input("Ícone da aba", "🚀")

        st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
        cor_primaria = st.color_picker("Cor principal", "#0066FF")
        cor_texto = st.color_picker("Cor dos textos", "#1a1a1a")
        cor_subtexto = st.color_picker("Cor dos subtextos", "#666666")

        st.markdown('<div class="section-label">🔝 Navegação</div>', unsafe_allow_html=True)
        navbar_logo = st.text_input("Logo", "🚀 AGÊNCIA")
        navbar_link1 = st.text_input("Link 1", "Serviços")
        navbar_link2 = st.text_input("Link 2", "Sobre")
        navbar_link3 = st.text_input("Link 3", "Contato")
        navbar_cta_txt = st.text_input("CTA Texto", "Começar")
        navbar_cta_url = st.text_input("CTA URL", "#")

        st.markdown('<div class="section-label">🦸 Hero</div>', unsafe_allow_html=True)
        hero_titulo_antes = st.text_input("Título Parte 1", "Transforme seu Negócio com")
        hero_titulo_destaque = st.text_input("Título Destaque", "Estratégia Digital")
        hero_subtitulo = st.text_area("Subtítulo", "Soluções completas de marketing digital...", height=80)
        hero_btn1_txt = st.text_input("Botão 1 Texto", "Solicitar Consultoria")
        hero_btn1_url = st.text_input("Botão 1 URL", "#")
        hero_btn2_txt = st.text_input("Botão 2 Texto", "Ver Portfólio")
        hero_btn2_url = st.text_input("Botão 2 URL", "#")

        st.markdown('<div class="section-label">📊 Estatísticas</div>', unsafe_allow_html=True)
        stat1_num = st.text_input("Stat 1 Número", "500+")
        stat1_lbl = st.text_input("Stat 1 Label", "Clientes")
        stat2_num = st.text_input("Stat 2 Número", "10+")
        stat2_lbl = st.text_input("Stat 2 Label", "Anos")
        stat3_num = st.text_input("Stat 3 Número", "300%")
        stat3_lbl = st.text_input("Stat 3 Label", "Crescimento")

        st.markdown('<div class="section-label">🃏 Serviços</div>', unsafe_allow_html=True)
        secao_titulo = st.text_input("Título Seção", "Nossos")
        secao_destaque = st.text_input("Destaque Seção", "Serviços")
        secao_descricao = st.text_area("Descrição Seção", "Oferecemos soluções completas...", height=60)

        cards = []
        default_cards = [("📱", "Social Media", "Gerenciamento..."), ("🎯", "Ads", "Campanhas...")]
        for i, (icon_d, title_d, desc_d) in enumerate(default_cards, start=1):
            with st.expander(f"Card {i}"):
                icon = st.text_input(f"Ícone {i}", icon_d, key=f"icon_{i}")
                title = st.text_input(f"Título {i}", title_d, key=f"title_{i}")
                desc = st.text_area(f"Descrição {i}", desc_d, key=f"desc_{i}", height=70)
                cards.append((icon, title, desc))

        st.markdown('<div class="section-label">📣 Seção CTA</div>', unsafe_allow_html=True)
        cta_titulo = st.text_input("CTA Título", "Pronto para começar?")
        cta_subtxt = st.text_input("CTA Subtítulo", "Agende uma consultoria")
        cta_btn_txt = st.text_input("CTA Botão", "Agendar Agora")
        cta_btn_url = st.text_input("CTA Botão URL", "#")

        st.markdown('<div class="section-label">🔻 Footer</div>', unsafe_allow_html=True)
        footer_txt = st.text_input("Texto footer", "© 2026 Agência Digital.")

        st.markdown("---")
        if st.button("✅ Finalizar e Enviar"):
            st.success("Informações enviadas!")

    with col_preview:
        cards_html = "".join([f'<div class="feature-card"><div class="feature-icon">{c[0]}</div><h3 class="feature-title">{c[1]}</h3><p class="feature-description">{c[2]}</p></div>' for c in cards])

        html = f"""<!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>{page_title}</title>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: 'Inter', sans-serif; background: #f8f9ff; color: {cor_texto}; line-height: 1.6; }}
                .navbar {{ background: white; padding: 16px 60px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 100; }}
                .navbar-logo {{ font-size: 22px; font-weight: 800; color: {cor_primaria}; text-decoration: none; }}
                .navbar-cta {{ background: {cor_primaria}; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-size: 14px; font-weight: 600; }}
                .hero-section {{ padding: 80px 60px; text-align: center; }}
                .hero-title {{ font-size: 48px; font-weight: 800; margin-bottom: 20px; }}
                .hero-title-highlight {{ color: {cor_primaria}; }}
                .hero-subtitle {{ color: {cor_subtexto}; max-width: 600px; margin: 0 auto 30px; }}
                .cta-button {{ display: inline-block; background: {cor_primaria}; color: white; padding: 12px 30px; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 5px; }}
                .hero-stats {{ display: flex; justify-content: center; gap: 40px; margin-top: 40px; }}
                .hero-stat-number {{ font-size: 32px; font-weight: 800; color: {cor_primaria}; }}
                .features-section {{ padding: 60px; background: white; }}
                .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; max-width: 1000px; margin: 0 auto; }}
                .feature-card {{ background: #f8f9ff; padding: 30px; border-radius: 12px; text-align: center; border: 1px solid #eee; }}
                .cta-section {{ background: {cor_primaria}; color: white; padding: 60px; text-align: center; }}
                .footer {{ padding: 30px; text-align: center; font-size: 13px; color: #999; }}
                .editor-notice {{ background: #fffbeb; padding: 8px; text-align: center; font-size: 12px; color: #92400e; border-bottom: 1px solid #fbbf24; }}
            </style>
        </head>
        <body>
            <div class="editor-notice">⚠️ Modo Visualização — Edite os campos na barra lateral</div>
            <nav class="navbar">
                <a href="#" class="navbar-logo">{navbar_logo}</a>
                <a href="{navbar_cta_url}" class="navbar-cta">{navbar_cta_txt}</a>
            </nav>
            <section class="hero-section">
                <h1 class="hero-title">{hero_titulo_antes} <span class="hero-title-highlight">{hero_titulo_destaque}</span></h1>
                <p class="hero-subtitle">{hero_subtitulo}</p>
                <a href="{hero_btn1_url}" class="cta-button">{hero_btn1_txt}</a>
                <div class="hero-stats">
                    <div><div class="hero-stat-number">{stat1_num}</div><div>{stat1_lbl}</div></div>
                    <div><div class="hero-stat-number">{stat2_num}</div><div>{stat2_lbl}</div></div>
                </div>
            </section>
            <section class="features-section">
                <div class="features-grid">{cards_html}</div>
            </section>
            <footer class="footer"><p>{footer_txt}</p></footer>
        </body>
        </html>"""
        st.components.v1.html(html, height=850, scrolling=True)
