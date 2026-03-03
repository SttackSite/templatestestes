import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img31.png"
TEMPLATE_NAME = "Template 31 — Epiminds Style (Neurotech & AI)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Epiminds
        "t31_cores": [
            {"nome": "Fundo (epi-bg)", "valor": "#F8F9FF"},
            {"nome": "Roxo (epi-purple)", "valor": "#6c5ce7"},
            {"nome": "Pêssego (epi-peach)", "valor": "#ff8a71"},
            {"nome": "Texto Escuro", "valor": "#1A1A2E"},
            {"nome": "Texto Leve", "valor": "#64648C"},
        ],
        # Navbar
        "t31_nav_logos": [{"texto": "epiminds", "ponto_cor": "#ff8a71"}],
        "t31_nav_links": [
            {"texto": "Produtos", "url": "#metodologia"},
            {"texto": "Neurociência", "url": "#metodologia"},
            {"texto": "Casos de Sucesso", "url": "#beneficios"},
            {"texto": "Sobre nós", "url": "#footer"},
        ],
        "t31_nav_ctas": [{"texto": "Agendar Demo", "url": "https://www.google.com/"}],
        # Hero Section
        "t31_hero_tags": [{"valor": "A NOVA ERA DA SAÚDE MENTAL"}],
        "t31_hero_titulos": [{"valor": "Sua mente é o seu maior <span style='color:#6c5ce7'>ativo tecnológico.</span>"}],
        "t31_hero_descs": [{"valor": "Unimos neurociência aplicada e inteligência artificial para decodificar o comportamento humano e potencializar a performance sustentável de líderes e equipes."}],
        "t31_hero_btns": [{"texto": "QUERO CONHECER A PLATAFORMA", "url": "#metodologia"}],
        # Prova Social (Logos)
        "t31_logo_labels": [{"valor": "CONFIADO POR GIGANTES DO MERCADO"}],
        "t31_logo_items": [
            {"texto": "MICROSOFT"},
            {"texto": "AMAZON"},
            {"texto": "NUBANK"},
            {"texto": "IFood"},
            {"texto": "GOOGLE"},
        ],
        # Metodologia
        "t31_metod_headers": [{"sub": "NOSSA METODOLOGIA", "titulo": "Como hackeamos a alta performance"}],
        "t31_metod_items": [
            {"num": "01", "title": "Mapeamento", "desc": "Utilizamos biomarcadores para entender o estado atual de estresse, foco e resiliência da sua equipe sem invasão de privacidade.", "link_texto": "Saiba mais →", "link_url": "https://www.google.com/"},
            {"num": "02", "title": "Diagnóstico IA", "desc": "Nossa inteligência analisa padrões comportamentais e prevê riscos de burnout com até 3 meses de antecedência.", "link_texto": "Saiba mais →", "link_url": "https://www.google.com/"},
            {"num": "03", "title": "Intervenção", "desc": "Protocolos de neuroplasticidade personalizados para cada indivíduo, focados em recuperação rápida e foco profundo.", "link_texto": "Saiba mais →", "link_url": "https://www.google.com/"},
        ],
        # Benefícios (Dashboard)
        "t31_bene_headers": [{"tag": "INSIGHTS EM TEMPO REAL", "titulo": "O Dashboard do cérebro."}],
        "t31_bene_content": [{"titulo": "Decisões baseadas em dados biológicos, não em suposições.", "desc": "A Epiminds integra-se às ferramentas que sua equipe já usa (Slack, Teams, Calendar) para fornecer uma camada de inteligência emocional e cognitiva."}],
        "t31_bene_list": [
            {"item": "✓ Redução de 40% no turnover por burnout"},
            {"item": "✓ Aumento de 25% na capacidade de foco profundo"},
            {"item": "✓ Melhora comprovada no clima organizacional"},
        ],
        "t31_bene_btns": [{"texto": "VER TODOS OS BENEFÍCIOS", "url": "https://www.google.com/"}],
        # Footer
        "t31_foot_brands": [{"nome": "epiminds.", "desc": "Liderando a fronteira da neurotecnologia aplicada ao trabalho no Brasil e no mundo."}],
        "t31_foot_cols": [
            {
                "titulo": "PRODUTO",
                "links": [
                    {"texto": "Plataforma IA", "url": "https://www.google.com/"},
                    {"texto": "Treinamentos", "url": "https://www.google.com/"},
                    {"texto": "Segurança", "url": "https://www.google.com/"},
                    {"texto": "API", "url": "https://www.google.com/"},
                ]
            },
            {
                "titulo": "RECURSOS",
                "links": [
                    {"texto": "Whitepapers", "url": "https://www.google.com/"},
                    {"texto": "Blog", "url": "https://www.google.com/"},
                    {"texto": "Neuro-Guia", "url": "https://www.google.com/"},
                    {"texto": "Suporte", "url": "https://www.google.com/"},
                ]
            },
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "contato@epiminds.com", "url": "mailto:contato@epiminds.com"},
                    {"texto": "LinkedIn", "url": "https://www.google.com/"},
                    {"texto": "Instagram", "url": "https://www.google.com/"},
                ]
            }
        ],
        "t31_foot_copys": [{"valor": "© 2026 EPIMINDS NEUROTECH S.A."}],
        "t31_foot_legal": [
            {"texto": "POLÍTICA DE PRIVACIDADE", "url": "https://www.google.com/"},
            {"texto": "LGPD", "url": "https://www.google.com/"},
        ],
        # Observações
        "t13_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
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

            # 🎨 CORES
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t31_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t31_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t31_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t31_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t31_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_cores) > 1 and _del_btn(f"t31_cor_del_{i}"):
                        st.session_state.t31_cores.pop(i); st.rerun()
            if _add_btn("t31_cor_add", "＋ Adicionar cor"):
                st.session_state.t31_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t31_nav_logos):
                c1, c2 = st.columns([7, 3])
                with c1: st.session_state.t31_nav_logos[i]["texto"] = st.text_input("Nome Marca", item["texto"], key=f"t31_nl_t_{i}")
                with c2: st.session_state.t31_nav_logos[i]["ponto_cor"] = st.color_picker("Cor Ponto", item["ponto_cor"], key=f"t31_nl_p_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t31_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t31_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t31_navl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t31_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t31_navl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_nav_links) > 1 and _del_btn(f"t31_navl_del_{i}"):
                        st.session_state.t31_nav_links.pop(i); st.rerun()
            if _add_btn("t31_navl_add", "＋ Adicionar link"):
                st.session_state.t31_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Botão de Destaque (CTA)")
            for i, cta in enumerate(st.session_state.t31_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t31_nav_ctas[i]["texto"] = st.text_input("Texto", cta["texto"], key=f"t31_ncta_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t31_nav_ctas[i]["url"] = st.text_input("URL", cta["url"], key=f"t31_ncta_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_nav_ctas) > 1 and _del_btn(f"t31_ncta_del_{i}"):
                        st.session_state.t31_nav_ctas.pop(i); st.rerun()
            if _add_btn("t31_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t31_nav_ctas.append({"texto": "DEMO", "url": "#"}); st.rerun()

            # 🧠 HERO SECTION
            st.markdown('<div class="section-label">🧠 Hero Section</div>', unsafe_allow_html=True)
            for i, tag in enumerate(st.session_state.t31_hero_tags):
                st.session_state.t31_hero_tags[i]["valor"] = st.text_input("Tag Hero", tag["valor"], key=f"t31_h_tag_{i}")
            for i, t in enumerate(st.session_state.t31_hero_titulos):
                st.session_state.t31_hero_titulos[i]["valor"] = st.text_area("Título Hero (HTML)", t["valor"], key=f"t31_h_t_{i}")
            for i, d in enumerate(st.session_state.t31_hero_descs):
                st.session_state.t31_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t31_h_d_{i}")
            
            st.caption("Botões Hero")
            for i, btn in enumerate(st.session_state.t31_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t31_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t31_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t31_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t31_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_hero_btns) > 1 and _del_btn(f"t31_hb_del_{i}"):
                        st.session_state.t31_hero_btns.pop(i); st.rerun()
            if _add_btn("t31_hb_add", "＋ Adicionar botão"):
                st.session_state.t31_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # 🏢 LOGOS (PROVA SOCIAL)
            st.markdown('<div class="section-label">🏢 Prova Social (Logos)</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t31_logo_labels):
                st.session_state.t31_logo_labels[i]["valor"] = st.text_input("Título Logos", l["valor"], key=f"t31_ll_{i}")
            
            for i, item in enumerate(st.session_state.t31_logo_items):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t31_logo_items[i]["texto"] = st.text_input("Logo", item["texto"], key=f"t31_li_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t31_logo_items) > 1 and _del_btn(f"t31_li_del_{i}"):
                        st.session_state.t31_logo_items.pop(i); st.rerun()
            if _add_btn("t31_li_add", "＋ Adicionar logo"):
                st.session_state.t31_logo_items.append({"texto": "NOVA"}); st.rerun()

            # ⚙️ METODOLOGIA
            st.markdown('<div class="section-label">⚙️ Metodologia</div>', unsafe_allow_html=True)
            for i, h in enumerate(st.session_state.t31_metod_headers):
                st.session_state.t31_metod_headers[i]["sub"] = st.text_input("Sub-título", h["sub"], key=f"t31_mh_s_{i}")
                st.session_state.t31_metod_headers[i]["titulo"] = st.text_input("Título Seção", h["titulo"], key=f"t31_mh_t_{i}")
            
            for i, item in enumerate(st.session_state.t31_metod_items):
                with st.expander(f"Passo {i+1}: {item['title']}"):
                    st.session_state.t31_metod_items[i]["num"] = st.text_input("Número", item["num"], key=f"t31_mi_n_{i}")
                    st.session_state.t31_metod_items[i]["title"] = st.text_input("Título", item["title"], key=f"t31_mi_t_{i}")
                    st.session_state.t31_metod_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t31_mi_d_{i}")
                    st.session_state.t31_metod_items[i]["link_texto"] = st.text_input("Texto Link", item["link_texto"], key=f"t31_mi_lt_{i}")
                    st.session_state.t31_metod_items[i]["link_url"] = st.text_input("URL Link", item["link_url"], key=f"t31_mi_lu_{i}")
                    if len(st.session_state.t31_metod_items) > 1 and _del_btn(f"t31_mi_del_{i}", "Remover passo"):
                        st.session_state.t31_metod_items.pop(i); st.rerun()
            if _add_btn("t31_mi_add", "＋ Adicionar passo"):
                st.session_state.t31_metod_items.append({"num": "04", "title": "NOVO", "desc": "DESC", "link_texto": "Saiba mais →", "link_url": "#"}); st.rerun()

            # 📊 BENEFÍCIOS (DASHBOARD)
            st.markdown('<div class="section-label">📊 Benefícios & Resultados</div>', unsafe_allow_html=True)
            for i, h in enumerate(st.session_state.t31_bene_headers):
                st.session_state.t31_bene_headers[i]["tag"] = st.text_input("Tag", h["tag"], key=f"t31_bh_tg_{i}")
                st.session_state.t31_bene_headers[i]["titulo"] = st.text_input("Título Dashboard", h["titulo"], key=f"t31_bh_t_{i}")
            
            for i, c in enumerate(st.session_state.t31_bene_content):
                st.session_state.t31_bene_content[i]["titulo"] = st.text_input("Título Conteúdo", c["titulo"], key=f"t31_bc_t_{i}")
                st.session_state.t31_bene_content[i]["desc"] = st.text_area("Descrição Conteúdo", c["desc"], key=f"t31_bc_d_{i}")
            
            st.caption("Lista de Benefícios")
            for i, item in enumerate(st.session_state.t31_bene_list):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t31_bene_list[i]["item"] = st.text_input("Benefício", item["item"], key=f"t31_bl_i_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t31_bene_list) > 1 and _del_btn(f"t31_bl_del_{i}"):
                        st.session_state.t31_bene_list.pop(i); st.rerun()
            if _add_btn("t31_bl_add", "＋ Adicionar benefício"):
                st.session_state.t31_bene_list.append({"item": "✓ NOVO ITEM"}); st.rerun()

            for i, btn in enumerate(st.session_state.t31_bene_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t31_bene_btns[i]["texto"] = st.text_input("Texto Botão Benefícios", btn["texto"], key=f"t31_bb_t_{i}")
                with c2: st.session_state.t31_bene_btns[i]["url"] = st.text_input("URL Botão Benefícios", btn["url"], key=f"t31_bb_u_{i}")

            # 👣 FOOTER
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, b in enumerate(st.session_state.t31_foot_brands):
                st.session_state.t31_foot_brands[i]["nome"] = st.text_input("Nome Marca Footer", b["nome"], key=f"t31_fb_n_{i}")
                st.session_state.t31_foot_brands[i]["desc"] = st.text_area("Descrição Footer", b["desc"], key=f"t31_fb_d_{i}")

            st.caption("Colunas de Links")
            for i, col in enumerate(st.session_state.t31_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t31_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t31_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t31_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t31_fcl_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t31_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t31_fcl_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t31_fcl_del_{i}_{j}"):
                                st.session_state.t31_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t31_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t31_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t31_foot_cols) > 1 and _del_btn(f"t31_fc_del_{i}", "Remover coluna"):
                        st.session_state.t31_foot_cols.pop(i); st.rerun()
            if _add_btn("t31_fc_add", "＋ Adicionar coluna"):
                st.session_state.t31_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "LINK", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t31_foot_copys):
                st.session_state.t31_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t31_fcp_{i}")
            
            st.caption("Links Legais")
            for i, link in enumerate(st.session_state.t31_foot_legal):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t31_foot_legal[i]["texto"] = st.text_input("Texto Legal", link["texto"], key=f"t31_fl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t31_foot_legal[i]["url"] = st.text_input("URL Legal", link["url"], key=f"t31_fl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_foot_legal) > 1 and _del_btn(f"t31_fl_del_{i}"):
                        st.session_state.t31_foot_legal.pop(i); st.rerun()
            if _add_btn("t31_fl_add", "＋ Adicionar link legal"):
                st.session_state.t31_foot_legal.append({"texto": "LINK", "url": "#"}); st.rerun()

            # 📝 OBSERVAÇÕES
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t31_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t31_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t31_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t31_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # 🖼️ PAINEL DIREITO
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
