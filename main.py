import streamlit as st
import json

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sttack Editor Ultra", layout="wide")

# --- ESTADO DA SESSÃO (O Banco de Dados Temporário) ---
# Aqui definimos o template padrão inicial
if 'layout' not in st.session_state:
    st.session_state.layout = [
        {"id": 1, "tipo": "Hero", "conteudo": {"titulo": "COMIDA DE RUA.<br>BOAS VIBES.", "subtitulo": "O melhor mercado de Glasgow.", "cor_fundo": "#ffcc00", "cor_texto": "#111111"}},
        {"id": 2, "tipo": "Cards", "conteudo": [
            {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
            {"titulo": "BEBIDA", "sub": "CRAFT BEERS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"}
        ]},
        {"id": 3, "tipo": "Sobre", "conteudo": {"titulo": "NOSSA HISTÓRIA", "texto": "Criado para ser um espaço inclusivo...", "cor_fundo": "#111111", "cor_texto": "#ffffff"}}
    ]

if 'global_config' not in st.session_state:
    st.session_state.global_config = {
        "nome_marca": "DOCKYARD SOCIAL",
        "cor_primaria": "#ffcc00",
        "cor_secundaria": "#111111"
    }

# --- FUNÇÕES DE RENDERIZAÇÃO (O seu motor de HTML) ---
def render_hero(data):
    st.markdown(f"""
    <div style="background-color: {data['cor_fundo']}; padding: 80px 5%; border-bottom: 8px solid #000;">
        <h1 style="font-family: 'Oswald', sans-serif; font-size: 80px; color: {data['cor_texto']}; line-height:0.9; text-transform:uppercase;">{data['titulo']}</h1>
        <p style="font-size: 20px; font-weight: bold; color: {data['cor_texto']}; margin-top: 20px;">{data['subtitulo']}</p>
    </div>
    """, unsafe_allow_html=True)

def render_cards(cards_list):
    cols = st.columns(len(cards_list))
    for i, card in enumerate(cards_list):
        with cols[i]:
            st.markdown(f"""
            <div style="background: #111; border: 4px solid #111; color: white;">
                <img src="{card['img']}" style="width:100%; height:250px; object-fit:cover;">
                <div style="padding: 20px;">
                    <h2 style="font-family: 'Oswald'; margin: 0;">{card['titulo']}</h2>
                    <p style="color: {st.session_state.global_config['cor_primaria']}; font-weight: bold;">{card['sub']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_sobre(data):
    st.markdown(f"""
    <div style="background-color: {data['cor_fundo']}; color: {data['cor_texto']}; padding: 80px 5%;">
        <h2 style="font-family: 'Oswald'; font-size: 50px;">{data['titulo']}</h2>
        <p style="font-size: 18px; max-width: 800px; line-height: 1.6;">{data['texto']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR: CONFIGURAÇÕES GLOBAIS E EXPORT ---
with st.sidebar:
    st.title("🎨 STTACK BUILDER")
    st.session_state.global_config['nome_marca'] = st.text_input("Nome da Marca", st.session_state.global_config['nome_marca'])
    st.session_state.global_config['cor_primaria'] = st.color_picker("Cor Primária", st.session_state.global_config['cor_primaria'])
    
    st.divider()
    
    if st.button("➕ Adicionar Nova Seção"):
        # Adiciona um bloco vazio de "Sobre" por padrão no final
        new_id = len(st.session_state.layout) + 1
        st.session_state.layout.append({"id": new_id, "tipo": "Sobre", "conteudo": {"titulo": "Nova Seção", "texto": "Edite o texto aqui", "cor_fundo": "#eeeeee", "cor_texto": "#111111"}})
        st.rerun()

    st.divider()
    
    json_export = json.dumps({"global": st.session_state.global_config, "layout": st.session_state.layout}, indent=4)
    st.download_button("📥 EXPORTAR JSON FINAL", json_export, "meu_site.json", "application/json")

# --- ÁREA PRINCIPAL: EDITOR VS PREVIEW ---
tab_editor, tab_preview = st.tabs(["🛠️ EDITOR DE CONTEÚDO", "🖥️ VISUALIZAÇÃO AO VIVO"])

with tab_editor:
    st.info("Altere a ordem das seções ou edite o conteúdo de cada bloco abaixo.")
    
    # Lista de seções com botões de controle
    for index, secao in enumerate(st.session_state.layout):
        with st.expander(f"Seção {index+1}: {secao['tipo']}"):
            col_header, col_delete = st.columns([4, 1])
            
            with col_header:
                secao['tipo'] = st.selectbox(f"Tipo do Bloco #{secao['id']}", ["Hero", "Cards", "Sobre"], index=["Hero", "Cards", "Sobre"].index(secao['tipo']), key=f"tipo_{index}")
            
            with col_delete:
                if st.button("🗑️ Remover", key=f"del_{index}"):
                    st.session_state.layout.pop(index)
                    st.rerun()

            # Campos dinâmicos baseados no tipo de bloco
            if secao['tipo'] == "Hero":
                secao['conteudo']['titulo'] = st.text_input("Título Hero", secao['conteudo']['titulo'], key=f"h_t_{index}")
                secao['conteudo']['subtitulo'] = st.text_area("Subtítulo", secao['conteudo']['subtitulo'], key=f"h_s_{index}")
                c1, c2 = st.columns(2)
                secao['conteudo']['cor_fundo'] = c1.color_picker("Cor de Fundo", secao['conteudo']['cor_fundo'], key=f"h_b_{index}")
                secao['conteudo']['cor_texto'] = c2.color_picker("Cor do Texto", secao['conteudo']['cor_texto'], key=f"h_txt_{index}")
            
            elif secao['tipo'] == "Sobre":
                secao['conteudo']['titulo'] = st.text_input("Título Seção", secao['conteudo']['titulo'], key=f"s_t_{index}")
                secao['conteudo']['texto'] = st.text_area("Corpo do Texto", secao['conteudo']['texto'], key=f"s_txt_{index}")
                c1, c2 = st.columns(2)
                secao['conteudo']['cor_fundo'] = c1.color_picker("Cor de Fundo", secao['conteudo']['cor_fundo'], key=f"s_b_{index}")
                secao['conteudo']['cor_texto'] = c2.color_picker("Cor do Texto", secao['conteudo']['cor_texto'], key=f"s_txt_c_{index}")

            elif secao['tipo'] == "Cards":
                st.write("Edite os cards na tabela abaixo:")
                secao['conteudo'] = st.data_editor(secao['conteudo'], key=f"ed_cards_{index}", num_rows="dynamic")

            # Botões de ordem
            c_up, c_down, _ = st.columns([1,1,8])
            if index > 0:
                if c_up.button("↑ Subir", key=f"up_{index}"):
                    st.session_state.layout[index], st.session_state.layout[index-1] = st.session_state.layout[index-1], st.session_state.layout[index]
                    st.rerun()
            if index < len(st.session_state.layout) - 1:
                if c_down.button("↓ Baixar", key=f"down_{index}"):
                    st.session_state.layout[index], st.session_state.layout[index+1] = st.session_state.layout[index+1], st.session_state.layout[index]
                    st.rerun()

with tab_preview:
    # Fontes
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap' rel='stylesheet'>", unsafe_allow_html=True)
    
    # Barra de Navegação Mockup
    st.markdown(f"""
    <div style="background: #111; color: {st.session_state.global_config['cor_primaria']}; padding: 15px 5%; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-family: 'Oswald'; font-size: 24px;">{st.session_state.global_config['nome_marca']}</div>
        <div style="font-size: 14px; font-weight: bold;">MENU ☰</div>
    </div>
    """, unsafe_allow_html=True)

    # Loop que percorre o layout e chama a função de renderização correta
    for secao in st.session_state.layout:
        if secao['tipo'] == "Hero":
            render_hero(secao['conteudo'])
        elif secao['tipo'] == "Cards":
            render_cards(secao['conteudo'])
        elif secao['tipo'] == "Sobre":
            render_sobre(secao['conteudo'])
    
    # Footer Mockup
    st.markdown(f"<div style='text-align:center; padding: 40px; background: #eee; font-size: 12px;'>© 2026 {st.session_state.global_config['nome_marca']}</div>", unsafe_allow_html=True)
