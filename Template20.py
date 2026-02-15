import streamlit as st

# ❌ NÃO ALTERE: Importações necessárias para o funcionamento do Streamlit
# Estas linhas carregam as bibliotecas essenciais para a aplicação rodar

# ✅ ALTERE: Configuração da Página (Título, Ícone, Layout)
# Você pode mudar o "page_title" para o nome do seu projeto
# Você pode mudar o "page_icon" para o emoji que preferir
st.set_page_config(
    page_title="Plunder & Poach | Estratégia e Design",  # ✅ ALTERE: Nome da página (aparece na aba do navegador)
    page_icon="⚓",  # ✅ ALTERE: Emoji do ícone
    layout="wide"  # ❌ NÃO ALTERE: Define o layout da página como largura total
)

# ❌ NÃO ALTERE: Bloco de CSS (Estilos Visuais)
# Este bloco define todas as cores, fontes, animações e efeitos visuais da página
# Alterar aqui pode quebrar completamente o design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Inter:wght@400;700&display=swap');

    .stApp {
        background-color: #f4f1ea;  /* ✅ ALTERE: Cor de fundo (papel/creme) */
        color: #1a1a1a;  /* ✅ ALTERE: Cor do texto principal */
    }

    [data-testid="stHeader"] { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, .serif-poach {
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: -1px;
    }

    .divider {
        border-top: 1px solid #1a1a1a;
        border-bottom: 4px solid #1a1a1a;
        height: 8px;
        margin: 40px 0;
    }

    .nav-pp {
        display: flex;
        justify-content: space-between;
        padding: 40px 6%;
        border-bottom: 1px solid #1a1a1a;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
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

    .hero-pp {
        padding: 100px 6% 80px 6%;
        text-align: center;
    }
    
    .hero-title {
        font-size: clamp(50px, 10vw, 130px);
        line-height: 0.9;
        margin-bottom: 30px;
    }

    .project-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        border-top: 1px solid #1a1a1a;
    }
    
    .project-item {
        border-right: 1px solid #1a1a1a;
        border-bottom: 1px solid #1a1a1a;
        padding: 60px;
        transition: background-color 0.4s ease;
    }
    
    .project-item:nth-child(even) { border-right: none; }
    .project-item:hover { background-color: #ede9e0; }

    .project-img {
        width: 100%;
        filter: sepia(0.2) contrast(1.1);
        margin-bottom: 30px;
    }

    div.stButton > button {
        background-color: #1a1a1a;
        color: #f4f1ea;
        border: none;
        border-radius: 0px;
        padding: 15px 40px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #333;
        color: #f4f1ea;
    }

    .action-button {
        display: inline-block !important;
        background: #1a1a1a !important;
        color: #f4f1ea !important;
        border: none !important;
        padding: 15px 40px !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        text-decoration: none !important;
        transition: 0.3s !important;
        cursor: pointer !important;
    }

    .action-button:hover {
        background-color: #333 !important;
        color: #f4f1ea !important;
        text-decoration: none !important;
    }

    .action-button:visited {
        color: #f4f1ea !important;
        text-decoration: none !important;
    }

    .footer-pp {
        padding: 100px 6%;
        background-color: #1a1a1a;
        color: #f4f1ea;
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 1: NAVEGAÇÃO ==========
# ❌ NÃO ALTERE: Estrutura de navegação
st.markdown("""
<div class="nav-pp">
    <div>Plunder & Poach</div>
    <div style="display: flex; gap: 40px;">
        <a href="#trabalhos" class="nav-link">Trabalhos</a>
        <a href="#estudio" class="nav-link">Estúdio</a>
        <a href="#contato" class="nav-link">Contato</a>
    </div>
</div>
""", unsafe_allow_html=True)  # ✅ ALTERE: Logo e textos de navegação

# ========== SEÇÃO 2: HERO ==========
# ✅ ALTERE: Conteúdo principal do hero
st.markdown("""
<div class="hero-pp">
    <p style="text-transform: uppercase; letter-spacing: 4px; font-size: 12px; margin-bottom: 20px;">Estratégia · Design · Rebeldia</p>
    <h1 class="hero-title">SAQUEAMOS<br>O COMUM.</h1>
    <div class="divider" style="max-width: 300px; margin: 40px auto;"></div>
    <p style="max-width: 700px; margin: 0 auto; font-size: 18px; line-height: 1.6;">
        Somos uma agência de criação para marcas que não têm medo de quebrar as regras. 
        Transformamos negócios em lendas através de um design audacioso e narrativas implacáveis.
    </p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: SHOWCASE (GRID ASSIMÉTRICO) ==========
# ❌ NÃO ALTERE: Estrutura de grid
st.markdown('<div id="trabalhos" class="project-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1527067829737-402993088e6b?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Ouro Negro</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">IDENTIDADE VISUAL / CAFÉ</p>
        <p>Uma marca construída sobre a herança e o sabor intenso.</p>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título, categoria, descrição e imagem do projeto 1
    
    st.markdown("""
    <div class="project-item" style="border-bottom: none;">
        <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Bússola Norte</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">ESTRATÉGIA DIGITAL / 2024</p>
        <p>Guiando marcas em mares nunca navegados.</p>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título, categoria, descrição e imagem do projeto 2

with col2:
    st.markdown("""
    <div class="project-item">
        <img src="https://images.unsplash.com/photo-1560067174-c5a3a8f37060?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Alcateia Alpha</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">DIREÇÃO DE ARTE / MODA</p>
        <p>O instinto selvagem traduzido em alfaiataria premium.</p>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título, categoria, descrição e imagem do projeto 3
    
    st.markdown("""
    <div class="project-item" style="border-bottom: none;">
        <img src="https://images.unsplash.com/photo-1520004434532-668416a08753?w=800" class="project-img">
        <h3 class="serif-poach" style="font-size: 32px;">Armazém V</h3>
        <p style="color: #666; font-size: 14px; margin-bottom: 20px;">BRANDING / ARQUITETURA</p>
        <p>Espaços que respiram história e design industrial.</p>
    </div>
    """, unsafe_allow_html=True)  # ✅ ALTERE: Título, categoria, descrição e imagem do projeto 4

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 4: MANIFESTO (SEÇÃO ESCURA) ==========
# ✅ ALTERE: Conteúdo do manifesto
st.markdown("""
<div id="estudio" style="background-color: #1a1a1a; color: #f4f1ea; padding: 150px 6%; text-align: center;">
    <h2 class="serif-poach" style="font-size: 50px; margin-bottom: 40px;">VOCÊ É A PRESA OU O PREDADOR?</h2>
    <p style="max-width: 800px; margin: 0 auto; font-size: 22px; font-style: italic; opacity: 0.8;">
        "No mercado moderno, a neutralidade é o caminho mais rápido para a extinção. 
        Nós ajudamos você a afiar as garras e dominar seu território."
    </p>
    <div style="margin-top: 60px;">
        <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin-bottom: 20px;">Pronto para o ataque?</p>
        <a href="https://www.google.com/" target="_blank" class="action-button">Inicie sua Jornada</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 5: FOOTER ==========
# ✅ ALTERE: Informações do rodapé
st.markdown("""
<div id="contato" class="footer-pp">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
        <div>
            <h2 class="serif-poach" style="font-size: 28px;">Plunder & Poach.</h2>
            <p style="opacity: 0.6; font-size: 13px;">Capturando a essência do extraordinário.</p>
        </div>
        <div style="text-align: right; line-height: 2;">
            <p style="font-weight: 700;">CONTATO</p>
            <p style="opacity: 0.6;">
                <a href="mailto:studio@plunderpoach.com" style="color: #f4f1ea; text-decoration: none;">studio@plunderpoach.com</a><br>
                Londres / Global
            </p>
        </div>
    </div>
    <div style="margin-top: 80px; padding-top: 20px; border-top: 1px solid rgba(244, 241, 234, 0.1); font-size: 10px; opacity: 0.4;">
        © 2026 PLUNDER & POACH — TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)  # ✅ ALTERE: Nome da empresa, descrição, email e localização

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
