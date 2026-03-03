import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img28.png"
TEMPLATE_NAME = "Template 28 — HGQ Coaching Style (Business & Leadership)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores HGQ
        "t28_cores": [
            {"nome": "Azul HGQ (Principal)", "valor": "#003366"},
            {"nome": "Amarelo Accent", "valor": "#ffcc00"},
            {"nome": "Texto Principal", "valor": "#333333"},
            {"nome": "Cinza de Fundo", "valor": "#f2f2f2"},
        ],
        # Navbar
        "t28_nav_logos": [{"valor": "HGQ<span style='color:#ffcc00'>.</span>"}],
        "t28_nav_links": [
            {"texto": "TREINAMENTOS", "url": "#programas"},
            {"texto": "FORMAÇÕES", "url": "#programas"},
            {"texto": "SOBRE", "url": "#depoimentos"},
        ],
        # Hero Section
        "t28_hero_subtitulos": [{"valor": "VOCÊ NASCEU PARA ALGO MAIOR"}],
        "t28_hero_titulos": [{"valor": "TRANSFORME A SUA PAIXÃO POR AJUDAR PESSOAS EM UMA PROFISSÃO LUCRATIVA."}],
        "t28_hero_descs": [{"valor": "Participe da maior comunidade de coaches e líderes que estão mudando o Brasil."}],
        "t28_hero_btns": [{"texto": "QUERO COMEÇAR AGORA", "url": "#programas"}],
        "t28_hero_imgs": [{"valor": "https://images.unsplash.com/photo-1475721027785-f74dea327912?w=1600"}],
        # Programas (Cards)
        "t28_prog_titulos": [{"valor": "NOSSAS SOLUÇÕES"}],
        "t28_prog_items": [
            {"title": "FORMAÇÃO EM COACHING", "subtitle": "O Começo de Tudo", "desc": "O treinamento número #1 para quem deseja dominar as ferramentas e começar a atender.", "btn_texto": "VER DETALHES", "btn_url": "https://www.google.com/"},
            {"title": "MENTORIA IMPACTO", "subtitle": "Alta Performance", "desc": "Para profissionais que já faturam e querem escalar o seu negócio e impacto.", "btn_texto": "VER DETALHES", "btn_url": "https://www.google.com/"},
            {"title": "LIDERANÇA PRO", "subtitle": "Gestão de Equipas", "desc": "Desenvolva a mentalidade de um líder que inspira e gera resultados fora da curva.", "btn_texto": "VER DETALHES", "btn_url": "https://www.google.com/"},
        ],
        # Números (Impacto)
        "t28_stat_items": [
            {"valor": "+100k", "label": "Alunos Formados"},
            {"valor": "+15", "label": "Anos de Experiência"},
            {"valor": "4.9/5", "label": "Avaliação Média"},
        ],
        # Depoimentos
        "t28_depo_titulos": [{"valor": "O QUE DIZEM NOSSOS ALUNOS"}],
        "t28_depo_items": [
            {"texto": "\"Minha vida mudou completamente após o treinamento. Hoje tenho clareza de propósito e faturo 3x mais.\"", "autor": "Maria Oliveira"},
            {"texto": "\"O melhor investimento que fiz na minha carreira. As ferramentas são práticas e os resultados imediatos.\"", "autor": "João Pedro"},
        ],
        # Footer
        "t28_foot_titulos": [{"valor": "HGQ - INSTITUTO GERÔNIMO THEML"}],
        "t28_foot_links": [
            {"texto": "Termos de Uso", "url": "https://www.google.com/"},
            {"texto": "Políticas de Privacidade", "url": "https://www.google.com/"},
        ],
        "t28_foot_copys": [{"valor": "© 2026 Todos os direitos reservados."}],
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
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t28_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t28_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t28_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t28_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t28_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_cores) > 1 and _del_btn(f"t28_cor_del_{i}"):
                        st.session_state.t28_cores.pop(i); st.rerun()
            if _add_btn("t28_cor_add", "＋ Adicionar cor"):
                st.session_state.t28_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t28_nav_logos):
                st.session_state.t28_nav_logos[i]["valor"] = st.text_input("Logo/Nome Marca (HTML)", item["valor"], key=f"t28_nl_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t28_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t28_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t28_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t28_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t28_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_nav_links) > 1 and _del_btn(f"t28_nl_del_{i}"):
                        st.session_state.t28_nav_links.pop(i); st.rerun()
            if _add_btn("t28_nl_add", "＋ Adicionar link"):
                st.session_state.t28_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚡ Hero Section</div>', unsafe_allow_html=True)
            for i, img in enumerate(st.session_state.t28_hero_imgs):
                st.session_state.t28_hero_imgs[i]["valor"] = st.text_input("URL Imagem de Fundo", img["valor"], key=f"t28_h_img_{i}")
            for i, s in enumerate(st.session_state.t28_hero_subtitulos):
                st.session_state.t28_hero_subtitulos[i]["valor"] = st.text_input("Subtítulo Hero", s["valor"], key=f"t28_h_s_{i}")
            for i, t in enumerate(st.session_state.t28_hero_titulos):
                st.session_state.t28_hero_titulos[i]["valor"] = st.text_area("Título Hero", t["valor"], key=f"t28_h_t_{i}")
            for i, d in enumerate(st.session_state.t28_hero_descs):
                st.session_state.t28_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t28_h_d_{i}")
            
            st.caption("Botões Hero")
            for i, btn in enumerate(st.session_state.t28_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t28_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t28_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t28_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t28_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_hero_btns) > 1 and _del_btn(f"t28_hb_del_{i}"):
                        st.session_state.t28_hero_btns.pop(i); st.rerun()
            if _add_btn("t28_hb_add", "＋ Adicionar botão"):
                st.session_state.t28_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROGRAMAS (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📚 Nossas Soluções (Cards)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t28_prog_titulos):
                st.session_state.t28_prog_titulos[i]["valor"] = st.text_input("Título Seção", t["valor"], key=f"t28_pt_{i}")
            
            for i, item in enumerate(st.session_state.t28_prog_items):
                with st.expander(f"Programa {i+1}: {item['title']}"):
                    st.session_state.t28_prog_items[i]["title"] = st.text_input("Título", item["title"], key=f"t28_pi_t_{i}")
                    st.session_state.t28_prog_items[i]["subtitle"] = st.text_input("Subtítulo", item["subtitle"], key=f"t28_pi_s_{i}")
                    st.session_state.t28_prog_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t28_pi_d_{i}")
                    st.session_state.t28_prog_items[i]["btn_texto"] = st.text_input("Texto Botão", item["btn_texto"], key=f"t28_pi_bt_{i}")
                    st.session_state.t28_prog_items[i]["btn_url"] = st.text_input("URL Botão", item["btn_url"], key=f"t28_pi_bu_{i}")
                    if len(st.session_state.t28_prog_items) > 1 and _del_btn(f"t28_pi_del_{i}", "Remover item"):
                        st.session_state.t28_prog_items.pop(i); st.rerun()
            if _add_btn("t28_pi_add", "＋ Adicionar solução"):
                st.session_state.t28_prog_items.append({"title": "NOVO", "subtitle": "SUB", "desc": "DESC", "btn_texto": "VER", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NÚMEROS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números de Impacto</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t28_stat_items):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t28_stat_items[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t28_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t28_stat_items[i]["label"] = st.text_input("Rótulo", stat["label"], key=f"t28_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_stat_items) > 1 and _del_btn(f"t28_st_del_{i}"):
                        st.session_state.t28_stat_items.pop(i); st.rerun()
            if _add_btn("t28_st_add", "＋ Adicionar número"):
                st.session_state.t28_stat_items.append({"valor": "0", "label": "LABEL"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t28_depo_titulos):
                st.session_state.t28_depo_titulos[i]["valor"] = st.text_input("Título Seção Depo", t["valor"], key=f"t28_dt_{i}")
            
            for i, item in enumerate(st.session_state.t28_depo_items):
                with st.expander(f"Depoimento {i+1}: {item['autor']}"):
                    st.session_state.t28_depo_items[i]["texto"] = st.text_area("Texto", item["texto"], key=f"t28_di_t_{i}")
                    st.session_state.t28_depo_items[i]["autor"] = st.text_input("Autor", item["autor"], key=f"t28_di_a_{i}")
                    if len(st.session_state.t28_depo_items) > 1 and _del_btn(f"t28_di_del_{i}", "Remover depoimento"):
                        st.session_state.t28_depo_items.pop(i); st.rerun()
            if _add_btn("t28_di_add", "＋ Adicionar depoimento"):
                st.session_state.t28_depo_items.append({"texto": "MUDOU MINHA VIDA!", "autor": "NOME"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t28_foot_titulos):
                st.session_state.t28_foot_titulos[i]["valor"] = st.text_input("Título (Footer)", t["valor"], key=f"t28_ftt_{i}")
            
            st.caption("Links do Rodapé")
            for i, link in enumerate(st.session_state.t28_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t28_foot_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t28_footl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t28_foot_links[i]["url"] = st.text_input("URL", link["url"], key=f"t28_footl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_foot_links) > 1 and _del_btn(f"t28_footl_del_{i}"):
                        st.session_state.t28_foot_links.pop(i); st.rerun()
            if _add_btn("t28_footl_add", "＋ Adicionar link"):
                st.session_state.t28_foot_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            for i, copy in enumerate(st.session_state.t28_foot_copys):
                st.session_state.t28_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t28_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t28_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t28_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t28_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t28_send", type="primary"):
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
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
