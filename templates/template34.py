import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img34.png"
TEMPLATE_NAME = "Template 34 — Frequency Style (Breathwork Experience)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Frequency
        "t34_cores": [
            {"nome": "Fundo (fq-bg)", "valor": "#050505"},
            {"nome": "Acento (fq-accent)", "valor": "#b5ff00"},
            {"nome": "Roxo (fq-purple)", "valor": "#4a148c"},
            {"nome": "Texto (fq-text)", "valor": "#ffffff"},
        ],
        # Navbar
        "t34_nav_logos": [{"texto": "FREQUENCY"}],
        "t34_nav_links": [
            {"texto": "A Jornada", "url": "#beneficios"},
            {"texto": "Estúdios", "url": "#aulas"},
            {"texto": "Digital", "url": "#aulas"},
        ],
        "t34_nav_ctas": [{"texto": "Membro", "url": "https://www.google.com/"}],
        # Hero Section
        "t34_hero_labels": [{"valor": "Sinta sua própria energia"}],
        "t34_hero_titulos": [{"valor": "Mude sua respiração.<br>Mude sua <span style='opacity: 0.6'>consciência.</span>"}],
        "t34_hero_btns": [{"texto": "COMECE SUA VIAGEM", "url": "#beneficios"}],
        # Mídia Placeholder
        "t34_media_imgs": [{"url": "https://images.unsplash.com/photo-1511216335778-7cb8f49fa7a3?w=1600", "texto": "O poder de se reconectar."}],
        # Benefícios (Cards)
        "t34_ben_headers": [{"valor": "Por que Frequency?"}],
        "t34_ben_items": [
            {
                "titulo": "Clareza Mental",
                "desc": "Remova o ruído cotidiano e acesse estados profundos de foco através de técnicas rítmicas de respiração.",
                "btn_texto": "SAIBA MAIS",
                "btn_url": "https://www.google.com/"
            },
            {
                "titulo": "Liberação Emocional",
                "desc": "Acesse e processe emoções estocadas no corpo de forma segura e guiada por especialistas.",
                "btn_texto": "SAIBA MAIS",
                "btn_url": "https://www.google.com/"
            },
            {
                "titulo": "Conexão Vital",
                "desc": "Sinta o fluxo de energia vital percorrendo seu sistema, revitalizando cada célula do seu ser.",
                "btn_texto": "SAIBA MAIS",
                "btn_url": "https://www.google.com/"
            }
        ],
        # Aulas / Agenda
        "t34_aulas_labels": [{"valor": "Aulas Ao Vivo"}],
        "t34_aulas_titulos": [{"valor": "Encontre seu ritmo."}],
        "t34_aulas_btns": [{"texto": "VER AGENDA COMPLETA", "url": "https://www.google.com/"}],
        "t34_aulas_items": [
            {"nome": "Breathwork Fundamental", "horario": "Segundas | 19:00", "url": "https://www.google.com/"},
            {"nome": "Jornada de Expansão", "horario": "Quartas | 20:30", "url": "https://www.google.com/"},
            {"nome": "Detox Dopaminérgico", "horario": "Sábados | 10:00", "url": "https://www.google.com/"},
        ],
        # Footer
        "t34_foot_logos": [{"texto": "FREQUENCY"}],
        "t34_foot_links": [
            {"texto": "Instagram", "url": "https://www.google.com/"},
            {"texto": "Spotify", "url": "https://www.google.com/"},
            {"texto": "Política de Privacidade", "url": "https://www.google.com/"},
            {"texto": "Contato", "url": "mailto:contato@frequency.com"},
        ],
        "t34_foot_copys": [{"valor": "© 2026 FREQUENCY BREATHWORK. TODOS OS DIREITOS RESERVADOS. <br> SINTA A FREQUÊNCIA."}],
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
            for i, cor in enumerate(st.session_state.t34_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t34_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t34_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t34_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t34_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t34_cores) > 1 and _del_btn(f"t34_cor_del_{i}"):
                        st.session_state.t34_cores.pop(i); st.rerun()
            if _add_btn("t34_cor_add", "＋ Adicionar cor"):
                st.session_state.t34_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t34_nav_logos):
                st.session_state.t34_nav_logos[i]["texto"] = st.text_input("Logo Marca", item["texto"], key=f"t34_nav_l_t_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t34_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t34_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t34_navl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t34_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t34_navl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t34_nav_links) > 1 and _del_btn(f"t34_navl_del_{i}"):
                        st.session_state.t34_nav_links.pop(i); st.rerun()
            if _add_btn("t34_navl_add", "＋ Adicionar link"):
                st.session_state.t34_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Botão Destaque (CTA)")
            for i, cta in enumerate(st.session_state.t34_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t34_nav_ctas[i]["texto"] = st.text_input("Texto", cta["texto"], key=f"t34_ncta_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t34_nav_ctas[i]["url"] = st.text_input("URL", cta["url"], key=f"t34_ncta_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t34_nav_ctas) > 1 and _del_btn(f"t34_ncta_del_{i}"):
                        st.session_state.t34_nav_ctas.pop(i); st.rerun()
            if _add_btn("t34_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t34_nav_ctas.append({"texto": "CTA", "url": "#"}); st.rerun()

            # 🧘 HERO SECTION
            st.markdown('<div class="section-label">🧘 Hero Section</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t34_hero_labels):
                st.session_state.t34_hero_labels[i]["valor"] = st.text_input("Label Hero", l["valor"], key=f"t34_h_l_{i}")
            for i, t in enumerate(st.session_state.t34_hero_titulos):
                st.session_state.t34_hero_titulos[i]["valor"] = st.text_area("Título Hero (HTML)", t["valor"], key=f"t34_h_t_{i}")
            for i, btn in enumerate(st.session_state.t34_hero_btns):
                c1, c2 = st.columns(2)
                with c1: st.session_state.t34_hero_btns[i]["texto"] = st.text_input("Texto Botão Hero", btn["texto"], key=f"t34_hb_t_{i}")
                with c2: st.session_state.t34_hero_btns[i]["url"] = st.text_input("URL Botão Hero", btn["url"], key=f"t34_hb_u_{i}")

            # 🎬 MÍDIA / VÍDEO
            st.markdown('<div class="section-label">🎬 Seção de Mídia</div>', unsafe_allow_html=True)
            for i, m in enumerate(st.session_state.t34_media_imgs):
                st.session_state.t34_media_imgs[i]["url"] = st.text_input("URL Imagem/Fundo", m["url"], key=f"t34_mi_u_{i}")
                st.session_state.t34_media_imgs[i]["texto"] = st.text_input("Texto Overlay", m["texto"], key=f"t34_mi_t_{i}")

            # ✨ BENEFÍCIOS
            st.markdown('<div class="section-label">✨ Benefícios (Cards)</div>', unsafe_allow_html=True)
            for i, bh in enumerate(st.session_state.t34_ben_headers):
                st.session_state.t34_ben_headers[i]["valor"] = st.text_input("Título Seção Benefícios", bh["valor"], key=f"t34_b_h_{i}")
            
            for i, item in enumerate(st.session_state.t34_ben_items):
                with st.expander(f"Benefício {i+1}: {item['titulo']}"):
                    st.session_state.t34_ben_items[i]["titulo"] = st.text_input("Título", item["titulo"], key=f"t34_bi_t_{i}")
                    st.session_state.t34_ben_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t34_bi_d_{i}")
                    st.session_state.t34_ben_items[i]["btn_texto"] = st.text_input("Texto Botão", item["btn_texto"], key=f"t34_bi_bt_{i}")
                    st.session_state.t34_ben_items[i]["btn_url"] = st.text_input("URL Botão", item["btn_url"], key=f"t34_bi_bu_{i}")
                    if len(st.session_state.t34_ben_items) > 1 and _del_btn(f"t34_bi_del_{i}", "Remover card"):
                        st.session_state.t34_ben_items.pop(i); st.rerun()
            if _add_btn("t34_bi_add", "＋ Adicionar benefício"):
                st.session_state.t34_ben_items.append({"titulo": "NOVO", "desc": "DESC", "btn_texto": "SAIBA MAIS", "btn_url": "#"}); st.rerun()

            # 📅 AULAS / AGENDA
            st.markdown('<div class="section-label">📅 Agenda de Aulas</div>', unsafe_allow_html=True)
            for i, al in enumerate(st.session_state.t34_aulas_labels):
                st.session_state.t34_aulas_labels[i]["valor"] = st.text_input("Label Agenda", al["valor"], key=f"t34_a_l_{i}")
            for i, at in enumerate(st.session_state.t34_aulas_titulos):
                st.session_state.t34_aulas_titulos[i]["valor"] = st.text_input("Título Agenda", at["valor"], key=f"t34_a_t_{i}")
            for i, abtn in enumerate(st.session_state.t34_aulas_btns):
                c1, c2 = st.columns(2)
                with c1: st.session_state.t34_aulas_btns[i]["texto"] = st.text_input("Texto Botão Agenda", abtn["texto"], key=f"t34_ab_t_{i}")
                with c2: st.session_state.t34_aulas_btns[i]["url"] = st.text_input("URL Botão Agenda", abtn["url"], key=f"t34_ab_u_{i}")
            
            st.caption("Itens da Agenda")
            for i, item in enumerate(st.session_state.t34_aulas_items):
                c1, c2, c3, c4 = st.columns([4, 4, 3, 1])
                with c1: st.session_state.t34_aulas_items[i]["nome"] = st.text_input("Nome Aula", item["nome"], key=f"t34_ai_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t34_aulas_items[i]["horario"] = st.text_input("Horário", item["horario"], key=f"t34_ai_h_{i}", label_visibility="collapsed")
                with c3: st.session_state.t34_aulas_items[i]["url"] = st.text_input("URL", item["url"], key=f"t34_ai_u_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t34_aulas_items) > 1 and _del_btn(f"t34_ai_del_{i}"):
                        st.session_state.t34_aulas_items.pop(i); st.rerun()
            if _add_btn("t34_ai_add", "＋ Adicionar aula"):
                st.session_state.t34_aulas_items.append({"nome": "NOVA AULA", "horario": "Dia | Hora", "url": "#"}); st.rerun()

            # 👣 FOOTER
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, fl in enumerate(st.session_state.t34_foot_logos):
                st.session_state.t34_foot_logos[i]["texto"] = st.text_input("Logo Footer", fl["texto"], key=f"t34_f_l_{i}")
            
            st.caption("Links do Rodapé")
            for i, flink in enumerate(st.session_state.t34_foot_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t34_foot_links[i]["texto"] = st.text_input("Texto", flink["texto"], key=f"t34_fl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t34_foot_links[i]["url"] = st.text_input("URL/Email", flink["url"], key=f"t34_fl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t34_foot_links) > 1 and _del_btn(f"t34_fl_del_{i}"):
                        st.session_state.t34_foot_links.pop(i); st.rerun()
            if _add_btn("t34_fl_add", "＋ Adicionar link social/legal"):
                st.session_state.t34_foot_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            for i, fcp in enumerate(st.session_state.t34_foot_copys):
                st.session_state.t34_foot_copys[i]["valor"] = st.text_area("Copyright", fcp["valor"], key=f"t34_fcp_{i}")

            # 📝 OBSERVAÇÕES
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t34_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t34_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t34_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t34_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # 🖼️ PAINEL DIREITO
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🧘",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
