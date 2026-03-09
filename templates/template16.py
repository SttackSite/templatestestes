import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img16.png"
TEMPLATE_NAME      = "Template 16 — LITIGUARD Style (Legal & Strategic Advisory)"
TEMPLATE_ID        = "template_16"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t16_nome_cliente":  "",
        "t16_email_cliente": "",
        "t16_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t16_cores": [
            {"nome": "Azul Marinho (Principal)", "valor": "#1a2b3c"},
            {"nome": "Dourado (Destaque)",        "valor": "#c5a059"},
            {"nome": "Fundo (Branco)",            "valor": "#ffffff"},
            {"nome": "Texto (Escuro)",            "valor": "#1a2b3c"},
        ],

        # ── TOP BAR ─────────────────────────────────────────────────────────
        "t16_top_bar_links": [
            {"texto": "LITIGATION & ADVISORY SERVICES", "url": "seção Nossa Expertise"},
            {"texto": "EN | FR | DE",                   "url": "seção Sobre"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t16_logos": [{"valor": "LITIGUARD"}],
        "t16_nav_links": [
            {"texto": "ABOUT",    "url": "seção Sobre"},
            {"texto": "SERVICES", "url": "seção Nossa Expertise"},
            {"texto": "NETWORK",  "url": "seção Rede Global"},
            {"texto": "CONTACT",  "url": "seção de contato ao final da página"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t16_hero_titulos": [{"valor": "Protecting Your Interests"}],
        "t16_hero_descs":   [{"valor": "A global network of legal experts dedicated to complex litigation and strategic advisory."}],
        "t16_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"}],

        # ── ABOUT ───────────────────────────────────────────────────────────
        "t16_about_titulos": [{"valor": "Strategic Legal Representation"}],
        "t16_about_descs":   [{"valor": "Litiguard provides comprehensive support in cross-border disputes. Our approach combines local expertise with a global perspective to ensure the best possible outcome for institutional and private clients."}],
        "t16_about_btns":    [{"texto": "Discover Our Vision", "url": "https://wa.me/5511999999999"}],

        # ── EXPERTISE (SERVICES) ────────────────────────────────────────────
        "t16_exp_secao_titulos": [{"valor": "Our Expertise"}],
        "t16_exp_items": [
            {"icon": "⚖️", "titulo": "Commercial Litigation",  "desc": "Resolving complex business disputes with precision and strategic foresight."},
            {"icon": "🌍", "titulo": "Cross-Border Claims",     "desc": "Navigating multiple jurisdictions to protect assets and enforce rights worldwide."},
            {"icon": "🤝", "titulo": "Arbitration",             "desc": "Expert representation in international arbitration proceedings and alternative dispute resolution."},
            {"icon": "🛡️", "titulo": "Asset Recovery",          "desc": "Tracing and recovering assets across global financial centers and tax havens."},
            {"icon": "📈", "titulo": "Investment Disputes",     "desc": "Protecting investors' rights under bilateral treaties and international law."},
            {"icon": "📜", "titulo": "Corporate Advisory",      "desc": "Proactive legal strategies to mitigate risks and ensure regulatory compliance."},
        ],

        # ── NETWORK ─────────────────────────────────────────────────────────
        "t16_net_titulos": [{"valor": "A Truly Global Presence"}],
        "t16_net_descs":   [{"valor": "Our network spans over 40 countries, providing seamless legal support whenever and wherever our clients need it most."}],
        "t16_net_cities": [
            {"nome": "LONDON"},
            {"nome": "BRUSSELS"},
            {"nome": "DUBAI"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t16_foot_logos": [{"valor": "LITIGUARD"}],
        "t16_foot_descs": [{"valor": "International Litigation & Advisory Support Network."}],
        "t16_foot_cols": [
            {"titulo": "OFFICES", "links": [{"texto": "Brussels, Belgium", "url": "seção Rede Global"}, {"texto": "Geneva, Switzerland", "url": "seção Rede Global"}, {"texto": "London, UK", "url": "seção Rede Global"}]},
            {"titulo": "LEGAL",   "links": [{"texto": "Privacy Policy", "url": "https://wa.me/5511999999999"}, {"texto": "Terms of Service", "url": "https://wa.me/5511999999999"}, {"texto": "Cookies", "url": "https://wa.me/5511999999999"}]},
        ],
        "t16_foot_copys": [{"valor": "© 2026 LITIGUARD. ALL RIGHTS RESERVED."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t16_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t16_nome_cliente,
            "email":     st.session_state.t16_email_cliente,
            "nome_site": st.session_state.t16_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t16_nome_site}",
        },
        "cores": st.session_state.t16_cores,
        "top_bar": st.session_state.t16_top_bar_links,
        "navbar": {
            "logos": st.session_state.t16_logos,
            "links": st.session_state.t16_nav_links,
        },
        "hero": {
            "titulos": st.session_state.t16_hero_titulos,
            "descs":   st.session_state.t16_hero_descs,
            "imagens": st.session_state.t16_hero_imgs,
        },
        "sobre": {
            "titulos": st.session_state.t16_about_titulos,
            "descs":   st.session_state.t16_about_descs,
            "botoes":  st.session_state.t16_about_btns,
        },
        "expertise": {
            "titulo_secao": st.session_state.t16_exp_secao_titulos,
            "itens":        st.session_state.t16_exp_items,
        },
        "network": {
            "titulos":  st.session_state.t16_net_titulos,
            "descs":    st.session_state.t16_net_descs,
            "cidades":  st.session_state.t16_net_cities,
        },
        "footer": {
            "logos":    st.session_state.t16_foot_logos,
            "descs":    st.session_state.t16_foot_descs,
            "colunas":  st.session_state.t16_foot_cols,
            "copyright":st.session_state.t16_foot_copys,
        },
        "observacoes": st.session_state.t16_obs,
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

            st.session_state.t16_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t16_nome_cliente,
                key="t16_nome_cliente_inp", placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t16_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t16_email_cliente,
                key="t16_email_cliente_inp", placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: litiguard, advocaciasilva, legalgroup2026).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t16_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t16_nome_site,
                key="t16_nome_site_inp",
                placeholder="Ex: litiguard  →  sttacksite.streamlit.app/?c=litiguard",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t16_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t16_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t16_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t16_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t16_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t16_cores) > 1 and _del_btn(f"t16_cor_del_{i}"):
                        st.session_state.t16_cores.pop(i); st.rerun()
            if _add_btn("t16_cor_add", "＋ Adicionar cor"):
                st.session_state.t16_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. TOP BAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Barra Superior (Top Bar)</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>Destinos:</strong> descreva a seção de destino (ex: <em>seção Nossa Expertise</em>)
                ou cole um link completo.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Itens da barra  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t16_top_bar_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_top_bar_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t16_tb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do item")
                with c2:
                    st.session_state.t16_top_bar_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t16_tb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t16_top_bar_links) > 1 and _del_btn(f"t16_tb_del_{i}"):
                        st.session_state.t16_top_bar_links.pop(i); st.rerun()
            if _add_btn("t16_tb_add", "＋ Adicionar item"):
                st.session_state.t16_top_bar_links.append({"texto": "ITEM", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da empresa")
            for i, logo in enumerate(st.session_state.t16_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t16_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: LITIGUARD ou Advocacia Silva")
                with c2:
                    if len(st.session_state.t16_logos) > 1 and _del_btn(f"t16_logo_del_{i}"):
                        st.session_state.t16_logos.pop(i); st.rerun()
            if _add_btn("t16_logo_add", "＋ Adicionar logo"):
                st.session_state.t16_logos.append({"valor": "EMPRESA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t16_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t16_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t16_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t16_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t16_nav_links) > 1 and _del_btn(f"t16_nl_del_{i}"):
                        st.session_state.t16_nav_links.pop(i); st.rerun()
            if _add_btn("t16_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t16_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t16_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_h_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Protecting Your Interests")
                with c2:
                    if len(st.session_state.t16_hero_titulos) > 1 and _del_btn(f"t16_h_t_del_{i}"):
                        st.session_state.t16_hero_titulos.pop(i); st.rerun()
            if _add_btn("t16_h_t_add", "＋ Adicionar título"):
                st.session_state.t16_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que resume a proposta de valor do escritório")
                with c2:
                    if len(st.session_state.t16_hero_descs) > 1 and _del_btn(f"t16_h_d_del_{i}"):
                        st.session_state.t16_hero_descs.pop(i); st.rerun()
            if _add_btn("t16_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t16_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do Hero:</strong> cole a URL de uma foto do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho ideal: <strong>1920 × 800 px</strong>. Prefira fotos de arquitetura corporativa ou tribunal.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t16_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t16_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t16_hero_imgs) > 1 and _del_btn(f"t16_h_i_del_{i}"):
                        st.session_state.t16_hero_imgs.pop(i); st.rerun()
            if _add_btn("t16_h_i_add", "＋ Adicionar imagem de fundo"):
                st.session_state.t16_hero_imgs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. ABOUT
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Seção Sobre (About)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t16_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_about_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t16_at_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: Representação Jurídica Estratégica")
                with c2:
                    if len(st.session_state.t16_about_titulos) > 1 and _del_btn(f"t16_at_del_{i}"):
                        st.session_state.t16_about_titulos.pop(i); st.rerun()
            if _add_btn("t16_at_add", "＋ Adicionar título"):
                st.session_state.t16_about_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_ad_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva a atuação e diferencial do escritório")
                with c2:
                    if len(st.session_state.t16_about_descs) > 1 and _del_btn(f"t16_ad_del_{i}"):
                        st.session_state.t16_about_descs.pop(i); st.rerun()
            if _add_btn("t16_ad_add", "＋ Adicionar descrição"):
                st.session_state.t16_about_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t16_about_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_about_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t16_ab_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t16_about_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t16_ab_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t16_about_btns) > 1 and _del_btn(f"t16_ab_del_{i}"):
                        st.session_state.t16_about_btns.pop(i); st.rerun()
            if _add_btn("t16_ab_add", "＋ Adicionar botão"):
                st.session_state.t16_about_btns.append({"texto": "SAIBA MAIS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. EXPERTISE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚖️ Nossa Expertise (Serviços)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t16_exp_secao_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_exp_secao_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_est_{i}", label_visibility="collapsed",
                        placeholder="Ex: Nossa Expertise")
                with c2:
                    if len(st.session_state.t16_exp_secao_titulos) > 1 and _del_btn(f"t16_est_del_{i}"):
                        st.session_state.t16_exp_secao_titulos.pop(i); st.rerun()
            if _add_btn("t16_est_add", "＋ Adicionar título"):
                st.session_state.t16_exp_secao_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de serviço  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t16_exp_items):
                with st.expander(f"Serviço {i+1}: {item['titulo']}"):
                    st.session_state.t16_exp_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t16_ei_t_{i}",
                        placeholder="Ex: Litígio Comercial")
                    st.session_state.t16_exp_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t16_ei_d_{i}", height=80,
                        placeholder="Descreva este serviço em 1 a 2 frases")
                    st.session_state.t16_exp_items[i]["icon"] = st.text_input(
                        "Ícone / Emoji", item["icon"], key=f"t16_ei_i_{i}",
                        help="Cole um emoji para representar este serviço",
                        placeholder="Ex: ⚖️ 🏛️ 📜 🌍")
                    if len(st.session_state.t16_exp_items) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t16_ei_del_{i}"):
                            st.session_state.t16_exp_items.pop(i); st.rerun()
            if _add_btn("t16_ei_add", "＋ Adicionar serviço"):
                st.session_state.t16_exp_items.append({
                    "icon": "⚖️", "titulo": "NOVO SERVIÇO", "desc": "Descrição do serviço."
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. NETWORK
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌍 Rede Global (Network)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t16_net_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_nt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Presença Global")
                with c2:
                    if len(st.session_state.t16_net_titulos) > 1 and _del_btn(f"t16_nt_del_{i}"):
                        st.session_state.t16_net_titulos.pop(i); st.rerun()
            if _add_btn("t16_nt_add", "＋ Adicionar título"):
                st.session_state.t16_net_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_net_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_nd_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Descreva o alcance da rede do escritório")
                with c2:
                    if len(st.session_state.t16_net_descs) > 1 and _del_btn(f"t16_nd_del_{i}"):
                        st.session_state.t16_net_descs.pop(i); st.rerun()
            if _add_btn("t16_nd_add", "＋ Adicionar descrição"):
                st.session_state.t16_net_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cidades / Escritórios da rede")
            for i, city in enumerate(st.session_state.t16_net_cities):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_cities[i]["nome"] = st.text_input(
                        "Cidade", city["nome"], key=f"t16_nc_n_{i}", label_visibility="collapsed",
                        placeholder="Ex: SÃO PAULO")
                with c2:
                    if len(st.session_state.t16_net_cities) > 1 and _del_btn(f"t16_nc_del_{i}"):
                        st.session_state.t16_net_cities.pop(i); st.rerun()
            if _add_btn("t16_nc_add", "＋ Adicionar cidade"):
                st.session_state.t16_net_cities.append({"nome": "NOVA CIDADE"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t16_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t16_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: LITIGUARD ou Advocacia Silva")
                with c2:
                    if len(st.session_state.t16_foot_logos) > 1 and _del_btn(f"t16_fl_del_{i}"):
                        st.session_state.t16_foot_logos.pop(i); st.rerun()
            if _add_btn("t16_fl_add", "＋ Adicionar logo"):
                st.session_state.t16_foot_logos.append({"valor": "EMPRESA"}); st.rerun()

            st.caption("Descrição da empresa  *(texto abaixo do logo)*")
            for i, desc in enumerate(st.session_state.t16_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_descs[i]["valor"] = st.text_area(
                        "Descrição Footer", desc["valor"], key=f"t16_fd_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Breve descrição do escritório para o rodapé")
                with c2:
                    if len(st.session_state.t16_foot_descs) > 1 and _del_btn(f"t16_fd_del_{i}"):
                        st.session_state.t16_foot_descs.pop(i); st.rerun()
            if _add_btn("t16_fd_add", "＋ Adicionar descrição"):
                st.session_state.t16_foot_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Colunas de links  *(clique para expandir e editar cada uma)*")
            for i, col in enumerate(st.session_state.t16_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t16_foot_cols[i]["titulo"] = st.text_input(
                        "Título da Coluna", col["titulo"], key=f"t16_fcol_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t16_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t16_fcol_lt_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t16_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t16_fcol_lu_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou seção")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t16_fcol_ld_{i}_{j}"):
                                st.session_state.t16_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t16_fcol_la_{i}", "＋ Adicionar link"):
                        st.session_state.t16_foot_cols[i]["links"].append({"texto": "Novo Link", "url": ""}); st.rerun()
                    if len(st.session_state.t16_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t16_fcol_del_{i}"):
                            st.session_state.t16_foot_cols.pop(i); st.rerun()
            if _add_btn("t16_fcol_add", "＋ Adicionar coluna ao rodapé"):
                st.session_state.t16_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t16_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t16_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 EMPRESA. TODOS OS DIREITOS RESERVADOS.")
                with c2:
                    if len(st.session_state.t16_foot_copys) > 1 and _del_btn(f"t16_fcp_del_{i}"):
                        st.session_state.t16_foot_copys.pop(i); st.rerun()
            if _add_btn("t16_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t16_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem de fundo do Hero acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero de fundo: <strong>1920 × 800 px</strong> (arquitetura corporativa ou tribunal)<br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 10. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "mudar o dourado para bronze", "adicionar seção de depoimentos de clientes",
                "adicionar FAQ", "adicionar formulário de contato", "remover seção Network"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t16_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t16_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_obs) > 1 and _del_btn(f"t16_obs_del_{i}"):
                        st.session_state.t16_obs.pop(i); st.rerun()
            if _add_btn("t16_obs_add", "＋ Adicionar observação"):
                st.session_state.t16_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t16_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t16_email_cliente.strip() or "@" not in st.session_state.t16_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t16_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t16_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t16_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t16_nome_cliente}'*."
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
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
