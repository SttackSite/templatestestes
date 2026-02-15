import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Daniel Aristizábal | Studio",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🎨",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown("""
<style>
    /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Inter:wght@900&display=swap');

    /* ❌ NÃO ALTERE: Reset geral - Define o fundo preto e texto branco */
    .stApp {
        background-color: #000000;  /* Fundo preto */
        color: #ffffff;  /* Texto branco */
    }
    
    /* ❌ NÃO ALTERE: Remove padding padrão do Streamlit para ocupar 100% da largura */
    .block-container { 
        padding: 0 !important;  /* Remove espaçamento interno */
        max-width: 100% !important;  /* Ocupa 100% da largura */
    }

    /* ❌ NÃO ALTERE: Tipografia padrão - Fonte monospace */
    html, body, [class*="css"] {
        font-family: 'JetBrains Mono', monospace;  /* Fonte monospace moderna */
    }

    /* ❌ NÃO ALTERE: Header fixo no topo */
    .header-daniel {
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        padding: 30px 40px;  /* Espaçamento interno */
        position: fixed;  /* Fica fixo ao rolar */
        width: 100%;  /* Largura total */
        top: 0;  /* Posição no topo */
        z-index: 1000;  /* Fica acima de outros elementos */
        background: rgba(0,0,0,0.8);  /* Fundo preto semi-transparente */
        backdrop-filter: blur(10px);  /* Efeito blur no fundo */
        border-bottom: 1px solid #222;  /* Linha divisória cinza escura */
        text-transform: uppercase;  /* Maiúsculas */
        font-size: 12px;  /* Tamanho pequeno */
        letter-spacing: 2px;  /* Espaçamento entre letras */
    }

    /* ❌ NÃO ALTERE: Seção hero */
    .hero-section {
        padding: 180px 40px 100px 40px;  /* Espaçamento interno */
        text-align: left;  /* Texto alinhado à esquerda */
    }
    
    /* ❌ NÃO ALTERE: Estilo do título principal */
    .hero-big-text {
        font-family: 'Inter', sans-serif;  /* Fonte sans-serif pesada */
        font-size: clamp(40px, 12vw, 160px);  /* Tamanho responsivo */
        font-weight: 900;  /* Peso muito pesado */
        line-height: 0.85;  /* Altura da linha compacta */
        letter-spacing: -0.05em;  /* Espaçamento negativo entre letras */
        margin-bottom: 40px;  /* Espaçamento inferior */
    }

    /* ❌ NÃO ALTERE: Grid de projetos */
    .grid-wrap {
        padding: 0 40px;  /* Espaçamento interno */
        display: grid;  /* Layout grid */
        grid-template-columns: repeat(12, 1fr);  /* 12 colunas */
        gap: 20px;  /* Espaçamento entre itens */
    }

    /* ❌ NÃO ALTERE: Item individual de projeto */
    .project-item {
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        margin-bottom: 40px;  /* Espaçamento inferior */
    }

    /* ❌ NÃO ALTERE: Imagem do projeto */
    .project-img {
        width: 100%;  /* Largura total */
        height: auto;  /* Altura automática */
        display: block;  /* Exibe como bloco */
        transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);  /* Animação suave */
        filter: saturate(1.2);  /* Aumenta saturação da cor */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover na imagem */
    .project-item:hover .project-img {
        transform: scale(1.03);  /* Aumenta 3% ao passar mouse */
    }

    /* ❌ NÃO ALTERE: Informações do projeto */
    .project-info {
        margin-top: 15px;  /* Espaçamento superior */
        font-size: 11px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        color: #666;  /* Cor cinza */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
    }

    /* ❌ NÃO ALTERE: Rodapé */
    .footer-daniel {
        padding: 100px 40px;  /* Espaçamento interno */
        border-top: 1px solid #222;  /* Linha divisória cinza escura */
        margin-top: 100px;  /* Espaçamento superior */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões em links */
    .action-button {
        display: inline-block !important;  /* Exibe como bloco inline */
        background-color: transparent !important;  /* Fundo transparente */
        color: #fff !important;  /* Texto branco */
        border: 1px solid #666 !important;  /* Borda cinza */
        border-radius: 0px !important;  /* Sem arredondamento */
        padding: 12px 30px !important;  /* Espaçamento interno */
        font-weight: 700 !important;  /* Peso pesado */
        font-size: 11px !important;  /* Tamanho pequeno */
        text-transform: uppercase !important;  /* Maiúsculas */
        letter-spacing: 2px !important;  /* Espaçamento entre letras */
        transition: 0.3s !important;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
        cursor: pointer !important;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
    .action-button:hover {
        background-color: #fff !important;  /* Fundo branco */
        color: #000 !important;  /* Texto preto */
        border: 1px solid #fff !important;  /* Borda branca */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Estilo para links visitados */
    .action-button:visited {
        color: #fff !important;  /* Texto branco */
        text-decoration: none !important;  /* Remove sublinhado */
    }

    /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
    [data-testid="stHeader"] { 
        display: none;  /* Oculta o header */
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
# ✅ ALTERE: Textos da navegação e nome
st.markdown("""
<div class="header-daniel">
    <!-- ✅ ALTERE: Nome do estúdio/artista -->
    <div>Daniel Aristizábal</div>
    <!-- ✅ ALTERE: Menu de navegação -->
    <div style="display: flex; gap: 40px;">
        <a href="#index" style="color: #fff; text-decoration: none; cursor: pointer;">Index</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#studio" style="color: #fff; text-decoration: none; cursor: pointer;">Studio</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#archive" style="color: #fff; text-decoration: none; cursor: pointer;">Archive</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#shop" style="color: #fff; text-decoration: none; cursor: pointer;">Shop</a>  <!-- ✅ ALTERE: Texto do menu -->
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO SECTION ==========
# ✅ ALTERE: Título, descrição e nome
st.markdown("""
<div id="index" class="hero-section">
    <!-- ✅ ALTERE: Título principal (quebrado em linhas) -->
    <div class="hero-big-text">
        DANIEL<br>ARISTI<br>ZÁBAL
    </div>
    <!-- ✅ ALTERE: Descrição do estúdio/artista -->
    <p style="max-width: 600px; font-size: 14px; color: #888; line-height: 1.6;">
        Digital Art Director and Motion Designer. Merging surrealism with CGI to explore new visual languages. 
        Based in Medellín, working globally.
    </p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 5: PROJETOS (GRID ASSIMÉTRICO) ==========
# ❌ NÃO ALTERE: Função que renderiza os projetos
def render_project(col, img_url, title, year, width="100%"):
    # ❌ NÃO ALTERE: Função que cria os cards de projeto
    with col:
        st.markdown(f"""
        <div class="project-item">
            <!-- ✅ ALTERE: URL da imagem do projeto -->
            <img src="{img_url}" class="project-img" style="width: {width};">
            <!-- ✅ ALTERE: Título e ano do projeto -->
            <div class="project-info">
                <span style="color:#fff;">{title}</span>  <!-- ✅ ALTERE: Nome do projeto -->
                <span>[{year}]</span>  <!-- ✅ ALTERE: Ano do projeto -->
            </div>
        </div>
        """, unsafe_allow_html=True)

# ❌ NÃO ALTERE: Linha 1 - Um grande e um pequeno
c1, c2 = st.columns([2, 1])
render_project(c1, "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200", "Digital Surrealism", "2024")  # ✅ ALTERE: Imagem, título e ano
render_project(c2, "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=600", "Chrome Study", "2023")  # ✅ ALTERE: Imagem, título e ano

# ❌ NÃO ALTERE: Linha 2 - Três imagens menores (estilo mosaico)
c3, c4, c5 = st.columns(3)
render_project(c3, "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=600", "Organic Forms", "2024")  # ✅ ALTERE: Imagem, título e ano
render_project(c4, "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=600", "Color Theory", "2023")  # ✅ ALTERE: Imagem, título e ano
render_project(c5, "https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=600", "Texture Flow", "2022")  # ✅ ALTERE: Imagem, título e ano

# ❌ NÃO ALTERE: Linha 3 - Um vertical e um horizontal
c6, c7 = st.columns([1, 2])
render_project(c6, "https://images.unsplash.com/photo-1574169208507-84376144848b?w=600", "CGI Sculpture", "2024")  # ✅ ALTERE: Imagem, título e ano
render_project(c7, "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=1200", "Metaverse Landscapes", "2024")  # ✅ ALTERE: Imagem, título e ano

# ========== SEÇÃO 6: SEÇÃO SOBRE (THE STUDIO) ==========
# ✅ ALTERE: Título, descrição e conteúdo
st.markdown("""
<div id="studio" style="padding: 150px 40px; background-color: #080808;">
    <!-- ✅ ALTERE: Título da seção -->
    <h2 style="font-family:'Inter'; font-size: 60px; font-weight: 900; letter-spacing: -2px;">THE STUDIO</h2>
    <!-- ✅ ALTERE: Descrição do estúdio -->
    <p style="font-size: 24px; max-width: 800px; color: #ccc; line-height: 1.2; margin-top: 30px;">
        Nós operamos na intersecção entre o design clássico e o futurismo digital. 
        Especializados em CGI, direção de arte e identidades visuais que desafiam a lógica.
    </p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 7: FOOTER (RODAPÉ) ==========
# ✅ ALTERE: Informações de contato, links e copyright
st.markdown("""
<div id="archive" class="footer-daniel">
    <!-- ❌ NÃO ALTERE: Grid de 2 colunas -->
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <!-- COLUNA 1: Redes sociais -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <p style="color: #fff; font-weight: 700;">CONNECT</p>
            <!-- ✅ ALTERE: Links de redes sociais -->
            <p style="color: #666; font-size: 14px; margin-top: 10px;">
                <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">Instagram</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">Behance</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">LinkedIn</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #666; text-decoration: none;">Vimeo</a>
            </p>
        </div>
        <!-- COLUNA 2: Contato -->
        <div style="text-align: right;">
            <!-- ✅ ALTERE: Título da coluna -->
            <p style="color: #fff; font-weight: 700;">NEW BUSINESS</p>
            <!-- ✅ ALTERE: Email de contato -->
            <p style="color: #666; font-size: 14px; margin-top: 10px;">
                <a href="mailto:studio@aristizabal.net" style="color: #666; text-decoration: none;">studio@aristizabal.net</a>
            </p>
        </div>
    </div>
    <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
    <div style="margin-top: 80px; font-size: 10px; color: #333; letter-spacing: 2px;">
        <!-- ✅ ALTERE: Texto de copyright -->
        © 2026 DANIEL ARISTIZÁBAL STUDIO — ALL RIGHTS RESERVED
    </div>
</div>
""", unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
