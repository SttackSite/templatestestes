import streamlit as st
import json

st.set_page_config(layout="wide", page_title="Dockyard Configurator Pro", page_icon="🛠️")

def render_configurator_pro():
    st.sidebar.title("🛠️ Editor Dinâmico")
    st.sidebar.info("Adicione ou remova itens nas tabelas abaixo.")

    config = {}

    # --- 1. CONFIGURAÇÕES GERAIS (Igual antes) ---
    with st.sidebar.expander("1. Cores e Textos Principais", expanded=False):
        config['cor_destaque'] = st.color_picker("Cor Destaque", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal", "#111111")
        config['cor_fundo'] = st.color_picker("Cor Fundo", "#f4f4f4")
        config['nome_site'] = st.text_input("Nome do Site", "DOCKYARD SOCIAL")
        config['hero_titulo'] = st.text_area("Título Hero", "COMIDA DE RUA.<br>BOAS VIBES.")

    # --- 2. CARDS DINÂMICOS (A MÁGICA AQUI) ---
    st.sidebar.markdown("### 2. Gerenciar Cards (Grid)")
    st.sidebar.caption("Adicione linhas para criar novos cards. Delete para remover.")

    # Dados iniciais (padrão) para não vir vazio
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "CRAFT BEER", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        {"titulo": "EVENTOS", "sub": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"},
    ]

    # O Editor de Dados (Permite adicionar/remover linhas)
    edited_cards = st.sidebar.data_editor(
        default_cards,
        num_rows="dynamic", # Isso permite adicionar/remover
        column_config={
            "titulo": st.column_config.TextColumn("Título"),
            "sub": st.column_config.TextColumn("Subtítulo"),
            "img": st.column_config.TextColumn("URL da Imagem", help="Cole o link da imagem aqui"),
        },
        key="editor_cards"
    )
    
    # Salva no config
    config['cards'] = edited_cards

    # --- 3. BOTÕES EXTRAS (Exemplo de lista dinâmica também) ---
    st.sidebar.markdown("### 3. Botões de Ação")
    
    default_buttons = [
        {"texto": "RESERVAR AGORA", "link": "https://google.com", "cor": "#111", "texto_cor": "#ffcc00"}
    ]

    edited_buttons = st.sidebar.data_editor(
        default_buttons,
        num_rows="dynamic",
        column_config={
            "texto": "Texto do Botão",
            "link": "Link de Destino",
            "cor": "Cor do Fundo",
            "texto_cor": "Cor da Letra"
        },
        key="editor_buttons"
    )
    config['botoes'] = edited_buttons

    # --- GERAR JSON ---
    st.sidebar.markdown("---")
    json_string = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button("📥 BAIXAR CONFIGURAÇÃO", json_string, "site_dinamico.json", "application/json")

    # =========================================================
    # PREVIEW DO SITE (RENDERIZAÇÃO DO ARRAY DINÂMICO)
    # =========================================================
    
    # CSS Dinâmico (usando as variáveis)
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');
        :root {{ --main: {config['cor_destaque']}; --dark: {config['cor_principal']}; --bg: {config['cor_fundo']}; }}
        .stApp {{ background-color: var(--bg); }}
        .card {{ border: 4px solid var(--dark); background: var(--dark); color: white; margin-bottom: 20px; }}
        .card img {{ width: 100%; height: 200px; object-fit: cover; filter: grayscale(20%); }}
        .card-content {{ padding: 15px; }}
        h1, h2 {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; }}
        
        /* Estilo dos Botões Dinâmicos */
        .dynamic-btn {{
            padding: 15px 30px; 
            font-family: 'Oswald'; 
            text-decoration: none; 
            display: inline-block; 
            margin: 5px;
            font-size: 18px;
            transition: 0.3s;
        }}
        .dynamic-btn:hover {{ opacity: 0.8; }}
    </style>
    """, unsafe_allow_html=True)

    # Hero
    st.markdown(f'<h1 style="font-size: 80px; color: {config["cor_principal"]}">{config["hero_titulo"]}</h1>', unsafe_allow_html=True)

    # --- RENDERIZAÇÃO INTELIGENTE DOS CARDS (GRID) ---
    st.write("---")
    
    # Lógica: Se o usuário colocar 5 cards, precisamos quebrar linha a cada 3
    cols_per_row = 3
    cards = config['cards']
    
    # Loop pulando de 3 em 3
    for i in range(0, len(cards), cols_per_row):
        # Cria as colunas para essa linha
        cols = st.columns(cols_per_row)
        
        # Preenche as colunas
        for j in range(cols_per_row):
            if i + j < len(cards): # Verifica se o card existe
                card = cards[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="card">
                        <img src="{card['img']}">
                        <div class="card-content">
                            <h2>{card['titulo']}</h2>
                            <p style="color: var(--main); font-weight: bold;">{card['sub']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    # --- RENDERIZAÇÃO DOS BOTÕES DINÂMICOS ---
    st.write("---")
    st.markdown("<div style='text-align: center; padding: 50px;'>", unsafe_allow_html=True)
    st.markdown("<h2>PRONTO PARA AÇÃO?</h2>", unsafe_allow_html=True)
    
    # Loop pelos botões
    for btn in config['botoes']:
        st.markdown(f"""
        <a href="{btn['link']}" class="dynamic-btn" 
           style="background-color: {btn['cor']}; color: {btn['texto_cor']};">
           {btn['texto']}
        </a>
        """, unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_configurator_pro()
