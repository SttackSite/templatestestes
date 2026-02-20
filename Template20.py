import streamlit as st
import json
from datetime import datetime
import base64

# ========== CONFIGURAÇÃO ==========
st.set_page_config(
    page_title="Editor Visual - Template 1",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========== INICIALIZAR SESSION STATE ==========
if 'selected_element' not in st.session_state:
    st.session_state.selected_element = None

if 'customizations' not in st.session_state:
    st.session_state.customizations = {
        'navbar_logo': '🚀 AGÊNCIA',
        'navbar_link1': 'Serviços',
        'navbar_link2': 'Sobre',
        'navbar_link3': 'Contato',
        'navbar_cta_text': 'Começar',
        'navbar_cta_url': 'https://www.google.com/',
        
        'hero_badge1': '✨ Novo',
        'hero_badge2': 'Transformação Digital',
        'hero_badge3': '⭐ Top Rated',
        
        'hero_title': 'Transforme seu Negócio com ',
        'hero_title_highlight': 'Estratégia Digital',
        'hero_subtitle': 'Soluções completas de marketing digital que aumentam suas vendas e presença online',
        
        'hero_cta1_text': 'Solicitar Consultoria',
        'hero_cta1_url': 'https://www.google.com/',
        'hero_cta2_text': 'Ver Portfólio',
        'hero_cta2_url': 'https://www.google.com/',
        
        'hero_stat1_number': '500+',
        'hero_stat1_label': 'Clientes Satisfeitos',
        'hero_stat2_number': '1.2M+',
        'hero_stat2_label': 'Em Vendas Geradas',
        'hero_stat3_number': '98%',
        'hero_stat3_label': 'Taxa de Satisfação',
        
        'features_title': 'Nossos Serviços',
        'features_subtitle': 'Tudo que você precisa para crescer digitalmente',
        
        'feature1_icon': '📱',
        'feature1_title': 'Design Web',
        'feature1_desc': 'Websites modernos e responsivos que convertem visitantes em clientes',
        
        'feature2_icon': '📊',
        'feature2_title': 'Marketing Digital',
        'feature2_desc': 'Estratégias de SEO, SEM e redes sociais que geram resultados',
        
        'feature3_icon': '🎨',
        'feature3_title': 'Branding',
        'feature3_desc': 'Identidade visual completa que diferencia sua marca',
        
        'feature4_icon': '💻',
        'feature4_title': 'Desenvolvimento',
        'feature4_desc': 'Aplicações web e mobile com tecnologia de ponta',
        
        'feature5_icon': '📈',
        'feature5_title': 'Analytics',
        'feature5_desc': 'Dados e insights para otimizar seus resultados',
        
        'feature6_icon': '🤝',
        'feature6_title': 'Consultoria',
        'feature6_desc': 'Orientação estratégica para o crescimento do seu negócio',
        
        'cta_title': 'Pronto para Transformar seu Negócio?',
        'cta_subtitle': 'Entre em contato conosco e descubra como podemos ajudar',
        'cta_button_text': 'Agendar Reunião',
        'cta_button_url': 'https://www.google.com/',
        
        'footer_text': '© 2024 Agência Digital. Todos os direitos reservados.',
        
        'user_email': '',
        'user_url': '',
    }

# ========== ELEMENTOS EDITÁVEIS ==========
EDITABLE_ELEMENTS = {
    'navbar_logo': {
        'name': 'Logo da Navbar',
        'type': 'text',
        'section': 'Navbar',
        'description': 'Logo/nome que aparece no topo'
    },
    'navbar_link1': {
        'name': 'Link 1 da Navbar',
        'type': 'text',
        'section': 'Navbar',
        'description': 'Primeiro link de navegação'
    },
    'navbar_link2': {
        'name': 'Link 2 da Navbar',
        'type': 'text',
        'section': 'Navbar',
        'description': 'Segundo link de navegação'
    },
    'navbar_link3': {
        'name': 'Link 3 da Navbar',
        'type': 'text',
        'section': 'Navbar',
        'description': 'Terceiro link de navegação'
    },
    'navbar_cta_text': {
        'name': 'Botão CTA da Navbar',
        'type': 'text',
        'section': 'Navbar',
        'description': 'Texto do botão de ação'
    },
    'navbar_cta_url': {
        'name': 'URL do Botão CTA',
        'type': 'url',
        'section': 'Navbar',
        'description': 'URL para onde o botão leva'
    },
    
    'hero_badge1': {
        'name': 'Badge 1',
        'type': 'text',
        'section': 'Hero',
        'description': 'Primeiro rótulo de destaque'
    },
    'hero_badge2': {
        'name': 'Badge 2',
        'type': 'text',
        'section': 'Hero',
        'description': 'Segundo rótulo de destaque'
    },
    'hero_badge3': {
        'name': 'Badge 3',
        'type': 'text',
        'section': 'Hero',
        'description': 'Terceiro rótulo de destaque'
    },
    
    'hero_title': {
        'name': 'Título Principal',
        'type': 'text',
        'section': 'Hero',
        'description': 'Título principal do hero'
    },
    'hero_title_highlight': {
        'name': 'Parte Destacada do Título',
        'type': 'text',
        'section': 'Hero',
        'description': 'Parte em azul do título'
    },
    'hero_subtitle': {
        'name': 'Subtítulo',
        'type': 'textarea',
        'section': 'Hero',
        'description': 'Descrição abaixo do título'
    },
    
    'hero_cta1_text': {
        'name': 'Botão CTA 1',
        'type': 'text',
        'section': 'Hero',
        'description': 'Texto do primeiro botão'
    },
    'hero_cta1_url': {
        'name': 'URL do Botão CTA 1',
        'type': 'url',
        'section': 'Hero',
        'description': 'URL do primeiro botão'
    },
    'hero_cta2_text': {
        'name': 'Botão CTA 2',
        'type': 'text',
        'section': 'Hero',
        'description': 'Texto do segundo botão'
    },
    'hero_cta2_url': {
        'name': 'URL do Botão CTA 2',
        'type': 'url',
        'section': 'Hero',
        'description': 'URL do segundo botão'
    },
    
    'hero_stat1_number': {
        'name': 'Estatística 1 - Número',
        'type': 'text',
        'section': 'Hero',
        'description': 'Número da primeira estatística'
    },
    'hero_stat1_label': {
        'name': 'Estatística 1 - Label',
        'type': 'text',
        'section': 'Hero',
        'description': 'Descrição da primeira estatística'
    },
    'hero_stat2_number': {
        'name': 'Estatística 2 - Número',
        'type': 'text',
        'section': 'Hero',
        'description': 'Número da segunda estatística'
    },
    'hero_stat2_label': {
        'name': 'Estatística 2 - Label',
        'type': 'text',
        'section': 'Hero',
        'description': 'Descrição da segunda estatística'
    },
    'hero_stat3_number': {
        'name': 'Estatística 3 - Número',
        'type': 'text',
        'section': 'Hero',
        'description': 'Número da terceira estatística'
    },
    'hero_stat3_label': {
        'name': 'Estatística 3 - Label',
        'type': 'text',
        'section': 'Hero',
        'description': 'Descrição da terceira estatística'
    },
    
    'features_title': {
        'name': 'Título da Seção',
        'type': 'text',
        'section': 'Serviços',
        'description': 'Título da seção de serviços'
    },
    'features_subtitle': {
        'name': 'Subtítulo da Seção',
        'type': 'text',
        'section': 'Serviços',
        'description': 'Subtítulo da seção de serviços'
    },
    
    'feature1_icon': {'name': 'Ícone 1', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature1_title': {'name': 'Título 1', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature1_desc': {'name': 'Descrição 1', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'feature2_icon': {'name': 'Ícone 2', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature2_title': {'name': 'Título 2', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature2_desc': {'name': 'Descrição 2', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'feature3_icon': {'name': 'Ícone 3', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature3_title': {'name': 'Título 3', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature3_desc': {'name': 'Descrição 3', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'feature4_icon': {'name': 'Ícone 4', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature4_title': {'name': 'Título 4', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature4_desc': {'name': 'Descrição 4', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'feature5_icon': {'name': 'Ícone 5', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature5_title': {'name': 'Título 5', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature5_desc': {'name': 'Descrição 5', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'feature6_icon': {'name': 'Ícone 6', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature6_title': {'name': 'Título 6', 'type': 'text', 'section': 'Serviços', 'description': ''},
    'feature6_desc': {'name': 'Descrição 6', 'type': 'textarea', 'section': 'Serviços', 'description': ''},
    
    'cta_title': {
        'name': 'Título CTA',
        'type': 'text',
        'section': 'CTA',
        'description': 'Título da seção de chamada para ação'
    },
    'cta_subtitle': {
        'name': 'Subtítulo CTA',
        'type': 'textarea',
        'section': 'CTA',
        'description': 'Subtítulo da seção CTA'
    },
    'cta_button_text': {
        'name': 'Botão CTA',
        'type': 'text',
        'section': 'CTA',
        'description': 'Texto do botão CTA'
    },
    'cta_button_url': {
        'name': 'URL do Botão CTA',
        'type': 'url',
        'section': 'CTA',
        'description': 'URL do botão CTA'
    },
    
    'footer_text': {
        'name': 'Texto do Rodapé',
        'type': 'textarea',
        'section': 'Rodapé',
        'description': 'Texto que aparece no rodapé'
    },
    
    'user_email': {
        'name': 'Seu Email',
        'type': 'email',
        'section': 'Identificação',
        'description': 'Email para identificação'
    },
    'user_url': {
        'name': 'URL do Seu Site',
        'type': 'text',
        'section': 'Identificação',
        'description': 'URL customizada (https://[TEXTO].streamlit.app)'
    },
}

# ========== CSS DO TEMPLATE ==========
TEMPLATE_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(180deg, #f8f9ff 0%, #f0f4ff 50%, #f8f9ff 100%);
        background-attachment: fixed;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: #1a1a1a;
        line-height: 1.6;
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
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .navbar-logo:hover {
        background: rgba(0, 102, 255, 0.1);
    }
    
    .navbar-links {
        display: flex;
        gap: 50px;
        align-items: center;
    }
    
    .navbar-link {
        color: #1a1a1a;
        text-decoration: none;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.3s ease;
        position: relative;
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 4px;
    }
    
    .navbar-link:hover {
        background: rgba(0, 102, 255, 0.1);
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
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
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
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .badge:hover {
        background: rgba(0, 102, 255, 0.1);
    }
    
    .hero-title {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 24px;
        color: #1a1a1a;
        letter-spacing: -1px;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .hero-title:hover {
        background: rgba(0, 102, 255, 0.1);
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
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .hero-subtitle:hover {
        background: rgba(0, 102, 255, 0.1);
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
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .hero-stat:hover {
        background: rgba(0, 102, 255, 0.1);
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
    
    .cta-buttons {
        margin-top: 50px;
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
        margin-bottom: 20px;
        color: #1a1a1a;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .section-title:hover {
        background: rgba(0, 102, 255, 0.1);
    }
    
    .section-subtitle {
        font-size: 20px;
        color: #666666;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .section-subtitle:hover {
        background: rgba(0, 102, 255, 0.1);
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 12px;
        border: 1px solid rgba(0, 102, 255, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 102, 255, 0.15);
        border-color: rgba(0, 102, 255, 0.2);
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
    
    .feature-desc {
        font-size: 15px;
        color: #666666;
        line-height: 1.6;
    }
    
    .cta-section {
        padding: 100px 60px;
        background: linear-gradient(135deg, #0066FF, #0052CC);
        color: white;
        text-align: center;
    }
    
    .cta-section-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 20px;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .cta-section-title:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .cta-section-subtitle {
        font-size: 20px;
        margin-bottom: 40px;
        cursor: pointer;
        padding: 8px;
        border-radius: 4px;
        transition: background 0.2s;
    }
    
    .cta-section-subtitle:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    
    .cta-button-white {
        background: white;
        color: #0066FF !important;
        padding: 16px 48px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 16px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-block;
    }
    
    .cta-button-white:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    
    .footer {
        background: #1a1a1a;
        color: white;
        padding: 40px 60px;
        text-align: center;
        font-size: 14px;
        cursor: pointer;
        transition: background 0.2s;
    }
    
    .footer:hover {
        background: #2a2a2a;
    }
    
    .editable {
        border: 2px dashed rgba(0, 102, 255, 0.3);
        border-radius: 4px;
        padding: 4px;
    }
    
    .editable:hover {
        border-color: rgba(0, 102, 255, 0.8);
        background: rgba(0, 102, 255, 0.05);
    }
</style>
"""

# ========== RENDERIZAR PREVIEW ==========
def render_preview():
    preview_html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Preview</title>
        {TEMPLATE_CSS}
    </head>
    <body>
        <div class="navbar">
            <div class="navbar-logo">{st.session_state.customizations['navbar_logo']}</div>
            <div class="navbar-links">
                <a href="#" class="navbar-link">{st.session_state.customizations['navbar_link1']}</a>
                <a href="#" class="navbar-link">{st.session_state.customizations['navbar_link2']}</a>
                <a href="#" class="navbar-link">{st.session_state.customizations['navbar_link3']}</a>
                <a href="{st.session_state.customizations['navbar_cta_url']}" class="navbar-cta">{st.session_state.customizations['navbar_cta_text']}</a>
            </div>
        </div>
        
        <div class="hero-section">
            <div class="hero-content">
                <div class="badges-container">
                    <span class="badge">{st.session_state.customizations['hero_badge1']}</span>
                    <span class="badge">{st.session_state.customizations['hero_badge2']}</span>
                    <span class="badge">{st.session_state.customizations['hero_badge3']}</span>
                </div>
                
                <h1 class="hero-title">
                    {st.session_state.customizations['hero_title']}
                    <span class="hero-title-highlight">{st.session_state.customizations['hero_title_highlight']}</span>
                </h1>
                
                <p class="hero-subtitle">{st.session_state.customizations['hero_subtitle']}</p>
                
                <div class="cta-buttons">
                    <a href="{st.session_state.customizations['hero_cta1_url']}" class="cta-button">{st.session_state.customizations['hero_cta1_text']}</a>
                    <a href="{st.session_state.customizations['hero_cta2_url']}" class="cta-button cta-button-secondary">{st.session_state.customizations['hero_cta2_text']}</a>
                </div>
                
                <div class="hero-stats">
                    <div class="hero-stat">
                        <div class="hero-stat-number">{st.session_state.customizations['hero_stat1_number']}</div>
                        <div class="hero-stat-label">{st.session_state.customizations['hero_stat1_label']}</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-number">{st.session_state.customizations['hero_stat2_number']}</div>
                        <div class="hero-stat-label">{st.session_state.customizations['hero_stat2_label']}</div>
                    </div>
                    <div class="hero-stat">
                        <div class="hero-stat-number">{st.session_state.customizations['hero_stat3_number']}</div>
                        <div class="hero-stat-label">{st.session_state.customizations['hero_stat3_label']}</div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="features-section">
            <div class="section-header">
                <h2 class="section-title">{st.session_state.customizations['features_title']}</h2>
                <p class="section-subtitle">{st.session_state.customizations['features_subtitle']}</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature1_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature1_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature1_desc']}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature2_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature2_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature2_desc']}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature3_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature3_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature3_desc']}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature4_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature4_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature4_desc']}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature5_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature5_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature5_desc']}</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">{st.session_state.customizations['feature6_icon']}</div>
                    <h3 class="feature-title">{st.session_state.customizations['feature6_title']}</h3>
                    <p class="feature-desc">{st.session_state.customizations['feature6_desc']}</p>
                </div>
            </div>
        </div>
        
        <div class="cta-section">
            <h2 class="cta-section-title">{st.session_state.customizations['cta_title']}</h2>
            <p class="cta-section-subtitle">{st.session_state.customizations['cta_subtitle']}</p>
            <a href="{st.session_state.customizations['cta_button_url']}" class="cta-button-white">{st.session_state.customizations['cta_button_text']}</a>
        </div>
        
        <div class="footer">
            <p>{st.session_state.customizations['footer_text']}</p>
        </div>
    </body>
    </html>
    """
    
    b64 = base64.b64encode(preview_html.encode()).decode()
    iframe_html = f'<iframe src="data:text/html;base64,{b64}" width="100%" height="2500" frameborder="0" style="border: none; border-radius: 8px;"></iframe>'
    st.markdown(iframe_html, unsafe_allow_html=True)

# ========== INTERFACE ==========
st.markdown("# ✏️ Editor Visual - Template 1: Agência Digital")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 🎨 Customize os Campos")
    
    # Agrupar por seção
    sections = {}
    for key, info in EDITABLE_ELEMENTS.items():
        section = info['section']
        if section not in sections:
            sections[section] = []
        sections[section].append(key)
    
    # Renderizar campos por seção
    for section in sorted(sections.keys()):
        with st.expander(f"📝 {section}", expanded=(section == "Identificação")):
            for field_key in sections[section]:
                field_info = EDITABLE_ELEMENTS[field_key]
                field_type = field_info['type']
                field_name = field_info['name']
                
                if field_type == 'text':
                    st.session_state.customizations[field_key] = st.text_input(
                        field_name,
                        value=st.session_state.customizations[field_key]
                    )
                elif field_type == 'textarea':
                    st.session_state.customizations[field_key] = st.text_area(
                        field_name,
                        value=st.session_state.customizations[field_key],
                        height=80
                    )
                elif field_type == 'url':
                    st.session_state.customizations[field_key] = st.text_input(
                        field_name,
                        value=st.session_state.customizations[field_key]
                    )
                elif field_type == 'email':
                    st.session_state.customizations[field_key] = st.text_input(
                        field_name,
                        value=st.session_state.customizations[field_key],
                        placeholder="seu@email.com"
                    )

with col2:
    st.markdown("## 👁️ Preview em Tempo Real")
    render_preview()

# ========== DOWNLOAD JSON ==========
st.markdown("---")
st.markdown("## 📥 Baixar Customizações")

json_data = {
    'template_id': 1,
    'template_name': 'Agência Digital',
    'user_email': st.session_state.customizations['user_email'],
    'user_url': f"https://{st.session_state.customizations['user_url']}.streamlit.app" if st.session_state.customizations['user_url'] else '',
    'created_at': datetime.now().isoformat(),
    'customizations': {k: v for k, v in st.session_state.customizations.items() if k not in ['user_email', 'user_url']}
}

json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

st.download_button(
    label="📥 Baixar JSON",
    data=json_str,
    file_name=f"template_1_customizations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
    mime="application/json"
)

st.info("""
📧 **Próximos Passos:**
1. Customize todos os campos que desejar
2. Clique em "Baixar JSON"
3. Envie o arquivo para: **sttacksite@gmail.com**
4. Você receberá um email de confirmação
5. Nós faremos as edições manualmente no seu template!
""")
