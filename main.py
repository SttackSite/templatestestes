import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(layout="wide", page_title="Editor Sttack - Template 26", page_icon="🏗️")

# --- 1. INICIALIZAÇÃO DOS DADOS (BASEADO NO SEU Template26.py) ---
if 'step' not in st.session_state:
    st.session_state.step = 1

if 'data' not in st.session_state:
    st.session_state.data = {
        "cor_yellow": "#ffcc00",
        "cor_black": "#111111",
        "aviso": "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO",
        "marca": "DOCKYARD SOCIAL",
        "hero_h1": "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS.",
        "hero_p": "O melhor mercado de comida de rua de Glasgow, agora na sua tela.",
        "card1": {"t": "COMIDA", "s": "10+ VENDEDORES", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        "card2": {"t": "BEBIDA", "s": "CRAFT BEER & COCKTAILS", "img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600"},
        "card3": {"t": "EVENTOS", "s": "MÚSICA AO VIVO", "img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600"},
        "sobre_h2": "MAIS QUE UM MERCADO.",
        "sobre_p": "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos.",
        "cta_h2": "PRONTO PARA VIVER A EXPERIÊNCIA?",
        "cta_p": "Garanta seu ingresso agora e venha fazer parte da melhor vibe de Glasgow.",
        "cta_btn_txt": "RESERVAR AGORA",
        "cta_url": "https://www.google.com/",
        "footer_end": "952 South St, Glasgow G14 0BX",
        "footer_email": "hello@dockyardsocial.com"
    }

# --- 2. FUNÇÃO DE RENDERIZAÇÃO (REPRODUÇÃO FIEL DO SEU HTML) ---
def render_live_preview(d):
    # Injetando o seu CSS e HTML original
    return f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Oswald:wght@700&display=swap');
        :root {{ --dock-yellow: {d['cor_yellow']}; --dock-black: {d['cor_black']}; --dock-white: #f4f4f4; }}
        body {{ background-color: var(--dock-white); margin: 0; font-family: 'Inter', sans-serif; }}
        h1, h2, h3 {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; line-height: 0.9; margin: 0; }}
        .announcement {{ background: var(--dock-black); color: white; padding: 10px; text-align: center; font-weight: bold; font-size: 14px; letter-spacing: 2px; }}
        .nav-dock {{ background-color: var(--dock-black); color: var(--dock-yellow); padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; }}
        .hero-dock {{ background-color: var(--dock-yellow); padding: 60px 5%; border-bottom: 8px solid var(--dock-black); }}
        .hero-h1 {{ font-size: 60px; color: var(--dock-black); font-family: 'Oswald'; }}
        .grid-dock {{ display: flex; gap: 20px; padding: 40px 5%; }}
        .dock-card {{ background: var(--dock-black); color: white; flex: 1; border: 4px solid var(--dock-black); }}
        .card-content {{ padding: 20px; }}
        .card-img {{ width: 100%; height: 200px; object-fit: cover; filter: grayscale(20%); }}
        .action-button {{ display: inline-block; background: var(--dock-black); color: var(--dock-yellow); padding: 15px 30px; text-decoration: none; font-family: 'Oswald'; font-weight: bold; margin-top: 20px; }}
        .sobre-box {{ background: #111; color: white; padding: 60px 5%; }}
    </style>

    {f'<div class="announcement">{d["aviso"]}</div>' if d["aviso"] else ""}
    <div class="nav-dock">
        <div style="font-size: 28px; font-family: 'Oswald'; font-weight: 700;">{d['marca']}</div>
        <div style="display: flex; gap: 20px; font-size: 12px; font-weight: bold;"><span>O QUE ROLA</span><span>COMIDA</span><span>RESERVAR</span></div>
    </div>
    <div class="hero-dock">
        <h1 class="hero-h1">{d['hero_h1']}</h1>
        <p style="font-size: 18px; font-weight: 900; color: #111; margin-top: 15px;">{d['hero_p']}</p>
    </div>
    <div class="grid-dock">
        <div class="dock-card"><img src="{d['card1']['img']}" class="card-img"><div class="card-content"><h2>{d['card1']['t']}</h2><p style="color:var(--dock-yellow)">{d['card1']['s']}</p></div></div>
        <div class="dock-card"><img src="{d['card2']['img']}" class="card-img"><div class="card-content"><h2>{d['card2']['t']}</h2><p style="color:var(--dock-yellow)">{d['card2']['s']}</p></div></div>
        <div class="dock-card"><img src="{d['card3']['img']}" class="card-img"><div class="card-content"><h2>{d['card3']['t']}</h2><p style="color:var(--dock-yellow)">{d['card3']['s']}</p></div></div>
    </div>
    <div class="sobre-box">
        <h2 style="color: var(--dock-yellow); font-size: 40px;">{d['sobre_h2']}</h2>
        <p style="font-size: 18px; line-height: 1.4; margin-top: 20px;">{d['sobre_p']}</p>
    </div>
    <div style="background: var(--dock-yellow); padding: 60px 5%; text-align: center;">
        <h2 style="font-size: 40px;">{d['cta_h2']}</h2>
        <p>{d['cta_p']}</p>
        <a href="{d['cta_url']}" class="action-button">{d['cta_btn_txt']}</a>
    </div>
    """

# --- 3. LAYOUT DO EDITOR ---
col_form, col_view = st.columns([1, 1.8])

with col_form:
    st.title("🛠️ Customizar Template 26")
    st.info(f"Etapa {st.session_state.step} de 5")

    # --- PASSO 1: CORES E MARCA ---
    if st.session_state.step == 1:
        st.subheader("🎨 Identidade Visual")
        st.session_state.data['marca'] = st.text_input("Nome da Marca", st.session_state.data['marca'])
        st.session_state.data['cor_yellow'] = st.color_picker("Cor Principal (Yellow)", st.session_state.data['cor_yellow'])
        st.session_state.data['cor_black'] = st.color_picker("Cor Secundária (Black)", st.session_state.data['cor_black'])
        
        acao_aviso = st.radio("Banner de Aviso Superior:", ["Manter Original", "Editar Texto", "Excluir"])
        if acao_aviso == "Editar Texto":
            st.session_state.data['aviso'] = st.text_input("Texto do Aviso", st.session_state.data['aviso'])
        elif acao_aviso == "Excluir":
            st.session_state.data['aviso'] = ""

    # --- PASSO 2: HERO (O IMPACTO) ---
    elif st.session_state.step == 2:
        st.subheader("🚀 Seção de Impacto (Hero)")
        st.session_state.data['hero_h1'] = st.text_area("Título Principal (HTML permitido)", st.session_state.data['hero_h1'])
        st.session_state.data['hero_p'] = st.text_area("Subtítulo/Descrição", st.session_state.data['hero_p'])

    # --- PASSO 3: CARDS (OS PRODUTOS) ---
    elif st.session_state.step == 3:
        st.subheader("🍔 Grid de Conteúdo (Cards)")
        with st.expander("Card 1 - Editar"):
            st.session_state.data['card1']['t'] = st.text_input("Título 1", st.session_state.data['card1']['t'])
            st.session_state.data['card1']['s'] = st.text_input("Subtítulo 1", st.session_state.data['card1']['s'])
            st.session_state.data['card1']['img'] = st.text_input("URL Imagem 1", st.session_state.data['card1']['img'])
        with st.expander("Card 2 - Editar"):
            st.session_state.data['card2']['t'] = st.text_input("Título 2", st.session_state.data['card2']['t'])
            st.session_state.data['card2']['s'] = st.text_input("Subtítulo 2", st.session_state.data['card2']['s'])
            st.session_state.data['card2']['img'] = st.text_input("URL Imagem 2", st.session_state.data['card2']['img'])

    # --- PASSO 4: TEXTO SOBRE E CTA ---
    elif st.session_state.step == 4:
        st.subheader("📝 Textos e Chamada para Ação")
        st.session_state.data['sobre_h2'] = st.text_input("Título 'Sobre'", st.session_state.data['sobre_h2'])
        st.session_state.data['sobre_p'] = st.text_area("Texto descritivo", st.session_state.data['sobre_p'])
        st.divider()
        st.session_state.data['cta_btn_txt'] = st.text_input("Texto do Botão", st.session_state.data['cta_btn_txt'])
        st.session_state.data['cta_url'] = st.text_input("Link do Botão (URL)", st.session_state.data['cta_url'])

    # --- PASSO 5: FINALIZAÇÃO ---
    elif st.session_state.step == 5:
        st.balloons()
        st.success("Tudo pronto! Seu template foi configurado.")
        st.markdown("### 📥 Próximos Passos:")
        st.write("1. Revise o design à direita.")
        st.write("2. Clique no botão abaixo para exportar as configurações.")
        if st.button("Exportar Configuração JSON"):
            st.json(st.session_state.data)

    # --- NAVEGAÇÃO ---
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        if st.session_state.step > 1:
            if st.button("⬅️ Voltar"):
                st.session_state.step -= 1
                st.rerun()
    with c2:
        if st.session_state.step < 5:
            if st.button("Próximo ➡️"):
                st.session_state.step += 1
                st.rerun()

# --- 4. RENDERIZAÇÃO DO PREVIEW (DIREITA) ---
with col_view:
    st.subheader("👁️ Visualização Real")
    st.markdown('<div style="border: 4px solid #111; border-radius: 10px; overflow: hidden;">', unsafe_allow_html=True)
    components.html(render_live_preview(st.session_state.data), height=800, scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)
