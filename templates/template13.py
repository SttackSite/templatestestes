import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img13.png"
TEMPLATE_NAME = "Template 13 — Ogreen Style (Sustentabilidade & Indústria)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Ogreen
        "t13_cores": [
            {"nome": "Verde Principal", "valor": "#005a31"},
            {"nome": "Verde Limão (Stats)", "valor": "#8ec641"},
            {"nome": "Cor de Texto (Escuro)", "valor": "#333333"},
            {"nome": "Cor de Fundo (Claro)", "valor": "#f8f9fa"},
        ],
        # Header / Navbar
        "t13_logos": [{"valor": "ogreen"}],
        "t13_nav_links": [
            {"texto": "A ogreen", "url": "#about"},
            {"texto": "NOSSOS NEGÓCIOS", "url": "#business"},
            {"texto": "SUSTENTABILIDADE", "url": "#sustainability"},
            {"texto": "INVESTIDORES", "url": "#investors"},
            {"texto": "PRODUTOS", "url": "#products"},
        ],
        # Hero Section
        "t13_hero_titulos": [{"valor": "O FUTURO É RENOVÁVEL"}],
        "t13_hero_descs": [{"valor": "Líder na produção de papéis e cartões para embalagens, embalagens de papelão ondulado e sacos industriais."}],
        "t13_hero_imgs": [{"valor": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80"}],
        # Sobre a Ogreen
        "t13_about_titulos": [{"valor": "Sobre a ogreen"}],
        "t13_about_descs": [{"valor": "Com 125 anos de história, somos a maior produtora e exportadora de papéis para embalagens e soluções sustentáveis do Brasil. Nossa atuação é baseada no desenvolvimento sustentável, com florestas 100% plantadas e certificadas."}],
        "t13_about_imgs": [{"valor": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80", "legenda": "Gestão Florestal Responsável"}],
        "t13_about_btns": [{"texto": "CONHEÇA NOSSA HISTÓRIA", "url": "https://www.google.com/"}],
        # Estatísticas (Stats)
        "t13_stats": [
            {"valor": "22", "label": "Fábricas no Brasil e Argentina"},
            {"valor": "125", "label": "Anos de Inovação"},
            {"valor": "719k", "label": "Hectares de Florestas"},
            {"valor": "25k", "label": "Colaboradores"},
        ],
        # Nossos Negócios (Business Cards)
        "t13_bus_secao_titulos": [{"valor": "Nossos Negócios"}],
        "t13_bus_items": [
            {"img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?auto=format&fit=crop&w=400&q=80", "titulo": "Papéis", "desc": "Papéis de alta qualidade para diversas aplicações industriais.", "url": "#"},
            {"img": "https://images.unsplash.com/photo-1530587191325-3db32d826c18?auto=format&fit=crop&w=400&q=80", "titulo": "Embalagens", "desc": "Soluções em papelão ondulado e sacos industriais sustentáveis.", "url": "#"},
            {"img": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=400&q=80", "titulo": "Florestal", "desc": "Manejo florestal certificado e produção de celulose.", "url": "#"},
        ],
        # Footer
        "t13_foot_logos": [{"valor": "ogreen"}],
        "t13_foot_descs": [{"valor": "Valor que se renova. © 2026 Ogreen Inc. Todos os direitos reservados."}],
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
            for i, cor in enumerate(st.session_state.t13_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t13_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t13_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t13_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_cores) > 1 and _del_btn(f"t13_cor_del_{i}"):
                        st.session_state.t13_cores.pop(i); st.rerun()
            if _add_btn("t13_cor_add", "＋ Adicionar cor"):
                st.session_state.t13_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)
            st.caption("Logo Principal")
            for i, logo in enumerate(st.session_state.t13_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t13_logos[i]["valor"] = st.text_input("Logo", logo["valor"], key=f"t13_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_logos) > 1 and _del_btn(f"t13_logo_del_{i}"):
                        st.session_state.t13_logos.pop(i); st.rerun()
            if _add_btn("t13_logo_add", "＋ Adicionar logo"):
                st.session_state.t13_logos.append({"valor": "ogreen"}); st.rerun()
            
            st.caption("Links do Menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t13_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t13_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t13_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t13_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_nav_links) > 1 and _del_btn(f"t13_nl_del_{i}"):
                        st.session_state.t13_nav_links.pop(i); st.rerun()
            if _add_btn("t13_nl_add", "＋ Adicionar link"):
                st.session_state.t13_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌲 Hero Banner (Indústria)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_hero_titulos):
                st.session_state.t13_hero_titulos[i]["valor"] = st.text_input("Título Hero", t["valor"], key=f"t13_h_t_{i}")
            for i, d in enumerate(st.session_state.t13_hero_descs):
                st.session_state.t13_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t13_h_d_{i}")
            for i, img in enumerate(st.session_state.t13_hero_imgs):
                st.session_state.t13_hero_imgs[i]["valor"] = st.text_input("URL Imagem Fundo", img["valor"], key=f"t13_h_i_{i}")

            # ══════════════════════════════════════════════════════════════════
            # SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Seção Sobre</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_about_titulos):
                st.session_state.t13_about_titulos[i]["valor"] = st.text_input("Título Sobre", t["valor"], key=f"t13_at_{i}")
            for i, d in enumerate(st.session_state.t13_about_descs):
                st.session_state.t13_about_descs[i]["valor"] = st.text_area("Descrição Sobre", d["valor"], key=f"t13_ad_{i}")
            for i, item in enumerate(st.session_state.t13_about_imgs):
                st.session_state.t13_about_imgs[i]["valor"] = st.text_input("URL Imagem Lateral", item["valor"], key=f"t13_ai_i_{i}")
                st.session_state.t13_about_imgs[i]["legenda"] = st.text_input("Legenda da Imagem", item["legenda"], key=f"t13_ai_l_{i}")
            for i, btn in enumerate(st.session_state.t13_about_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t13_about_btns[i]["texto"] = st.text_input("Texto Botão Sobre", btn["texto"], key=f"t13_ab_t_{i}")
                with c2: st.session_state.t13_about_btns[i]["url"] = st.text_input("URL Botão Sobre", btn["url"], key=f"t13_ab_u_{i}")

            # ══════════════════════════════════════════════════════════════════
            # ESTATÍSTICAS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números de Impacto</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t13_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t13_stats[i]["valor"] = st.text_input("Número", stat["valor"], key=f"t13_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_stats[i]["label"] = st.text_input("Descrição", stat["label"], key=f"t13_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_stats) > 1 and _del_btn(f"t13_st_del_{i}"):
                        st.session_state.t13_stats.pop(i); st.rerun()
            if _add_btn("t13_st_add", "＋ Adicionar estatística"):
                st.session_state.t13_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NEGÓCIOS (BUSINESS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 Nossos Negócios</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_bus_secao_titulos):
                st.session_state.t13_bus_secao_titulos[i]["valor"] = st.text_input("Título da Seção", t["valor"], key=f"t13_bst_{i}")
            
            for i, item in enumerate(st.session_state.t13_bus_items):
                with st.expander(f"Negócio {i+1}: {item['titulo']}"):
                    st.session_state.t13_bus_items[i]["titulo"] = st.text_input("Título do Card", item["titulo"], key=f"t13_bi_t_{i}")
                    st.session_state.t13_bus_items[i]["desc"] = st.text_area("Descrição do Card", item["desc"], key=f"t13_bi_d_{i}")
                    st.session_state.t13_bus_items[i]["img"] = st.text_input("URL Imagem Card", item["img"], key=f"t13_bi_i_{i}")
                    st.session_state.t13_bus_items[i]["url"] = st.text_input("URL do Botão", item["url"], key=f"t13_bi_u_{i}")
                    if len(st.session_state.t13_bus_items) > 1 and _del_btn(f"t13_bi_del_{i}", "Remover negócio"):
                        st.session_state.t13_bus_items.pop(i); st.rerun()
            if _add_btn("t13_bi_add", "＋ Adicionar negócio"):
                st.session_state.t13_bus_items.append({"img": "", "titulo": "NOVO NEGÓCIO", "desc": "...", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, logo in enumerate(st.session_state.t13_foot_logos):
                st.session_state.t13_foot_logos[i]["valor"] = st.text_input("Logo Footer", logo["valor"], key=f"t13_fl_{i}")
            for i, desc in enumerate(st.session_state.t13_foot_descs):
                st.session_state.t13_foot_descs[i]["valor"] = st.text_area("Copyright e Descrição", desc["valor"], key=f"t13_fd_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t13_obs_{i}", height=80,
                        placeholder="Ex: Mudar a cor verde para um tom mais escuro...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t13_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t13_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t13_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
