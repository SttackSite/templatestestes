import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Memphis Zoo | Experience the Wild",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🦁",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown("""
<style>
    /* ❌ NÃO ALTERE: Importa a fonte do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* ❌ NÃO ALTERE: Tipografia padrão */
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;  /* Fonte moderna */
    }

    /* ❌ NÃO ALTERE: Remove padding padrão do Streamlit */
    .block-container {
        padding: 0 !important;  /* Remove espaçamento interno */
        max-width: 100% !important;  /* Ocupa 100% da largura */
    }

    /* ❌ NÃO ALTERE: Header sobreposto (overlay) */
    .zoo-header {
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* Posição no topo */
        width: 100%;  /* Largura total */
        z-index: 1000;  /* Fica acima de outros elementos */
        padding: 20px 50px;  /* Espaçamento interno */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        align-items: center;  /* Alinha itens no centro verticalmente */
        background: rgba(0,0,0,0.2);  /* Fundo preto semi-transparente */
    }
    
    /* ❌ NÃO ALTERE: Estilo do logo */
    .logo-zoo {
        color: white;  /* Texto branco */
        font-weight: 900;  /* Peso muito pesado */
        font-size: 32px;  /* Tamanho grande */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }

    /* ❌ NÃO ALTERE: Seção hero com imagem de fundo */
    .hero-video-bg {
        height: 100vh;  /* Altura = 100% da altura da tela */
        background-image: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1600&q=80');  /* Imagem com overlay */
        background-size: cover;  /* Imagem cobre toda a área */
        background-position: center;  /* Imagem centralizada */
        display: flex;  /* Layout flexível */
        flex-direction: column;  /* Itens em coluna */
        justify-content: center;  /* Centraliza verticalmente */
        align-items: center;  /* Centraliza horizontalmente */
        color: white;  /* Texto branco */
        text-align: center;  /* Texto centralizado */
    }

    /* ❌ NÃO ALTERE: Barra de ações flutuante */
    .action-bar {
        display: flex;  /* Layout flexível */
        gap: 10px;  /* Espaçamento entre itens */
        margin-top: 30px;  /* Espaçamento superior */
    }
    
    /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
    div.stButton > button {
        border-radius: 0px;  /* Sem arredondamento */
        font-weight: 700;  /* Peso pesado */
        text-transform: uppercase;  /* Maiúsculas */
        padding: 15px 30px;  /* Espaçamento interno */
        border: none;  /* Sem borda */
        letter-spacing: 1px;  /* Espaçamento entre letras */
    }
    
    /* ❌ NÃO ALTERE: Botão laranja (tickets) */
    .ticket-btn > div > button {
        background-color: #f37021 !important;  /* Fundo laranja */
        color: white !important;  /* Texto branco */
    }
    
    /* ❌ NÃO ALTERE: Seções de conteúdo */
    .info-section {
        padding: 80px 10%;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
    }
    
    /* ✅ ALTERE: Fundos de cores */
    .green-bg { 
        background-color: #004a26;  /* Fundo verde */
        color: white;  /* Texto branco */
    }
    
    .sand-bg { 
        background-color: #f9f7f2;  /* Fundo bege */
        color: #333;  /* Texto escuro */
    }

    /* ❌ NÃO ALTERE: Cards de animais */
    .animal-card {
        background: white;  /* Fundo branco */
        border-radius: 0px;  /* Sem arredondamento */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        margin-bottom: 20px;  /* Espaçamento inferior */
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);  /* Sombra suave */
    }
    
    /* ❌ NÃO ALTERE: Imagem do animal */
    .animal-card img { 
        width: 100%;  /* Largura total */
        height: 250px;  /* Altura fixa */
        object-fit: cover;  /* Cobre a área sem distorcer */
    }
    
    /* ❌ NÃO ALTERE: Informações do animal */
    .animal-info { 
        padding: 20px;  /* Espaçamento interno */
        text-align: left;  /* Texto alinhado à esquerda */
    }
    
    /* ❌ NÃO ALTERE: Rodapé */
    .footer-zoo {
        background-color: #1a1a1a;  /* Fundo preto */
        color: white;  /* Texto branco */
        padding: 60px 10%;  /* Espaçamento interno */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões em links */
    .action-button {
        display: inline-block !important;  /* Exibe como bloco inline */
        background-color: #f37021 !important;  /* Fundo laranja */
        color: white !important;  /* Texto branco */
        border: none !important;  /* Sem borda */
        border-radius: 0px !important;  /* Sem arredondamento */
        padding: 15px 30px !important;  /* Espaçamento interno */
        font-weight: 700 !important;  /* Peso pesado */
        font-size: 14px !important;  /* Tamanho médio */
        text-transform: uppercase !important;  /* Maiúsculas */
        letter-spacing: 1px !important;  /* Espaçamento entre letras */
        transition: 0.3s !important;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
        cursor: pointer !important;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
    .action-button:hover {
        background-color: #d4571a !important;  /* Fundo laranja escuro */
        color: white !important;  /* Texto branco */
        border: none !important;  /* Sem borda */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Estilo para links visitados */
    .action-button:visited {
        color: white !important;  /* Texto branco */
        text-decoration: none !important;  /* Remove sublinhado */
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) E HERO ==========
# ✅ ALTERE: Logo, menu e título do hero
st.markdown("""
<div class="zoo-header">
    <!-- ✅ ALTERE: Nome do zoológico/marca -->
    <div class="logo-zoo">MEMPHIS ZOO</div>
    <!-- ✅ ALTERE: Menu de navegação -->
    <div style="display: flex; gap: 20px; color: white; font-weight: 700; font-size: 14px;">
        <a href="#animals" style="color: white; text-decoration: none; cursor: pointer;">ANIMALS</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#exhibits" style="color: white; text-decoration: none; cursor: pointer;">EXHIBITS</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#education" style="color: white; text-decoration: none; cursor: pointer;">EDUCATION</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#conservation" style="color: white; text-decoration: none; cursor: pointer;">CONSERVATION</a>  <!-- ✅ ALTERE: Texto do menu -->
    </div>
</div>
<div class="hero-video-bg">
    <!-- ✅ ALTERE: Título principal -->
    <h1 style="font-size: 80px; font-weight: 900; margin-bottom: 0;">ADVENTURE AWAITS</h1>
    <!-- ✅ ALTERE: Descrição do hero -->
    <p style="font-size: 24px; font-weight: 400;">Explore o mundo selvagem no coração de Memphis.</p>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 4: BARRA DE BOTÕES RÁPIDOS ==========
# ✅ ALTERE: Textos e URLs dos botões
c_btn1, c_btn2, c_btn3 = st.columns(3)

with c_btn1:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">BUY TICKETS</a>', unsafe_allow_html=True)

with c_btn2:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">BECOME A MEMBER</a>', unsafe_allow_html=True)

with c_btn3:
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button" style="width: 100%; text-align: center; display: block;">DONATE TODAY</a>', unsafe_allow_html=True)

# ========== SEÇÃO 5: PLANEJE SUA VISITA ==========
# ✅ ALTERE: Título, descrição e informações
st.markdown('<div id="animals" class="info-section sand-bg">', unsafe_allow_html=True)

# ✅ ALTERE: Título da seção
st.markdown("<h2 style='font-weight:900; color:#004a26;'>PLANEJE SUA VISITA</h2>", unsafe_allow_html=True)

# ✅ ALTERE: Descrição
st.write("Estamos abertos diariamente das 9h às 17h. Venha ver nossos novos filhotes!")

# ❌ NÃO ALTERE: Estrutura de 3 colunas
col_v1, col_v2, col_v3 = st.columns(3)

with col_v1:
    # ✅ ALTERE: Título e informação
    st.markdown("### 🕒 Horários")
    st.write("Seg - Dom: 09:00 - 17:00")

with col_v2:
    # ✅ ALTERE: Título e informação
    st.markdown("### 📍 Localização")
    st.write("2000 Prentiss Pl, Memphis, TN")

with col_v3:
    # ✅ ALTERE: Título e botão
    st.markdown("### 🗺️ Mapa do Zoo")
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">BAIXAR MAPA</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 6: NOSSOS ANIMAIS (CARDS) ==========
# ✅ ALTERE: Título da seção
st.markdown('<div id="exhibits" class="info-section">', unsafe_allow_html=True)

st.markdown("<h2 style='font-weight:900; margin-bottom:40px;'>CONHEÇA OS RESIDENTES</h2>", unsafe_allow_html=True)

# ❌ NÃO ALTERE: Função que renderiza os animais
def animal_card(col, img, name, category):
    # ❌ NÃO ALTERE: Função que cria os cards de animal
    with col:
        st.markdown(f"""
        <div class="animal-card">
            <!-- ✅ ALTERE: URL da imagem do animal -->
            <img src="{img}">
            <!-- ✅ ALTERE: Nome e categoria do animal -->
            <div class="animal-info">
                <span style="color:#f37021; font-weight:700; font-size:12px;">{category}</span>  <!-- ✅ ALTERE: Categoria -->
                <h3 style="margin:5px 0;">{name}</h3>  <!-- ✅ ALTERE: Nome do animal -->
            </div>
        </div>
        """, unsafe_allow_html=True)
        # ✅ ALTERE: Texto do botão e URL
        st.markdown(f'<a href="https://www.google.com/" target="_blank" class="action-button">Saber mais sobre {name}</a>', unsafe_allow_html=True)

# ❌ NÃO ALTERE: Primeira linha de animais (3 colunas)
ca1, ca2, ca3 = st.columns(3)

animal_card(ca1, "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?w=500", "Leão Africano", "FELINOS")  # ✅ ALTERE: Imagem, nome e categoria
animal_card(ca2, "https://images.unsplash.com/photo-1544860707-c352cc5a92e3?w=500", "Panda Gigante", "ÁSIA")  # ✅ ALTERE: Imagem, nome e categoria
animal_card(ca3, "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=500", "Girafa Reticulada", "SAVANA")  # ✅ ALTERE: Imagem, nome e categoria

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 7: CONSERVAÇÃO ==========
# ✅ ALTERE: Título, descrição e botão
st.markdown('<div id="conservation" class="info-section green-bg">', unsafe_allow_html=True)

# ✅ ALTERE: Título da seção
st.markdown("""
    <h2 style='font-weight:900;'>SALVANDO ESPÉCIES NO MUNDO TODO</h2>
    <!-- ✅ ALTERE: Descrição da conservação -->
    <p style='max-width:800px; margin: 20px auto; font-size:18px;'>
        O Memphis Zoo é líder em pesquisa e conservação. Desde a reintrodução de sapos raros até a proteção de habitats na África, seu ingresso faz a diferença.
    </p>
""", unsafe_allow_html=True)

# ✅ ALTERE: Texto do botão e URL
st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">VEJA NOSSO IMPACTO</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 8: EVENTOS E NOTÍCIAS ==========
# ✅ ALTERE: Título, descrição e imagem
st.markdown('<div id="education" class="info-section sand-bg">', unsafe_allow_html=True)

# ❌ NÃO ALTERE: Estrutura de 2 colunas
col_e1, col_e2 = st.columns(2)

with col_e1:
    # ✅ ALTERE: URL da imagem
    st.image("https://images.unsplash.com/photo-1502675135487-e971002a6adb?w=600")

with col_e2:
    st.markdown("<div style='text-align:left; padding-top:20px;'>", unsafe_allow_html=True)
    
    # ✅ ALTERE: Título do evento
    st.markdown("<h2 style='font-weight:900;'>NOITE NO ZOO</h2>", unsafe_allow_html=True)
    
    # ✅ ALTERE: Descrição do evento
    st.write("Participe de nossos eventos noturnos exclusivos para famílias. Jantares temáticos, tours guiados sob o luar e muito mais.")
    
    # ✅ ALTERE: Texto do botão e URL
    st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">VER CALENDÁRIO DE EVENTOS</a>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 9: FOOTER (RODAPÉ) ==========
# ✅ ALTERE: Informações do footer, links e copyright
st.markdown("""
<div class="footer-zoo">
    <!-- ❌ NÃO ALTERE: Grid de 3 colunas -->
    <div style="display:grid; grid-template-columns: 2fr 1fr 1fr; gap:50px;">
        <!-- COLUNA 1: Sobre o zoológico -->
        <div>
            <!-- ✅ ALTERE: Nome do zoológico -->
            <h2 style="font-weight:900;">MEMPHIS ZOO</h2>
            <!-- ✅ ALTERE: Descrição -->
            <p>Conectando pessoas aos animais através de experiências memoráveis.</p>
        </div>
        <!-- COLUNA 2: Explorar -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4>EXPLORE</h4>
            <!-- ✅ ALTERE: Links -->
            <p style="font-size:13px; line-height:2;">
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Animais</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Experiências</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Membros</a>
            </p>
        </div>
        <!-- COLUNA 3: Suporte -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4>SUPORTE</h4>
            <!-- ✅ ALTERE: Links -->
            <p style="font-size:13px; line-height:2;">
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Doar</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Voluntários</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: white; text-decoration: none;">Trabalhe Conosco</a>
            </p>
        </div>
    </div>
    <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
    <div style="text-align:center; margin-top:50px; border-top: 1px solid #444; padding-top:20px; font-size:12px; color:#888;">
        <!-- ✅ ALTERE: Texto de copyright -->
        © 2026 Memphis Zoo. Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
