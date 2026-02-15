import streamlit as st

# ✅ ALTERE: Configuração da página - Mude o título, ícone e nome conforme sua marca
st.set_page_config(
    page_title="Agência Digital - Transforme seu Negócio",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🚀",  # ✅ ALTERE: Ícone que aparece na aba do navegador
    layout="wide",  # ❌ NÃO ALTERE: Define o layout da página em modo wide
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Esconde a barra lateral do Streamlit
)

# ❌ NÃO ALTERE: CSS ULTRA PROFISSIONAL - Responsável por todo o visual da página
custom_css = """
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
    
    html::before, body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(0, 102, 255, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(0, 102, 255, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
        position: relative;
        z-index: 1;
    }
    
    /* ❌ NÃO ALTERE: NAVBAR - Barra de navegação no topo da página */
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
    
    /* ✅ ALTERE: Logo da navbar - Mude o texto e cor conforme sua marca */
    .navbar-logo {
        font-size: 24px;
        font-weight: 900;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    /* ❌ NÃO ALTERE: Container dos links da navbar */
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    /* ❌ NÃO ALTERE: Estilo dos links da navbar com underline animado */
    .navbar-link {
        color: #1a1a1a;
        text-decoration: none !important;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.3s ease;
        position: relative;
        cursor: pointer;
    }
    
    /* ❌ NÃO ALTERE: Efeito hover dos links - Underline animado */
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
    
    /* ✅ ALTERE: Botão CTA da navbar - Mude o texto e URL */
    .cta-button {
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
    }
    
    .navbar-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 102, 255, 0.3);
    }
    
    /* ❌ NÃO ALTERE: HERO SECTION - Seção principal de apresentação */
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
    
    /* ✅ ALTERE: Título principal do hero - Mude o texto conforme sua marca */
    .hero-title {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 24px;
        color: #1a1a1a;
        letter-spacing: -1px;
    }
    
    /* ✅ ALTERE: Parte destacada do título - Mude a cor conforme sua marca */
    .hero-title-highlight {
        color: #0066FF;
    }
    
    /* ✅ ALTERE: Subtítulo do hero - Mude o texto conforme sua marca */
    .hero-subtitle {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 50px;
        color: #666666;
        font-weight: 400;
    }
    
    /* ❌ NÃO ALTERE: Container das estatísticas do hero */
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
    
    /* ✅ ALTERE: Números das estatísticas - Mude os números conforme seus dados */
    .hero-stat-number {
        font-size: 36px;
        font-weight: 900;
        color: #0066FF;
        margin-bottom: 8px;
    }
    
    /* ✅ ALTERE: Labels das estatísticas - Mude os textos conforme seus dados */
    .hero-stat-label {
        font-size: 14px;
        color: #666666;
        font-weight: 500;
    }
    
    /* ❌ NÃO ALTERE: BADGES - Pequenos rótulos de destaque */
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
    
    .badge-icon {
        font-size: 14px;
    }
    
    .badge-primary {
        background: #0066FF;
        color: white;
    }
    
    .badge-success {
        background: #00AA44;
        color: white;
    }
    
    .badge-warning {
        background: #FF6600;
        color: white;
    }
    
    /* ❌ NÃO ALTERE: BUTTONS - Botões de ação */
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white !important;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.25);
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 102, 255, 0.35);
    }
    
    .cta-button-secondary {
        background: white;
        color: #0066FF;
        border: 2px solid #0066FF;
        box-shadow: none;
    }
    
    .cta-button-secondary:hover {
        background: #f0f6ff;
    }
    
    /* ❌ NÃO ALTERE: FEATURES SECTION - Seção de características */
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
    
    /* ✅ ALTERE: Título das seções - Mude o texto conforme sua marca */
    .section-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        color: #1a1a1a;
        letter-spacing: -0.5px;
    }
    
    /* ✅ ALTERE: Parte destacada do título da seção - Mude a cor conforme sua marca */
    .section-title-highlight {
        color: #0066FF;
    }
    
    /* ✅ ALTERE: Descrição das seções - Mude o texto conforme sua marca */
    .section-description {
        font-size: 18px;
        color: #666666;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* ❌ NÃO ALTERE: Grid de features */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* ❌ NÃO ALTERE: Card de feature */
    .feature-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 12px;
        border: 1px solid rgba(0, 102, 255, 0.15);
        transition: all 0.4s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: #0066FF;
        box-shadow: 0 12px 40px rgba(0, 102, 255, 0.12);
    }
    
    /* ✅ ALTERE: Ícone das features - Mude os emojis conforme sua marca */
    .feature-icon {
        font-size: 48px;
        margin-bottom: 20px;
        display: inline-block;
    }
    
    /* ✅ ALTERE: Título das features - Mude o texto conforme sua marca */
    .feature-title {
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 12px;
        color: #1a1a1a;
    }
    
    /* ✅ ALTERE: Descrição das features - Mude o texto conforme sua marca */
    .feature-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.7;
    }
    
    /* ❌ NÃO ALTERE: SERVICES SECTION - Seção de serviços */
    .services-section {
        padding: 100px 60px;
        background: linear-gradient(180deg, rgba(248, 249, 255, 0.8) 0%, rgba(240, 244, 255, 0.6) 100%);
        backdrop-filter: blur(5px);
    }
    
    /* ❌ NÃO ALTERE: Grid de serviços */
    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 40px;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* ❌ NÃO ALTERE: Card de serviço */
    .service-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 50px 40px;
        border-radius: 12px;
        border: 1px solid rgba(0, 102, 255, 0.15);
        text-align: center;
        transition: all 0.4s ease;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        border-color: #0066FF;
        box-shadow: 0 16px 48px rgba(0, 102, 255, 0.15);
    }
    
    /* ✅ ALTERE: Número dos serviços - Mude os números conforme sua ordem */
    .service-number {
        font-size: 48px;
        font-weight: 900;
        color: #0066FF;
        margin-bottom: 16px;
    }
    
    /* ✅ ALTERE: Título dos serviços - Mude o texto conforme sua marca */
    .service-title {
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 16px;
        color: #1a1a1a;
    }
    
    /* ✅ ALTERE: Descrição dos serviços - Mude o texto conforme sua marca */
    .service-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.7;
    }
    
    /* ❌ NÃO ALTERE: TESTIMONIALS SECTION - Seção de depoimentos */
    .testimonials-section {
        padding: 100px 60px;
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.7) 0%, rgba(248, 249, 255, 0.5) 100%);
        backdrop-filter: blur(5px);
    }
    
    /* ❌ NÃO ALTERE: Card de depoimento */
    .testimonial-card {
        background: rgba(248, 249, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 12px;
        border-left: 4px solid #0066FF;
        margin-bottom: 30px;
        border: 1px solid rgba(0, 102, 255, 0.15);
        border-left: 4px solid #0066FF;
    }
    
    /* ✅ ALTERE: Texto do depoimento - Mude o texto conforme seus clientes */
    .testimonial-text {
        font-size: 16px;
        color: #1a1a1a;
        line-height: 1.8;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    /* ✅ ALTERE: Nome do autor - Mude o nome conforme seus clientes */
    .testimonial-author {
        font-size: 14px;
        font-weight: 700;
        color: #1a1a1a;
    }
    
    /* ✅ ALTERE: Cargo do autor - Mude o cargo conforme seus clientes */
    .testimonial-role {
        font-size: 13px;
        color: #666666;
        font-weight: 500;
    }
    
    /* ❌ NÃO ALTERE: CTA FINAL SECTION - Seção final de chamada para ação */
    .cta-final-section {
        background: linear-gradient(135deg, #0066FF 0%, #0052CC 100%);
        color: white;
        padding: 100px 60px;
        text-align: center;
    }
    
    /* ✅ ALTERE: Título CTA final - Mude o texto conforme sua marca */
    .cta-final-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        letter-spacing: -0.5px;
    }
    
    /* ✅ ALTERE: Descrição CTA final - Mude o texto conforme sua marca */
    .cta-final-desc {
        font-size: 18px;
        margin-bottom: 50px;
        opacity: 0.95;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* ❌ NÃO ALTERE: Botão CTA final */
    .cta-final-button {
        background: white;
        color: #0066FF;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .cta-final-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }
    
    /* ❌ NÃO ALTERE: FOOTER - Rodapé da página */
    .footer {
        background: #1a1a1a;
        color: rgba(255, 255, 255, 0.7);
        padding: 60px;
        text-align: center;
    }
    
    /* ✅ ALTERE: Texto do footer - Mude as informações conforme sua empresa */
    .footer-text {
        font-size: 15px;
        margin-bottom: 10px;
    }
    
    /* ✅ ALTERE: Copyright do footer - Mude o texto conforme sua empresa */
    .footer-copyright {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 30px;
        margin-top: 30px;
        font-size: 13px;
    }
    
    /* ❌ NÃO ALTERE: RESPONSIVIDADE - Adaptação para dispositivos móveis */
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
            padding: 60px 20px;
        }
        
        .hero-title {
            font-size: 36px;
        }
        
        .hero-stats {
            flex-direction: column;
            gap: 40px;
        }
        
        .features-section,
        .services-section,
        .testimonials-section,
        .cta-final-section {
            padding: 60px 20px;
        }
        
        .section-title {
            font-size: 32px;
        }
        
        .cta-final-title {
            font-size: 32px;
        }
    }
</style>
"""

# ❌ NÃO ALTERE: Injetar CSS na página
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== NAVBAR ====================
# ✅ ALTERE: Navegação superior - Mude os textos dos links e URLs
navbar_html = '''<div class="navbar">
    <a href="#" class="navbar-logo">🚀 Agência Digital</a>
    <div class="navbar-links">
        <a href="#servicos" class="navbar-link">Serviços</a>
        <a href="#sobre" class="navbar-link">Sobre</a>
        <a href="#portfolio" class="navbar-link">Portfólio</a>
        <a href="#contato" class="navbar-link">Contato</a>
        <a href="https://www.google.com/" target="_blank" class="navbar-cta">Começar Agora</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
# ✅ ALTERE: Seção principal - Mude os textos, números e URLs dos botões
hero_html = '''<div class="hero-section" id="hero">
    <div class="hero-content">
        <div class="badges-container">
            <div class="badge badge-primary"><span class="badge-icon">⭐</span> Agência Premium</div>
            <div class="badge"><span class="badge-icon">🏆</span> Prêmio Melhor Agência 2024</div>
            <div class="badge"><span class="badge-icon">✓</span> +500 Clientes Satisfeitos</div>
        </div>
        <div class="hero-title">Transforme seu negócio com <span class="hero-title-highlight">marketing digital estratégico</span></div>
        <div class="hero-subtitle">Crescimento comprovado através de estratégias personalizadas, criatividade e tecnologia de ponta</div>
        <a href="https://www.google.com/" target="_blank" class="cta-button">Agende uma consultoria gratuita</a>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-number">+500%</div>
                <div class="hero-stat-label">Crescimento Médio em Vendas</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-number">98%</div>
                <div class="hero-stat-label">Taxa de Satisfação de Clientes</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-number">12+</div>
                <div class="hero-stat-label">Anos de Experiência</div>
            </div>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== FEATURES SECTION ====================
# ✅ ALTERE: Seção de características - Mude os textos, ícones e descrições
features_html = '''<div class="features-section">
    <div class="section-header">
        <div class="section-title">Por que escolher nossa <span class="section-title-highlight">agência?</span></div>
        <div class="section-description">Oferecemos soluções completas de marketing digital que transformam visitantes em clientes</div>
    </div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Estratégia Personalizada</div>
            <div class="feature-desc">Cada negócio é único. Criamos estratégias sob medida para seus objetivos específicos.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Resultados Mensuráveis</div>
            <div class="feature-desc">Relatórios detalhados e transparentes. Você acompanha cada métrica em tempo real.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Crescimento Acelerado</div>
            <div class="feature-desc">Técnicas comprovadas para aumentar sua visibilidade e conversões rapidamente.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Inovação Constante</div>
            <div class="feature-desc">Sempre atualizados com as últimas tendências e tecnologias do mercado.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">Equipe Experiente</div>
            <div class="feature-desc">Profissionais certificados com experiência em diversos segmentos de mercado.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">Parceria de Longo Prazo</div>
            <div class="feature-desc">Não somos apenas fornecedores, somos parceiros no crescimento do seu negócio.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ==================== SERVICES SECTION ====================
# ✅ ALTERE: Seção de serviços - Mude os textos, números e descrições
services_html = '''<div class="services-section" id="servicos">
    <div class="section-header">
        <div class="section-title">Nossos <span class="section-title-highlight">Serviços</span></div>
        <div class="section-description">Soluções completas de marketing digital para impulsionar seu negócio</div>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-number">01</div>
            <div class="service-title">Google Ads</div>
            <div class="service-desc">Campanhas otimizadas para máximo ROI. Anúncios que convertem visitantes em clientes.</div>
        </div>
        <div class="service-card">
            <div class="service-number">02</div>
            <div class="service-title">Social Media</div>
            <div class="service-desc">Gestão completa de redes sociais com conteúdo estratégico e engajamento real.</div>
        </div>
        <div class="service-card">
            <div class="service-number">03</div>
            <div class="service-title">SEO Avançado</div>
            <div class="service-desc">Posicionamento orgânico no Google para tráfego qualificado e sustentável.</div>
        </div>
        <div class="service-card">
            <div class="service-number">04</div>
            <div class="service-title">Criação de Conteúdo</div>
            <div class="service-desc">Conteúdo de qualidade que atrai, engaja e converte seu público-alvo.</div>
        </div>
        <div class="service-card">
            <div class="service-number">05</div>
            <div class="service-title">Email Marketing</div>
            <div class="service-desc">Campanhas de email segmentadas com alta taxa de abertura e conversão.</div>
        </div>
        <div class="service-card">
            <div class="service-number">06</div>
            <div class="service-title">Análise e Relatórios</div>
            <div class="service-desc">Dados precisos e insights acionáveis para otimizar suas estratégias.</div>
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# ==================== TESTIMONIALS SECTION ====================
# ✅ ALTERE: Seção de depoimentos - Mude os textos, nomes e cargos
testimonials_html = '''<div class="testimonials-section" id="sobre">
    <div class="section-header">
        <div class="section-title">O que nossos <span class="section-title-highlight">clientes dizem</span></div>
        <div class="section-description">Histórias reais de sucesso e transformação digital</div>
    </div>
    <div style="max-width: 900px; margin: 0 auto;">
        <div class="testimonial-card">
            <div class="testimonial-text">"A agência transformou completamente meu negócio. Em 6 meses, triplicamos nossas vendas. Profissionais incríveis!"</div>
            <div class="testimonial-author">João Silva</div>
            <div class="testimonial-role">CEO - E-commerce Fashion</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Melhor investimento que fiz. O retorno foi imediato e os resultados continuam crescendo. Recomendo muito!"</div>
            <div class="testimonial-author">Maria Santos</div>
            <div class="testimonial-role">Proprietária - Consultoria Empresarial</div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-text">"Equipe profissional, dedicada e com resultados comprovados. Não tenho dúvidas em recomendar para qualquer negócio."</div>
            <div class="testimonial-author">Carlos Oliveira</div>
            <div class="testimonial-role">Diretor - Agência Imobiliária</div>
        </div>
    </div>
</div>'''
st.markdown(testimonials_html, unsafe_allow_html=True)

# ==================== CTA FINAL SECTION ====================
# ✅ ALTERE: Seção final de chamada para ação - Mude os textos e URLs
cta_final_html = '''<div class="cta-final-section" id="contato">
    <div class="cta-final-title">Pronto para crescer?</div>
    <div class="cta-final-desc">Agende uma consultoria gratuita com nossos especialistas e descubra como podemos transformar seu negócio</div>
    <a href="https://www.google.com/" target="_blank" class="cta-final-button">Agende Agora</a>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ==================== FOOTER ====================
# ✅ ALTERE: Rodapé - Mude as informações de contato e copyright
footer_html = '''<div class="footer" id="portfolio">
    <div class="footer-text">📞 (99) 99999-9999 | 📧 contato@agenciadigital.com.br</div>
    <div class="footer-text">📍 São Paulo, SP - Brasil</div>
    <div class="footer-copyright">© 2025 Agência Digital. Todos os direitos reservados. Transformando negócios através do marketing digital.</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)
