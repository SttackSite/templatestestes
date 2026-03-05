import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img5.png"
TEMPLATE_NAME = "Template 5 — Interstellar (Site Pro)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores
        "t5_cores": [
            {"nome": "Cor Principal (Cyan)",    "valor": "#00f2ff"},
            {"nome": "Cor Secundária (Magenta)", "valor": "#ff00ff"},
            {"nome": "Cor de Fundo (Space)",     "valor": "#02040a"},
        ],
        # Hero
        "t5_hero_status": [{"valor": "[ STATUS: READY FOR DEPLOYMENT ]"}],
        "t5_hero_titulos": [{"valor": "CONSTRUA SUA<br>ESTAÇÃO DIGITAL."}],
        "t5_hero_descs": [{"valor": "Aprenda a criar seu novo site profissional em minutos, sem a dependência de um programador. Economize 80% do tempo e lance sua marca na velocidade da luz."}],
        "t5_hero_btns": [{"texto": "EXPLORAR CATÁLOGO DE TEMPLATES", "url": "#templates"}],
        # Galeria de Ships (Templates)
        "t5_ship_subtitulos": [{"valor": "// EXPLORAR CATÁLOGO DE TEMPLATES"}],
        "t5_ship_titulos": [{"valor": "ESQUADRÃO DE ELITE"}],
        "t5_ships": [
            {"nome": "NEON PULSE",    "tier": "LEGENDARY", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET NEON", "btn_url": "#"},
            {"nome": "QUANTUM SUITE", "tier": "EPIC",      "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET QUANTUM", "btn_url": "#"},
            {"nome": "VOID MINIMAL",  "tier": "RARE",      "img": "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET VOID", "btn_url": "#"},
        ],
        # Estatísticas (Data Nodes)
        "t5_stats": [
            {"valor": "1.2K", "label": "SITES PUBLICADOS"},
            {"valor": "98%",  "label": "SATISFAÇÃO"},
            {"valor": "24/7", "label": "UPLINK SUPORTE"},
            {"valor": "80%",  "label": "MAIS RÁPIDO"},
        ],
        # Missões (Objetivos)
        "t5_missoes_titulos": [{"valor": "OBJETIVOS DA MISSÃO"}],
        "t5_missoes": [
            {"valor": "Quer criar seu próprio site e customizá-lo em minutos pelo menor preço de mercado."},
            {"valor": "Deseja trabalhar vendendo sites de elite para terceiros com alta margem."},
            {"valor": "Precisa escalar a conversão de seus produtos físicos ou digitais."},
        ],
        # Protocolo (Passos)
        "t5_passos_titulos": [{"valor": "PROTOCOLO DE LANÇAMENTO"}],
        "t5_passos": [
            {"num": "01", "titulo": "DOWNLOAD DOS ASSETS",   "desc": "Após a compra, todos os templates são disponibilizados no seu painel de comando."},
            {"num": "02", "titulo": "CUSTOMIZAÇÃO DE DADOS", "desc": "Siga nosso passo a passo visual para inserir suas informações e imagens."},
            {"num": "03", "titulo": "DEPLOY EM SEGUNDOS",    "desc": "Configure sua URL personalizada e suba os arquivos para a rede global."},
            {"num": "04", "titulo": "SISTEMA ONLINE",        "desc": "Seu site está no ar e pronto para operações em larga escala."},
        ],
        # Preços (Acesso à Frota)
        "t5_precos_titulos": [{"valor": "ACESSO À FROTA"}],
        "t5_precos": [
            {"plano": "PILOT ACCESS",    "valor": "R$ 97",  "features": "1 Template de Elite\nSuporte Básico", "btn_txt": "SELECIONAR PILOT",    "url": "#"},
            {"plano": "COMMANDER BUNDLE", "valor": "R$ 197", "features": "Todos os Templates\nAcesso à Comunidade\nSuporte Prioritário", "btn_txt": "ADQUIRIR COMMANDER", "url": "#"},
            {"plano": "ADMIRAL PASS",    "valor": "R$ 497", "features": "Licença Comercial\nMentoria 1:1\nUpdates Vitalícios", "btn_txt": "TORNAR-SE ADMIRAL", "url": "#"},
        ],
        # FAQ (Database)
        "t5_faqs_titulos": [{"valor": "FREQUÊNCIA DE COMUNICAÇÃO"}],
        "t5_faqs": [
            {"pergunta": "COMO É FEITA A TRANSFERÊNCIA DOS ARQUIVOS?", "resposta": "Os códigos são entregues em formato digital pronto para deploy direto via GitHub ou hospedagens estáticas."},
            {"pergunta": "TEREI SUPORTE NA CONFIGURAÇÃO DO DOMÍNIO?",   "resposta": "Sim, fornecemos manuais detalhados e suporte técnico para garantir que sua URL personalizada funcione perfeitamente."},
        ],
        # Footer
        "t5_footer": [{"valor": "© 2026 SITE PRO // INTERSTELLAR DESIGN // ALL RIGHTS RESERVED"}],
        # Observações
        "t5_obs": [{"valor": ""}],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _add_btn(key, label="＋ Adicionar"):
    return st.button(label, key=key)

def _del_btn(key, label="🗑"):
    return st.button(label, key=key, help="Remover")


# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        @import url(\'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@300;500&family=Inter:wght@200;400;900&display=swap\');

        :root {
            --cyan: #00f2ff;       /* ✅ ALTERE: Cor principal */
            --magenta: #ff00ff;    /* ✅ ALTERE: Cor secundária */
            --deep-space: #02040a; /* ✅ ALTERE: Cor de fundo */
            --border-color: rgba(0, 242, 255, 0.2);
        }

        .stApp {
            background-color: var(--deep-space);
            color: #ffffff;
        }

        [data-testid="stHeader"] { display: none; }
        .block-container { padding: 0 !important; max-width: 100% !important; }

        h1, h2, .tech-font {
            font-family: \'Orbitron\', sans-serif;
            text-transform: uppercase;
            letter-spacing: 4px;
        }

        .mono-font {
            font-family: \'JetBrains Mono\', monospace;
            font-size: 12px;
            color: var(--cyan);
            text-transform: uppercase;
        }

        .hero-space {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-image: linear-gradient(rgba(2, 4, 10, 0.8), rgba(2, 4, 10, 0.8)),
                              url(\'https://images.unsplash.com/photo-1614728263952-84ea256f9679?w=1600\');
            background-size: cover;
            background-position: center;
            border-bottom: 1px solid var(--border-color);
        }

        .glitch-text {
            font-size: clamp(40px, 8vw, 100px);
            font-weight: 900;
            text-shadow: 0 0 20px var(--cyan);
            margin-bottom: 20px;
        }

        .ship-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-color);
            padding: 0;
            position: relative;
            transition: 0.5s;
            clip-path: polygon(0 0, 90% 0, 100% 10%, 100% 100%, 10% 100%, 0 90%);
        }
        .ship-card:hover {
            border-color: var(--cyan);
            background: rgba(0, 242, 255, 0.05);
            transform: scale(1.02);
        }

        .data-node {
            border-right: 1px solid var(--border-color);
            padding: 20px;
            text-align: center;
        }

        .mission-box {
            background: linear-gradient(90deg, rgba(0,242,255,0.1) 0%, transparent 100%);
            border-left: 4px solid var(--cyan);
            padding: 30px;
            margin-bottom: 20px;
        }

        .step-container {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 40px;
        }
        .hex-num {
            width: 60px;
            height: 60px;
            background: var(--cyan);
            clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--deep-space);
            font-weight: 900;
            font-family: \'Orbitron\';
            flex-shrink: 0;
        }

        .price-tier {
            background: rgba(2, 4, 10, 0.9);
            border: 1px solid var(--border-color);
            padding: 40px;
            text-align: center;
            position: relative;
        }
        .price-tier::before {
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, var(--cyan), transparent);
        }

        .cmd-btn {
            display: inline-block;
            background: transparent;
            color: var(--cyan) !important;
            border: 1px solid var(--cyan);
            padding: 15px 40px;
            font-family: \'Orbitron\', sans-serif;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-decoration: none !important;
            transition: 0.3s;
            box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
            cursor: pointer;
            margin-top: 16px;
        }
        .cmd-btn:hover {
            background: var(--cyan);
            color: var(--deep-space) !important;
            box-shadow: 0 0 30px var(--cyan);
        }
        .cmd-btn-full {
            display: block;
            width: 100%;
            box-sizing: border-box;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown("<div class=\"panel-title\">✏️ Editor de Template</div>", unsafe_allow_html=True)
        st.markdown(f"<div class=\"panel-subtitle\">{TEMPLATE_NAME}</div>", unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ══════════════════════════════════════════════════════════════════
            # CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">🎨 Cores Espaciais</div>", unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t5_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t5_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t5_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t5_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t5_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t5_cores) > 1 and _del_btn(f"t5_cor_del_{i}"):
                        st.session_state.t5_cores.pop(i); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">🌌 Hero (Comando Central)</div>", unsafe_allow_html=True)
            st.caption("Status / Título / Descrição")
            st.session_state.t5_hero_status[0]["valor"] = st.text_input("Status", st.session_state.t5_hero_status[0]["valor"], key="t5_h_stat_0")
            st.session_state.t5_hero_titulos[0]["valor"] = st.text_area("Título (use <br> para quebra)", st.session_state.t5_hero_titulos[0]["valor"], key="t5_h_tit_0")
            st.session_state.t5_hero_descs[0]["valor"] = st.text_area("Descrição", st.session_state.t5_hero_descs[0]["valor"], key="t5_h_desc_0")
            
            st.caption("Botão do Hero *(Texto | URL)*")
            c1, c2 = st.columns(2)
            with c1: st.session_state.t5_hero_btns[0]["texto"] = st.text_input("Texto", st.session_state.t5_hero_btns[0]["texto"], key="t5_h_btn_t_0")
            with c2: st.session_state.t5_hero_btns[0]["url"] = st.text_input("URL", st.session_state.t5_hero_btns[0]["url"], key="t5_h_btn_u_0")

            # ══════════════════════════════════════════════════════════════════
            # GALERIA (SHIPS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">🚀 Esquadrão (Galeria)</div>", unsafe_allow_html=True)
            st.session_state.t5_ship_subtitulos[0]["valor"] = st.text_input("Subtítulo da Seção", st.session_state.t5_ship_subtitulos[0]["valor"], key="t5_sh_sub_0")
            st.session_state.t5_ship_titulos[0]["valor"] = st.text_input("Título da Seção", st.session_state.t5_ship_titulos[0]["valor"], key="t5_sh_t_0")
            
            for i, ship in enumerate(st.session_state.t5_ships):
                with st.expander(f"Nave {i+1}: {ship[\'nome\']}"):
                    st.session_state.t5_ships[i]["nome"] = st.text_input("Nome", ship["nome"], key=f"t5_s_n_{i}")
                    st.session_state.t5_ships[i]["tier"] = st.text_input("Tier", ship["tier"], key=f"t5_s_tr_{i}")
                    st.session_state.t5_ships[i]["img"] = st.text_input("URL Imagem", ship["img"], key=f"t5_s_img_{i}")
                    st.session_state.t5_ships[i]["desc"] = st.text_area("Descrição", ship["desc"], key=f"t5_s_d_{i}")
                    st.session_state.t5_ships[i]["btn_txt"] = st.text_input("Texto do Botão", ship["btn_txt"], key=f"t5_s_bt_{i}")
                    st.session_state.t5_ships[i]["btn_url"] = st.text_input("URL Botão", ship["btn_url"], key=f"t5_s_u_{i}")
                    if len(st.session_state.t5_ships) > 1 and _del_btn(f"t5_s_del_{i}", "Excluir Nave"):
                        st.session_state.t5_ships.pop(i); st.rerun()
            if _add_btn("t5_s_add", "＋ Adicionar Nave ao Esquadrão"):
                st.session_state.t5_ships.append({"nome": "NOVA NAVE", "tier": "RARE", "img": "", "desc": "...", "btn_txt": "VER DATA-SHEET", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ESTATÍSTICAS (DATA NODES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">📊 Data Nodes (Estatísticas)</div>", unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t5_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t5_stats[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t5_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t5_stats[i]["label"] = st.text_input("Rótulo", stat["label"], key=f"t5_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t5_stats) > 1 and _del_btn(f"t5_st_del_{i}"):
                        st.session_state.t5_stats.pop(i); st.rerun()
            if _add_btn("t5_st_add", "＋ Adicionar Data Node"):
                st.session_state.t5_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBJETIVOS DA MISSÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">🎯 Objetivos da Missão</div>", unsafe_allow_html=True)
            st.session_state.t5_missoes_titulos[0]["valor"] = st.text_input("Título da Seção", st.session_state.t5_missoes_titulos[0]["valor"], key="t5_m_t_0")
            for i, missao in enumerate(st.session_state.t5_missoes):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t5_missoes[i]["valor"] = st.text_input("Missão", missao["valor"], key=f"t5_m_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t5_missoes) > 1 and _del_btn(f"t5_m_del_{i}"):
                        st.session_state.t5_missoes.pop(i); st.rerun()
            if _add_btn("t5_m_add", "＋ Adicionar Objetivo"):
                st.session_state.t5_missoes.append({"valor": "Novo objetivo da missão..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROTOCOLO (PASSOS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">⚙️ Protocolo de Lançamento</div>", unsafe_allow_html=True)
            st.session_state.t5_passos_titulos[0]["valor"] = st.text_input("Título da Seção", st.session_state.t5_passos_titulos[0]["valor"], key="t5_p_t_0")
            for i, passo in enumerate(st.session_state.t5_passos):
                with st.expander(f"Passo {i+1}: {passo[\'titulo\']}"):
                    st.session_state.t5_passos[i]["num"] = st.text_input("Número", passo["num"], key=f"t5_ps_n_{i}")
                    st.session_state.t5_passos[i]["titulo"] = st.text_input("Título", passo["titulo"], key=f"t5_ps_t_{i}")
                    st.session_state.t5_passos[i]["desc"] = st.text_area("Descrição", passo["desc"], key=f"t5_ps_d_{i}")
                    if len(st.session_state.t5_passos) > 1 and _del_btn(f"t5_ps_del_{i}", "Excluir Passo"):
                        st.session_state.t5_passos.pop(i); st.rerun()
            if _add_btn("t5_ps_add", "＋ Adicionar Passo"):
                st.session_state.t5_passos.append({"num": "00", "titulo": "NOVO PASSO", "desc": "Descrição do novo passo..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PREÇOS (ACESSO À FROTA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">💳 Acesso à Frota (Preços)</div>", unsafe_allow_html=True)
            st.session_state.t5_precos_titulos[0]["valor"] = st.text_input("Título da Seção", st.session_state.t5_precos_titulos[0]["valor"], key="t5_pr_t_0")
            for i, preco in enumerate(st.session_state.t5_precos):
                with st.expander(f"Plano {i+1}: {preco[\'plano\']}"):
                    st.session_state.t5_precos[i]["plano"] = st.text_input("Nome do Plano", preco["plano"], key=f"t5_pr_p_{i}")
                    st.session_state.t5_precos[i]["valor"] = st.text_input("Valor", preco["valor"], key=f"t5_pr_v_{i}")
                    st.session_state.t5_precos[i]["features"] = st.text_area("Recursos (um por linha)", preco["features"], key=f"t5_pr_f_{i}")
                    st.session_state.t5_precos[i]["btn_txt"] = st.text_input("Texto do Botão", preco["btn_txt"], key=f"t5_pr_bt_{i}")
                    st.session_state.t5_precos[i]["url"] = st.text_input("URL do Botão", preco["url"], key=f"t5_pr_u_{i}")
                    if len(st.session_state.t5_precos) > 1 and _del_btn(f"t5_pr_del_{i}", "Excluir Plano"):
                        st.session_state.t5_precos.pop(i); st.rerun()
            if _add_btn("t5_pr_add", "＋ Adicionar Plano"):
                st.session_state.t5_precos.append({"plano": "NOVO PLANO", "valor": "R$ 0", "features": "Recurso 1\nRecurso 2", "btn_txt": "SELECIONAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FAQ (DATABASE)
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">❓ Frequência de Comunicação (FAQ)</div>", unsafe_allow_html=True)
            st.session_state.t5_faqs_titulos[0]["valor"] = st.text_input("Título da Seção", st.session_state.t5_faqs_titulos[0]["valor"], key="t5_faq_t_0")
            for i, faq in enumerate(st.session_state.t5_faqs):
                with st.expander(f"FAQ {i+1}: {faq[\'pergunta\']}"):
                    st.session_state.t5_faqs[i]["pergunta"] = st.text_input("Pergunta", faq["pergunta"], key=f"t5_faq_p_{i}")
                    st.session_state.t5_faqs[i]["resposta"] = st.text_area("Resposta", faq["resposta"], key=f"t5_faq_r_{i}")
                    if len(st.session_state.t5_faqs) > 1 and _del_btn(f"t5_faq_del_{i}", "Excluir FAQ"):
                        st.session_state.t5_faqs.pop(i); st.rerun()
            if _add_btn("t5_faq_add", "＋ Adicionar FAQ"):
                st.session_state.t5_faqs.append({"pergunta": "NOVA PERGUNTA", "resposta": "Nova resposta..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">👣 Rodapé Futurista</div>", unsafe_allow_html=True)
            st.session_state.t5_footer[0]["valor"] = st.text_input("Texto do Rodapé", st.session_state.t5_footer[0]["valor"], key="t5_f_t_0")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown("<div class=\"section-label\">📝 Observações Adicionais</div>", unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t5_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t5_obs_{i}", height=80,
                        placeholder="Ex: quero mudar a fonte, adicionar FAQ, remover botão X...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t5_obs) > 1 and _del_btn(f"t5_obs_del_{i}"):
                        st.session_state.t5_obs.pop(i); st.rerun()
            if _add_btn("t5_obs_add", "＋ Adicionar observação"):
                st.session_state.t5_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FINALIZAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("--")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t5_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — IMAGEM DO TEMPLATE
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            \' <p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>\',
            unsafe_allow_html=True)
        st.markdown(
            f\' <div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>\',
            unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO DIRETA
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🌌",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
