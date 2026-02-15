# -*- coding: utf-8 -*-
"""
Landing Page Premium em Streamlit - Nexus AI

Autor: Manus AI
Data: 11 de Fevereiro de 2026

Uma landing page profissional e interativa para maximizar conversões.
Inclui design moderno, animações CSS, componentes interativos e estrutura
otimizada para vendas.

✅ ALTERE: Títulos, descrições, preços, emails e URLs
❌ NÃO ALTERE: CSS, estrutura HTML, configurações do Streamlit
"""

import streamlit as st  # ❌ NÃO ALTERE: Importa a biblioteca Streamlit para criar a aplicação web

# ========== SEÇÃO 1: CONFIGURAÇÃO DA PÁGINA ==========
# ❌ NÃO ALTERE: Define as configurações básicas da página
st.set_page_config(
    page_title="Nexus AI - Transforme Seus Dados em Lucro",  # ✅ ALTERE: Título que aparece na aba do navegador
    page_icon="✨",  # ✅ ALTERE: Emoji que aparece na aba do navegador
    layout="wide",  # ❌ NÃO ALTERE: Define o layout como largura total
    initial_sidebar_state="collapsed"  # ❌ NÃO ALTERE: Oculta a barra lateral
)

# ========== SEÇÃO 2: CSS E ESTILOS VISUAIS ==========
# ❌ NÃO ALTERE: Bloco CSS que define todas as cores, fontes, animações e efeitos
# Alterar aqui pode quebrar completamente o design da página
st.markdown('''
<style>
    /* ❌ NÃO ALTERE: Reset de estilos padrão */
    * {
        margin: 0;  /* Remove margem padrão */
        padding: 0;  /* Remove preenchimento padrão */
        box-sizing: border-box;  /* Inclui borda no tamanho total */
    }
    
    /* ❌ NÃO ALTERE: Estilos do body */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  /* Fonte padrão */
        background: linear-gradient(135deg, #0f0f1e 0%, #1a1a2e 50%, #16213e 100%);  /* Gradiente de fundo */
        color: #e0e0e0;  /* Cor de texto padrão */
        line-height: 1.6;  /* Altura da linha */
    }
    
    /* ❌ NÃO ALTERE: Estilos do main */
    .main {
        background: transparent;  /* Fundo transparente */
    }
    
    /* ❌ NÃO ALTERE: Seção hero */
    .hero-section {
        background: linear-gradient(135deg, rgba(15, 15, 30, 0.9) 0%, rgba(26, 26, 46, 0.9) 50%, rgba(22, 33, 62, 0.9) 100%);  /* Gradiente de fundo */
        padding: 6rem 2rem;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        position: relative;  /* Posicionamento relativo */
        overflow: hidden;  /* Oculta conteúdo que sai da área */
        border-bottom: 2px solid rgba(0, 188, 212, 0.3);  /* Borda inferior ciano */
    }
    
    /* ❌ NÃO ALTERE: Efeito de fundo do hero */
    .hero-section::before {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        top: 0;  /* No topo */
        left: 0;  /* À esquerda */
        right: 0;  /* À direita */
        bottom: 0;  /* No fundo */
        background: radial-gradient(circle at 20% 50%, rgba(0, 188, 212, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 80%, rgba(255, 64, 129, 0.1) 0%, transparent 50%);  /* Gradientes radiais */
        pointer-events: none;  /* Não interfere com cliques */
    }
    
    /* ❌ NÃO ALTERE: Conteúdo do hero */
    .hero-text {
        position: relative;  /* Posicionamento relativo */
        z-index: 1;  /* Acima do efeito de fundo */
        max-width: 900px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Título do hero */
    .hero-title {
        font-size: 4rem;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        margin-bottom: 1.5rem;  /* Espaçamento inferior */
        background: linear-gradient(135deg, #00bcd4 0%, #ff4081 50%, #00bcd4 100%);  /* Gradiente de cores */
        -webkit-background-clip: text;  /* Aplica gradiente ao texto (webkit) */
        -webkit-text-fill-color: transparent;  /* Texto transparente (webkit) */
        background-clip: text;  /* Aplica gradiente ao texto */
        animation: gradientShift 3s ease infinite;  /* Animação de mudança de gradiente */
    }
    
    /* ❌ NÃO ALTERE: Animação do gradiente */
    @keyframes gradientShift {
        0%, 100% { filter: hue-rotate(0deg); }  /* Rotação de cor normal */
        50% { filter: hue-rotate(10deg); }  /* Rotação de cor no meio */
    }
    
    /* ❌ NÃO ALTERE: Subtítulo do hero */
    .hero-subtitle {
        font-size: 1.3rem;  /* Tamanho grande */
        color: #b0b0b0;  /* Cor cinza claro */
        margin-bottom: 2.5rem;  /* Espaçamento inferior */
        line-height: 1.8;  /* Altura da linha generosa */
    }
    
    /* ❌ NÃO ALTERE: Botão do hero (LINK, não button) */
    .hero-button {
        display: inline-block;  /* Exibe como bloco inline */
        background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);  /* Gradiente de fundo ciano */
        color: white;  /* Texto branco */
        padding: 1.2rem 2.5rem;  /* Espaçamento interno */
        border-radius: 50px;  /* Arredondamento máximo */
        text-decoration: none !important;  /* Remove sublinhado */
        font-weight: 700;  /* Peso pesado */
        font-size: 1.1rem;  /* Tamanho grande */
        transition: all 0.3s ease;  /* Animação suave */
        box-shadow: 0 10px 30px rgba(0, 188, 212, 0.3);  /* Sombra ciano */
        border: 2px solid transparent;  /* Borda transparente */
        cursor: pointer;  /* Cursor de clique */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão */
    .hero-button:hover {
        transform: translateY(-3px);  /* Levanta o botão */
        box-shadow: 0 15px 40px rgba(0, 188, 212, 0.5);  /* Sombra aumentada */
        background: linear-gradient(135deg, #0097a7 0%, #00838f 100%);  /* Gradiente mais escuro */
    }
    
    /* ❌ NÃO ALTERE: Subtexto do hero */
    .hero-subtext {
        margin-top: 1.5rem;  /* Espaçamento superior */
        color: #888;  /* Cor cinza */
        font-size: 0.95rem;  /* Tamanho pequeno */
    }
    
    /* ❌ NÃO ALTERE: Seções gerais */
    .section {
        padding: 5rem 2rem;  /* Espaçamento interno */
        max-width: 1200px;  /* Largura máxima */
        margin: 0 auto;  /* Centraliza */
    }
    
    /* ❌ NÃO ALTERE: Título da seção */
    .section-title {
        font-size: 2.8rem;  /* Tamanho muito grande */
        font-weight: 700;  /* Peso pesado */
        text-align: center;  /* Texto centralizado */
        margin-bottom: 3rem;  /* Espaçamento inferior */
        color: #00bcd4;  /* Cor ciano */
        position: relative;  /* Posicionamento relativo */
        padding-bottom: 1rem;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Underline do título */
    .section-title::after {
        content: '';  /* Cria elemento vazio */
        position: absolute;  /* Posicionamento absoluto */
        bottom: 0;  /* No fundo */
        left: 50%;  /* Centralizado horizontalmente */
        transform: translateX(-50%);  /* Centraliza */
        width: 60px;  /* Largura */
        height: 4px;  /* Altura */
        background: linear-gradient(90deg, #00bcd4, #ff4081);  /* Gradiente */
        border-radius: 2px;  /* Arredondamento suave */
    }
    
    /* ❌ NÃO ALTERE: Grid de features */
    .features-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* Colunas responsivas */
        gap: 2rem;  /* Espaçamento entre itens */
        margin-top: 3rem;  /* Espaçamento superior */
    }
    
    /* ❌ NÃO ALTERE: Card de feature */
    .feature-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);  /* Gradiente de fundo */
        border: 1px solid rgba(0, 188, 212, 0.2);  /* Borda ciano semi-transparente */
        border-radius: 15px;  /* Arredondamento */
        padding: 2.5rem;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        transition: all 0.3s ease;  /* Animação suave */
        backdrop-filter: blur(10px);  /* Blur de fundo */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no card */
    .feature-card:hover {
        transform: translateY(-10px);  /* Levanta o card */
        border-color: rgba(0, 188, 212, 0.5);  /* Borda fica mais visível */
        box-shadow: 0 20px 40px rgba(0, 188, 212, 0.2);  /* Sombra aumentada */
        background: linear-gradient(135deg, rgba(0, 188, 212, 0.1) 0%, rgba(255, 64, 129, 0.05) 100%);  /* Gradiente mais visível */
    }
    
    /* ❌ NÃO ALTERE: Ícone da feature */
    .feature-icon {
        font-size: 3.5rem;  /* Tamanho muito grande */
        margin-bottom: 1.5rem;  /* Espaçamento inferior */
        display: inline-block;  /* Exibe como bloco inline */
        animation: float 3s ease-in-out infinite;  /* Animação de flutuação */
    }
    
    /* ❌ NÃO ALTERE: Animação de flutuação */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }  /* Posição normal */
        50% { transform: translateY(-10px); }  /* Sobe 10px no meio */
    }
    
    /* ❌ NÃO ALTERE: Título do card */
    .feature-card h3 {
        font-size: 1.5rem;  /* Tamanho grande */
        margin-bottom: 1rem;  /* Espaçamento inferior */
        color: #00bcd4;  /* Cor ciano */
    }
    
    /* ❌ NÃO ALTERE: Descrição do card */
    .feature-card p {
        color: #a0a0a0;  /* Cor cinza */
        line-height: 1.7;  /* Altura da linha generosa */
    }
    
    /* ❌ NÃO ALTERE: Container de logos */
    .logos-container {
        display: flex;  /* Layout flexível */
        justify-content: center;  /* Centraliza horizontalmente */
        align-items: center;  /* Centraliza verticalmente */
        gap: 3rem;  /* Espaçamento entre itens */
        flex-wrap: wrap;  /* Quebra em múltiplas linhas */
        margin: 3rem 0;  /* Espaçamento vertical */
        opacity: 0.7;  /* Opacidade reduzida */
    }
    
    /* ❌ NÃO ALTERE: Item de logo */
    .logo-item {
        font-size: 1.3rem;  /* Tamanho grande */
        font-weight: 600;  /* Peso pesado */
        color: #666;  /* Cor cinza */
        padding: 1rem 2rem;  /* Espaçamento interno */
        border: 1px solid rgba(0, 188, 212, 0.2);  /* Borda ciano semi-transparente */
        border-radius: 8px;  /* Arredondamento */
        background: rgba(0, 188, 212, 0.05);  /* Fundo ciano semi-transparente */
    }
    
    /* ❌ NÃO ALTERE: Grid de pricing */
    .pricing-grid {
        display: grid;  /* Layout em grade */
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));  /* Colunas responsivas */
        gap: 2rem;  /* Espaçamento entre itens */
        margin-top: 3rem;  /* Espaçamento superior */
    }
    
    /* ❌ NÃO ALTERE: Card de pricing */
    .pricing-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);  /* Gradiente de fundo */
        border: 2px solid rgba(0, 188, 212, 0.2);  /* Borda ciano */
        border-radius: 15px;  /* Arredondamento */
        padding: 2.5rem;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        transition: all 0.3s ease;  /* Animação suave */
        position: relative;  /* Posicionamento relativo */
    }
    
    /* ❌ NÃO ALTERE: Card de pricing em destaque */
    .pricing-card.featured {
        border-color: rgba(0, 188, 212, 0.8);  /* Borda mais visível */
        transform: scale(1.05);  /* Aumenta o tamanho */
        box-shadow: 0 20px 50px rgba(0, 188, 212, 0.3);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no card */
    .pricing-card:hover {
        border-color: rgba(0, 188, 212, 0.6);  /* Borda fica mais visível */
        box-shadow: 0 15px 40px rgba(0, 188, 212, 0.2);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: Título do card */
    .pricing-card h3 {
        font-size: 1.8rem;  /* Tamanho grande */
        margin-bottom: 1rem;  /* Espaçamento inferior */
        color: #00bcd4;  /* Cor ciano */
    }
    
    /* ❌ NÃO ALTERE: Preço */
    .price {
        font-size: 2.5rem;  /* Tamanho muito grande */
        font-weight: 800;  /* Peso muito pesado */
        color: #00bcd4;  /* Cor ciano */
        margin-bottom: 1.5rem;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Período do preço */
    .price-period {
        color: #888;  /* Cor cinza */
        font-size: 0.9rem;  /* Tamanho pequeno */
    }
    
    /* ❌ NÃO ALTERE: Lista de features */
    .pricing-features {
        list-style: none;  /* Remove marcadores */
        margin: 2rem 0;  /* Espaçamento vertical */
        text-align: left;  /* Texto alinhado à esquerda */
    }
    
    /* ❌ NÃO ALTERE: Item da lista */
    .pricing-features li {
        padding: 0.8rem 0;  /* Espaçamento interno */
        color: #a0a0a0;  /* Cor cinza */
        border-bottom: 1px solid rgba(0, 188, 212, 0.1);  /* Borda inferior */
    }
    
    /* ❌ NÃO ALTERE: Último item da lista */
    .pricing-features li:last-child {
        border-bottom: none;  /* Remove borda */
    }
    
    /* ❌ NÃO ALTERE: Botão de pricing (LINK, não button) */
    .pricing-button {
        width: 100%;  /* Largura total */
        padding: 1rem;  /* Espaçamento interno */
        margin-top: 1.5rem;  /* Espaçamento superior */
        background: linear-gradient(135deg, #00bcd4 0%, #0097a7 100%);  /* Gradiente de fundo ciano */
        color: white;  /* Texto branco */
        border: none;  /* Sem borda */
        border-radius: 8px;  /* Arredondamento */
        font-weight: 700;  /* Peso pesado */
        cursor: pointer;  /* Cursor de clique */
        transition: all 0.3s ease;  /* Animação suave */
        text-decoration: none !important;  /* Remove sublinhado */
    }
    
    /* ❌ NÃO ALTERE: Efeito hover no botão */
    .pricing-button:hover {
        transform: translateY(-2px);  /* Levanta o botão */
        box-shadow: 0 10px 25px rgba(0, 188, 212, 0.3);  /* Sombra aumentada */
    }
    
    /* ❌ NÃO ALTERE: Card de depoimento */
    .testimonial-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(0, 188, 212, 0.05) 100%);  /* Gradiente de fundo */
        border-left: 5px solid #00bcd4;  /* Borda esquerda ciano */
        border-radius: 10px;  /* Arredondamento */
        padding: 2rem;  /* Espaçamento interno */
        margin: 2rem 0;  /* Espaçamento vertical */
        max-width: 700px;  /* Largura máxima */
        margin-left: auto;  /* Centraliza à esquerda */
        margin-right: auto;  /* Centraliza à direita */
    }
    
    /* ❌ NÃO ALTERE: Texto do depoimento */
    .testimonial-text {
        font-size: 1.1rem;  /* Tamanho grande */
        color: #c0c0c0;  /* Cor cinza claro */
        margin-bottom: 1rem;  /* Espaçamento inferior */
        font-style: italic;  /* Itálico */
    }
    
    /* ❌ NÃO ALTERE: Autor do depoimento */
    .testimonial-author {
        color: #00bcd4;  /* Cor ciano */
        font-weight: 700;  /* Peso pesado */
    }
    
    /* ❌ NÃO ALTERE: Seção CTA */
    .cta-section {
        background: linear-gradient(135deg, rgba(0, 188, 212, 0.1) 0%, rgba(255, 64, 129, 0.1) 100%);  /* Gradiente de fundo */
        border: 2px solid rgba(0, 188, 212, 0.3);  /* Borda ciano */
        border-radius: 20px;  /* Arredondamento */
        padding: 4rem 2rem;  /* Espaçamento interno */
        text-align: center;  /* Texto centralizado */
        margin: 4rem 0;  /* Espaçamento vertical */
    }
    
    /* ❌ NÃO ALTERE: Título CTA */
    .cta-title {
        font-size: 2.5rem;  /* Tamanho muito grande */
        margin-bottom: 1rem;  /* Espaçamento inferior */
        color: #00bcd4;  /* Cor ciano */
    }
    
    /* ❌ NÃO ALTERE: Subtítulo CTA */
    .cta-subtitle {
        font-size: 1.2rem;  /* Tamanho grande */
        color: #a0a0a0;  /* Cor cinza */
        margin-bottom: 2rem;  /* Espaçamento inferior */
    }
    
    /* ❌ NÃO ALTERE: Footer */
    .footer {
        text-align: center;  /* Texto centralizado */
        padding: 3rem 2rem;  /* Espaçamento interno */
        border-top: 1px solid rgba(0, 188, 212, 0.2);  /* Borda superior */
        color: #666;  /* Cor cinza */
        margin-top: 4rem;  /* Espaçamento superior */
    }
    
    /* ❌ NÃO ALTERE: Responsividade */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;  /* Reduz tamanho em mobile */
        }
        
        .section-title {
            font-size: 2rem;  /* Reduz tamanho em mobile */
        }
        
        .pricing-card.featured {
            transform: scale(1);  /* Remove aumento em mobile */
        }
    }
</style>
''', unsafe_allow_html=True)

# ========== SEÇÃO 3: HERO ==========
# ✅ ALTERE: Título, descrição e botão
st.markdown('''
<div class="hero-section">
    <div class="hero-text">
        <!-- ✅ ALTERE: Título principal -->
        <h1 class="hero-title">Nexus AI: Transforme Seus Dados em Lucro</h1>
        <!-- ✅ ALTERE: Descrição -->
        <p class="hero-subtitle">
            Plataforma de IA que automatiza análises, prevê tendências e gera insights acionáveis. 
            Aumente seu faturamento em até 300% com decisões baseadas em dados inteligentes.
        </p>
        <!-- ✅ ALTERE: Texto do botão e URL -->
        <a href="https://www.google.com/" target="_blank" class="hero-button">Comece seu Teste Grátis</a>
        <!-- ✅ ALTERE: Subtexto -->
        <p class="hero-subtext">✓ Sem cartão de crédito | ✓ Acesso completo por 14 dias | ✓ Cancele quando quiser</p>
    </div>
</div>
''', unsafe_allow_html=True)

# ========== SEÇÃO 4: FEATURES ==========
# ✅ ALTERE: Título, ícones, títulos e descrições
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Funcionalidades que Vendem</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">🔮</div>  <!-- ✅ ALTERE: Emoji -->
        <h3>Análise Preditiva</h3>  <!-- ✅ ALTERE: Título -->
        <p>Modelos de machine learning que antecipam tendências do mercado com 95% de precisão. Saiba o que vai acontecer antes de seus concorrentes.</p>  <!-- ✅ ALTERE: Descrição -->
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">⚙️</div>  <!-- ✅ ALTERE: Emoji -->
        <h3>Automação Inteligente</h3>  <!-- ✅ ALTERE: Título -->
        <p>Automatize 80% das suas tarefas repetitivas. Libere seu time para focar em estratégia enquanto a IA trabalha 24/7.</p>  <!-- ✅ ALTERE: Descrição -->
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="feature-card">
        <div class="feature-icon">💡</div>  <!-- ✅ ALTERE: Emoji -->
        <h3>Insights Acionáveis</h3>  <!-- ✅ ALTERE: Título -->
        <p>Dashboards intuitivos que transformam dados complexos em decisões claras. Veja o que importa em segundos.</p>  <!-- ✅ ALTERE: Descrição -->
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 5: SOCIAL PROOF ==========
# ✅ ALTERE: Título, logos e depoimento
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Aprovado pelas Maiores Empresas</h2>', unsafe_allow_html=True)

st.markdown('''
<div class="logos-container">
    <div class="logo-item">🏢 Tech Corp</div>  <!-- ✅ ALTERE: Logo/nome da empresa -->
    <div class="logo-item">🏢 Finance Plus</div>  <!-- ✅ ALTERE: Logo/nome da empresa -->
    <div class="logo-item">🏢 Retail Max</div>  <!-- ✅ ALTERE: Logo/nome da empresa -->
    <div class="logo-item">🏢 Cloud Sys</div>  <!-- ✅ ALTERE: Logo/nome da empresa -->
    <div class="logo-item">🏢 Data Hub</div>  <!-- ✅ ALTERE: Logo/nome da empresa -->
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div style="text-align: center; margin-top: 2rem;">
    <!-- ✅ ALTERE: Avaliação e depoimento -->
    <p style="font-size: 1.2rem; color: #00bcd4; font-weight: 700;">
        ⭐ 4.9/5 em 2.500+ avaliações
    </p>
    <p style="color: #a0a0a0;">
        "Aumentamos nosso ROI em 250% em 3 meses" - CEO da Tech Corp
    </p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 6: PRICING ==========
# ✅ ALTERE: Títulos, preços e features
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Escolha o Plano Perfeito</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''
    <div class="pricing-card">
        <h3>Starter</h3>  <!-- ✅ ALTERE: Nome do plano -->
        <div class="price">R$ 299<span class="price-period">/mês</span></div>  <!-- ✅ ALTERE: Preço -->
        <ul class="pricing-features">
            <li>✓ Análise Preditiva Básica</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ 10.000 Requisições/mês</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ 1 Dashboard</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Suporte por Email</li>  <!-- ✅ ALTERE: Feature -->
            <li>✗ Automação Avançada</li>  <!-- ✅ ALTERE: Feature -->
        </ul>
        <a href="https://www.google.com/" target="_blank" class="pricing-button">Começar Agora</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="pricing-card featured">
        <h3>⭐ Pro (Mais Popular)</h3>  <!-- ✅ ALTERE: Nome do plano -->
        <div class="price">R$ 899<span class="price-period">/mês</span></div>  <!-- ✅ ALTERE: Preço -->
        <ul class="pricing-features">
            <li>✓ Análise Preditiva Avançada</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ 100.000 Requisições/mês</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ 10 Dashboards</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Automação Inteligente</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Suporte Prioritário 24/7</li>  <!-- ✅ ALTERE: Feature -->
        </ul>
        <a href="https://www.google.com/" target="_blank" class="pricing-button">Começar Agora</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div class="pricing-card">
        <h3>Enterprise</h3>  <!-- ✅ ALTERE: Nome do plano -->
        <div class="price">Customizado</div>  <!-- ✅ ALTERE: Preço -->
        <ul class="pricing-features">
            <li>✓ Tudo do Pro</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Requisições Ilimitadas</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Dashboards Ilimitados</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Gerente de Conta Dedicado</li>  <!-- ✅ ALTERE: Feature -->
            <li>✓ Integrações Customizadas</li>  <!-- ✅ ALTERE: Feature -->
        </ul>
        <a href="https://www.google.com/" target="_blank" class="pricing-button">Falar com Vendas</a>  <!-- ✅ ALTERE: Texto do botão e URL -->
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 7: TESTIMONIALS ==========
# ✅ ALTERE: Depoimentos e autores
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">O Que Nossos Clientes Dizem</h2>', unsafe_allow_html=True)

st.markdown('''
<div class="testimonial-card">
    <!-- ✅ ALTERE: Depoimento 1 -->
    <p class="testimonial-text">
        "A Nexus AI revolucionou nossa forma de analisar dados. Em apenas 3 meses, aumentamos nosso ROI em 250%. 
        É simplesmente incrível como a plataforma nos ajuda a tomar decisões mais rápidas e precisas."
    </p>
    <!-- ✅ ALTERE: Autor 1 -->
    <p class="testimonial-author">— João Silva, CEO da Tech Corp</p>
</div>

<div class="testimonial-card">
    <!-- ✅ ALTERE: Depoimento 2 -->
    <p class="testimonial-text">
        "Economizamos 40 horas por semana em tarefas manuais. O time agora foca em estratégia enquanto a IA faz o trabalho pesado. 
        Recomendo para qualquer empresa que quer crescer rápido."
    </p>
    <!-- ✅ ALTERE: Autor 2 -->
    <p class="testimonial-author">— Maria Santos, Diretora de Operações da Finance Plus</p>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 8: CTA FINAL ==========
# ✅ ALTERE: Título e descrição
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div id="cta"></div>', unsafe_allow_html=True)
st.markdown('''
<div class="cta-section">
    <!-- ✅ ALTERE: Título CTA -->
    <h2 class="cta-title">Pronto para Faturar Milhões?</h2>
    <!-- ✅ ALTERE: Descrição CTA -->
    <p class="cta-subtitle">
        Junte-se a 500+ empresas que já estão transformando seus negócios com a Nexus AI.
    </p>
</div>
''', unsafe_allow_html=True)

# ========== SEÇÃO 9: FORMULÁRIO DE INSCRIÇÃO ==========
# ✅ ALTERE: Placeholder do email e mensagens
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # ✅ ALTERE: Placeholder do input
    email = st.text_input(
        "Seu melhor email",
        placeholder="seu.email@empresa.com",  # ✅ ALTERE: Placeholder
        label_visibility="collapsed"
    )
    
    # ✅ ALTERE: Texto do botão e URLs
    if st.button("🚀 Começar Teste Grátis", use_container_width=True):
        if email and "@" in email:
            # ✅ ALTERE: Mensagem de sucesso
            st.success(f"✅ Ótimo! Enviamos um email de confirmação para {email}. Verifique sua caixa de entrada!")
        else:
            # ✅ ALTERE: Mensagem de erro
            st.error("❌ Por favor, insira um email válido.")

st.markdown('</div>', unsafe_allow_html=True)

# ========== SEÇÃO 10: FOOTER ==========
# ✅ ALTERE: Copyright, links e empresa
st.markdown('''
<div class="footer">
    <!-- ✅ ALTERE: Copyright -->
    <p>© 2026 Nexus AI. Todos os direitos reservados.</p>
    <p style="margin-top: 1rem; font-size: 0.9rem;">
        <!-- ✅ ALTERE: Créditos e links -->
        Feito por Nexus</strong> | 
        <a href="https://www.google.com/" target="_blank" style="color: #00bcd4; text-decoration: none;">Privacidade</a> | 
        <a href="https://www.google.com/" target="_blank" style="color: #00bcd4; text-decoration: none;">Termos</a>
    </p>
</div>
''', unsafe_allow_html=True)

# ========== FIM DO TEMPLATE ==========
# Lembre-se: Altere apenas o que tem ✅ ALTERE
# Não mexa no que tem ❌ NÃO ALTERE
