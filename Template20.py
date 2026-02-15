import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Corporativo Premium - Ambev Style",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="🏢",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide",  # ❌ NÃO ALTERE: Define o layout como largura total
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Oculta a barra lateral
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
custom_css = """
<style>
    /* ❌ NÃO ALTERE: Importa as fontes do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap');
    
    /* ❌ NÃO ALTERE: Reset de estilos padrão */
    * {
        margin: 0;  /* Remove margem padrão */
        padding: 0;  /* Remove preenchimento padrão */
        box-sizing: border-box;  /* Inclui borda no tamanho total */
    }
    
    /* ❌ NÃO ALTERE: Estilos globais */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);  /* Gradiente de fundo */
        font-family: 'Montserrat', sans-serif;  /* Fonte padrão */
        color: #1a1a1a;  /* Cor de texto padrão */
        overflow-x: hidden;  /* Oculta scroll horizontal */
    }
    
    /* ❌ NÃO ALTERE: Remove decorações do Streamlit */
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    /* ❌ NÃO ALTERE: Animações */
    @keyframes slideInLeft {
        0% { transform: translateX(-100px); opacity: 0; }  /* Começa fora da tela à esquerda */
        100% { transform: translateX(0); opacity: 1; }  /* Termina na posição normal */
    }
    
    @keyframes slideInRight {
        0% { transform: translateX(100px); opacity: 0; }  /* Começa fora da tela à direita */
        100% { transform: translateX(0); opacity: 1; }  /* Termina na posição normal */
    }
    
    @keyframes fadeInUp {
        0% { transform: translateY(40px); opacity: 0; }  /* Começa abaixo com opacidade 0 */
        100% { transform: translateY(0); opacity: 1; }  /* Termina na posição normal */
    }
    
    @keyframes scaleIn {
        0% { transform: scale(0.95); opacity: 0; }  /* Começa pequeno com opacidade 0 */
        100% { transform: scale(1); opacity: 1; }  /* Termina no tamanho normal */
    }
    
    @keyframes borderFlow {
        0% { border-left-color: #e0e0e0; }  /* Borda cinza */
        50% { border-left-color: #1a1a1a; }  /* Borda preta */
        100% { border-left-color: #e0e0e0; }  /* Volta para cinza */
    }
    
    /* ❌ NÃO ALTERE: Navbar */
    .navbar {
        background: #ffffff;  /* Fundo branco */
        padding: 25px 80px;  /* Espaçamento interno */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        align-items: center;  /* Alinha itens no centro */
        border-bottom: 1px solid #e0e0e0;  /* Borda inferior cinza clara */
        position: sticky;  /* Fica fixo ao scroll */
        top: 0;  /* No topo */
        z-index: 100;  /* Acima de outros elementos */
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);  /* Sombra suave */
    }
    
    /* ❌ NÃO ALTERE: Logo da navbar */
    .navbar-logo {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 800;  /* Peso muito pesado */
        color: #1a1a1a;  /* Cor preta */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
    }
    
    /* ❌ NÃO ALTERE: Menu de navegação */
    .navbar-nav {
        display: flex;  /* Layout flexível */
        gap: 60px;  /* Espaçamento entre itens */
    }
    
    /* ❌ NÃO ALTERE: Links do menu com efeito underline animado */
    .nav-link {
        color: #666666;  /* Cor cinza */
        text-decoration: none;  /* Remove sublinhado */
        font-size: 11px;  /* Tamanho pequeno */
        font-weight: 600;  /* Peso pesado */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        transition: all 0.3s ease;  /* Animação suave */
        position: relative;  /* Posicionamento relativo para o ::after */
    }
    
    /* ❌ NÃO ALTERE: Underline animado (pseudo-elemento) */
    .nav-link::after {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        bottom: -8px;  /* Posição abaixo do texto */
        left: 0;  /* Alinhado à esquerda */
        width: 0;  /* Largura inicial 0 */
        height: 2px;  /* Altura da linha */
        background: #1a1a1a;  /* Cor preta */
        transition: width 0.3s ease;  /* Animação suave da largura */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos links */
    .nav-link:hover { color: #1a1a1a; }  /* Texto fica preto */
    .nav-link:hover::after { width: 100%; }  /* Underline expande para 100% */
    
    /* ❌ NÃO ALTERE: Seção hero */
    .hero {
        min-height: 100vh;  /* Altura mínima da tela */
        display: flex;  /* Layout flexível */
        align-items: center;  /* Alinha itens no centro */
        justify-content: space-between;  /* Espaça itens nas extremidades */
        padding: 100px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);  /* Gradiente de fundo */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero */
    .hero::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        width: 600px;  /* Largura */
        height: 600px;  /* Altura */
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.05) 0%, transparent 70%);  /* Gradiente radial */
        border-radius: 50%;  /* Círculo */
        top: -200px;  /* Posição no topo */
        right: -200px;  /* Posição à direita */
    }
    
    /* ❌ NÃO ALTERE: Conteúdo do hero */
    .hero-content {
        max-width: 650px;  /* Largura máxima */
        position: relative;  /* Posicionamento relativo */
        z-index: 2;  /* Acima do efeito de fundo */
        animation: slideInLeft 0.8s ease-out;  /* Animação de entrada */
    }
    
    /* ❌ NÃO ALTERE: Label do hero */
    .hero-label {
        font-size: 12px;  /* Tamanho pequeno */
        color: #999999;  /* Cor cinza */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        margin-bottom: 20px;  /* Espaçamento inferior */
        font-weight: 600;  /* Peso pesado */
    }
    
    /* ❌ NÃO ALTERE: Título do hero */
    .hero-title {
        font-size: 72px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        line-height: 1.1;  /* Altura da linha compacta */
        margin-bottom: 30px;  /* Espaçamento inferior */
        color: #1a1a1a;  /* Texto preto */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }
    
    /* ❌ NÃO ALTERE: Descrição do hero */
    .hero-desc {
        font-size: 16px;  /* Tamanho médio */
        color: #666666;  /* Texto cinza */
        margin-bottom: 50px;  /* Espaçamento inferior */
        line-height: 1.8;  /* Altura da linha generosa */
        font-weight: 400;  /* Peso normal */
    }
    
    /* ❌ NÃO ALTERE: CTA do hero */
    .hero-cta {
        display: flex;  /* Layout flexível */
        gap: 20px;  /* Espaçamento entre itens */
        flex-wrap: wrap;  /* Quebra em múltiplas linhas */
    }
    
    /* ❌ NÃO ALTERE: Botão primário */
    .btn-primary {
        background: #1a1a1a;  /* Fundo preto */
        color: #ffffff;  /* Texto branco */
        padding: 16px 50px;  /* Espaçamento interno */
        border: none;  /* Sem borda */
        border-radius: 2px;  /* Arredondamento mínimo */
        font-weight: 700;  /* Peso pesado */
        font-size: 12px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão primário */
    .btn-primary:hover {
        background: #333333;  /* Preto mais claro */
        transform: translateY(-2px);  /* Levanta o botão */
    }
    
    /* ❌ NÃO ALTERE: Botão secundário */
    .btn-secondary {
        background: transparent;  /* Fundo transparente */
        color: #1a1a1a;  /* Texto preto */
        padding: 16px 50px;  /* Espaçamento interno */
        border: 2px solid #1a1a1a;  /* Borda preta */
        border-radius: 2px;  /* Arredondamento mínimo */
        font-weight: 700;  /* Peso pesado */
        font-size: 12px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão secundário */
    .btn-secondary:hover {
        background: #1a1a1a;  /* Fundo preto */
        color: #ffffff;  /* Texto branco */
    }
    
    /* ❌ NÃO ALTERE: Visual do hero */
    .hero-visual {
        position: relative;  /* Posicionamento relativo */
        z-index: 2;  /* Acima do efeito de fundo */
        width: 500px;  /* Largura */
        height: 500px;  /* Altura */
        background: linear-gradient(135deg, #f0f0f0 0%, #e8e8e8 100%);  /* Gradiente de fundo */
        border: 1px solid #e0e0e0;  /* Borda cinza clara */
        display: flex;  /* Layout flexível */
        align-items: center;  /* Alinha itens no centro */
        justify-content: center;  /* Centraliza itens */
        font-size: 100px;  /* Tamanho muito grande */
        animation: slideInRight 0.8s ease-out;  /* Animação de entrada */
    }
    
    /* ❌ NÃO ALTERE: Seção de estatísticas */
    .stats-section {
        background: #1a1a1a;  /* Fundo preto */
        color: #ffffff;  /* Texto branco */
        padding: 100px 80px;  /* Espaçamento interno */
    }
    
    /* ❌ NÃO ALTERE: Grid de estatísticas */
    .stats-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(4, 1fr);  /* 4 colunas */
        gap: 60px;  /* Espaçamento entre itens */
        max-width: 1600px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Item de estatística */
    .stat-item {
        animation: fadeInUp 0.8s ease-out;  /* Animação de entrada */
        animation-fill-mode: both;  /* Mantém o estado final da animação */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação */
    .stat-item:nth-child(1) { animation-delay: 0.1s; }
    .stat-item:nth-child(2) { animation-delay: 0.2s; }
    .stat-item:nth-child(3) { animation-delay: 0.3s; }
    .stat-item:nth-child(4) { animation-delay: 0.4s; }
    
    /* ❌ NÃO ALTERE: Número da estatística */
    .stat-number {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 900;  /* Peso extremamente pesado */
        margin-bottom: 15px;  /* Espaçamento inferior */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
    }
    
    /* ❌ NÃO ALTERE: Label da estatística */
    .stat-label {
        font-size: 13px;  /* Tamanho pequeno */
        color: #cccccc;  /* Texto cinza claro */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        font-weight: 600;  /* Peso pesado */
    }
    
    /* ❌ NÃO ALTERE: Seção de serviços */
    .services-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f2f5 100%);  /* Gradiente de fundo */
        padding: 150px 80px;  /* Espaçamento interno */
    }
    
    /* ❌ NÃO ALTERE: Título da seção */
    .section-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        text-align: center;  /* Texto centralizado */
        margin-bottom: 100px;  /* Espaçamento inferior */
        color: #1a1a1a;  /* Texto preto */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }
    
    /* ❌ NÃO ALTERE: Grid de serviços */
    .services-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(3, 1fr);  /* 3 colunas */
        gap: 50px;  /* Espaçamento entre itens */
        max-width: 1600px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Card de serviço */
    .service-card {
        padding: 60px 40px;  /* Espaçamento interno */
        background: #ffffff;  /* Fundo branco */
        border-left: 4px solid #1a1a1a;  /* Borda esquerda preta */
        transition: all 0.4s ease;  /* Animação suave */
        animation: fadeInUp 0.8s ease-out;  /* Animação de entrada */
        animation-fill-mode: both;  /* Mantém o estado final da animação */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);  /* Sombra suave */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação dos cards */
    .service-card:nth-child(1) { animation-delay: 0.1s; }
    .service-card:nth-child(2) { animation-delay: 0.2s; }
    .service-card:nth-child(3) { animation-delay: 0.3s; }
    
    /* ❌ NÃO ALTERE: Efeito hover nos cards */
    .service-card:hover {
        transform: translateY(-10px);  /* Levanta o card */
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);  /* Sombra aumentada */
        border-left-color: #666666;  /* Borda fica cinza */
    }
    
    /* ❌ NÃO ALTERE: Ícone do serviço */
    .service-icon {
        font-size: 48px;  /* Tamanho grande */
        margin-bottom: 25px;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Título do serviço */
    .service-title {
        font-size: 22px;  /* Tamanho grande */
        font-weight: 700;  /* Peso pesado */
        margin-bottom: 15px;  /* Espaçamento inferior */
        color: #1a1a1a;  /* Texto preto */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
    }
    
    /* ❌ NÃO ALTERE: Descrição do serviço */
    .service-desc {
        font-size: 14px;  /* Tamanho pequeno */
        color: #666666;  /* Texto cinza */
        line-height: 1.8;  /* Altura da linha generosa */
    }
    
    /* ❌ NÃO ALTERE: Seção de portfólio */
    .portfolio-section {
        background: linear-gradient(135deg, #f0f2f5 0%, #f8f9fa 100%);  /* Gradiente de fundo */
        padding: 150px 80px;  /* Espaçamento interno */
    }
    
    /* ❌ NÃO ALTERE: Grid de portfólio */
    .portfolio-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(2, 1fr);  /* 2 colunas */
        gap: 60px;  /* Espaçamento entre itens */
        max-width: 1600px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Item de portfólio */
    .portfolio-item {
        padding: 80px 60px;  /* Espaçamento interno */
        background: #ffffff;  /* Fundo branco */
        border: 1px solid #e0e0e0;  /* Borda cinza clara */
        transition: all 0.4s ease;  /* Animação suave */
        animation: scaleIn 0.8s ease-out;  /* Animação de entrada */
        animation-fill-mode: both;  /* Mantém o estado final da animação */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);  /* Sombra suave */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação dos itens */
    .portfolio-item:nth-child(1) { animation-delay: 0.1s; }
    .portfolio-item:nth-child(2) { animation-delay: 0.2s; }
    .portfolio-item:nth-child(3) { animation-delay: 0.3s; }
    .portfolio-item:nth-child(4) { animation-delay: 0.4s; }
    
    /* ❌ NÃO ALTERE: Efeito hover nos itens */
    .portfolio-item:hover {
        transform: translateY(-8px);  /* Levanta o item */
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.1);  /* Sombra aumentada */
        border-color: #1a1a1a;  /* Borda fica preta */
    }
    
    /* ❌ NÃO ALTERE: Número do portfólio */
    .portfolio-number {
        font-size: 48px;  /* Tamanho grande */
        font-weight: 900;  /* Peso extremamente pesado */
        color: #e0e0e0;  /* Cor cinza clara */
        margin-bottom: 20px;  /* Espaçamento inferior */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
    }
    
    /* ❌ NÃO ALTERE: Título do portfólio */
    .portfolio-title {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 700;  /* Peso pesado */
        color: #1a1a1a;  /* Texto preto */
        margin-bottom: 15px;  /* Espaçamento inferior */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
    }
    
    /* ❌ NÃO ALTERE: Descrição do portfólio */
    .portfolio-desc {
        font-size: 14px;  /* Tamanho pequeno */
        color: #666666;  /* Texto cinza */
        line-height: 1.8;  /* Altura da linha generosa */
    }
    
    /* ❌ NÃO ALTERE: Seção CTA */
    .cta-section {
        background: #1a1a1a;  /* Fundo preto */
        color: #ffffff;  /* Texto branco */
        padding: 120px 80px;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
    }
    
    /* ❌ NÃO ALTERE: Título CTA */
    .cta-title {
        font-size: 52px;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        margin-bottom: 30px;  /* Espaçamento inferior */
        font-family: 'Poppins', sans-serif;  /* Fonte Poppins */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
    }
    
    /* ❌ NÃO ALTERE: Descrição CTA */
    .cta-desc {
        font-size: 16px;  /* Tamanho médio */
        color: #cccccc;  /* Texto cinza claro */
        max-width: 700px;  /* Largura máxima */
        margin: 0 auto 50px;  /* Centraliza e espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Botão CTA */
    .cta-btn {
        background: #ffffff;  /* Fundo branco */
        color: #1a1a1a;  /* Texto preto */
        padding: 16px 60px;  /* Espaçamento interno */
        border: none;  /* Sem borda */
        border-radius: 2px;  /* Arredondamento mínimo */
        font-weight: 700;  /* Peso pesado */
        font-size: 12px;  /* Tamanho pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão CTA */
    .cta-btn:hover {
        background: #e0e0e0;  /* Cinza claro */
        transform: translateY(-2px);  /* Levanta o botão */
    }
    
    /* ❌ NÃO ALTERE: Footer */
    .footer {
        background: #0a0a0a;  /* Fundo muito preto */
        color: #999999;  /* Texto cinza */
        padding: 80px 80px;  /* Espaçamento interno */
        border-top: 1px solid #333333;  /* Borda superior cinza */
    }
    
    /* ❌ NÃO ALTERE: Grid do footer */
    .footer-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(4, 1fr);  /* 4 colunas */
        gap: 60px;  /* Espaçamento entre itens */
        max-width: 1600px;  /* Largura máxima */
        margin: 0 auto 60px;  /* Centraliza e espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Coluna do footer */
    .footer-col h4 {
        color: #ffffff;  /* Texto branco */
        font-size: 13px;  /* Tamanho pequeno */
        font-weight: 700;  /* Peso pesado */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        margin-bottom: 25px;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Links do footer */
    .footer-col a {
        display: block;  /* Exibe como bloco */
        color: #999999;  /* Texto cinza */
        text-decoration: none;  /* Remove sublinhado */
        font-size: 13px;  /* Tamanho pequeno */
        margin-bottom: 12px;  /* Espaçamento inferior */
        transition: color 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover nos links do footer */
    .footer-col a:hover { color: #ffffff; }  /* Fica branco ao passar o mouse */
    
    /* ❌ NÃO ALTERE: Rodapé do footer */
    .footer-bottom {
        text-align: center;  /* Texto centralizado */
        padding-top: 40px;  /* Espaçamento superior */
        border-top: 1px solid #333333;  /* Borda superior cinza */
        font-size: 12px;  /* Tamanho muito pequeno */
    }
    
    /* ❌ NÃO ALTERE: Responsividade */
    @media (max-width: 768px) {
        .navbar { padding: 15px 20px; flex-direction: column; gap: 15px; }
        .hero { flex-direction: column; padding: 50px 20px; }
        .hero-title { font-size: 42px; }
        .hero-visual { width: 100%; margin-top: 40px; }
        .stats-grid { grid-template-columns: repeat(2, 1fr); }
        .services-grid { grid-template-columns: 1fr; }
        .portfolio-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: repeat(2, 1fr); }
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVBAR ==========
# ✅ ALTERE: Logo e menu
navbar_html = '''<div class="navbar">
    <!-- ✅ ALTERE: Nome da empresa -->
    <div class="navbar-logo">CORPORATIVO</div>
    <!-- ✅ ALTERE: Menu de navegação -->
    <div class="navbar-nav">
        <a href="#sobre" class="nav-link">Sobre</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#servicos" class="nav-link">Serviços</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#portfolio" class="nav-link">Portfólio</a>  <!-- ✅ ALTERE: Texto do menu -->
        <a href="#contato" class="nav-link">Contato</a>  <!-- ✅ ALTERE: Texto do menu -->
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO ==========
# ✅ ALTERE: Título, descrição, emoji e botões
hero_html = '''<div class="hero">
    <div class="hero-content">
        <!-- ✅ ALTERE: Label do hero -->
        <div class="hero-label">Bem-vindo</div>
        <!-- ✅ ALTERE: Título principal -->
        <div class="hero-title">Excelência em Cada Detalhe</div>
        <!-- ✅ ALTERE: Descrição -->
        <div class="hero-desc">Soluções corporativas que transformam negócios. Expertise, inovação e resultados mensuráveis.</div>
        <!-- ✅ ALTERE: Botões e URLs -->
        <div class="hero-cta">
            <a href="https://www.google.com/" target="_blank" class="btn-primary">Começar</a>
            <a href="https://www.google.com/" target="_blank" class="btn-secondary">Saiba Mais</a>
        </div>
    </div>
    <!-- ✅ ALTERE: Emoji do visual -->
    <div class="hero-visual">📊</div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ========== SEÇÃO 5: ESTATÍSTICAS ==========
# ✅ ALTERE: Números e descrições
stats_html = '''<div class="stats-section">
    <div class="stats-grid">
        <!-- ✅ ALTERE: Estatística 1 -->
        <div class="stat-item">
            <div class="stat-number">500+</div>
            <div class="stat-label">Projetos Realizados</div>
        </div>
        <!-- ✅ ALTERE: Estatística 2 -->
        <div class="stat-item">
            <div class="stat-number">98%</div>
            <div class="stat-label">Satisfação de Clientes</div>
        </div>
        <!-- ✅ ALTERE: Estatística 3 -->
        <div class="stat-item">
            <div class="stat-number">25+</div>
            <div class="stat-label">Anos de Experiência</div>
        </div>
        <!-- ✅ ALTERE: Estatística 4 -->
        <div class="stat-item">
            <div class="stat-number">150+</div>
            <div class="stat-label">Profissionais Especializados</div>
        </div>
    </div>
</div>'''
st.markdown(stats_html, unsafe_allow_html=True)

# ========== SEÇÃO 6: SERVIÇOS ==========
# ✅ ALTERE: Título, ícones, títulos e descrições
services_html = '''<div id="servicos" class="services-section">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="section-title">Nossos Serviços</div>
    <div class="services-grid">
        <!-- ✅ ALTERE: Serviço 1 -->
        <div class="service-card">
            <div class="service-icon">🎯</div>  <!-- ✅ ALTERE: Emoji -->
            <div class="service-title">Consultoria Estratégica</div>  <!-- ✅ ALTERE: Título -->
            <div class="service-desc">Análise profunda de mercado e desenvolvimento de estratégias personalizadas para seu negócio.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
        <!-- ✅ ALTERE: Serviço 2 -->
        <div class="service-card">
            <div class="service-icon">💼</div>  <!-- ✅ ALTERE: Emoji -->
            <div class="service-title">Gestão Corporativa</div>  <!-- ✅ ALTERE: Título -->
            <div class="service-desc">Otimização de processos e implementação de sistemas para máxima eficiência operacional.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
        <!-- ✅ ALTERE: Serviço 3 -->
        <div class="service-card">
            <div class="service-icon">📈</div>  <!-- ✅ ALTERE: Emoji -->
            <div class="service-title">Transformação Digital</div>  <!-- ✅ ALTERE: Título -->
            <div class="service-desc">Modernização tecnológica e adaptação digital para o futuro dos negócios.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
    </div>
</div>'''
st.markdown(services_html, unsafe_allow_html=True)

# ========== SEÇÃO 7: PORTFÓLIO ==========
# ✅ ALTERE: Título, números, títulos e descrições dos casos
portfolio_html = '''<div id="portfolio" class="portfolio-section">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="section-title">Casos de Sucesso</div>
    <div class="portfolio-grid">
        <!-- ✅ ALTERE: Caso 1 -->
        <div class="portfolio-item">
            <div class="portfolio-number">01</div>  <!-- ✅ ALTERE: Número -->
            <div class="portfolio-title">Empresa Tecnológica</div>  <!-- ✅ ALTERE: Título -->
            <div class="portfolio-desc">Crescimento de 300% em receita através de estratégia digital integrada e otimização operacional.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
        <!-- ✅ ALTERE: Caso 2 -->
        <div class="portfolio-item">
            <div class="portfolio-number">02</div>  <!-- ✅ ALTERE: Número -->
            <div class="portfolio-title">Indústria de Manufatura</div>  <!-- ✅ ALTERE: Título -->
            <div class="portfolio-desc">Redução de custos em 45% com implementação de sistemas de gestão modernos.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
        <!-- ✅ ALTERE: Caso 3 -->
        <div class="portfolio-item">
            <div class="portfolio-number">03</div>  <!-- ✅ ALTERE: Número -->
            <div class="portfolio-title">Setor Financeiro</div>  <!-- ✅ ALTERE: Título -->
            <div class="portfolio-desc">Transformação digital completa com aumento de eficiência de 80% nos processos.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
        <!-- ✅ ALTERE: Caso 4 -->
        <div class="portfolio-item">
            <div class="portfolio-number">04</div>  <!-- ✅ ALTERE: Número -->
            <div class="portfolio-title">Varejo Premium</div>  <!-- ✅ ALTERE: Título -->
            <div class="portfolio-desc">Experiência de cliente revolucionária gerando aumento de 120% em vendas.</div>  <!-- ✅ ALTERE: Descrição -->
        </div>
    </div>
</div>'''
st.markdown(portfolio_html, unsafe_allow_html=True)

# ========== SEÇÃO 8: CTA ==========
# ✅ ALTERE: Título, descrição e botão
cta_html = '''<div id="contato" class="cta-section">
    <!-- ✅ ALTERE: Título CTA -->
    <div class="cta-title">Pronto para Transformar seu Negócio?</div>
    <!-- ✅ ALTERE: Descrição CTA -->
    <div class="cta-desc">Entre em contato conosco e descubra como podemos impulsionar seu crescimento.</div>
    <!-- ✅ ALTERE: Texto do botão e URL -->
    <a href="https://www.google.com/" target="_blank" class="cta-btn">Solicitar Consulta</a>
</div>'''
st.markdown(cta_html, unsafe_allow_html=True)

# ========== SEÇÃO 9: FOOTER ==========
# ✅ ALTERE: Títulos, links e copyright
footer_html = '''<div class="footer">
    <div class="footer-grid">
        <!-- ✅ ALTERE: Coluna 1 - Empresa -->
        <div class="footer-col">
            <h4>Empresa</h4>
            <a href="https://www.google.com/" target="_blank">Sobre Nós</a>
            <a href="https://www.google.com/" target="_blank">Carreira</a>
            <a href="https://www.google.com/" target="_blank">Imprensa</a>
            <a href="https://www.google.com/" target="_blank">Blog</a>
        </div>
        <!-- ✅ ALTERE: Coluna 2 - Serviços -->
        <div class="footer-col">
            <h4>Serviços</h4>
            <a href="https://www.google.com/" target="_blank">Consultoria</a>
            <a href="https://www.google.com/" target="_blank">Gestão</a>
            <a href="https://www.google.com/" target="_blank">Tecnologia</a>
            <a href="https://www.google.com/" target="_blank">Treinamento</a>
        </div>
        <!-- ✅ ALTERE: Coluna 3 - Recursos -->
        <div class="footer-col">
            <h4>Recursos</h4>
            <a href="https://www.google.com/" target="_blank">Documentação</a>
            <a href="https://www.google.com/" target="_blank">Guias</a>
            <a href="https://www.google.com/" target="_blank">Webinars</a>
            <a href="https://www.google.com/" target="_blank">Suporte</a>
        </div>
        <!-- ✅ ALTERE: Coluna 4 - Contato -->
        <div class="footer-col">
            <h4>Contato</h4>
            <a href="mailto:contato@corporativo.com.br">contato@corporativo.com.br</a>
            <a href="tel:+551198765432">+55 (11) 98765-4321</a>
            <a href="https://www.google.com/" target="_blank">São Paulo, Brasil</a>
            <a href="https://www.google.com/" target="_blank">LinkedIn</a>
        </div>
    </div>
    <!-- ✅ ALTERE: Copyright -->
    <div class="footer-bottom">
        © 2026 Corporativo Premium. Todos os direitos reservados.
    </div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
