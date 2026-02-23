import streamlit as st
import json

# Configuração da Página
st.set_page_config(layout="wide", page_title="Configurador de Site - Sttack", page_icon="🚀")

def render_configurator():
    # --- CSS PARA ESTILIZAÇÃO E CORREÇÕES ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&family=Oswald:wght@700&display=swap');
        
        /* Ajuste para o aviso inicial ficar bem destacado */
        .info-box {
            background-color: #e1f5fe;
            padding: 20px;
            border-left: 5px solid #01579b;
            border-radius: 5px;
            margin-bottom: 25px;
            font-family: 'Inter', sans-serif;
        }
        
        /* Estilo para o campo de URL */
        .url-container {
            display: flex;
            align-items: center;
            font-family: 'Inter', sans-serif;
            font-weight: bold;
            font-size: 18px;
            color: #333;
            background: #f0f2f6;
            padding: 10px;
            border-radius: 8px;
        }

        [data-testid="stHeader"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

    # --- 1. AVISO INICIAL (HEADER DA PÁGINA) ---
    st.markdown(f"""
    <div class="info-box">
        <strong>💡 Instruções Importantes:</strong><br>
        Estas são as alterações básicas para colocar seu site no ar de forma rápida. 
        Caso precise de alguma <strong>customização mais complexa</strong>, você pode detalhar no campo de 
        <em>'Observações Adicionais'</em> ao final da barra lateral ou no e-mail de envio. 
        Nós aplicamos para você, desde que não altere a estrutura base do template.
    </div>
    """, unsafe_allow_html=True)

    # --- BARRA LATERAL (PAINEL DE CONTROLE) ---
    st.sidebar.title("🛠️ PAINEL DE EDIÇÃO")
    
    config = {}

    # 2. Escolha da URL (NOVO)
    st.sidebar.subheader("🌐 Sua futura URL")
    url_input = st.sidebar.text_input("Digite o nome desejado:", placeholder="meu-negocio")
    config['url_planejada'] = f"https://{url_input}.streamlit.app" if url_input else ""
    
    # Exibição visual da URL para o usuário
    st.sidebar.markdown(f"**Resultado:** `{config['url_planejada'] if url_input else 'https://...streamlit.app'}`")

    # 3. Identidade e Cores
    with st.sidebar.expander("🎨 1. Cores e Logo", expanded=True):
        config['cor_destaque'] = st.color_picker("Cor Destaque", "#ffcc00")
        config['cor_principal'] = st.color_picker("Cor Principal", "#111111")
        config['nome_site'] = st.text_input("Nome da Marca", "DOCKYARD SOCIAL")
        config['aviso_topo'] = st.text_input("Frase do Topo", "ABERTO NESTE FINAL DE SEMANA")

    # 4. Conteúdo Dinâmico
    st.sidebar.markdown("### 🍔 2. Conteúdo (Cards)")
    default_cards = [
        {"titulo": "COMIDA", "sub": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"titulo": "BEBIDA", "sub": "COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"}
    ]
    config['cards'] = st.sidebar.data_editor(default_cards, num_rows="dynamic")

    # 5. Observações Adicionais (NOVO)
    st.sidebar.markdown("### 📝 3. Pedidos Especiais")
    config['observacoes'] = st.sidebar.text_area("Detalhe aqui outras customizações que você deseja:")

    # 6. Finalização e Envio (NOVO)
    st.sidebar.markdown("---")
    st.sidebar.warning("⚠️ **COMO FINALIZAR:**\n\nBaixe o arquivo abaixo e envie para **sttacksite@gmail.com** para que possamos aplicar as alterações.")
    
    json_export = json.dumps(config, indent=4, ensure_ascii=False)
    st.sidebar.download_button(
        label="📥 BAIXAR MEU JSON",
        data=json_export,
        file_name="configuracao_site.json",
        mime="application/json"
    )

    # =========================================================
    # PREVIEW DO SITE (DESIGN ORIGINAL)
    # =========================================================
    
    # (O CSS aqui dentro é o mesmo do Template26.py que ajustamos antes)
    st.markdown(f"""
    <style>
        :root {{
            --dock-yellow: {config['cor_destaque']};
            --dock-black: {config['cor_principal']};
        }}
        .announcement {{ background: var(--dock-black); color: white; padding: 10px; text-align: center; font-weight: bold; letter-spacing: 2px; }}
        .nav-dock {{ background: var(--dock-black); color: var(--dock-yellow); padding: 15px 5%; display: flex; justify-content: space-between; font-family: 'Oswald'; }}
        .hero-dock {{ background: var(--dock-yellow); padding: 60px 5%; border-bottom: 8px solid var(--dock-black); }}
        .hero-h1 {{ font-family: 'Oswald'; font-size: 80px; color: var(--dock-black); line-height: 0.9; text-transform: uppercase; }}
        .dock-card {{ background: var(--dock-black); color: white; border: 4px solid var(--dock-black); margin-bottom: 20px; }}
        .card-content {{ padding: 20px; }}
        h2 {{ font-family: 'Oswald'; text-transform: uppercase; }}
    </style>
    """, unsafe_allow_html=True)

    # Render do Preview
    st.markdown(f'<div class="announcement">{config["aviso_topo"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="nav-dock"><div style="font-size: 28px;">{config["nome_site"]}</div></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="hero-dock">
        <h1 class="hero-h1">DOCKYARD BUILDER<br>PREVIEW MODE</h1>
        <p style="font-weight: bold; color: #111;">Sua URL sugerida: {config['url_planejada'] if url_input else '(Defina na barra lateral)'}</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    cols = st.columns(3)
    for i, c in enumerate(config['cards']):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="dock-card">
                <img src="{c['img']}" style="width:100%; height:200px; object-fit:cover;">
                <div class="card-content">
                    <h3>{c['titulo']}</h3>
                    <p style="color: var(--dock-yellow); font-size: 14px;">{c['sub']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_configurator()
