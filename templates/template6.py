import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img6.png"
TEMPLATE_NAME = "Template 6 — Alta Precisão (Bautz Style)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Técnicas
        "t6_cores": [
            {"nome": "Cor de Destaque (Azul Técnico)", "valor": "#0047bb"},
            {"nome": "Cor de Fundo (Gray Soft)",       "valor": "#f5f5f7"},
            {"nome": "Cor do Texto (Deep Black)",      "valor": "#1a1a1a"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t6_navbar_logo":  [{"valor": "SITE PRO"}],
        "t6_navbar_links": [
            {"texto": "Catálogo",   "url": "#catalogo"},
            {"texto": "Aplicações", "url": "#aplicacoes"},
            {"texto": "Workflow",   "url": "#workflow"},
            {"texto": "Preços",     "url": "#precos"},
            {"texto": "FAQ",        "url": "#faq"},
        ],
        "t6_navbar_cta": [{"texto": "CONFIGURAR AGORA", "url": "#catalogo"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t6_hero_mono":      [{"valor": "Codeless Architecture v2.0"}],
        "t6_hero_titulos":   [{"valor": "SITES DE ALTA<br>PRECISÃO."}],
        "t6_hero_subtitulos":[{"valor": "Desenvolva a sua presença digital com a eficiência de um processo industrial. Templates otimizados para velocidade, conversão e autonomia total."}],
        "t6_hero_btns":      [{"texto": "CONFIGURAR AGORA", "url": "#catalogo"}],

        # ── CATÁLOGO ────────────────────────────────────────────────────────
        "t6_cat_mono":   [{"valor": "// CATÁLOGO DE COMPONENTES"}],
        "t6_cat_titulos":[{"valor": "MODELOS DISPONÍVEIS"}],
        "t6_cat_items": [
            {"nome": "STRUCTURAL MINIMAL", "ref": "BTZ-01", "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-01", "url": "https://www.google.com/"},
            {"nome": "DYNAMIC FLOW",        "ref": "BTZ-02", "img": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-02", "url": "https://www.google.com/"},
            {"nome": "CORPORATE CORE",      "ref": "BTZ-03", "img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-03", "url": "https://www.google.com/"},
        ],

        # ── PROVA SOCIAL (LOGOS) ─────────────────────────────────────────────
        "t6_trust_label": [{"valor": "TRUSTED BY INDUSTRY LEADERS:"}],
        "t6_logos": [
            {"valor": "MATTEL"},
            {"valor": "SIEMENS"},
            {"valor": "BMW"},
            {"valor": "BASF"},
        ],

        # ── APLICAÇÕES (CARDS) ───────────────────────────────────────────────
        "t6_apps_titulo": [{"valor": "APLICAÇÕES DO SISTEMA"}],
        "t6_apps": [
            {"num": "01", "label": "AUTONOMIA",     "titulo": "Crie e customize em minutos sem depender de terceiros ou agências lentas."},
            {"num": "02", "label": "RENTABILIDADE", "titulo": "Venda sites profissionais com margem de lucro industrial para o mercado B2B."},
            {"num": "03", "label": "PERFORMANCE",   "titulo": "Aumente a conversão dos seus produtos com layouts validados por testes de stress."},
        ],

        # ── WORKFLOW ────────────────────────────────────────────────────────
        "t6_flow_titulo": [{"valor": "FLUXO DE IMPLEMENTAÇÃO"}],
        "t6_flow": [
            {"num": "01", "titulo": "AQUISIÇÃO DO MÓDULO", "desc": "Acesso imediato ao repositório de códigos fonte após a validação."},
            {"num": "02", "titulo": "ASSEMBLY (MONTAGEM)", "desc": "Substitua textos e imagens seguindo o nosso manual de diretrizes visuais."},
            {"num": "03", "titulo": "DEPLOYMENT",          "desc": "Conecte o seu domínio e publique o site em servidores de alta velocidade."},
            {"num": "04", "titulo": "OPERAÇÃO",            "desc": "Seu site está pronto para gerar resultados com manutenção zero."},
        ],

        # ── PLANOS ──────────────────────────────────────────────────────────
        "t6_planos_titulo": [{"valor": "PLANOS DE ACESSO"}],
        "t6_planos": [
            {"nome": "BASIC UNIT", "valor": "R$ 97",  "features": "1 Template Modular\nManual de Montagem",                          "btn_txt": "ADQUIRIR BASIC",      "url": "https://www.google.com/", "destaque": False},
            {"nome": "FULL STACK",  "valor": "R$ 197", "features": "Todos os Templates\nSuporte Técnico Direto\nUpdates de Engenharia", "btn_txt": "ADQUIRIR FULL",       "url": "https://www.google.com/", "destaque": True},
            {"nome": "ENTERPRISE", "valor": "R$ 497", "features": "Licença Comercial\nWhitelabel Ready\nConsultoria de Deploy",        "btn_txt": "ADQUIRIR ENTERPRISE", "url": "https://www.google.com/", "destaque": False},
        ],

        # ── FAQ ─────────────────────────────────────────────────────────────
        "t6_faqs": [
            {"pergunta": "O CÓDIGO É OTIMIZADO PARA SEO?",  "resposta": "Sim, todos os modelos seguem a semântica correta de HTML5 para máxima indexação."},
            {"pergunta": "POSSO ALTERAR AS CORES E FONTES?", "resposta": "Absolutamente. O sistema é modular e permite alterações rápidas no ficheiro de estilos."},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t6_footer_left":   [{"valor": "SITE PRO / ENGINEERING DIVISION"}],
        "t6_footer_center": [{"valor": "© 2026 ALL RIGHTS RESERVED"}],
        "t6_footer_right":  [{"valor": "BUILD_V.4.0.1"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t6_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Cores Industriais</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t6_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t6_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t6_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t6_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t6_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t6_cores) > 1 and _del_btn(f"t6_cor_del_{i}"):
                        st.session_state.t6_cores.pop(i); st.rerun()
            if _add_btn("t6_cor_add", "＋ Adicionar cor"):
                st.session_state.t6_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, item in enumerate(st.session_state.t6_navbar_logo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_navbar_logo[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t6_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_navbar_logo) > 1 and _del_btn(f"t6_logo_del_{i}"):
                        st.session_state.t6_navbar_logo.pop(i); st.rerun()
            if _add_btn("t6_logo_add", "＋ Adicionar logo"):
                st.session_state.t6_navbar_logo.append({"valor": "NOVA MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL de destino)*")
            for i, link in enumerate(st.session_state.t6_navbar_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_navbar_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t6_nl_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t6_navbar_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t6_nl_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t6_navbar_links) > 1 and _del_btn(f"t6_nl_del_{i}"):
                        st.session_state.t6_navbar_links.pop(i); st.rerun()
            if _add_btn("t6_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t6_navbar_links.append({"texto": "Link", "url": "#"}); st.rerun()

            st.caption("Botão CTA da Navbar  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t6_navbar_cta):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_navbar_cta[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t6_ncta_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t6_navbar_cta[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t6_ncta_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t6_navbar_cta) > 1 and _del_btn(f"t6_ncta_del_{i}"):
                        st.session_state.t6_navbar_cta.pop(i); st.rerun()
            if _add_btn("t6_ncta_add", "＋ Adicionar botão CTA"):
                st.session_state.t6_navbar_cta.append({"texto": "NOVO CTA", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏗️ Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Label Mono (texto pequeno acima do título)")
            for i, m in enumerate(st.session_state.t6_hero_mono):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_mono[i]["valor"] = st.text_input(
                        "Mono Label", m["valor"], key=f"t6_h_m_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_hero_mono) > 1 and _del_btn(f"t6_h_m_del_{i}"):
                        st.session_state.t6_hero_mono.pop(i); st.rerun()
            if _add_btn("t6_h_m_add", "＋ Adicionar label mono"):
                st.session_state.t6_hero_mono.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título do Hero  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t6_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t6_h_t_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_hero_titulos) > 1 and _del_btn(f"t6_h_t_del_{i}"):
                        st.session_state.t6_hero_titulos.pop(i); st.rerun()
            if _add_btn("t6_h_t_add", "＋ Adicionar título"):
                st.session_state.t6_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo do Hero")
            for i, s in enumerate(st.session_state.t6_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_subtitulos[i]["valor"] = st.text_area(
                        "Subtítulo", s["valor"], key=f"t6_h_s_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_hero_subtitulos) > 1 and _del_btn(f"t6_h_s_del_{i}"):
                        st.session_state.t6_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t6_h_s_add", "＋ Adicionar subtítulo"):
                st.session_state.t6_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botões do Hero  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t6_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t6_h_btn_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t6_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t6_h_btn_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t6_hero_btns) > 1 and _del_btn(f"t6_h_btn_del_{i}"):
                        st.session_state.t6_hero_btns.pop(i); st.rerun()
            if _add_btn("t6_h_btn_add", "＋ Adicionar botão ao hero"):
                st.session_state.t6_hero_btns.append({"texto": "NOVO BOTÃO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CATÁLOGO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📦 Catálogo de Componentes</div>', unsafe_allow_html=True)

            st.caption("Label Mono da seção")
            for i, m in enumerate(st.session_state.t6_cat_mono):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_cat_mono[i]["valor"] = st.text_input(
                        "Mono", m["valor"], key=f"t6_cat_m_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_cat_mono) > 1 and _del_btn(f"t6_cat_m_del_{i}"):
                        st.session_state.t6_cat_mono.pop(i); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_cat_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_cat_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_cat_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_cat_titulos) > 1 and _del_btn(f"t6_cat_t_del_{i}"):
                        st.session_state.t6_cat_titulos.pop(i); st.rerun()

            st.caption("Itens do catálogo  *(Nome | REF | Imagem | Descrição | Texto Botão | URL)*")
            for i, item in enumerate(st.session_state.t6_cat_items):
                with st.expander(f"Modelo {i+1}: {item['nome']}"):
                    st.session_state.t6_cat_items[i]["nome"] = st.text_input(
                        "Nome do Modelo", item["nome"], key=f"t6_ci_n_{i}")
                    st.session_state.t6_cat_items[i]["ref"] = st.text_input(
                        "REF (Código)", item["ref"], key=f"t6_ci_r_{i}")
                    st.session_state.t6_cat_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t6_ci_i_{i}")
                    st.session_state.t6_cat_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t6_ci_d_{i}", height=70)
                    st.session_state.t6_cat_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t6_ci_bt_{i}")
                    st.session_state.t6_cat_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t6_ci_u_{i}")
                    if len(st.session_state.t6_cat_items) > 1:
                        if st.button("🗑 Remover este modelo", key=f"t6_ci_del_{i}"):
                            st.session_state.t6_cat_items.pop(i); st.rerun()
            if _add_btn("t6_ci_add", "＋ Adicionar modelo ao catálogo"):
                st.session_state.t6_cat_items.append({
                    "nome": "NOVO MODELO", "ref": "BTZ-00", "img": "",
                    "desc": "Descrição do modelo.", "btn_txt": "INSPECIONAR BTZ-00", "url": "#"
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROVA SOCIAL (LOGOS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Prova Social (Marcas de Confiança)</div>', unsafe_allow_html=True)

            st.caption("Label da faixa")
            for i, item in enumerate(st.session_state.t6_trust_label):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_trust_label[i]["valor"] = st.text_input(
                        "Label", item["valor"], key=f"t6_tl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_trust_label) > 1 and _del_btn(f"t6_tl_del_{i}"):
                        st.session_state.t6_trust_label.pop(i); st.rerun()

            st.caption("Marcas / Logos  *(nome em texto)*")
            for i, logo in enumerate(st.session_state.t6_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_logos[i]["valor"] = st.text_input(
                        "Marca", logo["valor"], key=f"t6_l_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_logos) > 1 and _del_btn(f"t6_l_del_{i}"):
                        st.session_state.t6_logos.pop(i); st.rerun()
            if _add_btn("t6_l_add", "＋ Adicionar marca"):
                st.session_state.t6_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # APLICAÇÕES (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Aplicações do Sistema</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_apps_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_apps_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_at_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_apps_titulo) > 1 and _del_btn(f"t6_at_del_{i}"):
                        st.session_state.t6_apps_titulo.pop(i); st.rerun()

            st.caption("Cards de aplicação  *(Número | Rótulo | Descrição)*")
            for i, app in enumerate(st.session_state.t6_apps):
                with st.expander(f"Card {app['num']}: {app['label']}"):
                    st.session_state.t6_apps[i]["num"] = st.text_input(
                        "Número", app["num"], key=f"t6_a_n_{i}")
                    st.session_state.t6_apps[i]["label"] = st.text_input(
                        "Rótulo", app["label"], key=f"t6_a_l_{i}")
                    st.session_state.t6_apps[i]["titulo"] = st.text_area(
                        "Descrição", app["titulo"], key=f"t6_a_t_{i}", height=70)
                    if len(st.session_state.t6_apps) > 1:
                        if st.button("🗑 Remover este card", key=f"t6_a_del_{i}"):
                            st.session_state.t6_apps.pop(i); st.rerun()
            if _add_btn("t6_a_add", "＋ Adicionar card de aplicação"):
                st.session_state.t6_apps.append({"num": "04", "label": "NOVO", "titulo": "Descrição da aplicação."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # WORKFLOW (FLUXO)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚙️ Fluxo de Implementação</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_flow_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_flow_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_ft_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_flow_titulo) > 1 and _del_btn(f"t6_ft_del_{i}"):
                        st.session_state.t6_flow_titulo.pop(i); st.rerun()

            st.caption("Passos do workflow  *(Número | Título | Descrição)*")
            for i, flow in enumerate(st.session_state.t6_flow):
                with st.expander(f"Passo {flow['num']}: {flow['titulo']}"):
                    st.session_state.t6_flow[i]["num"] = st.text_input(
                        "Número", flow["num"], key=f"t6_f_n_{i}")
                    st.session_state.t6_flow[i]["titulo"] = st.text_input(
                        "Título", flow["titulo"], key=f"t6_f_t_{i}")
                    st.session_state.t6_flow[i]["desc"] = st.text_area(
                        "Descrição", flow["desc"], key=f"t6_f_d_{i}", height=70)
                    if len(st.session_state.t6_flow) > 1:
                        if st.button("🗑 Remover este passo", key=f"t6_f_del_{i}"):
                            st.session_state.t6_flow.pop(i); st.rerun()
            if _add_btn("t6_f_add", "＋ Adicionar passo ao workflow"):
                st.session_state.t6_flow.append({"num": "05", "titulo": "NOVO PASSO", "desc": "Descrição do passo."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PLANOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos de Acesso</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_planos_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_planos_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_pt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_planos_titulo) > 1 and _del_btn(f"t6_pt_del_{i}"):
                        st.session_state.t6_planos_titulo.pop(i); st.rerun()

            st.caption("Planos  *(Nome | Preço | Features | Botão | URL | Destaque)*")
            for i, plano in enumerate(st.session_state.t6_planos):
                with st.expander(f"Plano: {plano['nome']}"):
                    st.session_state.t6_planos[i]["nome"] = st.text_input(
                        "Nome do Plano", plano["nome"], key=f"t6_p_n_{i}")
                    st.session_state.t6_planos[i]["valor"] = st.text_input(
                        "Preço", plano["valor"], key=f"t6_p_v_{i}")
                    st.session_state.t6_planos[i]["features"] = st.text_area(
                        "Features (uma por linha)", plano["features"], key=f"t6_p_f_{i}", height=100)
                    st.session_state.t6_planos[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", plano["btn_txt"], key=f"t6_p_bt_{i}")
                    st.session_state.t6_planos[i]["url"] = st.text_input(
                        "URL do Botão", plano["url"], key=f"t6_p_u_{i}")
                    st.session_state.t6_planos[i]["destaque"] = st.checkbox(
                        "Destaque (Fundo Preto)", value=plano["destaque"], key=f"t6_p_d_{i}")
                    if len(st.session_state.t6_planos) > 1:
                        if st.button("🗑 Remover este plano", key=f"t6_p_del_{i}"):
                            st.session_state.t6_planos.pop(i); st.rerun()
            if _add_btn("t6_p_add", "＋ Adicionar plano"):
                st.session_state.t6_planos.append({
                    "nome": "NOVO PLANO", "valor": "R$ 0", "features": "Feature 1\nFeature 2",
                    "btn_txt": "ADQUIRIR", "url": "#", "destaque": False
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ FAQ</div>', unsafe_allow_html=True)
            st.caption("Perguntas e Respostas")
            for i, faq in enumerate(st.session_state.t6_faqs):
                with st.expander(f"FAQ {i+1}: {faq['pergunta'][:40]}..."):
                    st.session_state.t6_faqs[i]["pergunta"] = st.text_input(
                        "Pergunta", faq["pergunta"], key=f"t6_faq_p_{i}")
                    st.session_state.t6_faqs[i]["resposta"] = st.text_area(
                        "Resposta", faq["resposta"], key=f"t6_faq_r_{i}", height=80)
                    if len(st.session_state.t6_faqs) > 1:
                        if st.button("🗑 Remover esta pergunta", key=f"t6_faq_del_{i}"):
                            st.session_state.t6_faqs.pop(i); st.rerun()
            if _add_btn("t6_faq_add", "＋ Adicionar pergunta ao FAQ"):
                st.session_state.t6_faqs.append({"pergunta": "Nova pergunta?", "resposta": "Resposta..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔻 Footer (Rodapé)</div>', unsafe_allow_html=True)

            st.caption("Texto esquerdo")
            for i, f in enumerate(st.session_state.t6_footer_left):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_left[i]["valor"] = st.text_input(
                        "Footer Esquerda", f["valor"], key=f"t6_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_footer_left) > 1 and _del_btn(f"t6_fl_del_{i}"):
                        st.session_state.t6_footer_left.pop(i); st.rerun()
            if _add_btn("t6_fl_add", "＋ Adicionar texto esquerdo"):
                st.session_state.t6_footer_left.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Texto central  *(ex: © 2026 ALL RIGHTS RESERVED)*")
            for i, f in enumerate(st.session_state.t6_footer_center):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_center[i]["valor"] = st.text_input(
                        "Footer Centro", f["valor"], key=f"t6_fc_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_footer_center) > 1 and _del_btn(f"t6_fc_del_{i}"):
                        st.session_state.t6_footer_center.pop(i); st.rerun()
            if _add_btn("t6_fc_add", "＋ Adicionar texto central"):
                st.session_state.t6_footer_center.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Texto direito  *(ex: BUILD_V.4.0.1)*")
            for i, f in enumerate(st.session_state.t6_footer_right):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_right[i]["valor"] = st.text_input(
                        "Footer Direita", f["valor"], key=f"t6_fr_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_footer_right) > 1 and _del_btn(f"t6_fr_del_{i}"):
                        st.session_state.t6_footer_right.pop(i); st.rerun()
            if _add_btn("t6_fr_add", "＋ Adicionar texto direito"):
                st.session_state.t6_footer_right.append({"valor": "Novo texto"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t6_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t6_obs_{i}", height=80,
                        placeholder="Ex: quero mudar a fonte, ajustar espaçamento...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_obs) > 1 and _del_btn(f"t6_obs_del_{i}"):
                        st.session_state.t6_obs.pop(i); st.rerun()
            if _add_btn("t6_obs_add", "＋ Adicionar observação"):
                st.session_state.t6_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t6_send", type="primary"):
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
