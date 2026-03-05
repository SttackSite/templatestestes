import streamlit as st

# -----------------------------------------------------------------------------
# CONFIGURAÇÕES DO TEMPLATE
# -----------------------------------------------------------------------------
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img5.png"
TEMPLATE_NAME = "Template 5 — Interstellar (Site Pro)"

# -----------------------------------------------------------------------------
# INICIALIZAÇÃO DO SESSION STATE
# -----------------------------------------------------------------------------
def _init():
    defaults = {
        "t5_cores": [
            {"nome": "Cor Principal (Cyan)", "valor": "#00f2ff"},
            {"nome": "Cor Secundária (Magenta)", "valor": "#ff00ff"},
            {"nome": "Cor de Fundo (Space)", "valor": "#02040a"},
        ],
        "t5_hero_status": [{"valor": "[ STATUS: READY FOR DEPLOYMENT ]"}],
        "t5_hero_titulos": [{"valor": "CONSTRUA SUA<br>ESTAÇÃO DIGITAL."}],
        "t5_hero_descs": [{"valor": "Aprenda a criar seu novo site profissional em minutos, sem a dependência de um programador. Economize 80% do tempo e lance sua marca na velocidade da luz."}],
        "t5_hero_btns": [{"texto": "INICIAR SEQUÊNCIA →", "url": "#templates"}],
        "t5_ship_subtitulos": [{"valor": "// EXPLORAR CATÁLOGO DE TEMPLATES"}],
        "t5_ship_titulos": [{"valor": "ESQUADRÃO DE ELITE"}],
        "t5_ships": [
            {"nome": "NEON PULSE", "tier": "LEGENDARY", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET NEON", "btn_url": "#"},
            {"nome": "QUANTUM SUITE", "tier": "EPIC", "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET QUANTUM", "btn_url": "#"},
            {"nome": "VOID MINIMAL", "tier": "RARE", "img": "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET VOID", "btn_url": "#"},
        ],
        "t5_stats_titulos": [{"valor": "NÚMEROS QUE FALAM"}],
        "t5_stats_subtitulos": [{"valor": "Resultados comprovados de padrões premium"}],
        "t5_stats": [
            {"valor": "1.2K", "label": "SITES PUBLICADOS"},
            {"valor": "98%", "label": "SATISFAÇÃO"},
            {"valor": "24/7", "label": "UPLINK SUPORTE"},
            {"valor": "80%", "label": "MAIS RÁPIDO"},
        ],
        "t5_missoes_titulos": [{"valor": "OBJETIVOS DA MISSÃO"}],
        "t5_missoes": [
            {"valor": "Quer criar seu próprio site e customizá-lo em minutos pelo menor preço de mercado."},
            {"valor": "Deseja trabalhar vendendo sites de elite para terceiros com alta margem."},
            {"valor": "Precisa escalar a conversão de seus produtos físicos ou digitais."},
        ],
        "t5_passos_titulos": [{"valor": "PROTOCOLO DE LANÇAMENTO"}],
        "t5_passos": [
            {"num": "01", "titulo": "DOWNLOAD DOS ASSETS", "desc": "Após a compra, todos os templates são disponibilizados no seu painel de comando."},
            {"num": "02", "titulo": "CUSTOMIZAÇÃO DE DADOS", "desc": "Siga nosso passo a passo visual para inserir suas informações e imagens."},
            {"num": "03", "titulo": "DEPLOY EM SEGUNDOS", "desc": "Configure sua URL personalizada e suba os arquivos para a rede global."},
            {"num": "04", "titulo": "SISTEMA ONLINE", "desc": "Seu site está no ar e pronto para operações em larga escala."},
        ],
        "t5_precos_titulos": [{"valor": "ACESSO À FROTA"}],
        "t5_precos": [
            {"plano": "PILOT ACCESS", "valor": "R$ 97", "features": "1 Template de Elite\nSuporte Básico", "btn_txt": "SELECIONAR PILOT", "url": "#"},
            {"plano": "COMMANDER BUNDLE", "valor": "R$ 197", "features": "Todos os Templates\nAcesso à Comunidade\nSuporte Prioritário", "btn_txt": "ADQUIRIR COMMANDER", "url": "#"},
            {"plano": "ADMIRAL PASS", "valor": "R$ 497", "features": "Licença Comercial\nMentoria 1:1\nUpdates Vitalícios", "btn_txt": "TORNAR-SE ADMIRAL", "url": "#"},
        ],
        "t5_faqs_titulos": [{"valor": "FREQUÊNCIA DE COMUNICAÇÃO"}],
        "t5_faqs": [
            {"pergunta": "COMO É FEITA A TRANSFERÊNCIA DOS ARQUIVOS?", "resposta": "Os códigos são entregues em formato digital pronto para deploy direto via GitHub ou hospedagens estáticas."},
            {"pergunta": "TEREI SUPORTE NA CONFIGURAÇÃO DO DOMÍNIO?", "resposta": "Sim, fornecemos manuais detalhados e suporte técnico para garantir que sua URL personalizada funcione perfeitamente."},
        ],
        "t5_footer": [{"valor": "© 2026 SITE PRO // INTERSTELLAR DESIGN // ALL RIGHTS RESERVED"}],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

# -----------------------------------------------------------------------------
# FUNÇÕES HELPER
# -----------------------------------------------------------------------------
def _add_btn(key, label="＋ Adicionar"):
    return st.button(label, key=key)

def _del_btn(key, label="🗑"):
    return st.button(label, key=key, help="Remover")

# -----------------------------------------------------------------------------
# RENDERIZAÇÃO PRINCIPAL
# -----------------------------------------------------------------------------
def render():
    _init()

    # --- COLUNA DE EDIÇÃO (ESQUERDA) ---
    with st.sidebar:
        st.markdown("## ✏️ Editor de Template")
        st.markdown(f"**Template:** {TEMPLATE_NAME}")

        with st.container(height=800):
            st.markdown("### 🎨 Cores")
            for i, cor in enumerate(st.session_state.t5_cores):
                st.session_state.t5_cores[i]["valor"] = st.color_picker(cor["nome"], cor["valor"], key=f"t5_c_{i}")

            st.markdown("### 🚀 Seção Hero")
            st.session_state.t5_hero_status[0]["valor"] = st.text_input("Status", st.session_state.t5_hero_status[0]["valor"], key="t5_h_st")
            st.session_state.t5_hero_titulos[0]["valor"] = st.text_area("Título", st.session_state.t5_hero_titulos[0]["valor"], key="t5_h_t")
            st.session_state.t5_hero_descs[0]["valor"] = st.text_area("Descrição", st.session_state.t5_hero_descs[0]["valor"], key="t5_h_d")
            st.session_state.t5_hero_btns[0]["texto"] = st.text_input("Texto do Botão", st.session_state.t5_hero_btns[0]["texto"], key="t5_h_bt")
            st.session_state.t5_hero_btns[0]["url"] = st.text_input("URL do Botão", st.session_state.t5_hero_btns[0]["url"], key="t5_h_bu")

            st.markdown("### 🛰️ Galeria de Naves")
            st.session_state.t5_ship_subtitulos[0]["valor"] = st.text_input("Subtítulo Galeria", st.session_state.t5_ship_subtitulos[0]["valor"], key="t5_sh_sub")
            st.session_state.t5_ship_titulos[0]["valor"] = st.text_input("Título Galeria", st.session_state.t5_ship_titulos[0]["valor"], key="t5_sh_t")
            for i, ship in enumerate(st.session_state.t5_ships):
                with st.expander(f"Nave {i+1}: {ship['nome']}"):
                    st.session_state.t5_ships[i]["nome"] = st.text_input("Nome", ship["nome"], key=f"t5_s_n_{i}")
                    st.session_state.t5_ships[i]["tier"] = st.text_input("Tier", ship["tier"], key=f"t5_s_tr_{i}")
                    st.session_state.t5_ships[i]["img"] = st.text_input("URL Imagem", ship["img"], key=f"t5_s_img_{i}")
                    st.session_state.t5_ships[i]["desc"] = st.text_area("Descrição", ship["desc"], key=f"t5_s_d_{i}")
                    st.session_state.t5_ships[i]["btn_txt"] = st.text_input("Texto Botão", ship["btn_txt"], key=f"t5_s_bt_{i}")
                    st.session_state.t5_ships[i]["btn_url"] = st.text_input("URL Botão", ship["btn_url"], key=f"t5_s_bu_{i}")

            st.markdown("### 📊 Estatísticas")
            st.session_state.t5_stats_titulos[0]["valor"] = st.text_input("Título Stats", st.session_state.t5_stats_titulos[0]["valor"], key="t5_st_t")
            st.session_state.t5_stats_subtitulos[0]["valor"] = st.text_input("Subtítulo Stats", st.session_state.t5_stats_subtitulos[0]["valor"], key="t5_st_sub")
            for i, stat in enumerate(st.session_state.t5_stats):
                with st.expander(f"Stat {i+1}: {stat['label']}"):
                    st.session_state.t5_stats[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t5_st_v_{i}")
                    st.session_state.t5_stats[i]["label"] = st.text_input("Label", stat["label"], key=f"t5_st_l_{i}")

            st.markdown("### 🎯 Objetivos da Missão")
            st.session_state.t5_missoes_titulos[0]["valor"] = st.text_input("Título Missão", st.session_state.t5_missoes_titulos[0]["valor"], key="t5_m_t")
            for i, missao in enumerate(st.session_state.t5_missoes):
                st.session_state.t5_missoes[i]["valor"] = st.text_area(f"Missão {i+1}", missao["valor"], key=f"t5_m_v_{i}")

            st.markdown("### ⚙️ Protocolo de Lançamento")
            st.session_state.t5_passos_titulos[0]["valor"] = st.text_input("Título Protocolo", st.session_state.t5_passos_titulos[0]["valor"], key="t5_p_t")
            for i, passo in enumerate(st.session_state.t5_passos):
                with st.expander(f"Passo {i+1}: {passo['titulo']}"):
                    st.session_state.t5_passos[i]["num"] = st.text_input("Num", passo["num"], key=f"t5_ps_n_{i}")
                    st.session_state.t5_passos[i]["titulo"] = st.text_input("Título", passo["titulo"], key=f"t5_ps_t_{i}")
                    st.session_state.t5_passos[i]["desc"] = st.text_area("Descrição", passo["desc"], key=f"t5_ps_d_{i}")

            st.markdown("### 💳 Acesso à Frota (Preços)")
            st.session_state.t5_precos_titulos[0]["valor"] = st.text_input("Título Preços", st.session_state.t5_precos_titulos[0]["valor"], key="t5_pr_t")
            for i, preco in enumerate(st.session_state.t5_precos):
                with st.expander(f"Plano {i+1}: {preco['plano']}"):
                    st.session_state.t5_precos[i]["plano"] = st.text_input("Plano", preco["plano"], key=f"t5_pr_p_{i}")
                    st.session_state.t5_precos[i]["valor"] = st.text_input("Valor", preco["valor"], key=f"t5_pr_v_{i}")
                    st.session_state.t5_precos[i]["features"] = st.text_area("Recursos", preco["features"], key=f"t5_pr_f_{i}")
                    st.session_state.t5_precos[i]["btn_txt"] = st.text_input("Texto Botão", preco["btn_txt"], key=f"t5_pr_bt_{i}")
                    st.session_state.t5_precos[i]["url"] = st.text_input("URL Botão", preco["url"], key=f"t5_pr_u_{i}")

            st.markdown("### ❓ FAQ")
            st.session_state.t5_faqs_titulos[0]["valor"] = st.text_input("Título FAQ", st.session_state.t5_faqs_titulos[0]["valor"], key="t5_faq_t")
            for i, faq in enumerate(st.session_state.t5_faqs):
                with st.expander(f"FAQ {i+1}: {faq['pergunta']}"):
                    st.session_state.t5_faqs[i]["pergunta"] = st.text_input("Pergunta", faq["pergunta"], key=f"t5_faq_p_{i}")
                    st.session_state.t5_faqs[i]["resposta"] = st.text_area("Resposta", faq["resposta"], key=f"t5_faq_r_{i}")

            st.markdown("### 📜 Footer")
            st.session_state.t5_footer[0]["valor"] = st.text_input("Footer", st.session_state.t5_footer[0]["valor"], key="t5_f_t")

    # --- ÁREA DE PREVIEW (DIREITA) ---
    # Monta o HTML dinamicamente
    
    # CSS Dinâmico
    st.markdown(f"""<style>
        :root {{
            --cyan: {st.session_state.t5_cores[0]["valor"]};
            --magenta: {st.session_state.t5_cores[1]["valor"]};
            --deep-space: {st.session_state.t5_cores[2]["valor"]};
            --border-color: {st.session_state.t5_cores[0]["valor"]}33;
        }}
    </style>""", unsafe_allow_html=True)

    # Hero
    hero_html = f"""
    <div class="hero-space" id="hero">
        <p class="mono-font">{st.session_state.t5_hero_status[0]["valor"]}</p>
        <h1 class="glitch-text">{st.session_state.t5_hero_titulos[0]["valor"]}</h1>
        <p style="max-width: 700px; font-size: 18px; color: rgba(255,255,255,0.6); margin-bottom: 40px; font-family: 'Inter';">
            {st.session_state.t5_hero_descs[0]["valor"]}
        </p>
        <a href='{st.session_state.t5_hero_btns[0]["url"]}' class="cmd-btn">{st.session_state.t5_hero_btns[0]["texto"]}</a>
    </div>"""
    st.markdown(hero_html, unsafe_allow_html=True)

    # Galeria
    ships_html = "".join([f"""
        <div class="ship-card">
            <img src='{ship["img"]}' style="width:100%; height:200px; object-fit:cover; filter: hue-rotate(180deg) brightness(0.7);">
            <div style="padding: 25px;">
                <p class="mono-font" style="font-size: 10px;">TIER: {ship["tier"]}</p>
                <h3 style="font-family: 'Orbitron'; font-size: 18px; margin: 10px 0;">{ship["nome"]}</h3>
                <div style="width: 100%; height: 1px; background: var(--border-color); margin-bottom: 15px;"></div>
                <p style="font-size: 12px; opacity: 0.6;">{ship["desc"]}</p>
                <a href='{ship["btn_url"]}' target="_blank" class="cmd-btn cmd-btn-full">{ship["btn_txt"]}</a>
            </div>
        </div>""" for ship in st.session_state.t5_ships])
    st.markdown(f"""
    <div id="templates" style="padding: 100px 8%;">
        <p class="mono-font">{st.session_state.t5_ship_subtitulos[0]["valor"]}</p>
        <h2 style="font-size: 32px; margin-bottom: 60px;">{st.session_state.t5_ship_titulos[0]["valor"]}</h2>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;">
            {ships_html}
        </div>
    </div>""", unsafe_allow_html=True)

    # Stats
    stats_html = "".join([f"""
        <div class="data-node" style="{'border-right': 'none' if i == len(st.session_state.t5_stats) - 1 else '1px solid var(--border-color)'}">
            <h2 style="color: var(--cyan);">{stat["valor"]}</h2>
            <p class="mono-font">{stat["label"]}</p>
        </div>""" for i, stat in enumerate(st.session_state.t5_stats)])
    st.markdown(f"""
    <div id="stats" style="background: {st.session_state.t5_cores[0]["valor"]}05; padding: 80px 8%; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
        <h2 style="text-align:center; margin-bottom: 10px;">{st.session_state.t5_stats_titulos[0]["valor"]}</h2>
        <p style="text-align:center; color: rgba(255,255,255,0.6); margin-bottom: 50px;">{st.session_state.t5_stats_subtitulos[0]["valor"]}</p>
        <div style="display: grid; grid-template-columns: repeat({len(st.session_state.t5_stats)}, 1fr);">{stats_html}</div>
    </div>""", unsafe_allow_html=True)

    # Missão
    missoes_html = "".join([f"""
        <div class="mission-box">
            <p style="font-family: 'JetBrains Mono'; font-size: 16px; margin: 0;">>> {missao["valor"]}</p>
        </div>""" for missao in st.session_state.t5_missoes])
    st.markdown(f"""
    <div id="missao" style="padding: 100px 8%;">
        <h2>{st.session_state.t5_missoes_titulos[0]["valor"]}</h2><br>
        {missoes_html}
    </div>""", unsafe_allow_html=True)

    # Protocolo
    passos_html = "".join([f"""
        <div class="step-container">
            <div class="hex-num">{passo["num"]}</div>
            <div>
                <h4 style="font-family: 'Orbitron'; color: var(--cyan);">{passo["titulo"]}</h4>
                <p style="font-size: 14px; opacity: 0.6; max-width: 400px;">{passo["desc"]}</p>
            </div>
        </div>""" for passo in st.session_state.t5_passos])
    st.markdown(f"""
    <div id="protocolo" style="padding: 100px 8%; background: #000;">
        <h2>{st.session_state.t5_passos_titulos[0]["valor"]}</h2><br>
        {passos_html}
    </div>""", unsafe_allow_html=True)

    # Preços
    precos_html = "".join([f"""
        <div class="price-tier" style="{'border-color: var(--cyan); background: rgba(0,242,255,0.05);' if i == 1 else ''}">
            <p class="mono-font">{preco["plano"]}</p>
            <h1 style="font-size: 50px; margin: 20px 0;">{preco["valor"]}</h1>
            <div style="min-height: 80px;">{"<br>".join([f"<p>{line}</p>" for line in preco["features"].splitlines()])}</div>
            <a href='{preco["url"]}' target="_blank" class="cmd-btn cmd-btn-full">{preco["btn_txt"]}</a>
        </div>""" for i, preco in enumerate(st.session_state.t5_precos)])
    st.markdown(f"""
    <div id="precos" style="padding: 100px 8%;">
        <h2 style="text-align:center;">{st.session_state.t5_precos_titulos[0]["valor"]}</h2><br>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; align-items: start;">
            {precos_html}
        </div>
    </div>""", unsafe_allow_html=True)

    # FAQ
    faqs_html = "".join([f"""
        <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 20px;">
            <h4 style="font-family: 'Orbitron';">{faq["pergunta"]}</h4>
            <p style="opacity: 0.7;">{faq["resposta"]}</p>
        </div>""" for faq in st.session_state.t5_faqs])
    st.markdown(f"""
    <div id="faq" style="padding: 100px 8%; border-top: 1px solid var(--border-color);">
        <h2 style="text-align:center;">{st.session_state.t5_faqs_titulos[0]["valor"]}</h2><br>
        <div style="max-width: 800px; margin: auto;">
            {faqs_html}
        </div>
    </div>""", unsafe_allow_html=True)

    # Footer
    st.markdown(f"""
    <footer style="text-align: center; padding: 50px 8%; background: #000; border-top: 1px solid var(--border-color);">
        <p class="mono-font" style="font-size: 10px; opacity: 0.5;">{st.session_state.t5_footer[0]["valor"]}</p>
    </footer>""", unsafe_allow_html=True)

    # CSS Base
    st.markdown("""<style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@300;500&family=Inter:wght@200;400;900&display=swap');
        [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stSidebarNav"] {display: none !important;}
        .block-container { padding: 0 !important; max-width: 100% !important; }
        h1, h2, h3, h4, h5, h6, .tech-font { font-family: 'Orbitron', sans-serif; text-transform: uppercase; letter-spacing: 4px; }
        .mono-font { font-family: 'JetBrains Mono', monospace; font-size: 12px; text-transform: uppercase; }
        .hero-space { height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background-size: cover; background-position: center; }
        .glitch-text { font-size: clamp(40px, 8vw, 100px); font-weight: 900; margin-bottom: 20px; }
        .ship-card { background: rgba(255, 255, 255, 0.02); padding: 0; position: relative; transition: 0.5s; clip-path: polygon(0 0, 90% 0, 100% 10%, 100% 100%, 10% 100%, 0 90%); }
        .ship-card:hover { transform: scale(1.02); }
        .data-node { padding: 20px; text-align: center; }
        .mission-box { padding: 30px; margin-bottom: 20px; }
        .step-container { display: flex; align-items: center; gap: 20px; margin-bottom: 40px; }
        .hex-num { width: 60px; height: 60px; clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); display: flex; align-items: center; justify-content: center; font-weight: 900; font-family: 'Orbitron'; flex-shrink: 0; }
        .price-tier { padding: 40px; text-align: center; position: relative; }
        .price-tier::before { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 2px; }
        .cmd-btn { display: inline-block; padding: 15px 40px; font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; text-decoration: none !important; transition: 0.3s; cursor: pointer; margin-top: 16px; }
        .cmd-btn-full { display: block; width: 100%; box-sizing: border-box; text-align: center; margin-top: 20px; }
        .stApp { background-color: var(--deep-space); color: #ffffff; }
        .mono-font { color: var(--cyan); }
        .hero-space { background-image: linear-gradient(rgba(2, 4, 10, 0.8), rgba(2, 4, 10, 0.8)), url('https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=1600'); border-bottom: 1px solid var(--border-color); }
        .glitch-text { text-shadow: 0 0 20px var(--cyan); }
        .ship-card { border: 1px solid var(--border-color); }
        .ship-card:hover { border-color: var(--cyan); background: rgba(0, 242, 255, 0.05); }
        .data-node { border-right: 1px solid var(--border-color); }
        .mission-box { background: linear-gradient(90deg, rgba(0,242,255,0.1) 0%, transparent 100%); border-left: 4px solid var(--cyan); }
        .hex-num { background: var(--cyan); color: var(--deep-space); }
        .price-tier { background: rgba(2, 4, 10, 0.9); border: 1px solid var(--border-color); }
        .price-tier::before { background: linear-gradient(90deg, transparent, var(--cyan), transparent); }
        .cmd-btn { color: var(--cyan) !important; border: 1px solid var(--cyan); box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2); }
        .cmd-btn:hover { background: var(--cyan); color: var(--deep-space) !important; box-shadow: 0 0 30px var(--cyan); }
    </style>""", unsafe_allow_html=True)

if __name__ == '__main__':
    render()
