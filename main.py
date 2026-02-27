import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Editor — Template 1",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS GLOBAL DO EDITOR
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: #f4f6fb;
    }

    /* Esconde elementos padrão do Streamlit */
    [data-testid="stHeader"], [data-testid="stToolbarActions"],
    [data-testid="stDecoration"], footer { display: none !important; }

    /* Painel esquerdo (formulário) */
    .editor-panel {
        background: #ffffff;
        border-right: 1px solid #e2e8f0;
        height: 100vh;
        overflow-y: auto;
        padding: 24px 20px;
    }

    /* Painel direito (preview) */
    .preview-panel {
        height: 100vh;
        overflow-y: auto;
        background: #f8faff;
    }

    /* Iframe do preview */
    iframe {
        border: none !important;
        width: 100% !important;
    }

    /* Título do painel */
    .panel-title {
        font-size: 18px;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 4px;
    }
    .panel-subtitle {
        font-size: 13px;
        color: #64748b;
        margin-bottom: 20px;
    }

    /* Separador de seção */
    .section-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94a3b8;
        margin: 20px 0 8px 0;
        padding-bottom: 6px;
        border-bottom: 1px solid #f1f5f9;
    }

    /* Botão de envio */
    .stButton > button {
        background: linear-gradient(135deg, #0066FF, #0052CC) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 10px 24px !important;
        width: 100% !important;
        margin-top: 12px !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0,102,255,0.3) !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CAMPOS EDITÁVEIS — VOCÊ DEFINE AQUI O QUE O CLIENTE PODE ALTERAR
# Basta adicionar ou remover st.text_input / st.color_picker / st.text_area
# ─────────────────────────────────────────────────────────────────────────────

col_form, col_preview = st.columns([1, 2], gap="small")

with col_form:
    st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-subtitle">Template 1 — Agência Digital</div>', unsafe_allow_html=True)

    # ── CONFIGURAÇÃO GERAL ────────────────────────────────────────────────────
    st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
    page_title   = st.text_input("Título da aba do navegador", "Agência Digital - Transforme seu Negócio")
    page_icon    = st.text_input("Ícone da aba (emoji)", "🚀")

    # ── CORES ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
    cor_primaria = st.color_picker("Cor principal (botões, destaques)", "#0066FF")
    cor_texto    = st.color_picker("Cor dos textos", "#1a1a1a")
    cor_subtexto = st.color_picker("Cor dos subtextos", "#666666")

    # ── NAVBAR ────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
    navbar_logo    = st.text_input("Logo / Nome da marca", "🚀 AGÊNCIA")
    navbar_link1   = st.text_input("Link 1 — Texto", "Serviços")
    navbar_link2   = st.text_input("Link 2 — Texto", "Sobre")
    navbar_link3   = st.text_input("Link 3 — Texto", "Contato")
    navbar_cta_txt = st.text_input("Botão CTA — Texto", "Começar")
    navbar_cta_url = st.text_input("Botão CTA — URL", "https://www.google.com/")

    # ── HERO ──────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)
    hero_titulo_antes    = st.text_input("Título — Parte 1 (antes do destaque)", "Transforme seu Negócio com")
    hero_titulo_destaque = st.text_input("Título — Parte 2 (em destaque colorido)", "Estratégia Digital")
    hero_subtitulo       = st.text_area("Subtítulo", "Soluções completas de marketing digital que aumentam suas vendas e presença online", height=80)
    hero_btn1_txt        = st.text_input("Botão 1 — Texto", "Solicitar Consultoria")
    hero_btn1_url        = st.text_input("Botão 1 — URL", "https://www.google.com/")
    hero_btn2_txt        = st.text_input("Botão 2 — Texto", "Ver Portfólio")
    hero_btn2_url        = st.text_input("Botão 2 — URL", "https://www.google.com/")

    # ── ESTATÍSTICAS ──────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">📊 Estatísticas do Hero</div>', unsafe_allow_html=True)
    stat1_num = st.text_input("Estatística 1 — Número", "500+")
    stat1_lbl = st.text_input("Estatística 1 — Label", "Clientes Satisfeitos")
    stat2_num = st.text_input("Estatística 2 — Número", "10+")
    stat2_lbl = st.text_input("Estatística 2 — Label", "Anos de Experiência")
    stat3_num = st.text_input("Estatística 3 — Número", "300%")
    stat3_lbl = st.text_input("Estatística 3 — Label", "Crescimento Médio")

    # ── SERVIÇOS / CARDS ──────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)
    secao_titulo    = st.text_input("Título da seção — Parte 1", "Nossos")
    secao_destaque  = st.text_input("Título da seção — Destaque", "Serviços")
    secao_descricao = st.text_area("Descrição da seção", "Oferecemos soluções completas de marketing digital para impulsionar seu negócio", height=60)

    cards = []
    for i, (icon_d, title_d, desc_d) in enumerate([
        ("📱", "Social Media", "Gerenciamento completo de suas redes sociais com estratégia de conteúdo"),
        ("🎯", "Publicidade Digital", "Campanhas otimizadas em Google Ads e Facebook para máximo ROI"),
        ("📊", "Análise de Dados", "Relatórios detalhados e insights para melhorar seu desempenho"),
        ("🌐", "SEO & Conteúdo", "Otimização para buscas e criação de conteúdo de alta qualidade"),
        ("💻", "Web Design", "Websites modernos e responsivos que convertem visitantes em clientes"),
        ("📧", "Email Marketing", "Campanhas de email personalizadas que geram resultados"),
    ], start=1):
        with st.expander(f"Card {i} — {title_d}"):
            icon  = st.text_input(f"Ícone {i}", icon_d, key=f"icon_{i}")
            title = st.text_input(f"Título {i}", title_d, key=f"title_{i}")
            desc  = st.text_area(f"Descrição {i}", desc_d, key=f"desc_{i}", height=70)
            cards.append((icon, title, desc))

    # ── CTA ───────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">📣 Seção CTA</div>', unsafe_allow_html=True)
    cta_titulo  = st.text_input("CTA — Título", "Pronto para Transformar seu Negócio?")
    cta_subtxt  = st.text_input("CTA — Subtítulo", "Agende uma consultoria gratuita com nossos especialistas")
    cta_btn_txt = st.text_input("CTA — Botão Texto", "Agendar Agora")
    cta_btn_url = st.text_input("CTA — Botão URL", "https://www.google.com/")

    # ── FOOTER ────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔻 Footer</div>', unsafe_allow_html=True)
    footer_txt = st.text_input("Texto do footer", "© 2026 Agência Digital. Todos os direitos reservados.")

    # ── ENVIAR ────────────────────────────────────────────────────────────────
    st.markdown("---")
    if st.button("✅ Finalizar e Enviar para a Equipe"):
        st.success("Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
        # Aqui você pode adicionar st.balloons() ou lógica de envio por e-mail


# ─────────────────────────────────────────────────────────────────────────────
# PREVIEW — RENDERIZA A LANDING PAGE COM OS VALORES PREENCHIDOS
# ─────────────────────────────────────────────────────────────────────────────

with col_preview:

    # Gera os cards HTML dinamicamente
    cards_html = ""
    for (icon, title, desc) in cards:
        cards_html += f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3 class="feature-title">{title}</h3>
            <p class="feature-description">{desc}</p>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Inter', sans-serif;
    background: linear-gradient(180deg, #f8f9ff 0%, #f0f4ff 50%, #f8f9ff 100%);
    color: {cor_texto};
    line-height: 1.6;
}}

/* NAVBAR */
.navbar {{
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(10px);
    padding: 16px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(0,102,255,0.1);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0,102,255,0.08);
}}
.navbar-logo {{
    font-size: 22px;
    font-weight: 900;
    color: {cor_primaria};
    text-decoration: none;
}}
.navbar-links {{
    display: flex;
    gap: 40px;
    align-items: center;
}}
.navbar-link {{
    color: {cor_texto};
    text-decoration: none;
    font-weight: 500;
    font-size: 15px;
    transition: color 0.2s;
}}
.navbar-link:hover {{ color: {cor_primaria}; }}
.navbar-cta {{
    background: {cor_primaria};
    color: white;
    padding: 10px 24px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
}}

/* HERO */
.hero-section {{
    padding: 100px 60px;
    text-align: center;
    background: linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(248,249,255,0.6) 100%);
    border-bottom: 1px solid rgba(0,102,255,0.1);
}}
.hero-title {{
    font-size: 56px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
    color: {cor_texto};
    letter-spacing: -1px;
}}
.hero-title-highlight {{ color: {cor_primaria}; }}
.hero-subtitle {{
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 40px;
    color: {cor_subtexto};
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}}
.cta-button {{
    display: inline-block;
    background: {cor_primaria};
    color: white;
    padding: 14px 36px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    margin: 0 8px 8px;
    transition: transform 0.2s;
}}
.cta-button:hover {{ transform: translateY(-2px); }}
.cta-button-secondary {{
    background: transparent;
    color: {cor_primaria};
    border: 2px solid {cor_primaria};
}}
.hero-stats {{
    display: flex;
    justify-content: center;
    gap: 60px;
    margin-top: 60px;
}}
.hero-stat-number {{
    font-size: 36px;
    font-weight: 900;
    color: {cor_primaria};
}}
.hero-stat-label {{
    font-size: 14px;
    color: {cor_subtexto};
    margin-top: 4px;
}}

/* FEATURES */
.features-section {{
    padding: 80px 60px;
    background: white;
}}
.section-header {{
    text-align: center;
    margin-bottom: 50px;
}}
.section-title {{
    font-size: 40px;
    font-weight: 800;
    color: {cor_texto};
}}
.section-title-highlight {{ color: {cor_primaria}; }}
.section-description {{
    font-size: 16px;
    color: {cor_subtexto};
    margin-top: 12px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}}
.features-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1100px;
    margin: 0 auto;
}}
.feature-card {{
    background: #f8f9ff;
    border-radius: 16px;
    padding: 32px 24px;
    border: 1px solid rgba(0,102,255,0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}}
.feature-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,102,255,0.1);
}}
.feature-icon {{ font-size: 36px; margin-bottom: 16px; }}
.feature-title {{
    font-size: 18px;
    font-weight: 700;
    color: {cor_texto};
    margin-bottom: 10px;
}}
.feature-description {{
    font-size: 14px;
    color: {cor_subtexto};
    line-height: 1.6;
}}

/* CTA */
.cta-section {{
    background: linear-gradient(135deg, {cor_primaria} 0%, #0052CC 100%);
    padding: 80px 60px;
    text-align: center;
    color: white;
}}
.cta-section h2 {{
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 16px;
}}
.cta-section p {{
    font-size: 18px;
    margin-bottom: 36px;
    opacity: 0.9;
}}

/* FOOTER */
.footer {{
    background: #1a1a1a;
    color: #999;
    padding: 40px 60px;
    text-align: center;
    font-size: 14px;
}}

/* AVISO EDITOR */
.editor-notice {{
    background: #fffbeb;
    border: 1px solid #fbbf24;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 13px;
    color: #92400e;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 200;
}}
</style>
</head>
<body>

<div class="editor-notice">
    ⚠️ <strong>Prévia de edição</strong> — Esta é uma versão simplificada. O site final entregue é muito mais bonito, com animações e efeitos completos.
</div>

<!-- NAVBAR -->
<nav class="navbar">
    <a href="#" class="navbar-logo">{navbar_logo}</a>
    <div class="navbar-links">
        <a href="#features" class="navbar-link">{navbar_link1}</a>
        <a href="#cta" class="navbar-link">{navbar_link2}</a>
        <a href="#footer" class="navbar-link">{navbar_link3}</a>
        <a href="{navbar_cta_url}" class="navbar-cta">{navbar_cta_txt}</a>
    </div>
</nav>

<!-- HERO -->
<section class="hero-section">
    <h1 class="hero-title">
        {hero_titulo_antes} <span class="hero-title-highlight">{hero_titulo_destaque}</span>
    </h1>
    <p class="hero-subtitle">{hero_subtitulo}</p>
    <div>
        <a href="{hero_btn1_url}" class="cta-button">{hero_btn1_txt}</a>
        <a href="{hero_btn2_url}" class="cta-button cta-button-secondary">{hero_btn2_txt}</a>
    </div>
    <div class="hero-stats">
        <div>
            <div class="hero-stat-number">{stat1_num}</div>
            <div class="hero-stat-label">{stat1_lbl}</div>
        </div>
        <div>
            <div class="hero-stat-number">{stat2_num}</div>
            <div class="hero-stat-label">{stat2_lbl}</div>
        </div>
        <div>
            <div class="hero-stat-number">{stat3_num}</div>
            <div class="hero-stat-label">{stat3_lbl}</div>
        </div>
    </div>
</section>

<!-- SERVIÇOS -->
<section id="features" class="features-section">
    <div class="section-header">
        <h2 class="section-title">{secao_titulo} <span class="section-title-highlight">{secao_destaque}</span></h2>
        <p class="section-description">{secao_descricao}</p>
    </div>
    <div class="features-grid">
        {cards_html}
    </div>
</section>

<!-- CTA -->
<section id="cta" class="cta-section">
    <h2>{cta_titulo}</h2>
    <p>{cta_subtxt}</p>
    <a href="{cta_btn_url}" class="cta-button" style="background:white; color:{cor_primaria}; border:none;">{cta_btn_txt}</a>
</section>

<!-- FOOTER -->
<footer id="footer" class="footer">
    <p>{footer_txt}</p>
</footer>

</body>
</html>"""

    st.components.v1.html(html, height=900, scrolling=True)
