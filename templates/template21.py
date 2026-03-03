import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img21.png"
TEMPLATE_NAME = "Template 21 — Feastables Style (MrBeast Inspired E-commerce)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Feastables
        "t21_cores": [
            {"nome": "Azul Principal (Feast Blue)", "valor": "#0047ff"},
            {"nome": "Rosa/Magenta (Feast Pink)", "valor": "#ff00ff"},
            {"nome": "Amarelo (Feast Yellow)", "valor": "#ffff00"},
            {"nome": "Texto (Branco)", "valor": "#ffffff"},
        ],
        # Banner Animado (Marquee)
        "t21_marquee_items": [
            {"texto": "MELHOR QUE O SEU CHOCOLATE ATUAL 🔥"},
            {"texto": "INGREDIENTES REAIS 🔥"},
            {"texto": "DO MR MOON 🔥"},
            {"texto": "PROVE A DIFERENÇA 🔥"},
        ],
        # Header / Logo
        "t21_header_logos": [{"valor": "FEASTABLES"}],
        # Hero Section
        "t21_hero_titulos": [{"valor": "O CHOCOLATE<br>QUE DETONA."}],
        "t21_hero_descs": [{"valor": "Zero porcaria. Apenas sabor épico."}],
        "t21_hero_btns": [{"texto": "COMPRE AGORA", "url": "https://www.google.com/"}],
        "t21_hero_imgs": [{"valor": "https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800"}],
        # Loja de Produtos
        "t21_shop_titulos": [{"valor": "ESCOLHA SEU TIME"}],
        "t21_product_items": [
            {"img": "https://images.unsplash.com/photo-1548907040-4baa42d10919?w=400", "nome": "MILK CRUNCH", "flavor": "Com Arroz Crocante", "price": "19,90", "url": "#"},
            {"img": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=400", "nome": "ORIGINAL MILK", "flavor": "Clássico e Cremoso", "price": "18,90", "url": "#"},
            {"img": "https://images.unsplash.com/photo-1581798459219-318e76aecc7b?w=400", "nome": "PEANUT BUTTER", "flavor": "Manteiga de Amendoim", "price": "22,90", "url": "#"},
        ],
        # Por que nós? (Benefícios)
        "t21_benefit_titulos": [{"valor": "O QUE TEM DENTRO IMPORTA."}],
        "t21_benefit_items": [
            {"emoji": "🌾", "titulo": "SEM GLÚTEN"},
            {"emoji": "🌱", "titulo": "INGREDIENTES SIMPLES"},
            {"emoji": "👅", "titulo": "SABOR INCRÍVEL"},
        ],
        # Footer
        "t21_foot_brand_names": [{"valor": "FEASTABLES"}],
        "t21_foot_brand_descs": [{"valor": "Inspirado pelo Mrmoon."}],
        "t21_foot_cols": [
            {
                "titulo": "RECURSOS",
                "links": [
                    {"texto": "Onde Comprar", "url": "#"},
                    {"texto": "Perguntas Frequentes", "url": "#"},
                    {"texto": "Termos de Uso", "url": "#"}
                ]
            },
            {
                "titulo": "NOS SIGA",
                "links": [
                    {"texto": "TikTok", "url": "#"},
                    {"texto": "Instagram", "url": "#"},
                    {"texto": "YouTube", "url": "#"}
                ]
            }
        ],
        "t21_foot_copys": [{"valor": "© 2026 FEASTABLES INC. TODOS OS DIREITOS RESERVADOS."}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;900&display=swap');
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
            for i, cor in enumerate(st.session_state.t21_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t21_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t21_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t21_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t21_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t21_cores) > 1 and _del_btn(f"t21_cor_del_{i}"):
                        st.session_state.t21_cores.pop(i); st.rerun()
            if _add_btn("t21_cor_add", "＋ Adicionar cor"):
                st.session_state.t21_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # BANNER ANIMADO (MARQUEE)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Banner Animado (Marquee)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t21_marquee_items):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t21_marquee_items[i]["texto"] = st.text_input("Texto do Banner", item["texto"], key=f"t21_mq_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t21_marquee_items) > 1 and _del_btn(f"t21_mq_del_{i}"):
                        st.session_state.t21_marquee_items.pop(i); st.rerun()
            if _add_btn("t21_mq_add", "＋ Adicionar texto ao banner"):
                st.session_state.t21_marquee_items.append({"texto": "NOVO AVISO 🔥"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HEADER / LOGO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Logo)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t21_header_logos):
                st.session_state.t21_header_logos[i]["valor"] = st.text_input("Logo Principal", item["valor"], key=f"t21_hl_{i}")

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💥 Hero Section</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t21_hero_titulos):
                st.session_state.t21_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br>)", t["valor"], key=f"t21_h_t_{i}")
            for i, d in enumerate(st.session_state.t21_hero_descs):
                st.session_state.t21_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t21_h_d_{i}")
            for i, img in enumerate(st.session_state.t21_hero_imgs):
                st.session_state.t21_hero_imgs[i]["valor"] = st.text_input("URL Imagem Hero", img["valor"], key=f"t21_h_i_{i}")
            for i, btn in enumerate(st.session_state.t21_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t21_hero_btns[i]["texto"] = st.text_input("Texto Botão", btn["texto"], key=f"t21_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t21_hero_btns[i]["url"] = st.text_input("URL Botão", btn["url"], key=f"t21_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t21_hero_btns) > 1 and _del_btn(f"t21_hb_del_{i}"):
                        st.session_state.t21_hero_btns.pop(i); st.rerun()
            if _add_btn("t21_hb_add", "＋ Adicionar botão"):
                st.session_state.t21_hero_btns.append({"texto": "COMPRE", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # LOJA DE PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍫 Loja de Produtos</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t21_shop_titulos):
                st.session_state.t21_shop_titulos[i]["valor"] = st.text_input("Título da Loja", t["valor"], key=f"t21_st_t_{i}")
            
            for i, item in enumerate(st.session_state.t21_product_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t21_product_items[i]["nome"] = st.text_input("Nome", item["nome"], key=f"t21_pi_n_{i}")
                    st.session_state.t21_product_items[i]["flavor"] = st.text_input("Sabor/Subtítulo", item["flavor"], key=f"t21_pi_f_{i}")
                    st.session_state.t21_product_items[i]["price"] = st.text_input("Preço (ex: 19,90)", item["price"], key=f"t21_pi_p_{i}")
                    st.session_state.t21_product_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t21_pi_i_{i}")
                    st.session_state.t21_product_items[i]["url"] = st.text_input("URL Compra", item["url"], key=f"t21_pi_u_{i}")
                    if len(st.session_state.t21_product_items) > 1 and _del_btn(f"t21_pi_del_{i}", "Remover produto"):
                        st.session_state.t21_product_items.pop(i); st.rerun()
            if _add_btn("t21_pi_add", "＋ Adicionar produto"):
                st.session_state.t21_product_items.append({"img": "", "nome": "NOVO SABOR", "flavor": "DESCRIÇÃO", "price": "0,00", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # BENEFÍCIOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌱 Por que nós? (Benefícios)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t21_benefit_titulos):
                st.session_state.t21_benefit_titulos[i]["valor"] = st.text_input("Título Benefícios", t["valor"], key=f"t21_bt_t_{i}")
            
            for i, item in enumerate(st.session_state.t21_benefit_items):
                c1, c2, c3 = st.columns([2, 7, 1])
                with c1: st.session_state.t21_benefit_items[i]["emoji"] = st.text_input("Emoji", item["emoji"], key=f"t21_bi_e_{i}", label_visibility="collapsed")
                with c2: st.session_state.t21_benefit_items[i]["titulo"] = st.text_input("Título", item["titulo"], key=f"t21_bi_t_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t21_benefit_items) > 1 and _del_btn(f"t21_bi_del_{i}"):
                        st.session_state.t21_benefit_items.pop(i); st.rerun()
            if _add_btn("t21_bi_add", "＋ Adicionar benefício"):
                st.session_state.t21_benefit_items.append({"emoji": "✨", "titulo": "NOVO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)
            for i, name in enumerate(st.session_state.t21_foot_brand_names):
                st.session_state.t21_foot_brand_names[i]["valor"] = st.text_input("Nome Marca (Footer)", name["valor"], key=f"t21_fn_{i}")
            for i, desc in enumerate(st.session_state.t21_foot_brand_descs):
                st.session_state.t21_foot_brand_descs[i]["valor"] = st.text_area("Descrição Marca", desc["valor"], key=f"t21_fd_{i}")
            
            st.caption("Colunas de Links")
            for i, col in enumerate(st.session_state.t21_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t21_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t21_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t21_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t21_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t21_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t21_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t21_fc_l_del_{i}_{j}"):
                                st.session_state.t21_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t21_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t21_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t21_foot_cols) > 1 and st.button("Remover Coluna Inteira", key=f"t21_fc_del_{i}"):
                        st.session_state.t21_foot_cols.pop(i); st.rerun()
            if _add_btn("t21_fc_add", "＋ Adicionar coluna"):
                st.session_state.t21_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t21_foot_copys):
                st.session_state.t21_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t21_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t21_obs_{i}", height=80,
                        placeholder="Ex: Deixar o azul ainda mais vibrante...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t21_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t21_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t21_send", type="primary"):
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
        page_icon="🍫",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
