import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img7.png"
TEMPLATE_NAME = "Template 7 — Elite Portfolio (Premium)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t7_cores": [
            {"nome": "Cor Principal (Ciano)",    "valor": "#64c8ff"},
            {"nome": "Cor Secundária (Azul)",    "valor": "#0099ff"},
            {"nome": "Cor de Fundo (Deep Blue)", "valor": "#0a0e27"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t7_logos": [{"valor": "ELITE"}],
        "t7_nav_links": [
            {"texto": "Sobre",     "url": "#sobre"},
            {"texto": "Expertise", "url": "#expertise"},
            {"texto": "Trabalhos", "url": "#trabalhos"},
            {"texto": "Contato",   "url": "#contato"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t7_hero_labels": [{"valor": "Bem-vindo"}],
        "t7_hero_titulos": [{"valor": "Transformando <span>Visões</span> em Realidade"}],
        "t7_hero_descs":   [{"valor": "Especialista em criar soluções de impacto com design sofisticado e estratégia de negócio."}],
        "t7_hero_btns": [
            {"texto": "Iniciar Projeto",    "url": "https://www.google.com/", "estilo": "primário"},
            {"texto": "Explorar Trabalhos", "url": "https://www.google.com/", "estilo": "secundário"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t7_stats": [
            {"numero": "150+", "label": "Projetos Entregues"},
            {"numero": "98%",  "label": "Satisfação Clientes"},
            {"numero": "12+",  "label": "Anos Experiência"},
            {"numero": "50M+", "label": "Impacto Gerado"},
        ],

        # ── EXPERTISE ───────────────────────────────────────────────────────
        "t7_exp_titulos": [{"valor": "Expertise"}],
        "t7_exp_items": [
            {"num": "01", "titulo": "Estratégia Digital", "desc": "Desenvolvimento de estratégias robustas que transformam objetivos em resultados mensuráveis e crescimento sustentável."},
            {"num": "02", "titulo": "Design Premium",     "desc": "Criação de interfaces sofisticadas que combinam estética com funcionalidade, elevando a experiência do usuário."},
            {"num": "03", "titulo": "Desenvolvimento",    "desc": "Implementação de soluções técnicas escaláveis e performáticas usando tecnologias de ponta do mercado."},
            {"num": "04", "titulo": "Consultoria",        "desc": "Orientação estratégica para empresas que buscam inovação, transformação digital e posicionamento de mercado."},
        ],

        # ── TRABALHOS ───────────────────────────────────────────────────────
        "t7_work_titulos": [{"valor": "Trabalhos em Destaque"}],
        "t7_work_items": [
            {"emoji": "🚀", "titulo": "Plataforma SaaS",    "desc": "Solução completa de gestão empresarial com impacto em 10K+ usuários.",  "url": "https://www.google.com/"},
            {"emoji": "💎", "titulo": "Marca Luxury",       "desc": "Rebranding completo para marca premium com presença global.",            "url": "https://www.google.com/"},
            {"emoji": "📊", "titulo": "Analytics Platform", "desc": "Dashboard inteligente para análise de dados em tempo real.",             "url": "https://www.google.com/"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t7_ctaf_titulos": [{"valor": "Pronto para Crescer?"}],
        "t7_ctaf_descs":   [{"valor": "Vamos transformar sua visão em uma solução que gera resultados reais e impacto mensurável."}],
        "t7_ctaf_btns":    [{"texto": "Conversar Agora", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t7_footer_infos": [{"valor": "Email: contato@elite.com | Telefone: +55 (99) 99999-9999"}],
        "t7_footer_links": [{"valor": "LinkedIn: linkedin.com/in/seu-perfil | Portfólio: seu-site.com"}],
        "t7_footer_copys": [{"valor": "© 2025 Elite Portfolio. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t7_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background: #f4f6fb; }
        [data-testid="stHeader"],[data-testid="stToolbarActions"],[data-testid="stDecoration"],footer { display:none!important; }
        .section-label {
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; color: #94a3b8;
            margin: 22px 0 8px; padding-bottom: 6px;
            border-bottom: 1px solid #f1f5f9;
        }
        .panel-title    { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
        .panel-subtitle { font-size: 13px; color: #64748b; margin-bottom: 14px; }
        .img-caption    { font-size: 12px; color: #94a3b8; text-align: center; padding: 6px 0 4px; }
        .template-img-wrapper {
            height: calc(100vh - 120px); overflow-y: auto;
            border-radius: 12px; border: 1px solid #e2e8f0; background: #f8faff;
        }
        .template-img-wrapper img { width: 100%; display: block; }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ══════════════════════════════════════════════════════════════════
            # CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t7_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t7_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t7_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t7_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t7_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t7_cores) > 1 and _del_btn(f"t7_cor_del_{i}"):
                        st.session_state.t7_cores.pop(i); st.rerun()
            if _add_btn("t7_cor_add", "＋ Adicionar cor"):
                st.session_state.t7_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t7_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t7_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_logos) > 1 and _del_btn(f"t7_logo_del_{i}"):
                        st.session_state.t7_logos.pop(i); st.rerun()
            if _add_btn("t7_logo_add", "＋ Adicionar logo"):
                st.session_state.t7_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t7_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t7_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t7_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t7_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t7_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t7_nav_links) > 1 and _del_btn(f"t7_nl_del_{i}"):
                        st.session_state.t7_nav_links.pop(i); st.rerun()
            if _add_btn("t7_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t7_nav_links.append({"texto": "Link", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Hero (Apresentação)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno acima do título)*")
            for i, label in enumerate(st.session_state.t7_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t7_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_hero_labels) > 1 and _del_btn(f"t7_h_l_del_{i}"):
                        st.session_state.t7_hero_labels.pop(i); st.rerun()
            if _add_btn("t7_h_l_add", "＋ Adicionar label"):
                st.session_state.t7_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título  *(use <span>palavra</span> para aplicar gradiente)*")
            for i, t in enumerate(st.session_state.t7_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t7_h_t_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_hero_titulos) > 1 and _del_btn(f"t7_h_t_del_{i}"):
                        st.session_state.t7_hero_titulos.pop(i); st.rerun()
            if _add_btn("t7_h_t_add", "＋ Adicionar título"):
                st.session_state.t7_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t7_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t7_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_hero_descs) > 1 and _del_btn(f"t7_h_d_del_{i}"):
                        st.session_state.t7_hero_descs.pop(i); st.rerun()
            if _add_btn("t7_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t7_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botões do Hero  *(Texto | URL | Estilo)*")
            for i, btn in enumerate(st.session_state.t7_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t7_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t7_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t7_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t7_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    st.session_state.t7_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"],
                        index=0 if btn["estilo"] == "primário" else 1,
                        key=f"t7_hb_e_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t7_hero_btns) > 1 and _del_btn(f"t7_hb_del_{i}"):
                        st.session_state.t7_hero_btns.pop(i); st.rerun()
            if _add_btn("t7_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t7_hero_btns.append({"texto": "Novo Botão", "url": "#", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # STATS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas (Stats)</div>', unsafe_allow_html=True)
            st.caption("Número | Descrição")
            for i, stat in enumerate(st.session_state.t7_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t7_stats[i]["numero"] = st.text_input(
                        "Valor", stat["numero"], key=f"t7_st_v_{i}", label_visibility="collapsed", placeholder="Ex: 150+")
                with c2:
                    st.session_state.t7_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t7_st_l_{i}", label_visibility="collapsed", placeholder="Descrição")
                with c3:
                    if len(st.session_state.t7_stats) > 1 and _del_btn(f"t7_st_del_{i}"):
                        st.session_state.t7_stats.pop(i); st.rerun()
            if _add_btn("t7_st_add", "＋ Adicionar estatística"):
                st.session_state.t7_stats.append({"numero": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # EXPERTISE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧠 Expertise & Serviços</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t7_exp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_exp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t7_et_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_exp_titulos) > 1 and _del_btn(f"t7_et_del_{i}"):
                        st.session_state.t7_exp_titulos.pop(i); st.rerun()
            if _add_btn("t7_et_add", "＋ Adicionar título de seção"):
                st.session_state.t7_exp_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Itens de expertise")
            for i, item in enumerate(st.session_state.t7_exp_items):
                with st.expander(f"Expertise {item['num']}: {item['titulo']}"):
                    st.session_state.t7_exp_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t7_ei_n_{i}")
                    st.session_state.t7_exp_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t7_ei_t_{i}")
                    st.session_state.t7_exp_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t7_ei_d_{i}", height=80)
                    if len(st.session_state.t7_exp_items) > 1:
                        if st.button("🗑 Remover este item", key=f"t7_ei_del_{i}"):
                            st.session_state.t7_exp_items.pop(i); st.rerun()
            if _add_btn("t7_ei_add", "＋ Adicionar item de expertise"):
                st.session_state.t7_exp_items.append({"num": "05", "titulo": "Nova Expertise", "desc": "Descrição da expertise."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # TRABALHOS (WORK)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💼 Trabalhos em Destaque</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t7_work_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_work_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t7_wt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_work_titulos) > 1 and _del_btn(f"t7_wt_del_{i}"):
                        st.session_state.t7_work_titulos.pop(i); st.rerun()
            if _add_btn("t7_wt_add", "＋ Adicionar título de seção"):
                st.session_state.t7_work_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de trabalho  *(Emoji | Título | Descrição | URL)*")
            for i, work in enumerate(st.session_state.t7_work_items):
                with st.expander(f"Trabalho {i+1}: {work['titulo']}"):
                    st.session_state.t7_work_items[i]["emoji"] = st.text_input(
                        "Emoji", work["emoji"], key=f"t7_wi_e_{i}")
                    st.session_state.t7_work_items[i]["titulo"] = st.text_input(
                        "Título", work["titulo"], key=f"t7_wi_t_{i}")
                    st.session_state.t7_work_items[i]["desc"] = st.text_area(
                        "Descrição", work["desc"], key=f"t7_wi_d_{i}", height=70)
                    st.session_state.t7_work_items[i]["url"] = st.text_input(
                        "URL (link do trabalho)", work["url"], key=f"t7_wi_u_{i}")
                    if len(st.session_state.t7_work_items) > 1:
                        if st.button("🗑 Remover este trabalho", key=f"t7_wi_del_{i}"):
                            st.session_state.t7_work_items.pop(i); st.rerun()
            if _add_btn("t7_wi_add", "＋ Adicionar trabalho"):
                st.session_state.t7_work_items.append({"emoji": "✨", "titulo": "Novo Trabalho", "desc": "Descrição do trabalho.", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏁 Chamada Final (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t7_ctaf_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_ctaf_titulos[i]["valor"] = st.text_input(
                        "Título CTA", t["valor"], key=f"t7_ctaft_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_ctaf_titulos) > 1 and _del_btn(f"t7_ctaft_del_{i}"):
                        st.session_state.t7_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t7_ctaft_add", "＋ Adicionar título CTA"):
                st.session_state.t7_ctaf_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t7_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_ctaf_descs[i]["valor"] = st.text_area(
                        "Descrição CTA", d["valor"], key=f"t7_ctafd_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_ctaf_descs) > 1 and _del_btn(f"t7_ctafd_del_{i}"):
                        st.session_state.t7_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t7_ctafd_add", "＋ Adicionar descrição CTA"):
                st.session_state.t7_ctaf_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t7_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t7_ctaf_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t7_ctafb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t7_ctaf_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t7_ctafb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t7_ctaf_btns) > 1 and _del_btn(f"t7_ctafb_del_{i}"):
                        st.session_state.t7_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t7_ctafb_add", "＋ Adicionar botão CTA"):
                st.session_state.t7_ctaf_btns.append({"texto": "Novo Botão", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé (Footer)</div>', unsafe_allow_html=True)

            st.caption("Informações de contato  *(ex: Email | Telefone)*")
            for i, info in enumerate(st.session_state.t7_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_infos[i]["valor"] = st.text_input(
                        "Infos", info["valor"], key=f"t7_finfo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_footer_infos) > 1 and _del_btn(f"t7_finfo_del_{i}"):
                        st.session_state.t7_footer_infos.pop(i); st.rerun()
            if _add_btn("t7_finfo_add", "＋ Adicionar linha de contato"):
                st.session_state.t7_footer_infos.append({"valor": "Novo contato"}); st.rerun()

            st.caption("Links sociais  *(ex: LinkedIn | Portfólio)*")
            for i, link in enumerate(st.session_state.t7_footer_links):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_links[i]["valor"] = st.text_input(
                        "Links Sociais", link["valor"], key=f"t7_flink_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_footer_links) > 1 and _del_btn(f"t7_flink_del_{i}"):
                        st.session_state.t7_footer_links.pop(i); st.rerun()
            if _add_btn("t7_flink_add", "＋ Adicionar linha de links sociais"):
                st.session_state.t7_footer_links.append({"valor": "Nova rede social"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t7_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t7_fcopy_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_footer_copys) > 1 and _del_btn(f"t7_fcopy_del_{i}"):
                        st.session_state.t7_footer_copys.pop(i); st.rerun()
            if _add_btn("t7_fcopy_add", "＋ Adicionar linha de copyright"):
                st.session_state.t7_footer_copys.append({"valor": "Novo texto"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t7_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t7_obs_{i}", height=80,
                        placeholder="Ex: Mudar paleta para tons de dourado...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_obs) > 1 and _del_btn(f"t7_obs_del_{i}"):
                        st.session_state.t7_obs.pop(i); st.rerun()
            if _add_btn("t7_obs_add", "＋ Adicionar observação"):
                st.session_state.t7_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t7_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
