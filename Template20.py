import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Moooi | A Life Extraordinary",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="✨",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown("""
<style>
    /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500&family=Inter:wght@200;300;400&display=swap');

    /* ❌ NÃO ALTERE: Reset geral - Define o fundo branco e texto preto */
    .stApp {
        background-color: #ffffff;  /* Cor de fundo branca */
        color: #000000;  /* Cor do texto preta */
    }
    
    /* ❌ NÃO ALTERE: Remove padding padrão do Streamlit para ocupar 100% da largura */
    .block-container { 
        padding: 0 !important;  /* Remove espaçamento interno */
        max-width: 100% !important;  /* Ocupa 100% da largura */
    }

    /* ❌ NÃO ALTERE: Tipografia padrão - Fonte leve e elegante */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;  /* Fonte padrão moderna */
        font-weight: 300;  /* Peso da fonte leve */
        letter-spacing: 0.5px;  /* Espaçamento entre letras */
    }

    /* ❌ NÃO ALTERE: Tipografia dos títulos - Fonte serif elegante */
    h1, h2, h3, .serif-moooi {
        font-family: 'Cormorant Garamond', serif;  /* Fonte serif clássica */
        font-weight: 400;  /* Peso da fonte normal */
        text-transform: uppercase;  /* Transforma texto em maiúsculas */
        letter-spacing: 3px;  /* Espaçamento maior entre letras */
    }

    /* ❌ NÃO ALTERE: Barra de navegação fixa no topo */
    .nav-moooi {
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        align-items: center;  /* Alinha itens no centro verticalmente */
        padding: 30px 50px;  /* Espaçamento interno */
        background: white;  /* Fundo branco */
        border-bottom: 1px solid #f2f2f2;  /* Linha divisória cinza clara */
        position: sticky;  /* Fica fixa ao rolar */
        top: 0;  /* Posição no topo */
        z-index: 1000;  /* Fica acima de outros elementos */
    }
    
    /* ❌ NÃO ALTERE: Estilo do logo na navegação */
    .logo-moooi {
        font-family: 'Cormorant Garamond', serif;  /* Fonte serif */
        font-size: 32px;  /* Tamanho grande */
        font-weight: 500;  /* Peso médio */
        letter-spacing: 8px;  /* Espaçamento grande entre letras */
        text-transform: uppercase;  /* Maiúsculas */
    }

    /* ❌ NÃO ALTERE: Seção hero com imagem de fundo */
    .hero-moooi {
        position: relative;  /* Posicionamento relativo */
        height: 90vh;  /* Altura = 90% da altura da tela */
        background-image: url('https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1600&q=80');  /* Imagem de fundo */
        background-size: cover;  /* Imagem cobre toda a área */
        background-position: center;  /* Imagem centralizada */
        display: flex;  /* Layout flexível */
        justify-content: center;  /* Centraliza horizontalmente */
        align-items: center;  /* Centraliza verticalmente */
        color: white;  /* Texto branco */
        text-align: center;  /* Texto centralizado */
    }
    
    /* ❌ NÃO ALTERE: Sobreposição escura sobre a imagem do hero */
    .hero-overlay {
        background: rgba(0,0,0,0.1);  /* Fundo preto semi-transparente */
        width: 100%;  /* Largura total */
        height: 100%;  /* Altura total */
        display: flex;  /* Layout flexível */
        flex-direction: column;  /* Itens em coluna */
        justify-content: center;  /* Centraliza verticalmente */
        align-items: center;  /* Centraliza horizontalmente */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
    div.stButton > button {
        background-color: transparent;  /* Fundo transparente */
        color: #000;  /* Texto preto */
        border: 1px solid #000;  /* Borda preta fina */
        border-radius: 0px;  /* Sem arredondamento */
        padding: 12px 40px;  /* Espaçamento interno */
        font-size: 12px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        transition: 0.4s;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover (ao passar mouse) nos botões */
    div.stButton > button:hover {
        background-color: #000;  /* Fundo preto */
        color: #fff;  /* Texto branco */
        border: 1px solid #000;  /* Borda preta */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões em links */
    .action-button {
        display: inline-block !important;  /* Exibe como bloco inline */
        background-color: transparent !important;  /* Fundo transparente */
        color: #000 !important;  /* Texto preto */
        border: 1px solid #000 !important;  /* Borda preta fina */
        border-radius: 0px !important;  /* Sem arredondamento */
        padding: 12px 40px !important;  /* Espaçamento interno */
        font-size: 12px !important;  /* Tamanho pequeno */
        text-transform: uppercase !important;  /* Maiúsculas */
        letter-spacing: 2px !important;  /* Espaçamento entre letras */
        transition: 0.4s !important;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
        cursor: pointer !important;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
    .action-button:hover {
        background-color: #000 !important;  /* Fundo preto */
        color: #fff !important;  /* Texto branco */
        border: 1px solid #000 !important;  /* Borda preta */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Estilo para links visitados */
    .action-button:visited {
        color: #000 !important;  /* Texto preto */
        text-decoration: none !important;  /* Remove sublinhado */
    }

    /* ❌ NÃO ALTERE: Seção de grid de produtos */
    .product-grid-section {
        padding: 100px 50px;  /* Espaçamento interno */
    }

    /* ❌ NÃO ALTERE: Card individual de produto */
    .product-card {
        text-align: center;  /* Texto centralizado */
        margin-bottom: 50px;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Imagem do produto */
    .product-img {
        width: 100%;  /* Largura total */
        height: 500px;  /* Altura fixa */
        object-fit: cover;  /* Cobre a área sem distorcer */
        margin-bottom: 20px;  /* Espaçamento inferior */
        transition: transform 0.6s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover na imagem do produto */
    .product-img:hover {
        transform: scale(1.02);  /* Aumenta 2% ao passar mouse */
    }

    /* ❌ NÃO ALTERE: Rodapé elegante */
    .footer-moooi {
        background-color: #fafafa;  /* Fundo cinza muito claro */
        padding: 100px 50px;  /* Espaçamento interno */
        border-top: 1px solid #eee;  /* Linha divisória cinza clara */
    }

    /* ❌ NÃO ALTERE: Esconde o header padrão do Streamlit */
    [data-testid="stHeader"] { 
        display: none;  /* Oculta o header */
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
# ✅ ALTERE: Textos da navegação e logo
st.markdown("""
<div class="nav-moooi">
    <!-- ✅ ALTERE: Menu esquerdo da navegação -->
    <div style="display: flex; gap: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">
        <a href="#colecao" style="color: #000; text-decoration: none; cursor: pointer;">Coleção</a>  <!-- ✅ ALTERE: Texto do menu e seção -->
        <a href="#estilo" style="color: #000; text-decoration: none; cursor: pointer;">Estilo de Vida</a>  <!-- ✅ ALTERE: Texto do menu e seção -->
        <a href="#historias" style="color: #000; text-decoration: none; cursor: pointer;">Histórias</a>  <!-- ✅ ALTERE: Texto do menu e seção -->
    </div>
    <!-- ✅ ALTERE: Logo da marca -->
    <div class="logo-moooi">Moooi</div>  <!-- ✅ ALTERE: Nome da marca -->
    <!-- ✅ ALTERE: Menu direito da navegação -->
    <div style="display: flex; gap: 30px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;">
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO SECTION ==========
# ✅ ALTERE: Título, descrição e imagem do hero
st.markdown("""
<div class="hero-moooi">
    <div class="hero-overlay">
        <!-- ✅ ALTERE: Texto pequeno acima do título -->
        <h2 style="font-size: 14px; letter-spacing: 5px; margin-bottom: 20px;">LANÇAMENTO DE COLEÇÃO</h2>
        <!-- ✅ ALTERE: Título principal do hero -->
        <h1 class="serif-moooi" style="font-size: 60px; color: white;">A Life Extraordinary</h1>
        <!-- ✅ ALTERE: Link/botão do hero -->
        <div style="margin-top: 30px;">
             <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: underline; font-size: 12px; letter-spacing: 2px;">DESCUBRA O NOVO</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 5: INTRODUÇÃO ==========
# ✅ ALTERE: Título e descrição da marca
st.markdown("""
<div id="colecao" style="padding: 120px 20%; text-align: center;">
    <!-- ✅ ALTERE: Título da seção -->
    <h2 class="serif-moooi" style="font-size: 32px; margin-bottom: 30px;">Inspirando o Mundo desde 2001</h2>
    <!-- ✅ ALTERE: Descrição da marca -->
    <p style="font-size: 16px; line-height: 1.8; color: #555;">
        A Moooi sempre foi sinônimo de um estilo de vida que é ao mesmo tempo lúdico e refinado. 
        Nossas criações desafiam a gravidade, a luz e a imaginação, transformando espaços cotidianos 
        em experiências extraordinárias.
    </p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 6: GRID DE PRODUTOS ==========
# ❌ NÃO ALTERE: Estrutura de colunas para exibir produtos
st.markdown('<div id="estilo" class="product-grid-section">', unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")  # ❌ NÃO ALTERE: Cria 2 colunas

# PRODUTO 1
with col1:
    # ✅ ALTERE: Imagem, título e descrição do primeiro produto
    st.markdown("""
    <div class="product-card">
        <!-- ✅ ALTERE: URL da imagem do produto -->
        <img src="https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800" class="product-img">
        <!-- ✅ ALTERE: Nome do produto -->
        <h3 class="serif-moooi" style="font-size: 20px;">Luminária Knotted</h3>
        <!-- ✅ ALTERE: Descrição/designer do produto -->
        <p style="font-size: 12px; color: #888; margin-top: 10px;">DESIGN POR MARCEL WANDERS</p>
    </div>
    """, unsafe_allow_html=True)
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Ver Detalhes</a>', unsafe_allow_html=True)

# PRODUTO 2
with col2:
    # ✅ ALTERE: Imagem, título e descrição do segundo produto
    st.markdown("""
    <div class="product-card" style="margin-top: 80px;">
        <!-- ✅ ALTERE: URL da imagem do produto -->
        <img src="https://images.unsplash.com/photo-1567016432779-094069958ea5?w=800" class="product-img">
        <!-- ✅ ALTERE: Nome do produto -->
        <h3 class="serif-moooi" style="font-size: 20px;">Sofá Cloud</h3>
        <!-- ✅ ALTERE: Descrição/designer do produto -->
        <p style="font-size: 12px; color: #888; margin-top: 10px;">SENTANDO NAS NUVENS</p>
    </div>
    """, unsafe_allow_html=True)
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Ver Detalhes</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # ❌ NÃO ALTERE: Fecha a seção

# ========== SEÇÃO 7: BANNER COM IMAGEM E TEXTO ==========
# ✅ ALTERE: Imagem de fundo, título e descrição
st.markdown("""
<!-- ❌ NÃO ALTERE: Estrutura do banner -->
<div id="historias" style="width: 100%; height: 600px; background-image: url('https://images.unsplash.com/photo-1534349762230-e0cadf78f5db?w=1600'); background-size: cover; background-position: center;">
</div>
<!-- ✅ ALTERE: Seção de texto sobre a imagem -->
<div style="padding: 80px 50px; text-align: left; background-color: #000; color: #fff;">
    <!-- ✅ ALTERE: Título da seção -->
    <h2 class="serif-moooi" style="font-size: 40px; color: #fff;">Paredes que Contam Histórias</h2>
    <!-- ✅ ALTERE: Descrição da seção -->
    <p style="max-width: 600px; margin-top: 20px; font-weight: 200;">Explore nossa coleção exclusiva de papéis de parede inspirados em animais extintos e mundos fantásticos.</p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
# ✅ ALTERE: Informações do rodapé, links e copyright
st.markdown("""
<div class="footer-moooi">
    <!-- ❌ NÃO ALTERE: Grid de 4 colunas -->
    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 50px;">
        <!-- COLUNA 1: Sobre a marca -->
        <div>
            <!-- ✅ ALTERE: Nome da marca no footer -->
            <h3 class="serif-moooi" style="font-size: 24px; margin-bottom: 20px;">Moooi</h3>
            <!-- ✅ ALTERE: Descrição e call-to-action -->
            <p style="font-size: 12px; line-height: 2;">A Life Extraordinary.<br>Subscreva para receber inspiração semanal.</p>
        </div>
        <!-- COLUNA 2: Produtos -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Produtos</h4>
            <!-- ✅ ALTERE: Links de produtos -->
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Iluminação</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Móveis</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Acessórios</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Tapetes</a>
            </p>
        </div>
        <!-- COLUNA 3: Serviços -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Serviços</h4>
            <!-- ✅ ALTERE: Links de serviços -->
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Localizador de Lojas</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Atendimento</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Downloads 3D</a>
            </p>
        </div>
        <!-- COLUNA 4: Redes sociais -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size: 11px; font-weight: 700; text-transform: uppercase;">Social</h4>
            <!-- ✅ ALTERE: Links de redes sociais -->
            <p style="font-size: 12px; line-height: 2; margin-top: 20px;">
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Instagram</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">Pinterest</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #000; text-decoration: none;">LinkedIn</a>
            </p>
        </div>
    </div>
    <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
    <div style="margin-top: 100px; padding-top: 20px; border-top: 1px solid #eee; font-size: 10px; color: #aaa; text-align: center;">
        <!-- ✅ ALTERE: Texto de copyright -->
        © 2026 MOOOI B.V. TODOS OS DIREITOS RESERVADOS.
    </div>
</div>
""", unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE