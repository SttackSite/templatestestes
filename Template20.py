import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Lemonade Giveback | Seguro com Propósito",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🍋",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide"  # ❌ NÃO ALTERE: Define o layout como largura total
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown("""
<style>
    /* ❌ NÃO ALTERE: Importa a fonte do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');

    /* ✅ ALTERE: Variáveis de cor da marca */
    :root {
        --lemonade-pink: #ff0083;  /* Cor rosa/magenta principal */
        --lemonade-black: #222;    /* Cor preta/escura */
    }

    /* ❌ NÃO ALTERE: Fundo branco da aplicação */
    .stApp {
        background-color: #ffffff;  /* Fundo branco */
    }

    /* ❌ NÃO ALTERE: Tipografia padrão */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;  /* Fonte moderna */
        color: var(--lemonade-black);  /* Cor do texto */
    }

    /* ❌ NÃO ALTERE: Barra de navegação fixa no topo */
    .nav-lemonade {
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        align-items: center;  /* Alinha itens no centro verticalmente */
        padding: 20px 10%;  /* Espaçamento interno */
        background: white;  /* Fundo branco */
        position: sticky;  /* Fica fixa ao rolar */
        top: 0;  /* Posição no topo */
        z-index: 1000;  /* Fica acima de outros elementos */
        border-bottom: 1px solid #f0f0f0;  /* Linha divisória cinza clara */
    }
    
    /* ❌ NÃO ALTERE: Estilo do logo */
    .logo-pink {
        color: #ff0083;  /* Cor rosa */
        font-weight: 800;  /* Peso muito pesado */
        font-size: 24px;  /* Tamanho grande */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }

    /* ❌ NÃO ALTERE: Seção hero */
    .hero-lemonade {
        padding: 100px 10%;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        background-color: #fff;  /* Fundo branco */
    }
    
    /* ✅ ALTERE: Estilo do contador de impacto */
    .giveback-counter {
        color: #ff0083;  /* Cor rosa */
        font-size: 80px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        margin: 20px 0;  /* Espaçamento vertical */
    }

    /* ❌ NÃO ALTERE: Estilo do título principal */
    .hero-h1 {
        font-size: 50px;  /* Tamanho grande */
        font-weight: 800;  /* Peso muito pesado */
        line-height: 1.1;  /* Altura da linha compacta */
        max-width: 800px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões nativos do Streamlit */
    div.stButton > button {
        background-color: #ff0083;  /* Fundo rosa */
        color: white;  /* Texto branco */
        border-radius: 50px;  /* Arredondado */
        padding: 18px 45px;  /* Espaçamento interno */
        font-weight: 700;  /* Peso pesado */
        font-size: 16px;  /* Tamanho médio */
        border: none;  /* Sem borda */
        transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões */
    div.stButton > button:hover {
        background-color: #d6006e;  /* Fundo rosa escuro */
        transform: scale(1.05);  /* Aumenta 5% */
        color: white;  /* Texto branco */
    }

    /* ❌ NÃO ALTERE: Estilo dos botões em links */
    .action-button {
        display: inline-block !important;  /* Exibe como bloco inline */
        background-color: #ff0083 !important;  /* Fundo rosa */
        color: white !important;  /* Texto branco */
        border-radius: 50px !important;  /* Arredondado */
        padding: 18px 45px !important;  /* Espaçamento interno */
        font-weight: 700 !important;  /* Peso pesado */
        font-size: 16px !important;  /* Tamanho médio */
        border: none !important;  /* Sem borda */
        transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
        cursor: pointer !important;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos botões em links */
    .action-button:hover {
        background-color: #d6006e !important;  /* Fundo rosa escuro */
        transform: scale(1.05) !important;  /* Aumenta 5% */
        color: white !important;  /* Texto branco */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Estilo para links visitados */
    .action-button:visited {
        color: white !important;  /* Texto branco */
        text-decoration: none !important;  /* Remove sublinhado */
    }

    /* ❌ NÃO ALTERE: Wrapper de seções */
    .section-wrap {
        padding: 100px 10%;  /* Espaçamento interno */
    }
    
    /* ✅ ALTERE: Fundo rosa suave para seções */
    .bg-soft-pink { 
        background-color: #fff5f9;  /* Rosa muito claro */
    }

    /* ❌ NÃO ALTERE: Cards de caridade */
    .charity-card {
        background: white;  /* Fundo branco */
        border-radius: 20px;  /* Arredondado */
        padding: 30px;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        border: 1px solid #eee;  /* Borda cinza clara */
        transition: 0.3s;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos cards */
    .charity-card:hover {
        box-shadow: 0 15px 30px rgba(255, 0, 131, 0.1);  /* Sombra rosa */
    }

    /* ❌ NÃO ALTERE: Ícones circulares */
    .circle-icon {
        width: 80px;  /* Largura */
        height: 80px;  /* Altura */
        background-color: #ff0083;  /* Fundo rosa */
        border-radius: 50%;  /* Círculo perfeito */
        display: flex;  /* Layout flexível */
        justify-content: center;  /* Centraliza horizontalmente */
        align-items: center;  /* Centraliza verticalmente */
        margin: 0 auto 20px auto;  /* Centraliza e espaçamento inferior */
        color: white;  /* Texto branco */
        font-size: 30px;  /* Tamanho grande */
    }

    /* ❌ NÃO ALTERE: Rodapé */
    .footer-lemonade {
        padding: 80px 10%;  /* Espaçamento interno */
        background-color: #222;  /* Fundo preto */
        color: #fff;  /* Texto branco */
    }
</style>
""", unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVEGAÇÃO (HEADER) ==========
# ✅ ALTERE: Textos da navegação e logo
st.markdown("""
<div class="nav-lemonade">
    <!-- ✅ ALTERE: Logo da marca -->
    <div class="logo-pink">Lemonade</div>  <!-- ✅ ALTERE: Nome da marca -->
    <!-- ✅ ALTERE: Menu de navegação -->
    <div style="display: flex; gap: 30px; font-weight: 600; font-size: 14px;">
        <a href="#seguros" style="color: #000; text-decoration: none; cursor: pointer;">Seguros</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#giveback" style="color: #000; text-decoration: none; cursor: pointer;">Giveback</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#sobre" style="color: #000; text-decoration: none; cursor: pointer;">Sobre</a>  <!-- ✅ ALTERE: Texto do menu -->
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO (O GIVEBACK) ==========
# ✅ ALTERE: Título, descrição e números
st.markdown('<div id="giveback" class="hero-lemonade">', unsafe_allow_html=True)
st.markdown('<p style="text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: #888;">Impacto Total do Giveback</p>', unsafe_allow_html=True)  # ✅ ALTERE: Texto
st.markdown('<div class="giveback-counter">$8,231,044</div>', unsafe_allow_html=True)  # ✅ ALTERE: Número de impacto
st.markdown('<h1 class="hero-h1">Transformamos o lucro não utilizado em doações.</h1>', unsafe_allow_html=True)  # ✅ ALTERE: Título principal
st.write("")  # ❌ NÃO ALTERE: Espaçamento
st.markdown('<a href="https://www.google.com/" target="_blank" class="action-button">Verifique nossos preços</a>', unsafe_allow_html=True)  # ✅ ALTERE: Texto do botão e URL
st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 5: COMO FUNCIONA (ILUSTRAÇÕES) ==========
# ✅ ALTERE: Título e descrições
st.markdown('<div id="sobre" class="section-wrap">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-size:36px; margin-bottom:60px;'>Como o Giveback funciona</h2>", unsafe_allow_html=True)  # ✅ ALTERE: Título

# ❌ NÃO ALTERE: Estrutura de 3 colunas
col1, col2, col3 = st.columns(3)

# COLUNA 1
with col1:
    st.markdown('<div class="circle-icon">1</div>', unsafe_allow_html=True)  # ❌ NÃO ALTERE: Ícone
    st.markdown("<h3 style='text-align:center;'>Você escolhe</h3>", unsafe_allow_html=True)  # ✅ ALTERE: Título
    st.write("Ao contratar o seguro, você escolhe uma causa em que acredita — como meio ambiente ou direitos humanos.")  # ✅ ALTERE: Descrição

# COLUNA 2
with col2:
    st.markdown('<div class="circle-icon">2</div>', unsafe_allow_html=True)  # ❌ NÃO ALTERE: Ícone
    st.markdown("<h3 style='text-align:center;'>Nós cuidamos</h3>", unsafe_allow_html=True)  # ✅ ALTERE: Título
    st.write("Usamos seu prêmio para pagar sinistros. Somos uma seguradora B-Corp, focada em transparência.")  # ✅ ALTERE: Descrição

# COLUNA 3
with col3:
    st.markdown('<div class="circle-icon">3</div>', unsafe_allow_html=True)  # ❌ NÃO ALTERE: Ícone
    st.markdown("<h3 style='text-align:center;'>O resto é doado</h3>", unsafe_allow_html=True)  # ✅ ALTERE: Título
    st.write("O dinheiro que sobra no final do ano não vira bônus para executivos. Ele vai direto para a sua causa escolhida.")  # ✅ ALTERE: Descrição

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 6: SEÇÃO DE CAUSAS (ESTILO GRID) ==========
# ✅ ALTERE: Título e causas
st.markdown('<div id="seguros" class="section-wrap bg-soft-pink">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>Algumas das causas que você apoia</h2>", unsafe_allow_html=True)  # ✅ ALTERE: Título

# ❌ NÃO ALTERE: Estrutura de 4 colunas
c_col1, c_col2, c_col3, c_col4 = st.columns(4)

def cause_box(col, title, img_emoji):
    # ❌ NÃO ALTERE: Função que renderiza os cards de causa
    with col:
        st.markdown(f"""
        <div class="charity-card">
            <div style="font-size:40px; margin-bottom:15px;">{img_emoji}</div>  <!-- ✅ ALTERE: Emoji -->
            <div style="font-weight:700; font-size:14px; text-transform:uppercase;">{title}</div>  <!-- ✅ ALTERE: Nome da causa -->
        </div>
        """, unsafe_allow_html=True)

# ✅ ALTERE: Causas, emojis e nomes
cause_box(c_col1, "American Red Cross", "🏥")
cause_box(c_col2, "Malala Fund", "🎓")
cause_box(c_col3, "Charity: Water", "💧")
cause_box(c_col4, "The Trevor Project", "🌈")

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 7: SEÇÃO DE CONFIANÇA ==========
# ✅ ALTERE: Título, descrição e imagem
st.markdown('<div class="section-wrap">', unsafe_allow_html=True)

# ❌ NÃO ALTERE: Estrutura de 2 colunas
col_text, col_img = st.columns([1, 1])

with col_text:
    st.markdown("<h2 style='font-size:40px;'>Seguro para o século 21.</h2>", unsafe_allow_html=True)  # ✅ ALTERE: Título
    st.write("""
    A Lemonade foi construída de forma diferente. Ao recebermos uma taxa fixa e doarmos o restante, 
    eliminamos o conflito de interesses entre a seguradora e o cliente. 
    Nós queremos pagar seus sinistros rapidamente porque não lucramos ao negá-los.
    """)  # ✅ ALTERE: Descrição
    st.write("**B-Corp Certificada. Focada no Bem Social.**")  # ✅ ALTERE: Texto de certificação

with col_img:
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=800")  # ✅ ALTERE: URL da imagem

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 8: FOOTER (RODAPÉ) ==========
# ✅ ALTERE: Informações do rodapé, links e copyright
st.markdown("""
<div class="footer-lemonade">
    <!-- ❌ NÃO ALTERE: Grid de 4 colunas -->
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px;">
        <!-- COLUNA 1: Sobre a marca -->
        <div>
            <!-- ✅ ALTERE: Nome da marca -->
            <div style="color:#ff0083; font-weight:800; font-size:20px; margin-bottom:20px;">Lemonade</div>
            <!-- ✅ ALTERE: Descrição da marca -->
            <p style="font-size:12px; opacity:0.7;">Seguros de casa, inquilino, pet e vida. Tudo em um só app.</p>
        </div>
        <!-- COLUNA 2: Produtos -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size:14px;">PRODUTOS</h4>
            <!-- ✅ ALTERE: Links de produtos -->
            <p style="font-size:12px; opacity:0.7;">
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Inquilinos</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Proprietários</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Vida</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Pet</a>
            </p>
        </div>
        <!-- COLUNA 3: Empresa -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size:14px;">EMPRESA</h4>
            <!-- ✅ ALTERE: Links de empresa -->
            <p style="font-size:12px; opacity:0.7;">
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Sobre nós</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Giveback</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Carreiras</a>
            </p>
        </div>
        <!-- COLUNA 4: Redes sociais -->
        <div>
            <!-- ✅ ALTERE: Título da coluna -->
            <h4 style="font-size:14px;">SIGA-NOS</h4>
            <!-- ✅ ALTERE: Links de redes sociais -->
            <p style="font-size:12px; opacity:0.7;">
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Instagram</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">Twitter</a><br>
                <a href="https://www.google.com/" target="_blank" style="color: #fff; text-decoration: none;">TikTok</a>
            </p>
        </div>
    </div>
    <!-- ❌ NÃO ALTERE: Linha divisória e copyright -->
    <div style="text-align:center; margin-top:80px; font-size:11px; opacity:0.5; border-top:1px solid #444; padding-top:20px;">
        <!-- ✅ ALTERE: Texto de copyright -->
        © 2026 Lemonade Inc. Todos os direitos reservados.
    </div>
</div>
""", unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
