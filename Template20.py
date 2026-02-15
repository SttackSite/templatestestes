import streamlit as st

# ❌ NÃO ALTERE: Configuração da página - Define o título da aba, ícone e layout
st.set_page_config(
    page_title="Inovação absoluta",  # ✅ ALTERE: Título da aba do navegador
    page_icon="⚡",  # ✅ ALTERE: Ícone que aparece na aba
    layout="wide",  # ❌ NÃO ALTERE: Layout da página
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Esconde a sidebar
)

# ❌ NÃO ALTERE: CSS ORIGINAL E INOVADOR - Estilos visuais da página inteira
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #000000;
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
        line-height: 1.6;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ❌ NÃO ALTERE: Animações originais que fazem elementos morph, girar e brilhar */
    @keyframes morphShape {
        0% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
        50% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
        100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
    }
    
    @keyframes liquidSwirl {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.1); }
        100% { transform: rotate(360deg) scale(1); }
    }
    
    @keyframes textReveal {
        0% { clip-path: polygon(0 0, 0 0, 0 100%, 0% 100%); }
        100% { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
    }
    
    @keyframes floatRotate {
        0% { transform: translateY(0px) rotateZ(0deg); }
        33% { transform: translateY(-20px) rotateZ(120deg); }
        66% { transform: translateY(10px) rotateZ(240deg); }
        100% { transform: translateY(0px) rotateZ(360deg); }
    }
    
    @keyframes neonGlow {
        0%, 100% { text-shadow: 0 0 10px #00FF88, 0 0 20px #00FF88, 0 0 40px #00FF88; }
        50% { text-shadow: 0 0 20px #00FF88, 0 0 40px #00FF88, 0 0 80px #00FF88; }
    }
    
    @keyframes slideAndFade {
        0% { transform: translateX(-100px) rotateY(90deg); opacity: 0; }
        100% { transform: translateX(0) rotateY(0deg); opacity: 1; }
    }
    
    @keyframes pulseRing {
        0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
        70% { box-shadow: 0 0 0 40px rgba(0, 255, 136, 0); }
        100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
    }
    
    @keyframes colorCycle {
        0% { color: #00FF88; }
        25% { color: #FF00FF; }
        50% { color: #00D9FF; }
        75% { color: #FFD700; }
        100% { color: #00FF88; }
    }
    
    @keyframes gridFlow {
        0% { background-position: 0 0; }
        100% { background-position: 40px 40px; }
    }
    
    /* ❌ NÃO ALTERE: Navbar futurista com backdrop blur e borda neon */
    .navbar {
        background: linear-gradient(90deg, rgba(0, 0, 0, 0.95) 0%, rgba(0, 20, 40, 0.95) 100%);
        backdrop-filter: blur(30px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #00FF88;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.2);
    }
    
    /* ✅ ALTERE: Logo - Mude o texto "CHAMPION" na navbar */
    .navbar-logo {
        font-size: 32px;
        font-weight: 900;
        color: #00FF88;
        letter-spacing: 3px;
        font-family: 'Space Mono', monospace;
        animation: neonGlow 2s ease-in-out infinite;
    }
    
    /* ❌ NÃO ALTERE: Container dos links da navbar */
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    /* ✅ ALTERE: Links da navbar - Mude cor, tamanho e espaçamento */
    .navbar-link {
        color: #ffffff;
        text-decoration: none !important;
        font-weight: 500;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'Space Mono', monospace;
    }
    
    /* ❌ NÃO ALTERE: Underline animado dos links - Aparece ao passar o mouse */
    .navbar-link::before {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(90deg, #00FF88, #FF00FF);
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::before {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #00FF88;
    }
    
    /* ✅ ALTERE: Botão CTA da navbar - Mude cor, texto e tamanho */
    .navbar-cta {
        background: linear-gradient(135deg, #00FF88, #00D9FF);
        color: #000000;
        padding: 12px 32px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid #00FF88;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
        font-family: 'Space Mono', monospace;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 40px rgba(0, 255, 136, 0.6);
    }
    
    /* ❌ NÃO ALTERE: Hero section - Seção principal com fundo gradiente e grid */
    .hero-section {
        background: linear-gradient(135deg, #000000 0%, #001a33 50%, #000000 100%);
        background-image: 
            repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0, 255, 136, 0.03) 2px,
                rgba(0, 255, 136, 0.03) 4px
            ),
            repeating-linear-gradient(
                90deg,
                transparent,
                transparent 2px,
                rgba(0, 255, 136, 0.03) 2px,
                rgba(0, 255, 136, 0.03) 4px
            );
        min-height: 800px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 80px 60px;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: liquidSwirl 8s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255, 0, 255, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: liquidSwirl 10s ease-in-out infinite reverse;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 1000px;
    }
    
    /* ✅ ALTERE: Título do hero - Mude o texto principal */
    .hero-title {
        font-size: 80px;
        font-weight: 900;
        margin-bottom: 20px;
        color: #00FF88;
        letter-spacing: -2px;
        line-height: 1.1;
        font-family: 'Space Mono', monospace;
        animation: neonGlow 2s ease-in-out infinite;
    }
    
    /* ✅ ALTERE: Subtítulo do hero - Mude o texto secundário */
    .hero-subtitle {
        font-size: 24px;
        font-weight: 300;
        margin-bottom: 50px;
        color: #00D9FF;
        letter-spacing: 2px;
        animation: slideAndFade 1s ease-out;
    }
    
    .hero-cta-group {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    /* ✅ ALTERE: Botão primário do hero - Mude cor, texto e tamanho */
    .hero-cta-primary {
        background: linear-gradient(135deg, #00FF88, #00D9FF);
        color: #000000;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: 2px solid #00FF88;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
        font-family: 'Space Mono', monospace;
        animation: slideAndFade 1.2s ease-out;
    }
    
    .hero-cta-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 50px rgba(0, 255, 136, 0.7);
    }
    
    /* ✅ ALTERE: Botão secundário do hero - Mude cor, texto e tamanho */
    .hero-cta-secondary {
        background: transparent;
        color: #00FF88;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: 2px solid #00FF88;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
        font-family: 'Space Mono', monospace;
        animation: slideAndFade 1.4s ease-out;
    }
    
    .hero-cta-secondary:hover {
        background: #00FF88;
        color: #000000;
        box-shadow: 0 0 40px rgba(0, 255, 136, 0.6);
    }
    
    /* ❌ NÃO ALTERE: Features section - Container com grid de cards */
    .features-section {
        padding: 120px 80px;
        background: #000000;
        position: relative;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.05), rgba(0, 217, 255, 0.05));
        border: 2px solid #00FF88;
        padding: 50px 40px;
        border-radius: 20px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideAndFade 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .feature-card:nth-child(1) { animation-delay: 0.1s; }
    .feature-card:nth-child(2) { animation-delay: 0.2s; }
    .feature-card:nth-child(3) { animation-delay: 0.3s; }
    .feature-card:nth-child(4) { animation-delay: 0.4s; }
    .feature-card:nth-child(5) { animation-delay: 0.5s; }
    .feature-card:nth-child(6) { animation-delay: 0.6s; }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-20px) rotateX(5deg);
        border-color: #00D9FF;
        box-shadow: 0 30px 60px rgba(0, 255, 136, 0.2);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
        animation: floatRotate 4s ease-in-out infinite;
    }
    
    .feature-title {
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #00FF88, #00D9FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 1px;
        font-family: 'Space Mono', monospace;
    }
    
    .feature-desc {
        font-size: 15px;
        color: #aaaaaa;
        line-height: 1.8;
        font-weight: 300;
    }
    
    /* ❌ NÃO ALTERE: Showcase section - Container com cards de números */
    .showcase-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #001a33 0%, #000000 100%);
        position: relative;
    }
    
    /* ✅ ALTERE: Título showcase - Mude o texto "NÚMEROS QUE FALAM" */
    .showcase-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        color: #00FF88;
        letter-spacing: -1px;
        font-family: 'Space Mono', monospace;
        animation: neonGlow 2s ease-in-out infinite;
    }
    
    .showcase-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .showcase-card {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(255, 0, 255, 0.05));
        border: 2px solid #00D9FF;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        transition: all 0.4s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        animation: slideAndFade 0.8s ease-out;
        animation-fill-mode: both;
    }
    
    .showcase-card:nth-child(1) { animation-delay: 0.1s; }
    .showcase-card:nth-child(2) { animation-delay: 0.2s; }
    .showcase-card:nth-child(3) { animation-delay: 0.3s; }
    .showcase-card:nth-child(4) { animation-delay: 0.4s; }
    
    .showcase-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.15), transparent);
        transition: left 0.5s ease;
    }
    
    .showcase-card:hover::after {
        left: 100%;
    }
    
    .showcase-card:hover {
        transform: translateY(-15px) scale(1.05);
        border-color: #00FF88;
        box-shadow: 0 0 40px rgba(0, 255, 136, 0.3);
    }
    
    .showcase-number {
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(135deg, #00FF88, #FF00FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        font-family: 'Space Mono', monospace;
    }
    
    .showcase-label {
        font-size: 18px;
        font-weight: 700;
        color: #00D9FF;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Space Mono', monospace;
    }
    
    /* ❌ NÃO ALTERE: CTA final - Seção com fundo gradiente colorido */
    .cta-final-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #00FF88 0%, #00D9FF 50%, #FF00FF 100%);
        background-size: 400% 400%;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .cta-final-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.3);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    /* ✅ ALTERE: Título final - Mude o texto "Pronto para Revolucionar?" */
    .cta-final-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        color: #000000;
        letter-spacing: -1px;
        font-family: 'Space Mono', monospace;
    }
    
    /* ✅ ALTERE: Descrição final - Mude o texto descritivo */
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: rgba(0, 0, 0, 0.9);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;
    }
    
    /* ✅ ALTERE: Botão final - Mude cor, texto e tamanho */
    .cta-final-button {
        background: #000000;
        color: #00FF88;
        padding: 18px 60px;
        border: 3px solid #00FF88;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 30px rgba(0, 0, 0, 0.4);
        font-family: 'Space Mono', monospace;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.6);
        background: #00FF88;
        color: #000000;
    }
    
    /* ❌ NÃO ALTERE: Footer - Rodapé com informações de contato */
    .footer {
        background: #000000;
        color: #888888;
        padding: 80px;
        text-align: center;
        border-top: 2px solid #00FF88;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.1);
    }
    
    /* ✅ ALTERE: Texto do footer - Mude email, telefone e endereço */
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 300;
        font-family: 'Space Mono', monospace;
    }
    
    /* ✅ ALTERE: Copyright - Mude o ano e nome da empresa */
    .footer-copyright {
        border-top: 1px solid rgba(0, 255, 136, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Space Mono', monospace;
    }
    
    /* ❌ NÃO ALTERE: Responsividade - Ajusta layout para telas menores */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 20px;
            padding: 15px 20px;
        }
        
        .navbar-links {
            flex-direction: column;
            gap: 15px;
            width: 100%;
        }
        
        .hero-section {
            min-height: 500px;
            padding: 40px 20px;
        }
        
        .hero-title {
            font-size: 42px;
        }
        
        .features-section,
        .showcase-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .showcase-title {
            font-size: 36px;
        }
        
        .cta-final-title {
            font-size: 36px;
        }
    }
</style>
"""

# ❌ NÃO ALTERE: Injetar CSS na página - Aplica todos os estilos acima
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
# ✅ ALTERE: Navbar - Mude os textos dos links e URLs das seções
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">CHAMPION</div>
    <div class="navbar-links">
        <a href="#recursos" class="navbar-link">Recursos</a>
        <a href="#portfolio" class="navbar-link">Portfólio</a>
        <a href="#sobre" class="navbar-link">Sobre</a>
        <a href="#contato" class="navbar-link">Contato</a>
        <a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
# ✅ ALTERE: Hero - Mude os textos dos botões e URLs
hero_html = '''<div class="hero-section" id="recursos">
    <div class="hero-content">
        <div class="hero-title">INOVAÇÃO ABSOLUTA</div>
        <div class="hero-subtitle">Design que transcende limites</div>
        <div class="hero-cta-group">
            <a href="https://www.google.com/" target="_blank" class="hero-cta-primary">Explorar Agora</a>
            <a href="https://www.google.com/" target="_blank" class="hero-cta-secondary">Saiba Mais</a>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
# ✅ ALTERE: Recursos - Mude os títulos, descrições e emojis dos cards
features_html = '''<div class="features-section">
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Velocidade</div>
            <div class="feature-desc">Performance extrema com carregamento instantâneo em qualquer dispositivo.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Design</div>
            <div class="feature-desc">Interface visual revolucionária com animações que impressionam.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔧</div>
            <div class="feature-title">Flexível</div>
            <div class="feature-desc">Totalmente customizável para qualquer tipo de negócio ou projeto.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📱</div>
            <div class="feature-title">Responsivo</div>
            <div class="feature-desc">Funciona perfeitamente em todos os dispositivos e tamanhos de tela.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Conversão</div>
            <div class="feature-desc">Design estratégico focado em maximizar taxas de conversão.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Premium</div>
            <div class="feature-desc">Experiência de luxo em cada interação e detalhe visual.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== SHOWCASE SECTION ====================
# ✅ ALTERE: Números - Mude os valores e labels dos cards
showcase_html = '''<div class="showcase-section" id="portfolio">
    <div class="showcase-title">NÚMEROS QUE FALAM</div>
    <div class="showcase-grid">
        <div class="showcase-card">
            <div class="showcase-number">500%</div>
            <div class="showcase-label">Mais Engajamento</div>
        </div>
        <div class="showcase-card">
            <div class="showcase-number">100K+</div>
            <div class="showcase-label">Usuários Ativos</div>
        </div>
        <div class="showcase-card">
            <div class="showcase-number">99.9%</div>
            <div class="showcase-label">Uptime</div>
        </div>
        <div class="showcase-card">
            <div class="showcase-number">24/7</div>
            <div class="showcase-label">Suporte Premium</div>
        </div>
    </div>
</div>'''
st.markdown(showcase_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
# ✅ ALTERE: CTA Final - Mude o texto e URL do botão
cta_final_html = '''<div class="cta-final-section" id="sobre">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronto para Revolucionar?</div>
        <div class="cta-final-desc">Junte-se aos líderes que já transformaram seus negócios com design de campeão.</div>
        <a href="https://www.google.com/" target="_blank" class="cta-final-button">Começar Sua Revolução</a>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
# ✅ ALTERE: Footer - Mude email, telefone, endereço e copyright
footer_html = '''<div class="footer" id="contato">
    <div class="footer-text">Email: hello@champion.com | Telefone: +55 (99) 99999-9999</div>
    <div class="footer-text">Endereço: Av. Inovação, 1000 - São Paulo, SP</div>
    <div class="footer-copyright">© 2025 Champion Design. Todos os direitos reservados. Design que vence campeonatos.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
