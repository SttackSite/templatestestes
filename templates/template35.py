import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img35.png"
TEMPLATE_NAME = "Template 35 — Good Secrets Style (Nutrição Chic)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Good Secrets
        "t35_cores": [
            {"nome": "Fundo (gs-bg)", "valor": "#FDF9F3"},
            {"nome": "Escuro (gs-dark)", "valor": "#2D1B14"},
            {"nome": "Texto (gs-text)", "valor": "#4A3B33"},
            {"nome": "Acento (gs-accent)", "valor": "#E8D5C4"},
        ],
        # Navbar
        "t35_nav_logos": [{"texto": "GOOD SECRETS"}],
        "t35_nav_links": [
            {"texto": "Suplementos", "url": "#produtos"},
            {"texto": "Ritual", "url": "#narrativa"},
            {"texto": "Sobre", "url": "#narrativa"},
        ],
        "t35_nav_ctas": [{"texto": "Comprar", "url": "https://www.google.com/"}],
        # Hero Section
        "t35_hero_labels": [{"valor": "O SEGREDO DA LONGEVIDADE"}],
        "t35_hero_titulos": [{"valor": "Nutrição consciente para <span style='font-style:italic'>mentes modernas.</span>"}],
        "t35_hero_descs": [{"valor": "Acreditamos que o bem-estar começa de dentro para fora. Criamos suplementos puros, potentes e elegantes para o seu ritual diário."}],
        "t35_hero_btns": [{"texto": "VER COLEÇÃO", "url": "#produtos"}],
        "t35_hero_imgs": [{"url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=800"}],
        # Produtos (Cards)
        "t35_prod_headers": [{"valor": "Feito para o seu melhor eu."}],
        "t35_prod_items": [
            {"titulo": "FOCO", "desc": "Clareza cognitiva e energia mental sustentada.", "url": "https://www.google.com/"},
            {"titulo": "CALMA", "desc": "Equilíbrio para os dias de alta intensidade.", "url": "https://www.google.com/"},
            {"titulo": "VITAL", "desc": "Recuperação profunda e suporte imunológico.", "url": "https://www.google.com/"},
        ],
        # Narrativa / Sobre
        "t35_narr_titulos": [{"valor": "A pureza é a nossa <br>única regra."}],
        "t35_narr_descs": [{"valor": "Cada ingrediente em nossos suplementos é selecionado com rigor científico e ético. Não usamos enchimentos, não usamos atalhos. Apenas o que seu corpo realmente precisa."}],
        "t35_narr_links": [{"texto": "Conheça nossa origem →", "url": "https://www.google.com/"}],
        "t35_narr_imgs": [{"url": "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=800"}],
        # Footer
        "t35_foot_logos": [{"texto": "GOOD SECRETS"}],
        "t35_foot_descs": [{"texto": "Inspirando rituais de saúde desde 2026."}],
        "t35_foot_cols": [
            {
                "titulo": "MENU",
                "links": [
                    {"texto": "Produtos", "url": "https://www.google.com/"},
                    {"texto": "Nosso Estudo", "url": "https://www.google.com/"},
                    {"texto": "Assinatura", "url": "https://www.google.com/"},
                    {"texto": "Imprensa", "url": "https://www.google.com/"}
                ]
            },
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "Instagram", "url": "https://www.google.com/"},
                    {"texto": "E-mail", "url": "mailto:contato@goodsecrets.com.br"},
                    {"texto": "Lojas", "url": "https://www.google.com/"}
                ]
            }
        ],
        "t35_foot_copys": [{"valor": "© 2026 GOOD SECRETS BRASIL."}],
        "t35_foot_legals": [{"texto": "PRIVACIDADE & TERMOS", "url": "https://www.google.com/"}],
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
            for i, cor in enumerate(st.session_state.t35_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t35_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t35_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t35_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t35_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t35_cores) > 1 and _del_btn(f"t35_cor_del_{i}"):
                        st.session_state.t35_cores.pop(i); st.rerun()
            if _add_btn("t35_cor_add", "＋ Adicionar cor"):
                st.session_state.t35_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t35_nav_logos):
                st.session_state.t35_nav_logos[i]["texto"] = st.text_input("Logo Marca", item["texto"], key=f"t35_nav_l_t_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t35_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t35_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t35_navl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t35_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t35_navl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t35_nav_links) > 1 and _del_btn(f"t35_navl_del_{i}"):
                        st.session_state.t35_nav_links.pop(i); st.rerun()
            if _add_btn("t35_navl_add", "＋ Adicionar link"):
                st.session_state.t35_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Botão Destaque (CTA)")
            for i, cta in enumerate(st.session_state.t35_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t35_nav_ctas[i]["texto"] = st.text_input("Texto", cta["texto"], key=f"t35_ncta_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t35_nav_ctas[i]["url"] = st.text_input("URL", cta["url"], key=f"t35_ncta_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t35_nav_ctas) > 1 and _del_btn(f"t35_ncta_del_{i}"):
                        st.session_state.t35_nav_ctas.pop(i); st.rerun()
            if _add_btn("t35_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t35_nav_ctas.append({"texto": "CTA", "url": "#"}); st.rerun()

            # ✨ HERO SECTION
            st.markdown('<div class="section-label">✨ Hero Section</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t35_hero_labels):
                st.session_state.t35_hero_labels[i]["valor"] = st.text_input("Label Hero", l["valor"], key=f"t35_h_l_{i}")
            for i, t in enumerate(st.session_state.t35_hero_titulos):
                st.session_state.t35_hero_titulos[i]["valor"] = st.text_area("Título Hero (HTML)", t["valor"], key=f"t35_h_t_{i}")
            for i, d in enumerate(st.session_state.t35_hero_descs):
                st.session_state.t35_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t35_h_d_{i}")
            for i, btn in enumerate(st.session_state.t35_hero_btns):
                c1, c2 = st.columns(2)
                with c1: st.session_state.t35_hero_btns[i]["texto"] = st.text_input("Texto Botão Hero", btn["texto"], key=f"t35_hb_t_{i}")
                with c2: st.session_state.t35_hero_btns[i]["url"] = st.text_input("URL Botão Hero", btn["url"], key=f"t35_hb_u_{i}")
            for i, img in enumerate(st.session_state.t35_hero_imgs):
                st.session_state.t35_hero_imgs[i]["url"] = st.text_input("URL Imagem Hero", img["url"], key=f"t35_h_i_{i}")

            # 💊 PRODUTOS
            st.markdown('<div class="section-label">💊 Produtos (Cards)</div>', unsafe_allow_html=True)
            for i, ph in enumerate(st.session_state.t35_prod_headers):
                st.session_state.t35_prod_headers[i]["valor"] = st.text_input("Título Seção Produtos", ph["valor"], key=f"t35_p_h_{i}")
            
            for i, item in enumerate(st.session_state.t35_prod_items):
                with st.expander(f"Produto {i+1}: {item['titulo']}"):
                    st.session_state.t35_prod_items[i]["titulo"] = st.text_input("Título", item["titulo"], key=f"t35_pi_t_{i}")
                    st.session_state.t35_prod_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t35_pi_d_{i}")
                    st.session_state.t35_prod_items[i]["url"] = st.text_input("URL Compra", item["url"], key=f"t35_pi_u_{i}")
                    if len(st.session_state.t35_prod_items) > 1 and _del_btn(f"t35_pi_del_{i}", "Remover card"):
                        st.session_state.t35_prod_items.pop(i); st.rerun()
            if _add_btn("t35_pi_add", "＋ Adicionar produto"):
                st.session_state.t35_prod_items.append({"titulo": "NOVO", "desc": "DESC", "url": "#"}); st.rerun()

            # 📖 NARRATIVA
            st.markdown('<div class="section-label">📖 Narrativa / Sobre</div>', unsafe_allow_html=True)
            for i, nt in enumerate(st.session_state.t35_narr_titulos):
                st.session_state.t35_narr_titulos[i]["valor"] = st.text_area("Título Narrativa (HTML)", nt["valor"], key=f"t35_n_t_{i}")
            for i, nd in enumerate(st.session_state.t35_narr_descs):
                st.session_state.t35_narr_descs[i]["valor"] = st.text_area("Descrição Narrativa", nd["valor"], key=f"t35_n_d_{i}")
            for i, nl in enumerate(st.session_state.t35_narr_links):
                c1, c2 = st.columns(2)
                with c1: st.session_state.t35_narr_links[i]["texto"] = st.text_input("Texto Link Narrativa", nl["texto"], key=f"t35_nl_t_{i}")
                with c2: st.session_state.t35_narr_links[i]["url"] = st.text_input("URL Link Narrativa", nl["url"], key=f"t35_nl_u_{i}")
            for i, ni in enumerate(st.session_state.t35_narr_imgs):
                st.session_state.t35_narr_imgs[i]["url"] = st.text_input("URL Imagem Narrativa", ni["url"], key=f"t35_n_i_{i}")

            # 👣 FOOTER
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, fl in enumerate(st.session_state.t35_foot_logos):
                st.session_state.t35_foot_logos[i]["texto"] = st.text_input("Logo Footer", fl["texto"], key=f"t35_f_l_{i}")
            for i, fd in enumerate(st.session_state.t35_foot_descs):
                st.session_state.t35_foot_descs[i]["texto"] = st.text_input("Descrição Footer", fd["texto"], key=f"t35_f_d_{i}")
            
            st.caption("Colunas de Links")
            for i, col in enumerate(st.session_state.t35_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t35_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t35_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 5, 1])
                        with c1: st.session_state.t35_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t35_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t35_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t35_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t35_fc_l_del_{i}_{j}"):
                                st.session_state.t35_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t35_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t35_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t35_foot_cols) > 1 and _del_btn(f"t35_fc_del_{i}", "Remover coluna"):
                        st.session_state.t35_foot_cols.pop(i); st.rerun()
            if _add_btn("t35_fc_add", "＋ Adicionar coluna"):
                st.session_state.t35_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "LINK", "url": "#"}]}); st.rerun()

            for i, fcp in enumerate(st.session_state.t35_foot_copys):
                st.session_state.t35_foot_copys[i]["valor"] = st.text_input("Copyright", fcp["valor"], key=f"t35_fcp_{i}")
            
            st.caption("Links Legais (Direita)")
            for i, flg in enumerate(st.session_state.t35_foot_legals):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t35_foot_legals[i]["texto"] = st.text_input("Texto", flg["texto"], key=f"t35_flg_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t35_foot_legals[i]["url"] = st.text_input("URL", flg["url"], key=f"t35_flg_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t35_foot_legals) > 1 and _del_btn(f"t35_flg_del_{i}"):
                        st.session_state.t35_foot_legals.pop(i); st.rerun()
            if _add_btn("t35_flg_add", "＋ Adicionar link legal"):
                st.session_state.t35_foot_legals.append({"texto": "TERMOS", "url": "#"}); st.rerun()

            # 📝 OBSERVAÇÕES
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t35_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t35_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t35_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t35_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # 🖼️ PAINEL DIREITO
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="💊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
