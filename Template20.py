import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Hugo Bazin | Digital Designer",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🕶️",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown("""
<style>
    /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;1,400&display=swap');

    /* ❌ NÃO ALTERE: Reset geral - Define o fundo cinza claro e texto preto */
    .stApp {
        background-color: #f6f6f6;  /* Fundo cinza claro */
    }

    /* ❌ NÃO ALTERE: Tipografia padrão */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;  /* Fonte moderna */
        color: #1a1a1a;  /* Texto preto */
    }

    /* ❌ NÃO ALTERE: Header minimalista */
    .header-hugo {
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        padding: 40px 5%;  /* Espaçamento interno */
        font-size: 13px;  /* Tamanho pequeno */
        font-weight: 600;  /* Peso pesado */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
    }

    /* ❌ NÃO ALTERE: Seção hero */
    .hero-container {
        padding: 100px 5% 150px 5%;  /* Espaçamento interno */
    }
    
    /* ❌ NÃO ALTERE: Estilo do título principal */
    .hero-title {
        font-size: clamp(40px, 8vw, 120px);  /* Tamanho responsivo */
        line-height: 0.9;  /* Altura da linha compacta */
        font-weight: 400;  /* Peso normal */
        letter-spacing: -2px;  /* Espaçamento negativo entre letras */
        margin-bottom: 40px;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Estilo do subtítulo */
    .hero-subtitle {
        font-family: 'Playfair Display', serif;  /* Fonte serif elegante */
        font-style: italic;  /* Itálico */
        font-size: 24px;  /* Tamanho médio */
        color: #666;  /* Cor cinza */
    }

    /* ❌ NÃO ALTERE: Linha de projetos */
    .project-row {
        margin-bottom: 120px;  /* Espaçamento inferior */
        padding: 0 5%;  /* Espaçamento interno */
    }
    
    /* ❌ NÃO ALTERE: Imagem do projeto */
    .project-image {
        width: 100%;  /* Largura total */
        height: auto;  /* Altura automática */
        border-radius: 4px;  /* Arredondamento suave */
        transition: opacity 0.4s;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover na imagem */
    .project-image:hover {
        opacity: 0.9;  /* Reduz opacidade ao passar mouse */
    }
    
    /* ❌ NÃO ALTERE: Metadados do projeto */
    .project-meta {
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        margin-top: 20px;  /* Espaçamento superior */
        border-top: 1px solid #ddd;  /* Linha divisória cinza clara */
        padding-top: 15px;  /* Espaçamento interno superior */
        font-size: 14px;  /* Tamanho pequeno */
        font-weight: 500;  /* Peso médio */
    }

    /* ❌ NÃO ALTERE: Seção about */
    .about-section {
        padding: 150px 20%;  /* Espaçamento interno */
        font-size: 28px;  /* Tamanho grande */
        line-height: 1.4;  /* Altura da linha confortável */
        text-align: left;  /* Texto alinhado à esquerda */
    }

    /* ❌ NÃO ALTERE: Rodapé */
    .footer-hugo {
        padding: 100px 5%;  /* Espaçamento interno */
        border-top: 1px solid #ddd;  /* Linha divisória cinza clara */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        font-size: 12px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        color: #999;  /* Cor cinza */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
    div.stButton > button {
        background: transparent;  /* Fundo transparente */
        border: none;  /* Sem borda */
        border-bottom: 1px solid #1a1a1a;  /* Borda inferior preta */
        color: #1a1a1a;  /* Texto preto */
        border-radius: 0;  /* Sem arredondamento */
        padding: 0;  /* Sem espaçamento */
        font-weight: 600;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões em links */
    .action-button {
        display: inline-block !important;  /* Exibe como bloco inline */
        background-color: transparent !important;  /* Fundo transparente */
        color: #1a1a1a !important;  /* Texto preto */
        border: none !important;  /* Sem borda */
        border-bottom: 1px solid #1a1a1a !important;  /* Borda inferior preta */
        border-radius: 0px !important;  /* Sem arredondamento */
        padding: 0 !important;  /* Sem espaçamento */
        font-weight: 600 !important;  /* Peso pesado */
        font-size: 14px !important;  /* Tamanho pequeno */
        text-transform: uppercase !important;  /* Maiúsculas */
        letter-spacing: 1px !important;  /* Espaçamento entre letras */
        transition: 0.3s !important;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
        cursor: pointer !important;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
    .action-button:hover {
        background-color: #1a1a1a !important;  /* Fundo preto */
        color: #f6f6f6 !important;  /* Texto cinza claro */
        border-bottom: 1px solid #1a1a1a !important;  /* Borda inferior preta */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Estilo para links visitados */
    .action-button:visited {
        color: #1a1a1a !important;  /* Texto preto */
        text-decoration: none !important;  /* Remove sublinhado */
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
# ✅ ALTERE: Textos do header
st.markdown("""
<div class="header-hugo">
    <!-- ✅ ALTERE: Nome e profissão -->
    <div>Hugo Bazin — Digital Designer</div>
    <!-- ✅ ALTERE: Localização e hora -->
    <div>Paris, FR — 14:52 PM</div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO SECTION ==========
# ✅ ALTERE: Título e subtítulo
st.markdown("""
<div class="hero-container">
    <!-- ✅ ALTERE: Título principal (quebrado em linhas) -->
    <div class="hero-title">CREATING DIGITAL<br>EXPERIENCES</div>
    <!-- ✅ ALTERE: Subtítulo/descrição -->
    <div class="hero-subtitle">Independent Designer & Art Director</div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 5: LISTA DE PROJETOS (COMPRIDA) ==========
# ❌ NÃO ALTERE: Função que renderiza os projetos
def render_project(image_url, title, year, category):
    # ❌ NÃO ALTERE: Função que cria os cards de projeto
    st.markdown(f"""
    <div class="project-row">
        <!-- ✅ ALTERE: URL da imagem do projeto -->
        <img src="{image_url}" class="project-image">
        <!-- ✅ ALTERE: Título, categoria e ano do projeto -->
        <div class="project-meta">
            <div>{title}</div>  <!-- ✅ ALTERE: Nome do projeto -->
            <div style="color: #999;">{category} — {year}</div>  <!-- ✅ ALTERE: Tipo e ano -->
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ ALTERE: Projeto 1 - Imagem, título, ano e categoria
render_project(
    "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=1500&q=80",
    "L'Art de Vivre",  # ✅ ALTERE: Nome do projeto
    "2024",  # ✅ ALTERE: Ano
    "Visual Identity"  # ✅ ALTERE: Categoria
)

# ✅ ALTERE: Projeto 2 - Imagem, título, ano e categoria
render_project(
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1500&q=80",
    "Techno Frontier",  # ✅ ALTERE: Nome do projeto
    "2023",  # ✅ ALTERE: Ano
    "Product Design"  # ✅ ALTERE: Categoria
)

# ✅ ALTERE: Projeto 3 - Imagem, título, ano e categoria
render_project(
    "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=1500&q=80",
    "Minimal Workspace",  # ✅ ALTERE: Nome do projeto
    "2023",  # ✅ ALTERE: Ano
    "CGI & Motion"  # ✅ ALTERE: Categoria
)

# ✅ ALTERE: Projeto 4 - Imagem, título, ano e categoria
render_project(
    "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1500&q=80",
    "Essential Watch",  # ✅ ALTERE: Nome do projeto
    "2022",  # ✅ ALTERE: Ano
    "E-commerce"  # ✅ ALTERE: Categoria
)

# ========== SEÇÃO 6: ABOUT SECTION ==========
# ✅ ALTERE: Descrição/filosofia do designer
st.markdown("""
<div class="about-section">
    <!-- ✅ ALTERE: Texto sobre o designer -->
    Eu ajudo marcas a traduzirem sua essência em produtos digitais que as pessoas amam usar. Focado em simplicidade, estética e performance.
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 7: CONTATO / LINKS ==========
# ✅ ALTERE: Botões de contato e URLs
st.markdown('<div style="padding: 0 5% 100px 5%;">', unsafe_allow_html=True)

# ❌ NÃO ALTERE: Estrutura de 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="mailto:hello@hugobazin.com" class="action-button">EMAIL ME</a>', unsafe_allow_html=True)

with col2:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">LINKEDIN</a>', unsafe_allow_html=True)

with col3:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">DRIBBBLE</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
# ✅ ALTERE: Informações do footer e copyright
st.markdown("""
<div class="footer-hugo">
    <!-- ✅ ALTERE: Copyright -->
    <div>© 2026 Hugo Bazin</div>
    <!-- ✅ ALTERE: Descrição -->
    <div>Design & Development</div>
    <!-- ✅ ALTERE: Link de voltar ao topo -->
    <div><a href="#" style="color: #999; text-decoration: none;">Back to Top ↑</a></div>
</div>
""", unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
