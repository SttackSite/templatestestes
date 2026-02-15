import streamlit as st

# ❌ NÃO ALTERE: Importações necessárias para o funcionamento do Streamlit
# Estas linhas carregam as bibliotecas essenciais para a aplicação rodar

# ✅ ALTERE: Configuração da Página (Título, Ícone, Layout)
# Você pode mudar o "page_title" para o nome do seu projeto
# Você pode mudar o "page_icon" para o emoji que preferir
st.set_page_config(
    page_title="PAIX | Estúdio de Design e Arquitetura",  # ✅ ALTERE: Nome da página (aparece na aba do navegador)
    page_icon="🏛️",  # ✅ ALTERE: Emoji do ícone
    layout="wide"  # ❌ NÃO ALTERE: Define o layout da página como largura total
)

# ❌ NÃO ALTERE: Bloco de CSS (Estilos Visuais)
# Este bloco define todas as cores, fontes, animações e efeitos visuais da página
# Alterar aqui pode quebrar completamente o design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');

    .stApp {
        background-color: #f7f7f7;  /* ✅ ALTERE: Cor de fundo (tom de pedra suave) */
        color: #1a1a1a;  /* ✅ ALTERE: Cor do texto principal */
    }
    
    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-weight: 200;
        letter-spacing: 0.05em;
    }

    h1, h2, .serif-light {
        font-family: 'Cormorant Garamond', serif;
        font-weight: 300;
        font-size: 48px;
        line-height: 1.1;
    }

    .nav-paix {
        display: flex;
        justify-content: space-between;
        padding: 50px 5%;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    .nav-link {
        color: #1a1a1a !important;
        text-decoration: none !important;
        transition: 0.3s;
        cursor: pointer;
    }

    .nav-link:hover {
        opacity: 0.6;
        text-decoration: none !important;
    }

    .nav-link:visited {
        color: #1a1a1a !important;
        text-decoration: none !important;
    }

    .hero-paix {
        padding: 100px 5% 150px 5%;
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 100px;
    }

    .project-section {
        padding: 0 5% 200px 5%;
    }

    .project-card {
        margin-bottom: 250px;
        transition: opacity 0.6s ease;
    }
    
    .project-img {
        width: 100%;
        filter: grayscale(10%) contrast(1.05);
        margin-bottom: 25px;
    }

    .project-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 32px;
        border-bottom: 1px solid #ddd;
        padding-bottom: 15px;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .project-year {
        font-size: 10px;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
        color: #888;
    }

    .action-button {
        display: inline-block !important;
        background: #1a1a1a !important;
        color: #f7f7f7 !important;
        border: none !important;
        padding: 12px 30px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 400 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        text-decoration: none !important;
        font-size: 10px !important;
        transition: 0.3s !important;
        cursor: pointer !important;
    }

    .action-button:hover {
        background-color: #333 !important;
        color: #f7f7f7 !important;
        text-decoration: none !important;
    }

    .action-button:visited {
        color: #f7f7f7 !important;
        text-decoration: none !important;
    }

    .footer-paix {
        padding: 100px 5%;
        border-top: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        font-size: 10px;
        letter-spacing: 2px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 1: NAVEGAÇÃO ==========
# ❌ NÃO ALTERE: Estrutura de navegação
st.markdown("""
<div class="nav-paix">
    <div style="font-weight: 400;">PAIX DESIGN</div>
    <div style="display: flex; gap: 50px;">
        <a href="#projetos" class="nav-link">Projetos</a>
        <a href="#escritorio" class="nav-link">Escritório</a>
        <a href="#contato" class="nav-link">Contato</a>
    </div>
</div>
""", unsafe_allow_html=True)  # ✅ ALTERE: Logo e textos de navegação

# ========== SEÇÃO 2: HERO SECTION ==========
# ✅ ALTERE: Conteúdo principal do hero
st.markdown("""
<div class="hero-paix">
    <div>
        <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #888; margin-bottom: 30px;">
            Arquitetura & Design de Interiores
        </p>
        <h1 class="serif-light">
            A beleza reside na <br>
            intenção e na calma.
        </h1>
    </div>
    <div style="font-size: 16px; line-height: 1.8; padding-top: 10px; color: #555;">
        PAIX é um estúdio de design focado na criação de espaços que transcendem o tempo. 
        Nossa abordagem é guiada pela pureza dos materiais e pela harmonia entre a luz natural e a forma construída.
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: PROJETOS ==========
# ❌ NÃO ALTERE: Função que renderiza os projetos
def render_paix_project(title, location, year, img_url, alignment="left"):
    # ❌ NÃO ALTERE: Função que renderiza um projeto
    st.markdown(f"""
    <div id="projetos" class="project-section">
        <div class="project-card">
            <img src="{img_url}" class="project-img">
            <div class="project-title">
                <span>{title} — {location}</span>
                <span class="project-year">{year}</span>
            </div>
            <p style="font-size: 12px; color: #999; text-transform: uppercase; letter-spacing: 1px;">
                Residencial / Design de Mobiliário
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ ALTERE: Títulos, localizações, anos e URLs das imagens dos projetos
render_paix_project(
    "Casa Minimalista", 
    "Sintra", 
    "2024", 
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600"
)

render_paix_project(
    "Apartamento Galeria", 
    "Porto", 
    "2023", 
    "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600"
)

# ========== SEÇÃO 4: SEÇÃO SOBRE (TRANSICIONAL) ==========
# ✅ ALTERE: Conteúdo da seção sobre
st.markdown("""
<div id="escritorio" style="padding: 150px 20% 250px 20%; text-align: center;">
    <h2 class="serif-light" style="font-size: 56px; margin-bottom: 40px;">Atmosferas Tangíveis</h2>
    <p style="color: #666; line-height: 2;">
        Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, 
        desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente.
    </p>
    <div style="margin-top: 60px;">
        <a href="https://www.google.com/" target="_blank" class="action-button">Conheça Nosso Trabalho</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 5: FOOTER ==========
# ✅ ALTERE: Informações do rodapé
st.markdown("""
<div id="contato" class="footer-paix">
    <div>
        PAIX DESIGN STUDIO<br>
        AVENIDA DA LIBERDADE, LISBOA
    </div>
    <div style="text-align: right;">
        <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">INSTAGRAM</a> / 
        <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">BEHANCE</a> / 
        <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">LINKEDIN</a><br>
        <a href="mailto:hello@paix-design.com" style="color: #666; text-decoration: none;">HELLO@PAIX-DESIGN.COM</a>
    </div>
</div>
<div style="padding: 30px 5%; font-size: 9px; color: #bbb; letter-spacing: 1px;">
    © 2026 PAIX DESIGN. TODOS OS DIREITOS RESERVADOS.
</div>
""", unsafe_allow_html=True)  # ✅ ALTERE: Nome da empresa, endereço, redes sociais e email

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
