import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img15.png"
TEMPLATE_NAME = "Template 15 — Hugo Bazin Style (Minimalist Portfolio)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Hugo Bazin
        "t15_cores": [
            {"nome": "Fundo (Cinza Claro)", "valor": "#f6f6f6"},
            {"nome": "Texto (Preto)", "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)", "valor": "#666666"},
            {"nome": "Bordas (Cinza Médio)", "valor": "#dddddd"},
        ],
        # Header / Navbar
        "t15_header_nome": [{"valor": "Hugo Bazin — Digital Designer"}],
        "t15_header_info": [{"valor": "Paris, FR — 14:52 PM"}],
        # Hero Section
        "t15_hero_titulos": [{"valor": "CREATING DIGITAL<br>EXPERIENCES"}],
        "t15_hero_subtitulos": [{"valor": "Independent Designer & Art Director"}],
        # Projetos (Project Cards)
        "t15_project_items": [
            {"img": "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=1500&q=80", "titulo": "L'Art de Vivre", "ano": "2024", "cat": "Visual Identity"},
            {"img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1500&q=80", "titulo": "Techno Frontier", "ano": "2023", "cat": "Product Design"},
            {"img": "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=1500&q=80", "titulo": "Minimal Workspace", "ano": "2023", "cat": "CGI & Motion"},
            {"img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1500&q=80", "titulo": "Essential Watch", "ano": "2022", "cat": "E-commerce"},
        ],
        # About Section
        "t15_about_textos": [{"valor": "Eu ajudo marcas a traduzirem sua essência em produtos digitais que as pessoas amam usar. Focado em simplicidade, estética e performance."}],
        # Contato / Links
        "t15_contact_btns": [
            {"texto": "EMAIL ME", "url": "mailto:hello@hugobazin.com"},
            {"texto": "LINKEDIN", "url": "https://www.google.com/"},
            {"texto": "DRIBBBLE", "url": "https://www.google.com/"},
        ],
        # Footer
        "t15_foot_copys": [{"valor": "© 2026 Hugo Bazin"}],
        "t15_foot_descs": [{"valor": "Design & Development"}],
        "t15_foot_tops": [{"texto": "Back to Top ↑", "url": "#"}],
        # Observações
        "t13_obs": [{"valor": ""}], # Mantendo a chave para consistência entre templates
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
            for i, cor in enumerate(st.session_state.t15_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t15_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t15_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t15_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t15_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t15_cores) > 1 and _del_btn(f"t15_cor_del_{i}"):
                        st.session_state.t15_cores.pop(i); st.rerun()
            if _add_btn("t15_cor_add", "＋ Adicionar cor"):
                st.session_state.t15_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Minimal)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t15_header_nome):
                st.session_state.t15_header_nome[i]["valor"] = st.text_input("Nome e Profissão", item["valor"], key=f"t15_hn_{i}")
            for i, item in enumerate(st.session_state.t15_header_info):
                st.session_state.t15_header_info[i]["valor"] = st.text_input("Localização e Hora", item["valor"], key=f"t15_hi_{i}")

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🕶️ Hero Section</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t15_hero_titulos):
                st.session_state.t15_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br> para quebrar linha)", t["valor"], key=f"t15_h_t_{i}")
            for i, s in enumerate(st.session_state.t15_hero_subtitulos):
                st.session_state.t15_hero_subtitulos[i]["valor"] = st.text_input("Subtítulo Hero", s["valor"], key=f"t15_h_s_{i}")

            # ══════════════════════════════════════════════════════════════════
            # PROJETOS (PROJECTS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t15_project_items):
                with st.expander(f"Projeto {i+1}: {item['titulo']}"):
                    st.session_state.t15_project_items[i]["titulo"] = st.text_input("Título do Projeto", item["titulo"], key=f"t15_pi_t_{i}")
                    st.session_state.t15_project_items[i]["cat"] = st.text_input("Categoria", item["cat"], key=f"t15_pi_c_{i}")
                    st.session_state.t15_project_items[i]["ano"] = st.text_input("Ano", item["ano"], key=f"t15_pi_a_{i}")
                    st.session_state.t15_project_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t15_pi_i_{i}")
                    if len(st.session_state.t15_project_items) > 1 and _del_btn(f"t15_pi_del_{i}", "Remover projeto"):
                        st.session_state.t15_project_items.pop(i); st.rerun()
            if _add_btn("t15_pi_add", "＋ Adicionar projeto"):
                st.session_state.t15_project_items.append({"img": "", "titulo": "NOVO PROJETO", "ano": "2026", "cat": "Visual Identity"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ABOUT
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Sobre / Filosofia</div>', unsafe_allow_html=True)
            for i, text in enumerate(st.session_state.t15_about_textos):
                st.session_state.t15_about_textos[i]["valor"] = st.text_area("Texto Sobre", text["valor"], key=f"t15_at_{i}", height=120)

            # ══════════════════════════════════════════════════════════════════
            # CONTATO (CONTACT)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✉️ Links de Contato</div>', unsafe_allow_html=True)
            for i, btn in enumerate(st.session_state.t15_contact_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t15_contact_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t15_cb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t15_contact_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t15_cb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t15_contact_btns) > 1 and _del_btn(f"t15_cb_del_{i}"):
                        st.session_state.t15_contact_btns.pop(i); st.rerun()
            if _add_btn("t15_cb_add", "＋ Adicionar link"):
                st.session_state.t15_contact_btns.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, copy in enumerate(st.session_state.t15_foot_copys):
                st.session_state.t15_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t15_fcp_{i}")
            for i, desc in enumerate(st.session_state.t15_foot_descs):
                st.session_state.t15_foot_descs[i]["valor"] = st.text_input("Descrição", desc["valor"], key=f"t15_fd_{i}")
            for i, top in enumerate(st.session_state.t15_foot_tops):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t15_foot_tops[i]["texto"] = st.text_input("Texto Top", top["texto"], key=f"t15_ft_t_{i}")
                with c2: st.session_state.t15_foot_tops[i]["url"] = st.text_input("URL Top", top["url"], key=f"t15_ft_u_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t15_obs_{i}", height=80,
                        placeholder="Ex: Mudar a fonte principal para uma mais clássica...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t15_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t15_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t15_send", type="primary"):
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
        page_icon="🕶️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
