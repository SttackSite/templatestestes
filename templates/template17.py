import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img17.png"
TEMPLATE_NAME = "Template 17 — Breakfast Style (Brutalist Agency)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Breakfast
        "t17_cores": [
            {"nome": "Fundo (Branco)", "valor": "#ffffff"},
            {"nome": "Texto (Preto)", "valor": "#000000"},
            {"nome": "Bordas (Preto)", "valor": "#000000"},
            {"nome": "Texto Secundário (Cinza)", "valor": "#888888"},
        ],
        # Header / Navbar
        "t17_header_logos": [{"valor": "Breakfast."}],
        "t17_header_taglines": [{"valor": "Design & Technology"}],
        # Hero Section
        "t17_hero_titulos": [{"valor": "WE DESIGN<br>DIGITAL<br>EXPERIENCES"}],
        # Projetos (Project Grid)
        "t17_project_items": [
            {"img": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800", "nome": "Solar System", "client": "Editorial"},
            {"img": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "nome": "Neon Future", "client": "Web Design"},
            {"img": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "nome": "Cyber Identity", "client": "Branding"},
            {"img": "https://images.unsplash.com/photo-1509343256512-d77a5cb3791b?w=800", "nome": "Monochrome Studio", "client": "CGI"},
        ],
        # Filosofia Section
        "t17_filosofia_textos": [{"valor": "Independent studio for strategy, design and code. We turn complex ideas into simple, functional and beautiful digital products."}],
        # Serviços Section
        "t17_servico_items": [
            {"titulo": "STRATEGY", "desc": "Product Discovery / User Research / Brand Positioning"},
            {"titulo": "DESIGN", "desc": "UI/UX Design / Visual Identity / Motion Graphics"},
            {"titulo": "CODE", "desc": "React / Webflow / Headless CMS / E-commerce"},
        ],
        # CTA Section
        "t17_cta_titulos": [{"valor": "LET'S TALK?"}],
        "t17_cta_btns": [{"texto": "Start a Project", "url": "https://www.google.com/"}],
        # Footer
        "t17_foot_logos": [{"valor": "Breakfast."}],
        "t17_foot_infos": [{"valor": "Rua de Trás, Porto, Portugal"}],
        "t17_foot_emails": [{"texto": "hello@wearebreakfast.com", "url": "mailto:hello@wearebreakfast.com"}],
        "t17_foot_socials": [
            {"texto": "INSTAGRAM", "url": "https://www.google.com/"},
            {"texto": "LINKEDIN", "url": "https://www.google.com/"},
            {"texto": "TWITTER", "url": "https://www.google.com/"},
        ],
        "t17_foot_copys": [{"valor": "© 2026 ALL RIGHTS RESERVED"}],
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

    # CSS do Painel de Edição
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
        
        /* Estilos do Preview Brutalista (Simulação) */
        .preview-container {
            background: white; color: black; padding: 20px; border: 2px solid black; font-family: 'Inter', sans-serif;
        }
        .preview-hero-text {
            font-size: 32px; font-weight: 900; text-transform: uppercase; line-height: 0.9; margin: 20px 0; border-bottom: 2px solid black; padding-bottom: 10px;
        }
        .preview-filosofia {
            font-size: 18px; font-weight: 700; border-bottom: 2px solid black; padding: 20px 0;
        }
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
            for i, cor in enumerate(st.session_state.t17_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t17_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t17_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t17_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t17_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t17_cores) > 1 and _del_btn(f"t17_cor_del_{i}"):
                        st.session_state.t17_cores.pop(i); st.rerun()
            if _add_btn("t17_cor_add", "＋ Adicionar cor"):
                st.session_state.t17_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Header)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t17_header_logos):
                st.session_state.t17_header_logos[i]["valor"] = st.text_input("Logo da Agência", item["valor"], key=f"t17_hl_{i}")
            for i, item in enumerate(st.session_state.t17_header_taglines):
                st.session_state.t17_header_taglines[i]["valor"] = st.text_input("Tagline/Descrição", item["valor"], key=f"t17_ht_{i}")

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💥 Hero Section</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t17_hero_titulos):
                st.session_state.t17_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br> para quebrar linha)", t["valor"], key=f"t17_h_t_{i}")

            # ══════════════════════════════════════════════════════════════════
            # PROJETOS (PROJECT GRID)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t17_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t17_project_items[i]["nome"] = st.text_input("Nome do Projeto", item["nome"], key=f"t17_pi_n_{i}")
                    st.session_state.t17_project_items[i]["client"] = st.text_input("Tipo/Cliente", item["client"], key=f"t17_pi_c_{i}")
                    st.session_state.t17_project_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t17_pi_i_{i}")
                    if len(st.session_state.t17_project_items) > 1 and _del_btn(f"t17_pi_del_{i}", "Remover projeto"):
                        st.session_state.t17_project_items.pop(i); st.rerun()
            if _add_btn("t17_pi_add", "＋ Adicionar projeto"):
                st.session_state.t17_project_items.append({"img": "", "nome": "NOVO PROJETO", "client": "Editorial"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FILOSOFIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Filosofia da Agência</div>', unsafe_allow_html=True)
            for i, text in enumerate(st.session_state.t17_filosofia_textos):
                st.session_state.t17_filosofia_textos[i]["valor"] = st.text_area("Texto de Filosofia", text["valor"], key=f"t17_ft_{i}", height=120)

            # ══════════════════════════════════════════════════════════════════
            # SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Nossos Serviços</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t17_servico_items):
                with st.expander(f"Serviço {i+1}: {item['titulo']}"):
                    st.session_state.t17_servico_items[i]["titulo"] = st.text_input("Título do Serviço", item["titulo"], key=f"t17_si_t_{i}")
                    st.session_state.t17_servico_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t17_si_d_{i}")
                    if len(st.session_state.t17_servico_items) > 1 and _del_btn(f"t17_si_del_{i}", "Remover serviço"):
                        st.session_state.t17_servico_items.pop(i); st.rerun()
            if _add_btn("t17_si_add", "＋ Adicionar serviço"):
                st.session_state.t17_servico_items.append({"titulo": "NOVO", "desc": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📞 Chamada para Ação (CTA)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t17_cta_titulos):
                st.session_state.t17_cta_titulos[i]["valor"] = st.text_input("Título CTA", t["valor"], key=f"t17_ct_t_{i}")
            for i, btn in enumerate(st.session_state.t17_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t17_cta_btns[i]["texto"] = st.text_input("Texto Botão", btn["texto"], key=f"t17_cb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t17_cta_btns[i]["url"] = st.text_input("URL Botão", btn["url"], key=f"t17_cb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t17_cta_btns) > 1 and _del_btn(f"t17_cb_del_{i}"):
                        st.session_state.t17_cta_btns.pop(i); st.rerun()
            if _add_btn("t17_cb_add", "＋ Adicionar botão"):
                st.session_state.t17_cta_btns.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Brutalista</div>', unsafe_allow_html=True)
            for i, logo in enumerate(st.session_state.t17_foot_logos):
                st.session_state.t17_foot_logos[i]["valor"] = st.text_input("Logo Footer", logo["valor"], key=f"t17_fl_{i}")
            for i, info in enumerate(st.session_state.t17_foot_infos):
                st.session_state.t17_foot_infos[i]["valor"] = st.text_input("Endereço/Info", info["valor"], key=f"t17_fi_{i}")
            for i, email in enumerate(st.session_state.t17_foot_emails):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t17_foot_emails[i]["texto"] = st.text_input("Texto Email", email["texto"], key=f"t17_fe_t_{i}")
                with c2: st.session_state.t17_foot_emails[i]["url"] = st.text_input("URL Email", email["url"], key=f"t17_fe_u_{i}")
            
            st.caption("Redes Sociais")
            for i, social in enumerate(st.session_state.t17_foot_socials):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t17_foot_socials[i]["texto"] = st.text_input("Nome", social["texto"], key=f"t17_fs_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t17_foot_socials[i]["url"] = st.text_input("URL", social["url"], key=f"t17_fs_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t17_foot_socials) > 1 and _del_btn(f"t17_fs_del_{i}"):
                        st.session_state.t17_foot_socials.pop(i); st.rerun()
            if _add_btn("t17_fs_add", "＋ Adicionar rede social"):
                st.session_state.t17_foot_socials.append({"texto": "SOCIAL", "url": "#"}); st.rerun()

            for i, copy in enumerate(st.session_state.t17_foot_copys):
                st.session_state.t17_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t17_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t17_obs_{i}", height=80,
                        placeholder="Ex: Mudar a fonte para uma mais brutalista...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t17_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t17_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t17_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        # Exibição do Preview Dinâmico (Hero e Filosofia corrigidos)
        st.markdown('<div class="preview-container">', unsafe_allow_html=True)
        
        # Simulação do Hero dinâmico
        hero_html = "".join([f'<div class="preview-hero-text">{t["valor"]}</div>' for t in st.session_state.t17_hero_titulos])
        st.markdown(hero_html, unsafe_allow_html=True)
        
        # Simulação da Filosofia dinâmica
        filo_html = "".join([f'<div class="preview-filosofia">{f["valor"]}</div>' for f in st.session_state.t17_filosofia_textos])
        st.markdown(filo_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🍳",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
