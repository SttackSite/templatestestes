import streamlit as st
import json
from datetime import datetime

# ========== CONFIGURAÇÃO - DEVE SER A PRIMEIRA COISA ==========
st.set_page_config(
    page_title="Template 1 - Customizador",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== INICIALIZAR SESSION STATE ==========
if 'customizations' not in st.session_state:
    st.session_state.customizations = {
        # Página
        'page_title': 'Agência Digital - Transforme seu Negócio',
        'page_icon': '🚀',
        # Navbar
        'navbar_logo': '🚀 AGÊNCIA',
        'navbar_link1': 'Serviços',
        'navbar_link2': 'Sobre',
        'navbar_link3': 'Contato',
        'navbar_cta': 'Começar',
        'navbar_cta_url': 'https://www.google.com/',
        # Hero
        'hero_badge1': '✨ Novo',
        'hero_badge2': 'Transformação Digital',
        'hero_badge3': '⭐ Top Rated',
        'hero_title': 'Transforme seu Negócio com Estratégia Digital',
        'hero_subtitle': 'Soluções completas de marketing digital que aumentam suas vendas e presença online',
        'hero_btn1': 'Solicitar Consultoria',
        'hero_btn1_url': 'https://www.google.com/',
        'hero_btn2': 'Ver Portfólio',
        'hero_btn2_url': 'https://www.google.com/',
        'hero_stat1_num': '500+',
        'hero_stat1_label': 'Clientes Satisfeitos',
        'hero_stat2_num': '10+',
        'hero_stat2_label': 'Anos de Experiência',
        'hero_stat3_num': '300%',
        'hero_stat3_label': 'Crescimento Médio',
        # Serviços
        'services_title': 'Nossos Serviços',
        'services_desc': 'Oferecemos soluções completas de marketing digital para impulsionar seu negócio',
        'service1_icon': '📱',
        'service1_title': 'Social Media',
        'service1_desc': 'Gerenciamento completo de suas redes sociais com estratégia de conteúdo',
        'service2_icon': '🎯',
        'service2_title': 'Publicidade Digital',
        'service2_desc': 'Campanhas otimizadas em Google Ads e Facebook para máximo ROI',
        'service3_icon': '📊',
        'service3_title': 'Análise de Dados',
        'service3_desc': 'Relatórios detalhados e insights para melhorar seu desempenho',
        'service4_icon': '🌐',
        'service4_title': 'SEO & Conteúdo',
        'service4_desc': 'Otimização para buscas e criação de conteúdo de alta qualidade',
        'service5_icon': '💻',
        'service5_title': 'Web Design',
        'service5_desc': 'Websites modernos e responsivos que convertem visitantes em clientes',
        'service6_icon': '📧',
        'service6_title': 'Email Marketing',
        'service6_desc': 'Campanhas de email personalizadas que geram resultados',
        # CTA
        'cta_title': 'Pronto para Transformar seu Negócio?',
        'cta_desc': 'Agende uma consultoria gratuita com nossos especialistas',
        'cta_btn': 'Agendar Agora',
        'cta_btn_url': 'https://www.google.com/',
        # Footer
        'footer_text': '&copy; 2026 Agência Digital. Todos os direitos reservados.',
        # Identificação
        'user_email': '',
        'user_url': '',
    }

# ========== CSS DO TEMPLATE 1 ==========
template_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #f8f9ff 0%, #f0f4ff 50%, #f8f9ff 100%);
        background-attachment: fixed;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: #1a1a1a;
        line-height: 1.6;
    }
    
    [data-testid="stHeader"] { display: none; }
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    .navbar {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 16px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(0, 102, 255, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 10px rgba(0, 102, 255, 0.08);
    }
    
    .navbar-logo {
        font-size: 24px;
        font-weight: 900;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #1a1a1a;
        text-decoration: none !important;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.3s ease;
        position: relative;
        cursor: pointer;
    }
    
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 2px;
        background: #0066FF;
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #0066FF;
    }
    
    .navbar-cta {
        background: linear-gradient(90deg, #0066FF, #0052CC);
        color: white !important;
        padding: 10px 28px;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.2);
        display: inline-block;
    }
    
    .navbar-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 102, 255, 0.3);
    }
    
    .hero-section {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.8) 0%, rgba(248, 249, 255, 0.6) 100%);
        backdrop-filter: blur(10px);
        padding: 120px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
        border-bottom: 1px solid rgba(0, 102, 255, 0.1);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(0, 102, 255, 0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(0, 102, 255, 0.05) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 24px;
        color: #1a1a1a;
        letter-spacing: -1px;
    }
    
    .hero-title-highlight {
        color: #0066FF;
    }
    
    .hero-subtitle {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 50px;
        color: #666666;
        font-weight: 400;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 80px;
        margin-top: 60px;
        padding-top: 60px;
        border-top: 1px solid #e0e0e0;
    }
    
    .hero-stat {
        text-align: center;
    }
    
    .hero-stat-number {
        font-size: 36px;
        font-weight: 900;
        color: #0066FF;
        margin-bottom: 8px;
    }
    
    .hero-stat-label {
        font-size: 14px;
        color: #666666;
        font-weight: 500;
    }
    
    .badges-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 30px;
    }
    
    .badge {
        background: #f0f0f0;
        color: #1a1a1a;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    .badge-primary {
        background: #0066FF;
        color: white;
    }
    
    .badge-success {
        background: #00AA44;
        color: white;
    }
    
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white !important;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.25);
        margin-right: 20px;
        margin-bottom: 20px;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 102, 255, 0.35);
    }
    
    .cta-button-secondary {
        background: white;
        color: #0066FF !important;
        border: 2px solid #0066FF;
        box-shadow: none;
    }
    
    .cta-button-secondary:hover {
        background: #f0f6ff;
    }
    
    .features-section {
        padding: 100px 60px;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.7) 0%, rgba(248, 249, 255, 0.5) 100%);
        backdrop-filter: blur(5px);
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 80px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .section-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 16px;
        color: #1a1a1a;
        letter-spacing: -0.5px;
    }
    
    .section-title-highlight {
        color: #0066FF;
    }
    
    .section-description {
        font-size: 18px;
        color: #666666;
        line-height: 1.6;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
        padding: 40px 30px;
        border-radius: 12px;
        border: 1px solid rgba(0, 102, 255, 0.1);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 102, 255, 0.3);
        box-shadow: 0 12px 40px rgba(0, 102, 255, 0.1);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
    }
    
    .feature-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #1a1a1a;
    }
    
    .feature-description {
        font-size: 15px;
        color: #666666;
        line-height: 1.6;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white;
        padding: 100px 60px;
        text-align: center;
    }
    
    .cta-section h2 {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
    }
    
    .cta-section p {
        font-size: 18px;
        margin-bottom: 40px;
        opacity: 0.9;
    }
    
    .footer {
        background: #1a1a1a;
        color: white;
        padding: 60px;
        text-align: center;
    }
    
    .footer p {
        font-size: 14px;
        color: #999999;
    }
</style>
"""

# ========== RENDERIZAR PREVIEW ==========
def render_preview():
    from streamlit.components.v1 import html as st_html
    
    preview_html = f"""
    {template_css}
    
    <div class="navbar">
        <div class="navbar-logo">{st.session_state.customizations['navbar_logo']}</div>
        <div class="navbar-links">
            <a href="#features" class="navbar-link">{st.session_state.customizations['navbar_link1']}</a>
            <a href="#features" class="navbar-link">{st.session_state.customizations['navbar_link2']}</a>
            <a href="#footer" class="navbar-link">{st.session_state.customizations['navbar_link3']}</a>
            <a href="{st.session_state.customizations['navbar_cta_url']}" class="navbar-cta">{st.session_state.customizations['navbar_cta']}</a>
        </div>
    </div>
    
    <div class="hero-section">
        <div class="hero-content">
            <div class="badges-container">
                <span class="badge badge-primary">{st.session_state.customizations['hero_badge1']}</span>
                <span class="badge">{st.session_state.customizations['hero_badge2']}</span>
                <span class="badge badge-success">{st.session_state.customizations['hero_badge3']}</span>
            </div>
            <h1 class="hero-title">
                {st.session_state.customizations['hero_title'].replace('Estratégia Digital', '<span class="hero-title-highlight">Estratégia Digital</span>')}
            </h1>
            <p class="hero-subtitle">
                {st.session_state.customizations['hero_subtitle']}
            </p>
            <div style="margin-bottom: 60px;">
                <a href="{st.session_state.customizations['hero_btn1_url']}" class="cta-button">{st.session_state.customizations['hero_btn1']}</a>
                <a href="{st.session_state.customizations['hero_btn2_url']}" class="cta-button cta-button-secondary">{st.session_state.customizations['hero_btn2']}</a>
            </div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-number">{st.session_state.customizations['hero_stat1_num']}</div>
                    <div class="hero-stat-label">{st.session_state.customizations['hero_stat1_label']}</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">{st.session_state.customizations['hero_stat2_num']}</div>
                    <div class="hero-stat-label">{st.session_state.customizations['hero_stat2_label']}</div>
                </div>
                <div class="hero-stat">
                    <div class="hero-stat-number">{st.session_state.customizations['hero_stat3_num']}</div>
                    <div class="hero-stat-label">{st.session_state.customizations['hero_stat3_label']}</div>
                </div>
            </div>
        </div>
    </div>
    
    <div id="features" class="features-section">
        <div class="section-header">
            <h2 class="section-title">{st.session_state.customizations['services_title']} <span class="section-title-highlight">Serviços</span></h2>
            <p class="section-description">
                {st.session_state.customizations['services_desc']}
            </p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service1_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service1_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service1_desc']}</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service2_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service2_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service2_desc']}</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service3_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service3_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service3_desc']}</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service4_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service4_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service4_desc']}</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service5_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service5_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service5_desc']}</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">{st.session_state.customizations['service6_icon']}</div>
                <h3 class="feature-title">{st.session_state.customizations['service6_title']}</h3>
                <p class="feature-description">{st.session_state.customizations['service6_desc']}</p>
            </div>
        </div>
    </div>
    
    <div id="cta" class="cta-section">
        <h2>{st.session_state.customizations['cta_title']}</h2>
        <p>{st.session_state.customizations['cta_desc']}</p>
        <a href="{st.session_state.customizations['cta_btn_url']}" class="cta-button cta-button-secondary" style="padding: 16px 48px;">{st.session_state.customizations['cta_btn']}</a>
    </div>
    
    <div id="footer" class="footer">
        <p>{st.session_state.customizations['footer_text']}</p>
    </div>
    """
    
    st_html(preview_html, height=2000)

# ========== INTERFACE ==========
st.markdown("# 🚀 Customizador - Template 1: Agência Digital")

col_left, col_right = st.columns([1, 1.5])

# ========== PAINEL DE EDIÇÃO ==========
with col_left:
    st.markdown("### ✏️ Customize os Campos")
    
    with st.expander("📄 Página", expanded=True):
        st.session_state.customizations['page_title'] = st.text_input(
            "Título da Página",
            value=st.session_state.customizations['page_title']
        )
        st.session_state.customizations['page_icon'] = st.text_input(
            "Ícone da Página",
            value=st.session_state.customizations['page_icon']
        )
    
    with st.expander("🔗 Navbar", expanded=True):
        st.session_state.customizations['navbar_logo'] = st.text_input(
            "Logo",
            value=st.session_state.customizations['navbar_logo']
        )
        st.session_state.customizations['navbar_link1'] = st.text_input(
            "Link 1",
            value=st.session_state.customizations['navbar_link1']
        )
        st.session_state.customizations['navbar_link2'] = st.text_input(
            "Link 2",
            value=st.session_state.customizations['navbar_link2']
        )
        st.session_state.customizations['navbar_link3'] = st.text_input(
            "Link 3",
            value=st.session_state.customizations['navbar_link3']
        )
        st.session_state.customizations['navbar_cta'] = st.text_input(
            "Botão CTA",
            value=st.session_state.customizations['navbar_cta']
        )
        st.session_state.customizations['navbar_cta_url'] = st.text_input(
            "URL do Botão CTA",
            value=st.session_state.customizations['navbar_cta_url']
        )
    
    with st.expander("🎯 Hero", expanded=True):
        st.session_state.customizations['hero_badge1'] = st.text_input(
            "Badge 1",
            value=st.session_state.customizations['hero_badge1']
        )
        st.session_state.customizations['hero_badge2'] = st.text_input(
            "Badge 2",
            value=st.session_state.customizations['hero_badge2']
        )
        st.session_state.customizations['hero_badge3'] = st.text_input(
            "Badge 3",
            value=st.session_state.customizations['hero_badge3']
        )
        st.session_state.customizations['hero_title'] = st.text_area(
            "Título Principal",
            value=st.session_state.customizations['hero_title'],
            height=60
        )
        st.session_state.customizations['hero_subtitle'] = st.text_area(
            "Subtítulo",
            value=st.session_state.customizations['hero_subtitle'],
            height=60
        )
        st.session_state.customizations['hero_btn1'] = st.text_input(
            "Botão 1",
            value=st.session_state.customizations['hero_btn1']
        )
        st.session_state.customizations['hero_btn1_url'] = st.text_input(
            "URL Botão 1",
            value=st.session_state.customizations['hero_btn1_url']
        )
        st.session_state.customizations['hero_btn2'] = st.text_input(
            "Botão 2",
            value=st.session_state.customizations['hero_btn2']
        )
        st.session_state.customizations['hero_btn2_url'] = st.text_input(
            "URL Botão 2",
            value=st.session_state.customizations['hero_btn2_url']
        )
        st.session_state.customizations['hero_stat1_num'] = st.text_input(
            "Estatística 1 - Número",
            value=st.session_state.customizations['hero_stat1_num']
        )
        st.session_state.customizations['hero_stat1_label'] = st.text_input(
            "Estatística 1 - Label",
            value=st.session_state.customizations['hero_stat1_label']
        )
        st.session_state.customizations['hero_stat2_num'] = st.text_input(
            "Estatística 2 - Número",
            value=st.session_state.customizations['hero_stat2_num']
        )
        st.session_state.customizations['hero_stat2_label'] = st.text_input(
            "Estatística 2 - Label",
            value=st.session_state.customizations['hero_stat2_label']
        )
        st.session_state.customizations['hero_stat3_num'] = st.text_input(
            "Estatística 3 - Número",
            value=st.session_state.customizations['hero_stat3_num']
        )
        st.session_state.customizations['hero_stat3_label'] = st.text_input(
            "Estatística 3 - Label",
            value=st.session_state.customizations['hero_stat3_label']
        )
    
    with st.expander("💼 Serviços"):
        st.session_state.customizations['services_title'] = st.text_input(
            "Título da Seção",
            value=st.session_state.customizations['services_title']
        )
        st.session_state.customizations['services_desc'] = st.text_area(
            "Descrição",
            value=st.session_state.customizations['services_desc'],
            height=60
        )
        for i in range(1, 7):
            st.markdown(f"**Serviço {i}**")
            st.session_state.customizations[f'service{i}_icon'] = st.text_input(
                f"Ícone",
                value=st.session_state.customizations[f'service{i}_icon'],
                key=f"service{i}_icon"
            )
            st.session_state.customizations[f'service{i}_title'] = st.text_input(
                f"Título",
                value=st.session_state.customizations[f'service{i}_title'],
                key=f"service{i}_title"
            )
            st.session_state.customizations[f'service{i}_desc'] = st.text_area(
                f"Descrição",
                value=st.session_state.customizations[f'service{i}_desc'],
                height=60,
                key=f"service{i}_desc"
            )
    
    with st.expander("📢 CTA Final"):
        st.session_state.customizations['cta_title'] = st.text_input(
            "Título",
            value=st.session_state.customizations['cta_title']
        )
        st.session_state.customizations['cta_desc'] = st.text_input(
            "Descrição",
            value=st.session_state.customizations['cta_desc']
        )
        st.session_state.customizations['cta_btn'] = st.text_input(
            "Botão",
            value=st.session_state.customizations['cta_btn']
        )
        st.session_state.customizations['cta_btn_url'] = st.text_input(
            "URL do Botão",
            value=st.session_state.customizations['cta_btn_url']
        )
    
    with st.expander("🔗 Rodapé"):
        st.session_state.customizations['footer_text'] = st.text_area(
            "Texto do Rodapé",
            value=st.session_state.customizations['footer_text'],
            height=60
        )
    
    with st.expander("👤 Identificação"):
        st.session_state.customizations['user_email'] = st.text_input(
            "Seu Email",
            value=st.session_state.customizations['user_email']
        )
        st.session_state.customizations['user_url'] = st.text_input(
            "Sua URL (https://[TEXTO].streamlit.app)",
            value=st.session_state.customizations['user_url']
        )

# ========== PREVIEW ==========
with col_right:
    st.markdown("### 👁️ Preview")
    render_preview()

# ========== BOTÕES DE AÇÃO ==========
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Baixar JSON", use_container_width=True):
        json_data = {
            "template_id": 1,
            "template_name": "Agência Digital",
            "user_email": st.session_state.customizations.get("user_email", ""),
            "user_url": st.session_state.customizations.get("user_url", ""),
            "created_at": datetime.now().isoformat(),
            "customizations": st.session_state.customizations
        }
        
        st.download_button(
            label="Clique aqui para baixar",
            data=json.dumps(json_data, indent=2, ensure_ascii=False),
            file_name=f"template_1_customizations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

with col2:
    st.info("📧 Envie o JSON para: **sttacksite@gmail.com**")

with col3:
    if st.button("🔄 Resetar Valores", use_container_width=True):
        st.session_state.customizations = {}
        st.rerun()
