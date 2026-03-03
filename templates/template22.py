import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img22.png"
TEMPLATE_NAME = "Template 22 — Zajno Motion Style (Digital Design Studio)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Zajno
        "t22_cores": [
            {"nome": "Fundo (Preto)", "valor": "#0b0b0b"},
            {"nome": "Texto Principal (Branco)", "valor": "#ffffff"},
            {"nome": "Bordas e Linhas", "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)", "valor": "#888888"},
        ],
        # Navbar
        "t22_nav_logos": [{"valor": "Zajno / Motion"}],
        "t22_nav_links": [
            {"texto": "Trabalhos", "url": "#trabalhos"},
            {"texto": "Estúdio", "url": "#estudio"},
            {"texto": "Contato", "url": "#contato"},
        ],
        # Hero Section
        "t22_hero_titulos": [{"valor": "MOVIMENTO<br>É A NOSSA<br>LINGUAGEM"}],
        "t22_hero_descs": [{"valor": "Somos um estúdio de design focado em criar experiências digitais que ganham vida através do movimento e da tecnologia de ponta."}],
        # Showcase de Projetos
        "t22_project_items": [
            {"img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800", "category": "Motion Graphics / 2024", "nome": "Cyber Identity"},
            {"img": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=800", "category": "Interface Design / 2023", "nome": "Liquid UI"},
            {"img": "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=800", "category": "Art Direction / 2024", "nome": "Astro Forms"},
            {"img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800", "category": "3D Animation / 2024", "nome": "Glass Echo"},
        ],
        # Manifesto
        "t22_manifest_titulos": [{"valor": "Nós não apenas movemos pixels. Nós contamos histórias que definem o futuro das marcas."}],
        "t22_manifest_descs": [{"valor": "Trabalhamos com marcas audaciosas para transformar ideias complexas em interações digitais simples, memoráveis e impactantes."}],
        # Footer (CTA)
        "t22_foot_labels": [{"valor": "Pronto para elevar sua marca?"}],
        "t22_foot_titulos": [{"valor": "VAMOS<br>CRIAR JUNTOS"}],
        "t22_foot_emails": [{"valor": "studio@zajno.com"}],
        "t22_foot_btns": [{"texto": "Iniciar Projeto", "url": "https://www.google.com/"}],
        "t22_foot_copys": [{"valor": "© 2026 Zajno Studio — São Francisco / Remoto"}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
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
            for i, cor in enumerate(st.session_state.t22_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t22_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t22_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t22_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t22_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t22_cores) > 1 and _del_btn(f"t22_cor_del_{i}"):
                        st.session_state.t22_cores.pop(i); st.rerun()
            if _add_btn("t22_cor_add", "＋ Adicionar cor"):
                st.session_state.t22_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t22_nav_logos):
                st.session_state.t22_nav_logos[i]["valor"] = st.text_input("Logo/Nome Estúdio", item["valor"], key=f"t22_nl_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t22_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t22_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t22_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t22_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t22_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t22_nav_links) > 1 and _del_btn(f"t22_nl_del_{i}"):
                        st.session_state.t22_nav_links.pop(i); st.rerun()
            if _add_btn("t22_nl_add", "＋ Adicionar link"):
                st.session_state.t22_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎬 Hero Section</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t22_hero_titulos):
                st.session_state.t22_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br>)", t["valor"], key=f"t22_h_t_{i}")
            for i, d in enumerate(st.session_state.t22_hero_descs):
                st.session_state.t22_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t22_h_d_{i}")

            # ══════════════════════════════════════════════════════════════════
            # SHOWCASE DE PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Showcase de Projetos</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t22_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t22_project_items[i]["nome"] = st.text_input("Título", item["nome"], key=f"t22_pi_n_{i}")
                    st.session_state.t22_project_items[i]["category"] = st.text_input("Categoria / Ano", item["category"], key=f"t22_pi_c_{i}")
                    st.session_state.t22_project_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t22_pi_i_{i}")
                    if len(st.session_state.t22_project_items) > 1 and _del_btn(f"t22_pi_del_{i}", "Remover projeto"):
                        st.session_state.t22_project_items.pop(i); st.rerun()
            if _add_btn("t22_pi_add", "＋ Adicionar projeto"):
                st.session_state.t22_project_items.append({"img": "", "category": "MOTION / 2026", "nome": "NOVO PROJETO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # MANIFESTO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Manifesto do Estúdio</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t22_manifest_titulos):
                st.session_state.t22_manifest_titulos[i]["valor"] = st.text_area("Título Manifesto", t["valor"], key=f"t22_mt_{i}")
            for i, d in enumerate(st.session_state.t22_manifest_descs):
                st.session_state.t22_manifest_descs[i]["valor"] = st.text_area("Descrição Manifesto", d["valor"], key=f"t22_md_{i}")

            # ══════════════════════════════════════════════════════════════════
            # FOOTER (CTA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✉️ Rodapé (Contato)</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t22_foot_labels):
                st.session_state.t22_foot_labels[i]["valor"] = st.text_input("Label CTA", l["valor"], key=f"t22_fl_{i}")
            for i, t in enumerate(st.session_state.t22_foot_titulos):
                st.session_state.t22_foot_titulos[i]["valor"] = st.text_area("Título CTA (use <br>)", t["valor"], key=f"t22_ft_{i}")
            for i, e in enumerate(st.session_state.t22_foot_emails):
                st.session_state.t22_foot_emails[i]["valor"] = st.text_input("Email de Contato", e["valor"], key=f"t22_fe_{i}")
            
            st.caption("Botões de Ação")
            for i, btn in enumerate(st.session_state.t22_foot_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t22_foot_btns[i]["texto"] = st.text_input("Texto Botão", btn["texto"], key=f"t22_fb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t22_foot_btns[i]["url"] = st.text_input("URL Botão", btn["url"], key=f"t22_fb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t22_foot_btns) > 1 and _del_btn(f"t22_fb_del_{i}"):
                        st.session_state.t22_foot_btns.pop(i); st.rerun()
            if _add_btn("t22_fb_add", "＋ Adicionar botão"):
                st.session_state.t22_foot_btns.append({"texto": "CONTATO", "url": "#"}); st.rerun()

            for i, copy in enumerate(st.session_state.t22_foot_copys):
                st.session_state.t22_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t22_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t22_obs_{i}", height=80,
                        placeholder="Ex: Tornar o layout mais cinematográfico...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t22_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t22_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t22_send", type="primary"):
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
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
