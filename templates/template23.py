import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img23.png"
TEMPLATE_NAME      = "Template 23 — PAIX Design Style (Architecture & Interior Design)"
TEMPLATE_ID        = "template_23"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t23_nome_cliente":  "",
        "t23_email_cliente": "",
        "t23_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t23_cores": [
            {"nome": "Fundo (Tom de Pedra)",    "valor": "#f7f7f7"},
            {"nome": "Texto Principal (Preto)", "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)","valor": "#555555"},
            {"nome": "Linhas e Bordas",         "valor": "#dddddd"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t23_nav_logos": [{"valor": "PAIX DESIGN"}],
        "t23_nav_links": [
            {"texto": "Projetos",   "url": "seção Projetos em Destaque"},
            {"texto": "Escritório", "url": "seção Sobre o Escritório"},
            {"texto": "Contato",    "url": "seção Rodapé de Contato"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t23_hero_labels":  [{"valor": "Arquitetura & Design de Interiores"}],
        "t23_hero_titulos": [{"valor": "A beleza reside na intenção e na calma."}],
        "t23_hero_descs":   [{"valor": "PAIX é um estúdio de design focado na criação de espaços que transcendem o tempo. Nossa abordagem é guiada pela pureza dos materiais e pela harmonia entre a luz natural e a forma construída."}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t23_project_items": [
            {"img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600", "title": "Casa Minimalista",    "location": "Sintra", "year": "2024", "category": "Residencial / Design de Mobiliário"},
            {"img": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600", "title": "Apartamento Galeria", "location": "Porto",  "year": "2023", "category": "Residencial / Design de Mobiliário"},
        ],

        # ── SOBRE (TRANSICIONAL) ─────────────────────────────────────────────
        "t23_about_titulos": [{"valor": "Atmosferas Tangíveis"}],
        "t23_about_descs":   [{"valor": "Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente."}],
        "t23_about_btns":    [{"texto": "Conheça Nosso Trabalho", "url": "seção Projetos em Destaque"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t23_foot_brand_names": [{"valor": "PAIX DESIGN STUDIO"}],
        "t23_foot_addresses":   [{"valor": "AV. PAULISTA, SÃO PAULO"}],
        "t23_foot_emails":      [{"valor": "hello@paix-design.com"}],
        "t23_foot_cols": [
            {"titulo": "REDES SOCIAIS", "links": [
                {"texto": "INSTAGRAM", "url": "https://instagram.com/"},
                {"texto": "BEHANCE",   "url": "https://behance.net/"},
                {"texto": "LINKEDIN",  "url": "https://linkedin.com/"},
            ]},
        ],
        "t23_foot_copys": [{"valor": "© 2026 PAIX DESIGN. TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t23_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t23_nome_cliente,
            "email":     st.session_state.t23_email_cliente,
            "nome_site": st.session_state.t23_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t23_nome_site}",
        },
        "cores": st.session_state.t23_cores,
        "navbar": {
            "logos": st.session_state.t23_nav_logos,
            "links": st.session_state.t23_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t23_hero_labels,
            "titulos": st.session_state.t23_hero_titulos,
            "descs":   st.session_state.t23_hero_descs,
        },
        "projetos": st.session_state.t23_project_items,
        "sobre": {
            "titulos": st.session_state.t23_about_titulos,
            "descs":   st.session_state.t23_about_descs,
            "botoes":  st.session_state.t23_about_btns,
        },
        "footer": {
            "brand_names": st.session_state.t23_foot_brand_names,
            "enderecos":   st.session_state.t23_foot_addresses,
            "emails":      st.session_state.t23_foot_emails,
            "colunas":     st.session_state.t23_foot_cols,
            "copyright":   st.session_state.t23_foot_copys,
        },
        "observacoes": st.session_state.t23_obs,
    }

def _enviar_resend(payload: dict):
    """Retorna (sucesso: bool, mensagem_erro: str) via Gmail SMTP"""
    try:
        nome    = payload["identificacao"]["nome"]
        subject = f"[Novo Pedido] {TEMPLATE_NAME} — {nome}"
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = GMAIL_USER
        msg["To"]      = DESTINO_EMAIL
        msg.attach(MIMEText(body_html, "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, DESTINO_EMAIL, msg.as_string())
        return True, ""
    except Exception as ex:
        return False, str(ex)


# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');
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

            st.session_state.t23_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t23_nome_cliente,
                key="t23_nome_cliente_inp", placeholder="Ex: Mariana Costa",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t23_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t23_email_cliente,
                key="t23_email_cliente_inp", placeholder="Ex: mariana@estudio.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: paix, estudioarquitetura, casadesign).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t23_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t23_nome_site,
                key="t23_nome_site_inp",
                placeholder="Ex: paix  →  sttacksite.streamlit.app/?c=paix",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t23_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t23_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t23_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t23_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t23_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t23_cores) > 1 and _del_btn(f"t23_cor_del_{i}"):
                        st.session_state.t23_cores.pop(i); st.rerun()
            if _add_btn("t23_cor_add", "＋ Adicionar cor"):
                st.session_state.t23_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome do escritório  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t23_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t23_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: SEU ESTÚDIO DESIGN")
                with c2:
                    if len(st.session_state.t23_nav_logos) > 1 and _del_btn(f"t23_logo_del_{i}"):
                        st.session_state.t23_nav_logos.pop(i); st.rerun()
            if _add_btn("t23_logo_add", "＋ Adicionar logo"):
                st.session_state.t23_nav_logos.append({"valor": "ESTÚDIO"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t23_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t23_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t23_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t23_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t23_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t23_nav_links) > 1 and _del_btn(f"t23_nl_del_{i}"):
                        st.session_state.t23_nav_links.pop(i); st.rerun()
            if _add_btn("t23_nl_add", "＋ Adicionar link"):
                st.session_state.t23_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label / Subtítulo  *(texto pequeno em cinza — especialidade do escritório)*")
            for i, l in enumerate(st.session_state.t23_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t23_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Arquitetura & Design de Interiores")
                with c2:
                    if len(st.session_state.t23_hero_labels) > 1 and _del_btn(f"t23_h_l_del_{i}"):
                        st.session_state.t23_hero_labels.pop(i); st.rerun()
            if _add_btn("t23_h_l_add", "＋ Adicionar label"):
                st.session_state.t23_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título poético:</strong> escreva o texto normalmente.
                Se quiser quebrar em linhas diferentes, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(frase poética em tipografia elegante)*")
            for i, t in enumerate(st.session_state.t23_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t23_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: A beleza reside na intenção e na calma.")
                with c2:
                    if len(st.session_state.t23_hero_titulos) > 1 and _del_btn(f"t23_h_t_del_{i}"):
                        st.session_state.t23_hero_titulos.pop(i); st.rerun()
            if _add_btn("t23_h_t_add", "＋ Adicionar título"):
                st.session_state.t23_hero_titulos.append({"valor": "Novo título poético."}); st.rerun()

            st.caption("Descrição  *(apresentação do escritório)*")
            for i, d in enumerate(st.session_state.t23_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t23_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Apresente o escritório: filosofia, especialidade, diferencial em 2-3 frases")
                with c2:
                    if len(st.session_state.t23_hero_descs) > 1 and _del_btn(f"t23_h_d_del_{i}"):
                        st.session_state.t23_hero_descs.pop(i); st.rerun()
            if _add_btn("t23_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t23_hero_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Projetos em Destaque</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos projetos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho ideal: <strong>1600 × 900 px</strong> (paisagem larga) para o visual de portfólio editorial.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t23_project_items):
                with st.expander(f"Projeto {i+1}: {item['title']}"):
                    st.session_state.t23_project_items[i]["title"] = st.text_input(
                        "Título do Projeto", item["title"], key=f"t23_pi_t_{i}",
                        placeholder="Ex: Casa Minimalista")
                    st.session_state.t23_project_items[i]["location"] = st.text_input(
                        "Localização", item["location"], key=f"t23_pi_l_{i}",
                        placeholder="Ex: São Paulo")
                    st.session_state.t23_project_items[i]["year"] = st.text_input(
                        "Ano", item["year"], key=f"t23_pi_y_{i}",
                        placeholder="Ex: 2025")
                    st.session_state.t23_project_items[i]["category"] = st.text_input(
                        "Categoria", item["category"], key=f"t23_pi_c_{i}",
                        placeholder="Ex: Residencial / Design de Mobiliário")
                    st.session_state.t23_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t23_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Foto do projeto — 1600×900 px ideal")
                    if len(st.session_state.t23_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t23_pi_del_{i}"):
                            st.session_state.t23_project_items.pop(i); st.rerun()
            if _add_btn("t23_pi_add", "＋ Adicionar projeto"):
                st.session_state.t23_project_items.append({
                    "img": "", "title": "NOVO PROJETO", "location": "CIDADE",
                    "year": "2026", "category": "RESIDENCIAL"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. SOBRE (TRANSICIONAL)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Sobre o Escritório</div>', unsafe_allow_html=True)

            st.caption("Título  *(nome poético da seção)*")
            for i, t in enumerate(st.session_state.t23_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_about_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t23_at_{i}", label_visibility="collapsed",
                        placeholder="Ex: Nossa Filosofia")
                with c2:
                    if len(st.session_state.t23_about_titulos) > 1 and _del_btn(f"t23_at_del_{i}"):
                        st.session_state.t23_about_titulos.pop(i); st.rerun()
            if _add_btn("t23_at_add", "＋ Adicionar título"):
                st.session_state.t23_about_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(texto sobre o método e valores do escritório)*")
            for i, d in enumerate(st.session_state.t23_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t23_ad_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva o processo, os materiais, a abordagem colaborativa...")
                with c2:
                    if len(st.session_state.t23_about_descs) > 1 and _del_btn(f"t23_ad_del_{i}"):
                        st.session_state.t23_about_descs.pop(i); st.rerun()
            if _add_btn("t23_ad_add", "＋ Adicionar descrição"):
                st.session_state.t23_about_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botões  *(Texto | Destino ou URL)*")
            for i, btn in enumerate(st.session_state.t23_about_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t23_about_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t23_ab_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Conheça Nosso Trabalho")
                with c2:
                    st.session_state.t23_about_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t23_ab_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção de destino")
                with c3:
                    if len(st.session_state.t23_about_btns) > 1 and _del_btn(f"t23_ab_del_{i}"):
                        st.session_state.t23_about_btns.pop(i); st.rerun()
            if _add_btn("t23_ab_add", "＋ Adicionar botão"):
                st.session_state.t23_about_btns.append({"texto": "VEJA MAIS", "url": "seção Projetos em Destaque"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Nome do escritório")
            for i, name in enumerate(st.session_state.t23_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t23_fn_{i}", label_visibility="collapsed",
                        placeholder="Ex: SEU ESTÚDIO DESIGN")
                with c2:
                    if len(st.session_state.t23_foot_brand_names) > 1 and _del_btn(f"t23_fn_del_{i}"):
                        st.session_state.t23_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t23_fn_add", "＋ Adicionar nome"):
                st.session_state.t23_foot_brand_names.append({"valor": "ESTÚDIO"}); st.rerun()

            st.caption("Endereço  *(exibido no rodapé)*")
            for i, addr in enumerate(st.session_state.t23_foot_addresses):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_addresses[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t23_fa_{i}", label_visibility="collapsed",
                        placeholder="Ex: AV. PAULISTA, SÃO PAULO — SP")
                with c2:
                    if len(st.session_state.t23_foot_addresses) > 1 and _del_btn(f"t23_fa_del_{i}"):
                        st.session_state.t23_foot_addresses.pop(i); st.rerun()
            if _add_btn("t23_fa_add", "＋ Adicionar endereço"):
                st.session_state.t23_foot_addresses.append({"valor": "RUA, CIDADE"}); st.rerun()

            st.caption("E-mail de contato  *(exibido como link clicável)*")
            for i, email in enumerate(st.session_state.t23_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_emails[i]["valor"] = st.text_input(
                        "Email", email["valor"], key=f"t23_fe_{i}", label_visibility="collapsed",
                        placeholder="email@estudio.com",
                        help="Este e-mail será exibido no rodapé como link de contato.")
                with c2:
                    if len(st.session_state.t23_foot_emails) > 1 and _del_btn(f"t23_fe_del_{i}"):
                        st.session_state.t23_foot_emails.pop(i); st.rerun()
            if _add_btn("t23_fe_add", "＋ Adicionar email"):
                st.session_state.t23_foot_emails.append({"valor": "email@estudio.com"}); st.rerun()

            st.caption("Colunas de links  *(redes sociais e outros links)*")
            for i, col in enumerate(st.session_state.t23_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t23_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t23_fc_t_{i}",
                        placeholder="Ex: REDES SOCIAIS ou SERVIÇOS")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t23_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t23_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t23_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t23_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https://instagram.com/...")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t23_fc_l_del_{i}_{j}"):
                                st.session_state.t23_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t23_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t23_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t23_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t23_fc_del_{i}"):
                            st.session_state.t23_foot_cols.pop(i); st.rerun()
            if _add_btn("t23_fc_add", "＋ Adicionar coluna"):
                st.session_state.t23_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t23_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t23_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 SEU ESTÚDIO. TODOS OS DIREITOS RESERVADOS.")
                with c2:
                    if len(st.session_state.t23_foot_copys) > 1 and _del_btn(f"t23_fcp_del_{i}"):
                        st.session_state.t23_foot_copys.pop(i); st.rerun()
            if _add_btn("t23_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t23_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem do projeto correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Projetos (destaque full-width): <strong>1600 × 900 px</strong> (paisagem larga)<br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 8. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "usar uma paleta mais monocromática", "adicionar seção de serviços",
                "adicionar depoimentos de clientes", "adicionar mapa do escritório"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t23_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t23_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_obs) > 1 and _del_btn(f"t23_obs_del_{i}"):
                        st.session_state.t23_obs.pop(i); st.rerun()
            if _add_btn("t23_obs_add", "＋ Adicionar observação"):
                st.session_state.t23_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t23_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t23_email_cliente.strip() or "@" not in st.session_state.t23_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t23_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t23_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso, erro_msg = _enviar_resend(payload)
                if erro_msg:
                    st.error(f"🔴 Erro ao enviar: {erro_msg}")
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t23_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t23_nome_cliente}'*."
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
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
