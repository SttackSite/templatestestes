import streamlit as st

# ❌ NÃO ALTERE: Configuração da página - Define o título da aba, ícone e layout
st.set_page_config(
    page_title="Bela Feminine - Elegância Absoluta",  # ✅ ALTERE: Título da aba do navegador
    page_icon="✨",  # ✅ ALTERE: Ícone que aparece na aba
    layout="wide",  # ❌ NÃO ALTERE: Layout da página
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Esconde a sidebar
)

# ❌ NÃO ALTERE: CSS PREMIUM FEMININO - Estilos visuais da página inteira
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Cormorant+Garamond:wght@300;400;500;600;700&family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #faf8f5;
        font-family: 'Cormorant Garamond', serif;
        color: #2d2d2d;
        line-height: 1.8;
        overflow-x: hidden;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ❌ NÃO ALTERE: Animações sofisticadas que fazem elementos flutuar e brilhar */
    @keyframes petalFloat {
        0% { transform: translateY(0px) rotateZ(-15deg); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(-30px) rotateZ(15deg); opacity: 0; }
    }
    
    @keyframes shimmerGold {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes softGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(212, 175, 130, 0.3); }
        50% { box-shadow: 0 0 40px rgba(212, 175, 130, 0.6); }
    }
    
    @keyframes elegantSlide {
        0% { transform: translateX(-50px) rotateY(20deg); opacity: 0; }
        100% { transform: translateX(0) rotateY(0deg); opacity: 1; }
    }
    
    @keyframes fadeInScale {
        0% { transform: scale(0.95); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes floatDelicate {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    @keyframes borderFlow {
        0% { border-color: rgba(212, 175, 130, 0.3); }
        50% { border-color: rgba(212, 175, 130, 0.8); }
        100% { border-color: rgba(212, 175, 130, 0.3); }
    }
    
    @keyframes textGradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* ❌ NÃO ALTERE: Navbar elegante com backdrop blur e gradiente */
    .navbar {
        background: linear-gradient(135deg, rgba(250, 248, 245, 0.98) 0%, rgba(245, 240, 235, 0.98) 100%);
        backdrop-filter: blur(20px);
        padding: 25px 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid rgba(212, 175, 130, 0.3);
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 8px 32px rgba(212, 175, 130, 0.1);
    }
    
    /* ✅ ALTERE: Logo - Mude o texto "Bela" na navbar */
    .navbar-logo {
        font-size: 32px;
        font-weight: 900;
        background: linear-gradient(135deg, #d4af82, #c99a6e, #d4af82);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 3px;
        font-family: 'Playfair Display', serif;
        animation: textGradientShift 3s ease infinite;
    }
    
    /* ❌ NÃO ALTERE: Container dos links da navbar */
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    /* ✅ ALTERE: Links da navbar - Mude cor, tamanho e espaçamento */
    .navbar-link {
        color: #2d2d2d;
        text-decoration: none !important;
        font-weight: 500;
        font-size: 13px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        font-family: 'Poppins', sans-serif;
    }
    
    /* ❌ NÃO ALTERE: Underline animado dos links - Aparece ao passar o mouse */
    .navbar-link::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #d4af82, #c99a6e);
        transition: width 0.3s ease;
    }
    
    .navbar-link:hover::after {
        width: 100%;
    }
    
    .navbar-link:hover {
        color: #d4af82;
    }
    
    /* ✅ ALTERE: Botão CTA da navbar - Mude cor, texto e tamanho */
    .navbar-cta {
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        color: white;
        padding: 12px 32px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
        font-size: 12px;
        transition: all 0.3s ease;
        border: 2px solid #d4af82;
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(212, 175, 130, 0.3);
        font-family: 'Poppins', sans-serif;
    }
    
    .navbar-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(212, 175, 130, 0.5);
    }
    
    /* ❌ NÃO ALTERE: Hero section - Seção principal com fundo gradiente */
    .hero-section {
        background: linear-gradient(135deg, #faf8f5 0%, #f5f0eb 50%, #faf8f5 100%);
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
        background: radial-gradient(circle, rgba(212, 175, 130, 0.08) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: floatDelicate 6s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(201, 154, 110, 0.06) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: floatDelicate 8s ease-in-out infinite reverse;
    }
    
    .hero-content {
        text-align: center;
        z-index: 2;
        position: relative;
        max-width: 900px;
    }
    
    /* ✅ ALTERE: Título do hero - Mude o texto principal */
    .hero-title {
        font-size: 80px;
        font-weight: 900;
        margin-bottom: 20px;
        background: linear-gradient(135deg, #d4af82, #c99a6e, #b8860b, #d4af82);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -2px;
        line-height: 1.1;
        font-family: 'Playfair Display', serif;
        animation: textGradientShift 4s ease infinite;
    }
    
    /* ✅ ALTERE: Subtítulo do hero - Mude o texto secundário */
    .hero-subtitle {
        font-size: 24px;
        font-weight: 300;
        margin-bottom: 50px;
        color: #c99a6e;
        letter-spacing: 2px;
        font-family: 'Cormorant Garamond', serif;
        animation: elegantSlide 1s ease-out;
    }
    
    .hero-cta-group {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }
    
    /* ✅ ALTERE: Botão primário do hero - Mude cor, texto e tamanho */
    .hero-cta-primary {
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        color: white;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: 2px solid #d4af82;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 30px rgba(212, 175, 130, 0.4);
        font-family: 'Poppins', sans-serif;
        animation: elegantSlide 1.2s ease-out;
    }
    
    .hero-cta-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(212, 175, 130, 0.6);
    }
    
    /* ✅ ALTERE: Botão secundário do hero - Mude cor, texto e tamanho */
    .hero-cta-secondary {
        background: transparent;
        color: #d4af82;
        padding: 18px 50px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: 2px solid #d4af82;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(212, 175, 130, 0.2);
        font-family: 'Poppins', sans-serif;
        animation: elegantSlide 1.4s ease-out;
    }
    
    .hero-cta-secondary:hover {
        background: #d4af82;
        color: white;
        box-shadow: 0 8px 30px rgba(212, 175, 130, 0.4);
    }
    
    /* ❌ NÃO ALTERE: Seção de benefícios - Container com padding e fundo */
    .benefits-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #f5f0eb 0%, #faf8f5 100%);
        position: relative;
    }
    
    /* ✅ ALTERE: Título da seção - Mude o texto "Por Que Escolher" */
    .section-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Playfair Display', serif;
        animation: fadeInScale 0.8s ease-out;
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .benefit-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(245, 240, 235, 0.9));
        border: 2px solid rgba(212, 175, 130, 0.3);
        padding: 50px 40px;
        border-radius: 20px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: elegantSlide 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 8px 32px rgba(212, 175, 130, 0.08);
    }
    
    .benefit-card:nth-child(1) { animation-delay: 0.1s; }
    .benefit-card:nth-child(2) { animation-delay: 0.2s; }
    .benefit-card:nth-child(3) { animation-delay: 0.3s; }
    
    .benefit-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(212, 175, 130, 0.15), transparent);
        transition: left 0.5s ease;
    }
    
    .benefit-card:hover::before {
        left: 100%;
    }
    
    .benefit-card:hover {
        transform: translateY(-15px);
        border-color: #d4af82;
        box-shadow: 0 20px 50px rgba(212, 175, 130, 0.2);
    }
    
    .benefit-icon {
        font-size: 48px;
        margin-bottom: 20px;
        animation: floatDelicate 3s ease-in-out infinite;
    }
    
    .benefit-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
        color: #d4af82;
        letter-spacing: 0.5px;
        font-family: 'Playfair Display', serif;
    }
    
    .benefit-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.8;
        font-weight: 300;
    }
    
    /* ❌ NÃO ALTERE: Seção de preços - Container com tabela */
    .pricing-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #faf8f5 0%, #f5f0eb 100%);
    }
    
    /* ✅ ALTERE: Título de preços - Mude o texto "Nossos Planos" */
    .pricing-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Playfair Display', serif;
    }
    
    .pricing-table-wrapper {
        max-width: 1200px;
        margin: 0 auto;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 240, 235, 0.95));
        border: 2px solid rgba(212, 175, 130, 0.3);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(212, 175, 130, 0.15);
        animation: fadeInScale 0.8s ease-out;
    }
    
    .pricing-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .pricing-table thead {
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        color: white;
    }
    
    .pricing-table th {
        padding: 25px;
        text-align: left;
        font-weight: 700;
        font-size: 16px;
        letter-spacing: 1px;
        font-family: 'Playfair Display', serif;
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .pricing-table th:last-child {
        border-right: none;
    }
    
    .pricing-table td {
        padding: 20px 25px;
        border-bottom: 1px solid rgba(212, 175, 130, 0.2);
        font-size: 14px;
        color: #2d2d2d;
    }
    
    .pricing-table tbody tr:hover {
        background: rgba(212, 175, 130, 0.05);
    }
    
    .pricing-table tbody tr:last-child td {
        border-bottom: none;
    }
    
    .price-value {
        font-size: 28px;
        font-weight: 700;
        color: #d4af82;
        font-family: 'Playfair Display', serif;
    }
    
    .feature-check {
        color: #d4af82;
        font-weight: 700;
        font-size: 18px;
    }
    
    .feature-cross {
        color: #999999;
        font-weight: 700;
        font-size: 18px;
    }
    
    /* ❌ NÃO ALTERE: Seção de comparação - Container com cards de números */
    .comparison-section {
        padding: 120px 80px;
        background: linear-gradient(135deg, #f5f0eb 0%, #faf8f5 100%);
    }
    
    /* ✅ ALTERE: Título de comparação - Mude o texto "Números que Falam" */
    .comparison-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 100px;
        text-align: center;
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
        font-family: 'Playfair Display', serif;
    }
    
    .comparison-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .comparison-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(245, 240, 235, 0.95));
        border: 2px solid rgba(212, 175, 130, 0.3);
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: elegantSlide 0.8s ease-out;
        animation-fill-mode: both;
        box-shadow: 0 8px 32px rgba(212, 175, 130, 0.08);
    }
    
    .comparison-card:nth-child(1) { animation-delay: 0.1s; }
    .comparison-card:nth-child(2) { animation-delay: 0.2s; }
    .comparison-card:nth-child(3) { animation-delay: 0.3s; }
    
    .comparison-card:hover {
        transform: translateY(-15px);
        border-color: #d4af82;
        box-shadow: 0 20px 50px rgba(212, 175, 130, 0.2);
    }
    
    .comparison-number {
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(135deg, #d4af82, #c99a6e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        font-family: 'Playfair Display', serif;
    }
    
    .comparison-label {
        font-size: 18px;
        font-weight: 700;
        color: #2d2d2d;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: 'Poppins', sans-serif;
    }
    
    /* ❌ NÃO ALTERE: CTA final - Seção com fundo gradiente dourado */
    .cta-final-section {
        padding: 150px 80px;
        background: linear-gradient(135deg, #d4af82 0%, #c99a6e 50%, #b8860b 100%);
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
        background: rgba(255, 255, 255, 0.1);
    }
    
    .cta-final-content {
        position: relative;
        z-index: 2;
    }
    
    /* ✅ ALTERE: Título final - Mude o texto "Pronta para Brilhar?" */
    .cta-final-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        color: white;
        letter-spacing: -1px;
        font-family: 'Playfair Display', serif;
    }
    
    /* ✅ ALTERE: Descrição final - Mude o texto descritivo */
    .cta-final-desc {
        font-size: 20px;
        margin-bottom: 50px;
        color: rgba(255, 255, 255, 0.95);
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 300;
        font-family: 'Cormorant Garamond', serif;
    }
    
    /* ✅ ALTERE: Botão final - Mude cor, texto e tamanho */
    .cta-final-button {
        background: white;
        color: #d4af82;
        padding: 18px 60px;
        border: 3px solid white;
        border-radius: 50px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        cursor: pointer;
        display: inline-block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        font-family: 'Poppins', sans-serif;
    }
    
    .cta-final-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
    }
    
    /* ❌ NÃO ALTERE: Footer - Rodapé com informações de contato */
    .footer {
        background: #2d2d2d;
        color: #888888;
        padding: 80px;
        text-align: center;
        border-top: 2px solid rgba(212, 175, 130, 0.3);
        box-shadow: 0 -8px 32px rgba(212, 175, 130, 0.1);
    }
    
    /* ✅ ALTERE: Texto do footer - Mude email, telefone e endereço */
    .footer-text {
        font-size: 14px;
        margin-bottom: 12px;
        font-weight: 300;
        font-family: 'Poppins', sans-serif;
    }
    
    /* ✅ ALTERE: Copyright - Mude o ano e nome da empresa */
    .footer-copyright {
        border-top: 1px solid rgba(212, 175, 130, 0.2);
        padding-top: 40px;
        margin-top: 40px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: 'Poppins', sans-serif;
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
        
        .benefits-section,
        .pricing-section,
        .comparison-section,
        .cta-final-section {
            padding: 80px 20px;
        }
        
        .section-title,
        .pricing-title,
        .comparison-title,
        .cta-final-title {
            font-size: 36px;
        }
        
        .pricing-table {
            font-size: 12px;
        }
        
        .pricing-table th,
        .pricing-table td {
            padding: 15px;
        }
    }
</style>
"""

# ❌ NÃO ALTERE: Injetar CSS na página - Aplica todos os estilos acima
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
# ✅ ALTERE: Navbar - Mude os textos dos links e URLs das seções
navbar_html = '''<div class="navbar">
    <div class="navbar-logo">Bela</div>
    <div class="navbar-links">
        <a href="#colecao" class="navbar-link">Coleção</a>
        <a href="#beneficios" class="navbar-link">Benefícios</a>
        <a href="#precos" class="navbar-link">Preços</a>
        <a href="#contato" class="navbar-link">Contato</a>
        <a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar Agora</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
# ✅ ALTERE: Hero - Mude os textos dos botões e URLs
hero_html = '''<div class="hero-section" id="colecao">
    <div class="hero-content">
        <div class="hero-title">Elegância Absoluta</div>
        <div class="hero-subtitle">Experiência Premium para Mulheres Sofisticadas</div>
        <div class="hero-cta-group">
            <a href="https://www.google.com/" target="_blank" class="hero-cta-primary">Descobrir Agora</a>
            <a href="https://www.google.com/" target="_blank" class="hero-cta-secondary">Saiba Mais</a>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== BENEFITS SECTION ====================
# ✅ ALTERE: Benefícios - Mude os títulos, descrições e emojis dos cards
benefits_html = '''<div class="benefits-section" id="beneficios">
    <div class="section-title">Por Que Escolher</div>
    <div class="benefits-grid">
        <div class="benefit-card">
            <div class="benefit-icon">💎</div>
            <div class="benefit-title">Qualidade Premium</div>
            <div class="benefit-desc">Produtos de luxo selecionados com rigor absoluto para sua satisfação.</div>
        </div>
        <div class="benefit-card">
            <div class="benefit-icon">✨</div>
            <div class="benefit-title">Exclusividade</div>
            <div class="benefit-desc">Acesso a coleções limitadas e edições especiais para você.</div>
        </div>
        <div class="benefit-card">
            <div class="benefit-icon">🌸</div>
            <div class="benefit-title">Sofisticação</div>
            <div class="benefit-desc">Design elegante que reflete sua personalidade e estilo único.</div>
        </div>
    </div>
</div>'''
st.markdown(benefits_html, unsafe_allow_html=True)

# ==================== PRICING TABLE ====================
# ✅ ALTERE: Preços - Mude os valores, nomes dos planos e features
pricing_html = '''<div class="pricing-section" id="precos">
    <div class="pricing-title">Nossos Planos</div>
    <div class="pricing-table-wrapper">
        <table class="pricing-table">
            <thead>
                <tr>
                    <th>Recurso</th>
                    <th>Essencial</th>
                    <th>Premium</th>
                    <th>Bela</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Preço Mensal</strong></td>
                    <td><span class="price-value">R$ 99</span></td>
                    <td><span class="price-value">R$ 199</span></td>
                    <td><span class="price-value">R$ 399</span></td>
                </tr>
                <tr>
                    <td>Acesso à Coleção Base</td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Coleções Exclusivas</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Atendimento Prioritário</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Consultoria Pessoal</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Frete Grátis</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <td>Eventos Exclusivos</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>'''
st.markdown(pricing_html, unsafe_allow_html=True)

# ==================== COMPARISON SECTION ====================
# ✅ ALTERE: Números - Mude os valores e labels dos cards
comparison_html = '''<div class="comparison-section">
    <div class="comparison-title">Números que Falam</div>
    <div class="comparison-grid">
        <div class="comparison-card">
            <div class="comparison-number">50K+</div>
            <div class="comparison-label">Clientes Satisfeitas</div>
        </div>
        <div class="comparison-card">
            <div class="comparison-number">1000+</div>
            <div class="comparison-label">Produtos Premium</div>
        </div>
        <div class="comparison-card">
            <div class="comparison-number">98%</div>
            <div class="comparison-label">Taxa de Satisfação</div>
        </div>
    </div>
</div>'''
st.markdown(comparison_html, unsafe_allow_html=True)

# ==================== CTA FINAL ====================
# ✅ ALTERE: CTA Final - Mude o texto e URL do botão
cta_final_html = '''<div class="cta-final-section">
    <div class="cta-final-content">
        <div class="cta-final-title">Pronta para Brilhar?</div>
        <div class="cta-final-desc">Junte-se a milhares de mulheres que já descobriram a verdadeira elegância.</div>
        <a href="https://www.google.com/" target="_blank" class="cta-final-button">Acessar Agora</a>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
# ✅ ALTERE: Footer - Mude email, telefone, endereço e copyright
footer_html = '''<div class="footer" id="contato">
    <div class="footer-text">Email: hello@Bela.com.br | Telefone: +55 (99) 99999-9999</div>
    <div class="footer-text">Endereço: Av. Paulista, 1000 - São Paulo, SP</div>
    <div class="footer-copyright">© 2025 Bela Feminine. Todos os direitos reservados. Elegância é um estilo de vida.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
