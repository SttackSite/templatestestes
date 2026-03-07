import streamlit as st
import json
import urllib.request

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img12.png"
TEMPLATE_NAME      = "Template 12 — Crehana Style (Cursos Online & Educação)"
TEMPLATE_ID        = "template_12"
RESEND_API_KEY     = st.secrets.get("RESEND_KEY", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t12_nome_cliente":  "",
        "t12_email_cliente": "",
        "t12_nome_site":     "",

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
            {"texto": "Categorias",    "url": "seção Vitrine de Cursos"},
            {"texto": "Para Empresas", "url": "seção Empresas"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t12_hero_labels":  [{"valor": "MAIS DE 1000 CURSOS ONLINE"}],
        "t12_hero_titulos": [{"valor": "Aumente suas oportunidades profissionais"}],
        "t12_hero_descs":   [{"valor": "Aprenda com especialistas as habilidades mais demandadas no mercado digital. Do zero ao avançado."}],
        "t12_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80"}],
        "t12_hero_btns":    [{"texto": "🎯 Explorar cursos agora", "url": "seção Vitrine de Cursos"}],

        # ── PERGUNTA ENGAJADORA ──────────────────────────────────────────────
        "t12_eng_perguntas": [{"valor": "O que você quer estudar hoje?"}],

        # ── CURSOS ──────────────────────────────────────────────────────────
        "t12_course_items": [
            {"img": "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80", "cat": "Marketing Digital", "titulo": "Facebook Ads: Domine o Gerenciador",     "rating": "4.8", "alunos": "12k alunos", "btn_txt": "Ver detalhes", "url": "https://wa.me/5511999999999"},
            {"img": "https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=400&q=80", "cat": "Design",            "titulo": "Adobe Illustrator: Ilustração Vetorial", "rating": "4.9", "alunos": "45k alunos", "btn_txt": "Ver detalhes", "url": "https://wa.me/5511999999999"},
            {"img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=400&q=80", "cat": "Tecnologia",     "titulo": "Introdução ao Desenvolvimento Web",      "rating": "4.7", "alunos": "30k alunos", "btn_txt": "Ver detalhes", "url": "https://wa.me/5511999999999"},
            {"img": "https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&w=400&q=80", "cat": "Dados",             "titulo": "Excel para Negócios: Avançado",           "rating": "4.9", "alunos": "18k alunos", "btn_txt": "Ver detalhes", "url": "https://wa.me/5511999999999"},
        ],

        # ── EMPRESAS ────────────────────────────────────────────────────────
        "t12_emp_imgs":     [{"valor": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80"}],
        "t12_emp_titulos":  [{"valor": "Treine sua equipe com a Crehana"}],
        "t12_emp_descs":    [{"valor": "Soluções de SaaS e conteúdo para fechar a lacuna de habilidades na sua empresa."}],
        "t12_emp_features": [
            {"valor": "Planos de aprendizado personalizados"},
            {"valor": "Painel de controle para o RH"},
        ],
        "t12_emp_btns": [{"texto": "🚀 Solicitar Demo", "url": "https://wa.me/5511999999999"}],

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

def _build_json():
    return {
        "template":      TEMPLATE_ID,
        "template_nome": TEMPLATE_NAME,
        "identificacao": {
            "nome":      st.session_state.t12_nome_cliente,
            "email":     st.session_state.t12_email_cliente,
            "nome_site": st.session_state.t12_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t12_nome_site}",
        },
        "cores": st.session_state.t12_cores,
        "navbar": {
            "logos": st.session_state.t12_logos,
            "links": st.session_state.t12_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t12_hero_labels,
            "titulos": st.session_state.t12_hero_titulos,
            "descs":   st.session_state.t12_hero_descs,
            "imagens": st.session_state.t12_hero_imgs,
            "botoes":  st.session_state.t12_hero_btns,
        },
        "engajamento": st.session_state.t12_eng_perguntas,
        "cursos": st.session_state.t12_course_items,
        "empresas": {
            "imagens":   st.session_state.t12_emp_imgs,
            "titulos":   st.session_state.t12_emp_titulos,
            "descs":     st.session_state.t12_emp_descs,
            "features":  st.session_state.t12_emp_features,
            "botoes":    st.session_state.t12_emp_btns,
        },
        "footer": {
            "logos": st.session_state.t12_foot_logos,
            "descs": st.session_state.t12_foot_descs,
        },
        "observacoes": st.session_state.t12_obs,
    }

def _enviar_resend(payload: dict) -> bool:
    try:
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"
        data = json.dumps({
            "from":    "editor@sttacksite.com.br",
            "to":      [DESTINO_EMAIL],
            "subject": f"[Novo Pedido] {TEMPLATE_NAME} — {payload['identificacao']['nome']}",
            "html":    body_html,
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=data,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type":  "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status in (200, 201)
    except Exception:
        return False


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
        .info-box {
            background: #eff6ff; border: 1px solid #bfdbfe;
            border-radius: 10px; padding: 14px 16px; margin-bottom: 10px;
            font-size: 13px; color: #1e40af; line-height: 1.6;
        }
        .info-box strong { color: #1e3a8a; }
        .warn-box {
            background: #fefce8; border: 1px solid #fde68a;
            border-radius: 10px; padding: 14px 16px; margin-bottom: 10px;
            font-size: 13px; color: #92400e; line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        👋 <strong>Bem-vindo ao editor do seu site!</strong><br>
        Preencha os campos abaixo para personalizar o seu site. Não precisa ser técnico — é só digitar!
        Você também poderá vir aqui e ajustar seu site quantas vezes quiser.<br><br>
        💡 <strong>Tem alguma ideia que não encontrou aqui?</strong> Use o campo <em>Observações</em> no final
        para descrever o que deseja. Nossa equipe analisa tudo e aplica para você. 😊
    </div>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ══════════════════════════════════════════════════════════════════
            # 0. IDENTIFICAÇÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👤 Seus Dados</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin-top:4px">
                Preencha seus dados antes de começar. Usamos essas informações para identificar seu pedido e
                entrar em contato quando o site estiver pronto. 🚀
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t12_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t12_nome_cliente,
                key="t12_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t12_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t12_email_cliente,
                key="t12_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: minhaplataforma, cursosdigitais, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t12_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t12_nome_site,
                key="t12_nome_site_inp",
                placeholder="Ex: minhaplataforma  →  sttacksite.streamlit.app/?c=minhaplataforma",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t12_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t12_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t12_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t12_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t12_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t12_cores) > 1 and _del_btn(f"t12_cor_del_{i}"):
                        st.session_state.t12_cores.pop(i); st.rerun()
            if _add_btn("t12_cor_add", "＋ Adicionar cor"):
                st.session_state.t12_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da plataforma")
            for i, logo in enumerate(st.session_state.t12_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t12_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: minha plataforma ou Cursos Online")
                with c2:
                    if len(st.session_state.t12_logos) > 1 and _del_btn(f"t12_logo_del_{i}"):
                        st.session_state.t12_logos.pop(i); st.rerun()
            if _add_btn("t12_logo_add", "＋ Adicionar logo"):
                st.session_state.t12_logos.append({"valor": "plataforma"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos links:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), qualquer link — ou simplesmente descrever
                para qual seção o link deve levar (ex: <em>seção de cursos</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t12_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t12_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t12_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t12_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t12_nav_links) > 1 and _del_btn(f"t12_nl_del_{i}"):
                        st.session_state.t12_nav_links.pop(i); st.rerun()
            if _add_btn("t12_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t12_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎓 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto roxo acima do título)*")
            for i, label in enumerate(st.session_state.t12_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t12_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: MAIS DE 1000 CURSOS ONLINE")
                with c2:
                    if len(st.session_state.t12_hero_labels) > 1 and _del_btn(f"t12_h_l_del_{i}"):
                        st.session_state.t12_hero_labels.pop(i); st.rerun()
            if _add_btn("t12_h_l_add", "＋ Adicionar label"):
                st.session_state.t12_hero_labels.append({"valor": "NOVO LABEL"}); st.rerun()

            st.caption("Título  *(para destacar palavras em roxo, descreva nas Observações)*")
            for i, t in enumerate(st.session_state.t12_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t12_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Título principal do hero")
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
                        "Descrição", d["valor"], key=f"t12_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que apresenta sua plataforma de cursos")
                with c2:
                    if len(st.session_state.t12_hero_descs) > 1 and _del_btn(f"t12_h_d_del_{i}"):
                        st.session_state.t12_hero_descs.pop(i); st.rerun()
            if _add_btn("t12_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t12_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem do Hero:</strong> cole a URL de uma foto do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem do hero  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t12_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t12_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t12_hero_imgs) > 1 and _del_btn(f"t12_h_i_del_{i}"):
                        st.session_state.t12_hero_imgs.pop(i); st.rerun()
            if _add_btn("t12_h_i_add", "＋ Adicionar imagem hero"):
                st.session_state.t12_hero_imgs.append({"valor": ""}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t12_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t12_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t12_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t12_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t12_hero_btns) > 1 and _del_btn(f"t12_hb_del_{i}"):
                        st.session_state.t12_hero_btns.pop(i); st.rerun()
            if _add_btn("t12_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t12_hero_btns.append({"texto": "NOVO BOTÃO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PERGUNTA ENGAJADORA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ Pergunta de Engajamento</div>', unsafe_allow_html=True)
            st.caption("Pergunta exibida acima da vitrine de cursos")
            for i, perg in enumerate(st.session_state.t12_eng_perguntas):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_eng_perguntas[i]["valor"] = st.text_input(
                        "Pergunta", perg["valor"], key=f"t12_ep_{i}", label_visibility="collapsed",
                        placeholder="Ex: O que você quer aprender hoje?")
                with c2:
                    if len(st.session_state.t12_eng_perguntas) > 1 and _del_btn(f"t12_ep_del_{i}"):
                        st.session_state.t12_eng_perguntas.pop(i); st.rerun()
            if _add_btn("t12_ep_add", "＋ Adicionar pergunta"):
                st.session_state.t12_eng_perguntas.append({"valor": "Nova pergunta?"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. CURSOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📚 Vitrine de Cursos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos cursos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>400 × 300 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de curso  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t12_course_items):
                with st.expander(f"Curso {i+1}: {item['titulo']}"):
                    st.session_state.t12_course_items[i]["titulo"] = st.text_input(
                        "Título do Curso", item["titulo"], key=f"t12_ci_t_{i}",
                        placeholder="Nome do curso")
                    st.session_state.t12_course_items[i]["cat"] = st.text_input(
                        "Categoria", item["cat"], key=f"t12_ci_c_{i}",
                        placeholder="Ex: Marketing Digital, Design, Tecnologia")
                    st.session_state.t12_course_items[i]["rating"] = st.text_input(
                        "Avaliação", item["rating"], key=f"t12_ci_r_{i}",
                        placeholder="Ex: 4.9")
                    st.session_state.t12_course_items[i]["alunos"] = st.text_input(
                        "Qtd. de Alunos", item["alunos"], key=f"t12_ci_a_{i}",
                        placeholder="Ex: 12k alunos")
                    st.session_state.t12_course_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t12_ci_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t12_course_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t12_ci_bt_{i}")
                    st.session_state.t12_course_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t12_ci_u_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t12_course_items) > 1:
                        if st.button("🗑 Remover este curso", key=f"t12_ci_del_{i}"):
                            st.session_state.t12_course_items.pop(i); st.rerun()
            if _add_btn("t12_ci_add", "＋ Adicionar curso"):
                st.session_state.t12_course_items.append({
                    "img": "", "cat": "CATEGORIA", "titulo": "NOVO CURSO",
                    "rating": "5.0", "alunos": "0 alunos",
                    "btn_txt": "Ver detalhes", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. EMPRESAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 Seção para Empresas</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem lateral:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t12_emp_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t12_ei_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t12_emp_imgs) > 1 and _del_btn(f"t12_ei_i_del_{i}"):
                        st.session_state.t12_emp_imgs.pop(i); st.rerun()
            if _add_btn("t12_ei_i_add", "＋ Adicionar imagem"):
                st.session_state.t12_emp_imgs.append({"valor": ""}); st.rerun()

            st.caption("Título")
            for i, t in enumerate(st.session_state.t12_emp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t12_ei_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Treine sua equipe")
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
                        "Descrição", d["valor"], key=f"t12_ei_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Descreva sua proposta para empresas")
                with c2:
                    if len(st.session_state.t12_emp_descs) > 1 and _del_btn(f"t12_ei_d_del_{i}"):
                        st.session_state.t12_emp_descs.pop(i); st.rerun()
            if _add_btn("t12_ei_d_add", "＋ Adicionar descrição"):
                st.session_state.t12_emp_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Benefícios  *(checklist de diferenciais)*")
            for i, feat in enumerate(st.session_state.t12_emp_features):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_emp_features[i]["valor"] = st.text_input(
                        "Benefício", feat["valor"], key=f"t12_ef_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: Planos personalizados por time")
                with c2:
                    if len(st.session_state.t12_emp_features) > 1 and _del_btn(f"t12_ef_del_{i}"):
                        st.session_state.t12_emp_features.pop(i); st.rerun()
            if _add_btn("t12_ef_add", "＋ Adicionar benefício"):
                st.session_state.t12_emp_features.append({"valor": "Novo Benefício"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t12_emp_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t12_emp_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t12_eb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t12_emp_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t12_eb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t12_emp_btns) > 1 and _del_btn(f"t12_eb_del_{i}"):
                        st.session_state.t12_emp_btns.pop(i); st.rerun()
            if _add_btn("t12_eb_add", "＋ Adicionar botão"):
                st.session_state.t12_emp_btns.append({"texto": "NOVO BOTÃO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t12_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t12_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: minha plataforma")
                with c2:
                    if len(st.session_state.t12_foot_logos) > 1 and _del_btn(f"t12_fl_del_{i}"):
                        st.session_state.t12_foot_logos.pop(i); st.rerun()
            if _add_btn("t12_fl_add", "＋ Adicionar logo"):
                st.session_state.t12_foot_logos.append({"valor": "plataforma"}); st.rerun()

            st.caption("Copyright e descrição do rodapé")
            for i, desc in enumerate(st.session_state.t12_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_foot_descs[i]["valor"] = st.text_area(
                        "Copyright", desc["valor"], key=f"t12_fd_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t12_foot_descs) > 1 and _del_btn(f"t12_fd_del_{i}"):
                        st.session_state.t12_foot_descs.pop(i); st.rerun()
            if _add_btn("t12_fd_add", "＋ Adicionar linha ao rodapé"):
                st.session_state.t12_foot_descs.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo correspondente nas seções acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero lateral: <strong>800 × 600 px</strong><br>
                • Cards de cursos: <strong>400 × 300 px</strong><br>
                • Seção Empresas: <strong>800 × 600 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 9. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "destacar palavra X em roxo no título", "adicionar categorias de filtro", "colocar vídeo do YouTube",
                "adicionar FAQ", "remover seção de Empresas", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t12_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t12_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t12_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t12_obs) > 1 and _del_btn(f"t12_obs_del_{i}"):
                        st.session_state.t12_obs.pop(i); st.rerun()
            if _add_btn("t12_obs_add", "＋ Adicionar observação"):
                st.session_state.t12_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t12_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t12_email_cliente.strip() or "@" not in st.session_state.t12_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t12_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t12_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso = _enviar_resend(payload)
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t12_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t12_nome_cliente}'*."
                    )
                    st.code(json.dumps(payload, ensure_ascii=False, indent=2), language="json")

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
