import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img24.png"
TEMPLATE_NAME = "Template 24 — YOLU Night Care Style (Beauty & Cosmetics)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores YOLU
        "t24_cores": [
            {"nome": "Fundo Início (Azul Escuro)", "valor": "#050a14"},
            {"nome": "Fundo Meio (Azul Noite)", "valor": "#0f1c3d"},
            {"nome": "Fundo Fim (Roxo Profundo)", "valor": "#1e1b4b"},
            {"nome": "Texto Principal (Branco)", "valor": "#ffffff"},
            {"nome": "Destaque (Dourado Suave)", "valor": "#d4af37"},
        ],
        # Navbar
        "t24_nav_logos": [{"valor": "YOLU"}],
        "t24_nav_links": [
            {"texto": "CONCEITO", "url": "#conceito"},
            {"texto": "PRODUTOS", "url": "#produtos"},
            {"texto": "CONTATO", "url": "#contato"},
        ],
        # Hero Section
        "t24_hero_labels": [{"valor": "BELEZA QUE NASCE À NOITE"}],
        "t24_hero_titulos": [{"valor": "A Night Calm<br>Experience"}],
        "t24_hero_descs": [{"valor": "Reparação profunda enquanto você dorme. Sinta a tranquilidade da noite em cada fio."}],
        "t24_hero_imgs": [{"valor": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600"}],
        # Conceito
        "t24_concept_titulos": [{"valor": "Por que Cuidados Noturnos?"}],
        "t24_concept_descs": [{"valor": "Durante a noite, o seu cabelo está livre das agressões externas do dia. É o momento perfeito para a penetração intensa de nutrientes. Nossa fórmula inspirada no 'sono reparador' protege as cutículas do atrito com o travesseiro, garantindo um despertar radiante."}],
        # Produtos
        "t24_product_items": [
            {
                "img": "https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600",
                "nome": "Calm Night Repair",
                "category": "SHAMPOO & TRATAMENTO",
                "desc": "Para cabelos secos e indisciplinados. Foco em hidratação profunda.",
                "btn_text": "SAIBA MAIS",
                "btn_url": "https://www.google.com/"
            },
            {
                "img": "https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600",
                "nome": "Relax Night Repair",
                "category": "CUIDADO INTENSIVO",
                "desc": "Para cabelos danificados por processos químicos. Foco em reconstrução.",
                "btn_text": "SAIBA MAIS",
                "btn_url": "https://www.google.com/"
            },
        ],
        # Footer
        "t24_foot_brand_names": [{"valor": "YOLU"}],
        "t24_foot_copys": [{"valor": "© 2026 YOLU | I-ne Co., Ltd. Todos os direitos reservados."}],
        "t24_foot_cols": [
            {
                "titulo": "REDES SOCIAIS",
                "links": [
                    {"texto": "INSTAGRAM", "url": "#"},
                    {"texto": "TWITTER", "url": "#"},
                    {"texto": "REVIEWS", "url": "#"}
                ]
            }
        ],
        # Observações
        "t13_obs": [{"valor": ""}], # Mantendo a chave para consistência
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

            # ══════════════════════════════════════════════════════════════════
            # CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual (Gradiente)</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t24_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t24_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t24_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t24_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t24_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t24_cores) > 1 and _del_btn(f"t24_cor_del_{i}"):
                        st.session_state.t24_cores.pop(i); st.rerun()
            if _add_btn("t24_cor_add", "＋ Adicionar cor"):
                st.session_state.t24_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t24_nav_logos):
                st.session_state.t24_nav_logos[i]["valor"] = st.text_input("Logo/Nome Marca", item["valor"], key=f"t24_nl_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t24_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t24_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t24_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t24_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t24_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t24_nav_links) > 1 and _del_btn(f"t24_nl_del_{i}"):
                        st.session_state.t24_nav_links.pop(i); st.rerun()
            if _add_btn("t24_nl_add", "＋ Adicionar link"):
                st.session_state.t24_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌙 Hero Section</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t24_hero_labels):
                st.session_state.t24_hero_labels[i]["valor"] = st.text_input("Label Hero", l["valor"], key=f"t24_h_l_{i}")
            for i, t in enumerate(st.session_state.t24_hero_titulos):
                st.session_state.t24_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br>)", t["valor"], key=f"t24_h_t_{i}")
            for i, d in enumerate(st.session_state.t24_hero_descs):
                st.session_state.t24_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t24_h_d_{i}")
            for i, img in enumerate(st.session_state.t24_hero_imgs):
                st.session_state.t24_hero_imgs[i]["valor"] = st.text_input("URL Imagem de Fundo", img["valor"], key=f"t24_h_i_{i}")

            # ══════════════════════════════════════════════════════════════════
            # CONCEITO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Seção de Conceito</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t24_concept_titulos):
                st.session_state.t24_concept_titulos[i]["valor"] = st.text_input("Título Conceito", t["valor"], key=f"t24_ct_{i}")
            for i, d in enumerate(st.session_state.t24_concept_descs):
                st.session_state.t24_concept_descs[i]["valor"] = st.text_area("Descrição Conceito", d["valor"], key=f"t24_cd_{i}")

            # ══════════════════════════════════════════════════════════════════
            # PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧴 Vitrine de Produtos</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t24_product_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t24_product_items[i]["nome"] = st.text_input("Nome Produto", item["nome"], key=f"t24_pi_n_{i}")
                    st.session_state.t24_product_items[i]["category"] = st.text_input("Categoria", item["category"], key=f"t24_pi_c_{i}")
                    st.session_state.t24_product_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t24_pi_d_{i}")
                    st.session_state.t24_product_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t24_pi_i_{i}")
                    c1, c2 = st.columns(2)
                    with c1: st.session_state.t24_product_items[i]["btn_text"] = st.text_input("Texto Botão", item["btn_text"], key=f"t24_pi_bt_{i}")
                    with c2: st.session_state.t24_product_items[i]["btn_url"] = st.text_input("URL Botão", item["btn_url"], key=f"t24_pi_bu_{i}")
                    
                    if len(st.session_state.t24_product_items) > 1 and _del_btn(f"t24_pi_del_{i}", "Remover produto"):
                        st.session_state.t24_product_items.pop(i); st.rerun()
            if _add_btn("t24_pi_add", "＋ Adicionar produto"):
                st.session_state.t24_product_items.append({"img": "", "nome": "NOVO PRODUTO", "category": "CATEGORIA", "desc": "DESCRIÇÃO", "btn_text": "SAIBA MAIS", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, name in enumerate(st.session_state.t24_foot_brand_names):
                st.session_state.t24_foot_brand_names[i]["valor"] = st.text_input("Nome Marca (Footer)", name["valor"], key=f"t24_fn_{i}")
            
            st.caption("Colunas de Links (Redes Sociais)")
            for i, col in enumerate(st.session_state.t24_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t24_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t24_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t24_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t24_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t24_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t24_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t24_fc_l_del_{i}_{j}"):
                                st.session_state.t24_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t24_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t24_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t24_foot_cols) > 1 and st.button("Remover Coluna Inteira", key=f"t24_fc_del_{i}"):
                        st.session_state.t24_foot_cols.pop(i); st.rerun()
            if _add_btn("t24_fc_add", "＋ Adicionar coluna"):
                st.session_state.t24_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t24_foot_copys):
                st.session_state.t24_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t24_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t24_obs_{i}", height=80,
                        placeholder="Ex: Usar tons mais puxados para o dourado...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t24_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t24_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t24_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW (LIMPO)
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
