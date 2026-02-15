# -*- coding: utf-8 -*-
"""

✅ ALTERE: Títulos, descrições, números, emails, links, cores
❌ NÃO ALTERE: CSS, estrutura HTML, configurações do Streamlit
"""

import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Criativa Pink - Criatividade em Cores",  # ✅ ALTERE: Título da aba
    page_icon="💖",  # ✅ ALTERE: Emoji da aba
    layout="wide",  # ❌ NÃO ALTERE: Layout em largura total
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Oculta a barra lateral
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
custom_css = """
<style>
    /* ❌ NÃO ALTERE: Importação de fontes do Google */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    
    /* ❌ NÃO ALTERE: Reset de estilos padrão */
    * {
        margin: 0;  /* Remove margem padrão */
        padding: 0;  /* Remove preenchimento padrão */
        box-sizing: border-box;  /* Inclui borda no tamanho total */
    }
    
    /* ❌ NÃO ALTERE: Estilos do body */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);  /* Gradiente rosa */
        background-size: 400% 400%;  /* Tamanho do gradiente para animação */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
        color: #ffffff;  /* Cor de texto branco */
        line-height: 1.8;  /* Altura da linha generosa */
        overflow-x: hidden;  /* Oculta scroll horizontal */
        animation: gradientShift 8s ease infinite;  /* Animação de gradiente */
    }
    
    /* ❌ NÃO ALTERE: Animação de gradiente */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }  /* Posição inicial */
        50% { background-position: 100% 50%; }  /* Posição do meio */
        100% { background-position: 0% 50%; }  /* Volta à posição inicial */
    }
    
    /* ❌ NÃO ALTERE: Remove decorações padrão */
    [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; background: transparent; }
    
    /* ❌ NÃO ALTERE: ANIMAÇÕES */
    @keyframes floatBounce {
        0%, 100% { transform: translateY(0px) rotateZ(-5deg); }  /* Posição normal */
        50% { transform: translateY(-30px) rotateZ(5deg); }  /* Salta para cima */
    }
    
    @keyframes spinGlow {
        0% { transform: rotate(0deg) scale(1); }  /* Começa normal */
        50% { transform: rotate(180deg) scale(1.1); }  /* Gira e cresce */
        100% { transform: rotate(360deg) scale(1); }  /* Volta ao normal */
    }
    
    @keyframes slideInPink {
        0% { transform: translateX(-100px) rotateY(45deg); opacity: 0; }  /* Começa à esquerda e invisível */
        100% { transform: translateX(0) rotateY(0deg); opacity: 1; }  /* Desliza para a direita e fica visível */
    }
    
    @keyframes popIn {
        0% { transform: scale(0.5); opacity: 0; }  /* Começa pequeno e invisível */
        100% { transform: scale(1); opacity: 1; }  /* Cresce e fica visível */
    }
    
    @keyframes neonFlicker {
        0%, 100% { text-shadow: 0 0 10px #ff1493, 0 0 20px #ff1493; }  /* Brilho fraco */
        50% { text-shadow: 0 0 20px #ff1493, 0 0 40px #ff1493, 0 0 60px #ff1493; }  /* Brilho forte */
    }
    
    /* ❌ NÃO ALTERE: NAVBAR */
    .navbar {
        background: linear-gradient(135deg, rgba(255, 20, 147, 0.95) 0%, rgba(255, 105, 180, 0.95) 100%);  /* Gradiente rosa */
        backdrop-filter: blur(20px);  /* Blur de fundo */
        padding: 25px 80px;  /* Espaçamento interno */
        display: flex;  /* Layout flexível */
        justify-content: space-between;  /* Espaço entre logo e nav */
        align-items: center;  /* Centraliza verticalmente */
        border-bottom: 3px dashed rgba(255, 255, 255, 0.5);  /* Borda inferior tracejada */
        position: sticky;  /* Fica fixo ao rolar */
        top: 0;  /* No topo */
        z-index: 100;  /* Acima de tudo */
        box-shadow: 0 8px 32px rgba(255, 20, 147, 0.4);  /* Sombra rosa */
    }
    
    /* ❌ NÃO ALTERE: Logo da navbar */
    .navbar-logo {
        font-size: 36px;  /* Tamanho grande */
        font-weight: 900;  /* Peso muito pesado */
        color: white;  /* Cor branca */
        letter-spacing: 3px;  /* Espaçamento entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        animation: neonFlicker 2s ease-in-out infinite;  /* Animação de brilho */
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);  /* Sombra de texto */
    }
    
    /* ❌ NÃO ALTERE: Container de navegação */
    .navbar-links {
        display: flex;  /* Layout flexível */
        gap: 50px;  /* Espaçamento entre itens */
        align-items: center;  /* Centraliza verticalmente */
    }
    
    /* ✅ ALTERE: Links de navegação (estilo) */
    .navbar-link {
        color: white;  /* Cor branca */
        text-decoration: none !important;  /* Remove sublinhado */
        font-weight: 600;  /* Peso pesado */
        font-size: 13px;  /* Tamanho pequeno */
        transition: all 0.3s ease;  /* Animação suave */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        position: relative;  /* Posicionamento relativo */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
    }
    
    /* ❌ NÃO ALTERE: Underline animado do link */
    .navbar-link::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        bottom: -8px;  /* Abaixo do texto */
        left: 0;  /* À esquerda */
        width: 0;  /* Largura inicial zero */
        height: 3px;  /* Altura da linha */
        background: white;  /* Cor branca */
        transition: width 0.3s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no link */
    .navbar-link:hover::before { width: 100%; }  /* Underline cresce */
    .navbar-link:hover { transform: scale(1.1); }  /* Texto cresce */
    
    /* ❌ NÃO ALTERE: Botão CTA da navbar */
    .navbar-cta {
        background: linear-gradient(135deg, white, #ffe0ec);  /* Gradiente branco/rosa claro */
        color: #ff1493;  /* Texto rosa */
        padding: 12px 32px;  /* Espaçamento interno */
        border-radius: 50px;  /* Arredondamento máximo */
        text-decoration: none !important;  /* Remove sublinhado */
        font-weight: 700;  /* Peso pesado */
        font-size: 12px;  /* Tamanho pequeno */
        transition: all 0.3s ease;  /* Animação suave */
        border: 2px solid white;  /* Borda branca */
        cursor: pointer;  /* Cursor de clique */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);  /* Sombra */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão CTA */
    .navbar-cta:hover {
        transform: translateY(-3px) scale(1.05);  /* Levanta e cresce */
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.5);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: HERO SECTION */
    .hero-section {
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);  /* Gradiente rosa */
        background-size: 400% 400%;  /* Tamanho do gradiente para animação */
        min-height: 800px;  /* Altura mínima */
        display: flex;  /* Layout flexível */
        align-items: center;  /* Centraliza verticalmente */
        justify-content: center;  /* Centraliza horizontalmente */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        padding: 80px 60px;  /* Espaçamento interno */
        animation: gradientShift 8s ease infinite;  /* Animação de gradiente */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero (círculo superior direito) */
    .hero-section::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        width: 800px;  /* Largura */
        height: 800px;  /* Altura */
        background: radial-gradient(circle, rgba(255, 255, 255, 0.15) 0%, transparent 70%);  /* Gradiente radial */
        border-radius: 50%;  /* Círculo */
        top: -200px;  /* Acima da tela */
        right: -200px;  /* À direita da tela */
        animation: floatBounce 6s ease-in-out infinite;  /* Animação de flutuação */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero (círculo inferior esquerdo) */
    .hero-section::after {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        width: 600px;  /* Largura */
        height: 600px;  /* Altura */
        background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);  /* Gradiente radial */
        border-radius: 50%;  /* Círculo */
        bottom: -150px;  /* Abaixo da tela */
        left: -150px;  /* À esquerda da tela */
        animation: floatBounce 8s ease-in-out infinite reverse;  /* Animação de flutuação reversa */
    }
    
    /* ❌ NÃO ALTERE: Container do hero */
    .hero-content {
        text-align: center;  /* Texto centralizado */
        z-index: 2;  /* Acima dos efeitos de fundo */
        position: relative;  /* Posicionamento relativo */
        max-width: 900px;  /* Largura máxima */
    }
    
    /* ✅ ALTERE: Título do hero */
    .hero-title {
        font-size: 80px;  /* Tamanho muito grande */
        font-weight: 900;  /* Peso muito pesado */
        margin-bottom: 20px;  /* Espaçamento inferior */
        color: white;  /* Cor branca */
        letter-spacing: -2px;  /* Espaçamento negativo entre letras */
        line-height: 1.1;  /* Altura da linha mínima */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        animation: neonFlicker 2s ease-in-out infinite;  /* Animação de brilho */
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.8);  /* Sombra de texto */
    }
    
    /* ✅ ALTERE: Subtítulo do hero */
    .hero-subtitle {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 400;  /* Peso normal */
        margin-bottom: 50px;  /* Espaçamento inferior */
        color: white;  /* Cor branca */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        animation: slideInPink 1s ease-out;  /* Animação de deslize */
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.6);  /* Sombra de texto */
    }
    
    /* ❌ NÃO ALTERE: Container de CTA do hero */
    .hero-cta-group {
        display: flex;  /* Layout flexível */
        gap: 20px;  /* Espaçamento entre botões */
        justify-content: center;  /* Centraliza horizontalmente */
        flex-wrap: wrap;  /* Quebra em múltiplas linhas */
    }
    
    /* ❌ NÃO ALTERE: Botão primário */
    .hero-cta-primary {
        background: linear-gradient(135deg, white, #ffe0ec);  /* Gradiente branco/rosa claro */
        color: #ff1493;  /* Texto rosa */
        padding: 18px 50px;  /* Espaçamento interno */
        border-radius: 50px;  /* Arredondamento máximo */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-decoration: none !important;  /* Remove sublinhado */
        transition: all 0.3s ease;  /* Animação suave */
        border: 2px solid white;  /* Borda branca */
        cursor: pointer;  /* Cursor de clique */
        display: inline-block;  /* Display inline-block */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        box-shadow: 0 8px 30px rgba(255, 255, 255, 0.4);  /* Sombra */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
        animation: popIn 0.8s ease-out;  /* Animação de pop */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão primário */
    .hero-cta-primary:hover {
        transform: translateY(-5px) scale(1.05);  /* Levanta e cresce */
        box-shadow: 0 12px 40px rgba(255, 255, 255, 0.6);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: Botão secundário */
    .hero-cta-secondary {
        background: transparent;  /* Fundo transparente */
        color: white;  /* Texto branco */
        padding: 18px 50px;  /* Espaçamento interno */
        border-radius: 50px;  /* Arredondamento máximo */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-decoration: none !important;  /* Remove sublinhado */
        transition: all 0.3s ease;  /* Animação suave */
        border: 2px solid white;  /* Borda branca */
        cursor: pointer;  /* Cursor de clique */
        display: inline-block;  /* Display inline-block */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);  /* Sombra */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
        animation: popIn 1s ease-out;  /* Animação de pop */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão secundário */
    .hero-cta-secondary:hover {
        background: white;  /* Fundo branco */
        color: #ff1493;  /* Texto rosa */
        box-shadow: 0 8px 30px rgba(255, 255, 255, 0.5);  /* Sombra */
    }
    
    /* ❌ NÃO ALTERE: FEATURES SECTION */
    .features-section {
        padding: 120px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #ff69b4 0%, #ff85c1 50%, #ffb6d9 100%);  /* Gradiente rosa */
        position: relative;  /* Posicionamento relativo */
    }
    
    /* ✅ ALTERE: Título da seção */
    .section-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 900;  /* Peso muito pesado */
        margin-bottom: 100px;  /* Espaçamento inferior */
        text-align: center;  /* Texto centralizado */
        color: white;  /* Cor branca */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        animation: neonFlicker 2s ease-in-out infinite;  /* Animação de brilho */
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);  /* Sombra de texto */
    }
    
    /* ❌ NÃO ALTERE: Grid de features */
    .features-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* Colunas responsivas */
        gap: 40px;  /* Espaçamento entre itens */
        max-width: 1400px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Card de feature */
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 224, 236, 0.95));  /* Gradiente branco/rosa claro */
        border: 3px dashed rgba(255, 20, 147, 0.4);  /* Borda tracejada rosa */
        padding: 50px 40px;  /* Espaçamento interno */
        border-radius: 30px;  /* Arredondamento grande */
        transition: all 0.4s ease;  /* Animação suave */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        animation: slideInPink 0.8s ease-out;  /* Animação de deslize */
        animation-fill-mode: both;  /* Mantém estado final */
        box-shadow: 0 8px 32px rgba(255, 20, 147, 0.2);  /* Sombra rosa */
    }
    
    /* ❌ NÃO ALTERE: Delays de animação */
    .feature-card:nth-child(1) { animation-delay: 0.1s; }
    .feature-card:nth-child(2) { animation-delay: 0.2s; }
    .feature-card:nth-child(3) { animation-delay: 0.3s; }
    .feature-card:nth-child(4) { animation-delay: 0.4s; }
    .feature-card:nth-child(5) { animation-delay: 0.5s; }
    .feature-card:nth-child(6) { animation-delay: 0.6s; }
    
    /* ❌ NÃO ALTERE: Efeito shine no card */
    .feature-card::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* No topo */
        left: -100%;  /* À esquerda da área */
        width: 100%;  /* Largura total */
        height: 100%;  /* Altura total */
        background: linear-gradient(90deg, transparent, rgba(255, 20, 147, 0.2), transparent);  /* Gradiente */
        transition: left 0.5s ease;  /* Animação suave */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no card */
    .feature-card:hover::before { left: 100%; }  /* Shine desliza */
    
    .feature-card:hover {
        transform: translateY(-20px) rotateX(5deg) scale(1.05);  /* Levanta, rotaciona e cresce */
        border-color: #ff1493;  /* Borda fica rosa */
        box-shadow: 0 20px 50px rgba(255, 20, 147, 0.3);  /* Sombra aumentada */
    }
    
    /* ✅ ALTERE: Ícone do card */
    .feature-icon {
        font-size: 48px;  /* Tamanho grande */
        margin-bottom: 20px;  /* Espaçamento inferior */
        animation: spinGlow 4s ease-in-out infinite;  /* Animação de giro */
    }
    
    /* ✅ ALTERE: Título do card */
    .feature-title {
        font-size: 24px;  /* Tamanho grande */
        font-weight: 800;  /* Peso muito pesado */
        margin-bottom: 15px;  /* Espaçamento inferior */
        color: #ff1493;  /* Cor rosa */
        letter-spacing: 0.5px;  /* Espaçamento entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
    }
    
    /* ✅ ALTERE: Descrição do card */
    .feature-desc {
        font-size: 15px;  /* Tamanho pequeno */
        color: #666666;  /* Cor cinza */
        line-height: 1.8;  /* Altura da linha generosa */
        font-weight: 400;  /* Peso normal */
    }
    
    /* ❌ NÃO ALTERE: PRICING SECTION */
    .pricing-section {
        padding: 120px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #ff85c1 0%, #ffb6d9 50%, #ffc0cb 100%);  /* Gradiente rosa */
    }
    
    /* ✅ ALTERE: Título de preços */
    .pricing-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 900;  /* Peso muito pesado */
        margin-bottom: 100px;  /* Espaçamento inferior */
        text-align: center;  /* Texto centralizado */
        color: white;  /* Cor branca */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        animation: neonFlicker 2s ease-in-out infinite;  /* Animação de brilho */
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.6);  /* Sombra de texto */
    }
    
    /* ❌ NÃO ALTERE: Wrapper da tabela de preços */
    .pricing-table-wrapper {
        max-width: 1200px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(255, 224, 236, 0.98));  /* Gradiente branco/rosa claro */
        border: 3px dashed rgba(255, 20, 147, 0.4);  /* Borda tracejada rosa */
        border-radius: 30px;  /* Arredondamento grande */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        box-shadow: 0 20px 60px rgba(255, 20, 147, 0.25);  /* Sombra rosa */
        animation: popIn 0.8s ease-out;  /* Animação de pop */
    }
    
    /* ❌ NÃO ALTERE: Tabela de preços */
    .pricing-table {
        width: 100%;  /* Largura total */
        border-collapse: collapse;  /* Remove espaço entre células */
    }
    
    /* ❌ NÃO ALTERE: Cabeçalho da tabela */
    .pricing-table thead {
        background: linear-gradient(135deg, #ff1493, #ff69b4);  /* Gradiente rosa */
        color: white;  /* Cor branca */
    }
    
    /* ❌ NÃO ALTERE: Célula de cabeçalho */
    .pricing-table th {
        padding: 25px;  /* Espaçamento interno */
        text-align: left;  /* Alinhamento à esquerda */
        font-weight: 700;  /* Peso pesado */
        font-size: 16px;  /* Tamanho grande */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        border-right: 1px solid rgba(255, 255, 255, 0.2);  /* Borda direita */
    }
    
    /* ❌ NÃO ALTERE: Última célula de cabeçalho */
    .pricing-table th:last-child {
        border-right: none;  /* Sem borda direita */
    }
    
    /* ❌ NÃO ALTERE: Célula de dados */
    .pricing-table td {
        padding: 20px 25px;  /* Espaçamento interno */
        border-bottom: 1px solid rgba(255, 20, 147, 0.15);  /* Borda inferior rosa */
        font-size: 14px;  /* Tamanho pequeno */
        color: #2d2d2d;  /* Cor escura */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover na linha */
    .pricing-table tbody tr:hover {
        background: rgba(255, 20, 147, 0.08);  /* Fundo rosa semi-transparente */
    }
    
    /* ❌ NÃO ALTERE: Última linha */
    .pricing-table tbody tr:last-child td {
        border-bottom: none;  /* Sem borda inferior */
    }
    
    /* ✅ ALTERE: Valor de preço */
    .price-value {
        font-size: 28px;  /* Tamanho grande */
        font-weight: 700;  /* Peso pesado */
        color: #ff1493;  /* Cor rosa */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
    }
    
    /* ✅ ALTERE: Check de feature */
    .feature-check {
        color: #ff1493;  /* Cor rosa */
        font-weight: 700;  /* Peso pesado */
        font-size: 18px;  /* Tamanho grande */
    }
    
    /* ✅ ALTERE: Cross de feature */
    .feature-cross {
        color: #999999;  /* Cor cinza */
        font-weight: 700;  /* Peso pesado */
        font-size: 18px;  /* Tamanho grande */
    }
    
    /* ❌ NÃO ALTERE: CTA FINAL */
    .cta-final-section {
        padding: 150px 80px;  /* Espaçamento interno */
        background: linear-gradient(135deg, #ff1493 0%, #ff69b4 25%, #ff85c1 50%, #ffb6d9 75%, #ffc0cb 100%);  /* Gradiente rosa */
        background-size: 400% 400%;  /* Tamanho do gradiente para animação */
        text-align: center;  /* Texto centralizado */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        animation: gradientShift 8s ease infinite;  /* Animação de gradiente */
    }
    
    /* ❌ NÃO ALTERE: Overlay do CTA */
    .cta-final-section::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* No topo */
        left: 0;  /* À esquerda */
        right: 0;  /* À direita */
        bottom: 0;  /* No fundo */
        background: rgba(255, 255, 255, 0.1);  /* Overlay branco semi-transparente */
    }
    
    /* ❌ NÃO ALTERE: Conteúdo do CTA */
    .cta-final-content {
        position: relative;  /* Posicionamento relativo */
        z-index: 2;  /* Acima do overlay */
    }
    
    /* ✅ ALTERE: Título do CTA */
    .cta-final-title {
        font-size: 56px;  /* Tamanho muito grande */
        font-weight: 900;  /* Peso muito pesado */
        margin-bottom: 20px;  /* Espaçamento inferior */
        color: white;  /* Cor branca */
        letter-spacing: -1px;  /* Espaçamento negativo entre letras */
        font-family: 'Poppins', sans-serif;  /* Fonte especial */
        animation: neonFlicker 2s ease-in-out infinite;  /* Animação de brilho */
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.8);  /* Sombra de texto */
    }
    
    /* ✅ ALTERE: Descrição do CTA */
    .cta-final-desc {
        font-size: 20px;  /* Tamanho grande */
        margin-bottom: 50px;  /* Espaçamento inferior */
        color: white;  /* Cor branca */
        max-width: 700px;  /* Largura máxima */
        margin-left: auto;  /* Centraliza à esquerda */
        margin-right: auto;  /* Centraliza à direita */
        font-weight: 400;  /* Peso normal */
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.6);  /* Sombra de texto */
    }
    
    /* ❌ NÃO ALTERE: Botão do CTA */
    .cta-final-button {
        background: white;  /* Fundo branco */
        color: #ff1493;  /* Texto rosa */
        padding: 18px 60px;  /* Espaçamento interno */
        border: 3px dashed #ff1493;  /* Borda tracejada rosa */
        border-radius: 50px;  /* Arredondamento máximo */
        font-weight: 700;  /* Peso pesado */
        font-size: 14px;  /* Tamanho pequeno */
        text-decoration: none !important;  /* Remove sublinhado */
        transition: all 0.3s ease;  /* Animação suave */
        cursor: pointer;  /* Cursor de clique */
        display: inline-block;  /* Display inline-block */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 1px;  /* Espaçamento entre letras */
        box-shadow: 0 8px 25px rgba(255, 255, 255, 0.3);  /* Sombra */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
        animation: popIn 1.2s ease-out;  /* Animação de pop */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão */
    .cta-final-button:hover {
        transform: translateY(-5px) scale(1.05);  /* Levanta e cresce */
        box-shadow: 0 12px 35px rgba(255, 255, 255, 0.5);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: FOOTER */
    .footer {
        background: rgba(255, 20, 147, 0.95);  /* Fundo rosa */
        color: white;  /* Cor branca */
        padding: 80px;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        border-top: 3px dashed rgba(255, 255, 255, 0.5);  /* Borda superior tracejada */
        box-shadow: 0 -8px 32px rgba(255, 20, 147, 0.3);  /* Sombra rosa */
    }
    
    /* ✅ ALTERE: Texto do footer */
    .footer-text {
        font-size: 14px;  /* Tamanho pequeno */
        margin-bottom: 12px;  /* Espaçamento inferior */
        font-weight: 400;  /* Peso normal */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
    }
    
    /* ✅ ALTERE: Copyright do footer */
    .footer-copyright {
        border-top: 1px solid rgba(255, 255, 255, 0.3);  /* Borda superior */
        padding-top: 40px;  /* Espaçamento superior */
        margin-top: 40px;  /* Espaçamento superior */
        font-size: 12px;  /* Tamanho muito pequeno */
        text-transform: uppercase;  /* Maiúsculas */
        letter-spacing: 2px;  /* Espaçamento entre letras */
        font-family: 'Fredoka', sans-serif;  /* Fonte padrão */
    }
    
    /* ❌ NÃO ALTERE: Responsividade */
    @media (max-width: 768px) {
        .navbar { flex-direction: column; gap: 20px; padding: 15px 20px; }
        .navbar-links { flex-direction: column; gap: 15px; width: 100%; }
        .hero-section { min-height: 500px; padding: 40px 20px; }
        .hero-title { font-size: 42px; }
        .features-section, .pricing-section, .cta-final-section { padding: 80px 20px; }
        .section-title, .pricing-title, .cta-final-title { font-size: 36px; }
        .pricing-table { font-size: 12px; }
        .pricing-table th, .pricing-table td { padding: 15px; }
    }
</style>
"""

# ❌ NÃO ALTERE: Renderiza o CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ========== SEÇÃO 3: NAVBAR ==========
# ✅ ALTERE: Logo, textos dos links e URLs
navbar_html = '''<div class="navbar">
    <!-- ✅ ALTERE: Logo -->
    <div class="navbar-logo">criativa PINK</div>
    <div class="navbar-links">
        <!-- ✅ ALTERE: Links de navegação (texto e URL) -->
        <a href="#colecao" class="navbar-link">Coleção</a>
        <a href="#vibes" class="navbar-link">Vibes</a>
        <a href="#precos" class="navbar-link">Preços</a>
        <a href="#contato" class="navbar-link">Contato</a>
        <!-- ✅ ALTERE: Botão CTA (texto e URL) -->
        <a href="https://www.google.com/" target="_blank" class="navbar-cta">Entrar</a>
    </div>
</div>'''
st.markdown(navbar_html, unsafe_allow_html=True)

# ========== SEÇÃO 4: HERO ==========
# ✅ ALTERE: Título, subtítulo e botões
hero_html = '''<div class="hero-section" id="colecao">
    <div class="hero-content">
        <!-- ✅ ALTERE: Título -->
        <div class="hero-title">VIBE criativa</div>
        <!-- ✅ ALTERE: Subtítulo -->
        <div class="hero-subtitle">Criatividade, Cor e Diversão em Cada Clique</div>
        <div class="hero-cta-group">
            <!-- ✅ ALTERE: Texto do botão e URL -->
            <a href="https://www.google.com/" target="_blank" class="hero-cta-primary">Explorar Agora</a>
            <!-- ✅ ALTERE: Texto do botão e URL -->
            <a href="https://www.google.com/" target="_blank" class="hero-cta-secondary">Saiba Mais</a>
        </div>
    </div>
</div>'''
st.markdown(hero_html, unsafe_allow_html=True)

# ========== SEÇÃO 5: FEATURES ==========
# ✅ ALTERE: Título, ícones, títulos e descrições
features_html = '''<div class="features-section" id="vibes">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="section-title">Por Que Amar</div>
    <div class="features-grid">
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">🎀</div>
            <div class="feature-title">Estilo Único</div>
            <div class="feature-desc">Expressa sua personalidade com cores vibrantes e design criativo.</div>
        </div>
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">💖</div>
            <div class="feature-title">Diversão Total</div>
            <div class="feature-desc">Cada interação é uma experiência alegre e envolvente.</div>
        </div>
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">✨</div>
            <div class="feature-title">Criatividade</div>
            <div class="feature-desc">Ferramentas poderosas para soltar sua imaginação.</div>
        </div>
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">🌸</div>
            <div class="feature-title">Comunidade</div>
            <div class="feature-desc">Conecte-se com pessoas que compartilham sua vibe.</div>
        </div>
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Customização</div>
            <div class="feature-desc">Personalize tudo do seu jeito, sem limites.</div>
        </div>
        <div class="feature-card">
            <!-- ✅ ALTERE: Ícone, título e descrição -->
            <div class="feature-icon">🚀</div>
            <div class="feature-title">Velocidade</div>
            <div class="feature-desc">Rápido, responsivo e sempre pronto para você.</div>
        </div>
    </div>
</div>'''
st.markdown(features_html, unsafe_allow_html=True)

# ========== SEÇÃO 6: PRICING ==========
# ✅ ALTERE: Título, nomes dos planos, preços e features
pricing_html = '''<div class="pricing-section" id="precos">
    <!-- ✅ ALTERE: Título da seção -->
    <div class="pricing-title">Planos Incríveis</div>
    <div class="pricing-table-wrapper">
        <table class="pricing-table">
            <thead>
                <tr>
                    <!-- ✅ ALTERE: Nomes dos planos -->
                    <th>Recurso</th>
                    <th>Rosa</th>
                    <th>Magenta</th>
                    <th>Fúcsia</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Preço Mensal</strong></td>
                    <!-- ✅ ALTERE: Preços -->
                    <td><span class="price-value">R$ 49</span></td>
                    <td><span class="price-value">R$ 99</span></td>
                    <td><span class="price-value">R$ 199</span></td>
                </tr>
                <tr>
                    <!-- ✅ ALTERE: Nome da feature -->
                    <td>Acesso Básico</td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <!-- ✅ ALTERE: Nome da feature -->
                    <td>Cores Exclusivas</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <!-- ✅ ALTERE: Nome da feature -->
                    <td>Suporte Prioritário</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <!-- ✅ ALTERE: Nome da feature -->
                    <td>Conteúdo Ilimitado</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
                <tr>
                    <!-- ✅ ALTERE: Nome da feature -->
                    <td>Comunidade VIP</td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-cross">✗</span></td>
                    <td><span class="feature-check">✓</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>'''
st.markdown(pricing_html, unsafe_allow_html=True)

# ========== SEÇÃO 7: CTA FINAL ==========
# ✅ ALTERE: Título, descrição e botão
cta_final_html = '''<div class="cta-final-section" id="contato">
    <div class="cta-final-content">
        <!-- ✅ ALTERE: Título -->
        <div class="cta-final-title">Pronta para Brilhar?</div>
        <!-- ✅ ALTERE: Descrição -->
        <div class="cta-final-desc">Junte-se à revolução rosa e descubra um mundo de cores, criatividade e diversão!</div>
        <!-- ✅ ALTERE: Texto do botão e URL -->
        <a href="https://www.google.com/" target="_blank" class="cta-final-button">Começar a Jornada</a>
    </div>
</div>'''
st.markdown(cta_final_html, unsafe_allow_html=True)

# ========== SEÇÃO 8: FOOTER ==========
# ✅ ALTERE: Email, telefone, endereço e copyright
footer_html = '''<div class="footer">
    <!-- ✅ ALTERE: Email e telefone -->
    <div class="footer-text">Email: hello@criativapink.com | Telefone: +55 (99) 99999-9999</div>
    <!-- ✅ ALTERE: Endereço -->
    <div class="footer-text">Endereço: Av. Criatividade, 1000 - São Paulo, SP</div>
    <!-- ✅ ALTERE: Copyright -->
    <div class="footer-copyright">© 2025 criativa Pink. Todos os direitos reservados. Vibe Rosa é Vibe Boa!</div>
</div>'''
st.markdown(footer_html, unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
