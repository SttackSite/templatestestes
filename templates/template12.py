import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img12.png"
TEMPLATE_NAME = "Template 12 — Crehana Style (Cursos Online & Educação)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t12_cores": [
            {"nome": "Cor Principal (Roxo)",      "valor": "#4b22b4"},
            {"nome": "Cor de Texto (Escuro)",      "valor": "#1b1c1e"},
            {"nome": "Cor de Estrela (Amarelo)",   "valor": "#ffb400"},
            {"nome": "Cor de Fundo (Branco)",      "valor": "#ffffff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t12_logos": [{"valor": "crehana"}],
        "t12_nav_links": [
            {"texto": "Categorias",    "url": "#categories"},
            {"texto": "Para Empresas", "url": "#business"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t12_hero_labels":  [{"valor": "MAIS DE 1000 CURSOS ONLINE"}],
        "t12_hero_titulos": [{"valor": "Aumente suas <span class=\"highlight\">oportunidades</span> profissionais"}],
        "t12_hero_descs":   [{"valor": "Aprenda com especialistas as habilidades mais demandadas no mercado digital. Do zero ao avançado."}],
        "t12_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80"}],
        "t12_hero_btns":    [{"texto": "🎯 Explorar cursos agora", "url": "https://www.google.com/"}],

        # ── PERGUNTA ENGAJADORA ──────────────────────────────────────────────
        "t12_eng_perguntas": [{"valor": "O que você quer estudar hoje?"}],

        # ── CURSOS ──────────────────────────────────────────────────────────
        "t12_course_items": [
            {"img": "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80", "cat": "Marketing Digital", "titulo": "Facebook Ads: Domine o Gerenciador",    "rating": "4.8", "alunos": "12k alunos", "btn_txt": "Ver detalhes", "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=400&q=80", "cat": "Design",            "titulo": "Adobe Illustrator: Ilustração Vetorial", "rating": "4.9", "alunos": "45k alunos", "btn_txt": "Ver detalhes", "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80", "cat": "Tecnologia",      "titulo": "Introdução ao Desenvolvimento Web",     "rating": "4.7", "alunos": "30k alunos", "btn_txt": "Ver detalhes", "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80", "cat": "Dados",             "titulo": "Excel para Negócios: Avançado",          "rating": "4.9", "alunos": "18k alunos", "btn_txt": "Ver detalhes", "url": "https://www.google.com/"},
        ],

        # ── EMPRESAS ────────────────────────────────────────────────────────
        "t12_emp_imgs":     [{"valor": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80"}],
        "t12_emp_titulos":  [{"valor": "Treine sua equipe com a Crehana"}],
        "t12_emp_descs":    [{"valor": "Soluções de SaaS e conteúdo para fechar a lacuna de habilidades na sua empresa."}],
        "t12_emp_features": [
            {"valor": "✅ Planos de aprendizado personalizados"},
            {"valor": "✅ Painel de controle para o RH"},
        ],
        "t12_emp_btns": [{"texto": "🚀 Solicitar Demo", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t12_foot_logos": [{"valor": "crehana"}],
        "t12_foot_descs": [{"valor": "Transformando o futuro através da educação.\n© 2026 Crehana Inc. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t12_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t12_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t12_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t12_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t12_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t12_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t12_cores) > 1 and _del_btn(f"t12_cor_del_{i}"):
                        st.session_state.t12_cores.pop(i); st.rerun()
            if _add_btn("t12_cor_add", "＋ Adicionar cor"):
                st.session_state.t12_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da plataforma")
            for i, logo in enumerate(st.session_state.t12_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t12_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_logos) > 1 and _del_btn(f"t12_logo_del_{i}"):
                        st.session_state.t12_logos.pop(i); st.rerun()
            if _add_btn("t12_logo_add", "＋ Adicionar logo"):
                st.session_state.t12_logos.append({"valor": "plataforma"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t12_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t12_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t12_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t12_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t12_nav_links) > 1 and _del_btn(f"t12_nl_del_{i}"):
                        st.session_state.t12_nav_links.pop(i); st.rerun()
            if _add_btn("t12_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t12_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎓 Hero (Educação)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto roxo acima do título)*")
            for i, label in enumerate(st.session_state.t12_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t12_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_hero_labels) > 1 and _del_btn(f"t12_h_l_del_{i}"):
                        st.session_state.t12_hero_labels.pop(i); st.rerun()
            if _add_btn("t12_h_l_add", "＋ Adicionar label"):
                st.session_state.t12_hero_labels.append({"valor": "NOVO LABEL"}); st.rerun()

            st.caption("Título  *(use <span class=\"highlight\"> para deixar palavras em roxo)*")
            for i, t in enumerate(st.session_state.t12_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t12_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_hero_titulos) > 1 and _del_btn(f"t12_h_t_del_{i}"):
                        st.session_state.t12_hero_titulos.pop(i); st.rerun()
            if _add_btn("t12_h_t_add", "＋ Adicionar título"):
                st.session_state.t12_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t12_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t12_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_hero_descs) > 1 and _del_btn(f"t12_h_d_del_{i}"):
                        st.session_state.t12_hero_descs.pop(i); st.rerun()
            if _add_btn("t12_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t12_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Imagem do hero  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t12_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t12_h_i_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t12_hero_imgs) > 1 and _del_btn(f"t12_h_i_del_{i}"):
                        st.session_state.t12_hero_imgs.pop(i); st.rerun()
            if _add_btn("t12_h_i_add", "＋ Adicionar imagem hero"):
                st.session_state.t12_hero_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Botão do hero  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t12_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t12_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t12_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t12_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t12_hero_btns) > 1 and _del_btn(f"t12_hb_del_{i}"):
                        st.session_state.t12_hero_btns.pop(i); st.rerun()
            if _add_btn("t12_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t12_hero_btns.append({"texto": "NOVO BOTÃO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PERGUNTA ENGAJADORA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ Pergunta de Engajamento</div>', unsafe_allow_html=True)
            for i, perg in enumerate(st.session_state.t12_eng_perguntas):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_eng_perguntas[i]["valor"] = st.text_input(
                        "Pergunta", perg["valor"], key=f"t12_ep_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_eng_perguntas) > 1 and _del_btn(f"t12_ep_del_{i}"):
                        st.session_state.t12_eng_perguntas.pop(i); st.rerun()
            if _add_btn("t12_ep_add", "＋ Adicionar pergunta"):
                st.session_state.t12_eng_perguntas.append({"valor": "Nova pergunta?"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CURSOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📚 Vitrine de Cursos</div>', unsafe_allow_html=True)
            st.caption("Cards de curso  *(Título | Categoria | Avaliação | Alunos | Imagem | Botão | URL)*")
            for i, item in enumerate(st.session_state.t12_course_items):
                with st.expander(f"Curso {i+1}: {item['titulo']}"):
                    st.session_state.t12_course_items[i]["titulo"] = st.text_input(
                        "Título do Curso", item["titulo"], key=f"t12_ci_t_{i}")
                    st.session_state.t12_course_items[i]["cat"] = st.text_input(
                        "Categoria", item["cat"], key=f"t12_ci_c_{i}")
                    st.session_state.t12_course_items[i]["rating"] = st.text_input(
                        "Avaliação  (ex: 4.9)", item["rating"], key=f"t12_ci_r_{i}")
                    st.session_state.t12_course_items[i]["alunos"] = st.text_input(
                        "Qtd. de Alunos  (ex: 12k alunos)", item["alunos"], key=f"t12_ci_a_{i}")
                    st.session_state.t12_course_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t12_ci_i_{i}")
                    st.session_state.t12_course_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t12_ci_bt_{i}")
                    st.session_state.t12_course_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t12_ci_u_{i}")
                    if len(st.session_state.t12_course_items) > 1:
                        if st.button("🗑 Remover este curso", key=f"t12_ci_del_{i}"):
                            st.session_state.t12_course_items.pop(i); st.rerun()
            if _add_btn("t12_ci_add", "＋ Adicionar curso"):
                st.session_state.t12_course_items.append({
                    "img": "", "cat": "CATEGORIA", "titulo": "NOVO CURSO",
                    "rating": "5.0", "alunos": "0 alunos",
                    "btn_txt": "Ver detalhes", "url": "#"
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # EMPRESAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 Seção para Empresas</div>', unsafe_allow_html=True)

            st.caption("Imagem  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t12_emp_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t12_ei_i_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t12_emp_imgs) > 1 and _del_btn(f"t12_ei_i_del_{i}"):
                        st.session_state.t12_emp_imgs.pop(i); st.rerun()
            if _add_btn("t12_ei_i_add", "＋ Adicionar imagem"):
                st.session_state.t12_emp_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Título")
            for i, t in enumerate(st.session_state.t12_emp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t12_ei_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_emp_titulos) > 1 and _del_btn(f"t12_ei_t_del_{i}"):
                        st.session_state.t12_emp_titulos.pop(i); st.rerun()
            if _add_btn("t12_ei_t_add", "＋ Adicionar título"):
                st.session_state.t12_emp_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t12_emp_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t12_ei_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_emp_descs) > 1 and _del_btn(f"t12_ei_d_del_{i}"):
                        st.session_state.t12_emp_descs.pop(i); st.rerun()
            if _add_btn("t12_ei_d_add", "＋ Adicionar descrição"):
                st.session_state.t12_emp_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Benefícios / Features  *(checklist)*")
            for i, feat in enumerate(st.session_state.t12_emp_features):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_features[i]["valor"] = st.text_input(
                        "Benefício", feat["valor"], key=f"t12_ef_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_emp_features) > 1 and _del_btn(f"t12_ef_del_{i}"):
                        st.session_state.t12_emp_features.pop(i); st.rerun()
            if _add_btn("t12_ef_add", "＋ Adicionar benefício"):
                st.session_state.t12_emp_features.append({"valor": "✅ Novo Benefício"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t12_emp_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_emp_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t12_eb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t12_emp_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t12_eb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t12_emp_btns) > 1 and _del_btn(f"t12_eb_del_{i}"):
                        st.session_state.t12_emp_btns.pop(i); st.rerun()
            if _add_btn("t12_eb_add", "＋ Adicionar botão"):
                st.session_state.t12_emp_btns.append({"texto": "NOVO BOTÃO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t12_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t12_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_foot_logos) > 1 and _del_btn(f"t12_fl_del_{i}"):
                        st.session_state.t12_foot_logos.pop(i); st.rerun()
            if _add_btn("t12_fl_add", "＋ Adicionar logo"):
                st.session_state.t12_foot_logos.append({"valor": "plataforma"}); st.rerun()

            st.caption("Copyright e descrição")
            for i, desc in enumerate(st.session_state.t12_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_foot_descs[i]["valor"] = st.text_area(
                        "Copyright", desc["valor"], key=f"t12_fd_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_foot_descs) > 1 and _del_btn(f"t12_fd_del_{i}"):
                        st.session_state.t12_foot_descs.pop(i); st.rerun()
            if _add_btn("t12_fd_add", "＋ Adicionar linha ao rodapé"):
                st.session_state.t12_foot_descs.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t12_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t12_obs_{i}", height=80,
                        placeholder="Ex: Mudar a imagem do curso de Marketing para uma mais vibrante...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_obs) > 1 and _del_btn(f"t12_obs_del_{i}"):
                        st.session_state.t12_obs.pop(i); st.rerun()
            if _add_btn("t12_obs_add", "＋ Adicionar observação"):
                st.session_state.t12_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t12_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
