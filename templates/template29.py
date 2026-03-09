import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img29.png"
TEMPLATE_NAME      = "Template 29 — Website Sustentável Style (Eco-Design & Tech)"
TEMPLATE_ID        = "template_29"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t29_nome_cliente":  "",
        "t29_email_cliente": "",
        "t29_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t29_cores": [
            {"nome": "Verde Eco (Principal)", "valor": "#2d5a27"},
            {"nome": "Fundo Eco (Light)",      "valor": "#f0f4ef"},
            {"nome": "Destaque Eco (Accent)",  "valor": "#8eb486"},
            {"nome": "Escuro Eco (Dark)",      "valor": "#1a2e19"},
            {"nome": "Texto Gray",             "valor": "#4a4a4a"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t29_nav_logos": [{"emoji": "🌿", "texto": "Website Sustentável"}],
        "t29_nav_links": [
            {"texto": "Manifesto",    "url": "seção Diferenciais", "active": False},
            {"texto": "Certificação", "url": "seção Impacto",      "active": False},
            {"texto": "Tecnologia",   "url": "seção Diferenciais", "active": False},
            {"texto": "CONTATO",      "url": "seção Rodapé",       "active": True},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t29_hero_badges":  [{"valor": "Otimizado para baixo consumo"}],
        "t29_hero_titulos": [{"valor": "Seu site pode ser mais rápido e menos poluente."}],
        "t29_hero_descs":   [{"valor": "Desenvolvemos tecnologias web focadas em performance extrema e responsabilidade ambiental. O futuro da internet é sustentável."}],
        "t29_hero_btns":    [{"texto": "CERTIFIQUE SEU WEBSITE", "url": "https://wa.me/5511999999999"}],

        # ── DIFERENCIAIS ────────────────────────────────────────────────────
        "t29_diff_titulos": [{"valor": "Por que ser sustentável?"}],
        "t29_diff_items": [
            {"icon": "🍃", "title": "Baixa Emissão",  "desc": "Reduzimos o tamanho dos arquivos e a requisição de servidores, diminuindo a pegada de carbono de cada acesso.", "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
            {"icon": "🔍", "title": "SEO Consciente", "desc": "Sites mais leves carregam instantaneamente, o que o Google ama. Sustentabilidade é a melhor estratégia de ranking.", "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
            {"icon": "🔋", "title": "Green Hosting",  "desc": "Hospedagem em servidores alimentados por fontes de energia 100% renováveis e limpas.", "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── IMPACTO (STATS) ─────────────────────────────────────────────────
        "t29_stat_items": [
            {"valor": "-40%", "label": "NA EMISSÃO DE CO2", "cor": "#8eb486"},
            {"valor": "2.5x", "label": "MAIS VELOCIDADE",   "cor": "#8eb486"},
            {"valor": "100%", "label": "ENERGIA LIMPA",     "cor": "#8eb486"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t29_cta_titulos": [{"valor": "Pronto para o próximo passo?"}],
        "t29_cta_descs":   [{"valor": "Seja parte da mudança positiva no ecossistema digital."}],
        "t29_cta_btns":    [{"texto": "SOLICITAR ORÇAMENTO VERDE", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t29_foot_copys": [{"valor": "© 2026 Website Sustentável. Tecnologia com Propósito."}],
        "t29_foot_links": [
            {"texto": "Política de Privacidade", "url": "https://wa.me/5511999999999"},
            {"texto": "Eco-Design Guide",         "url": "https://wa.me/5511999999999"},
        ],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t29_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t29_nome_cliente,
            "email":     st.session_state.t29_email_cliente,
            "nome_site": st.session_state.t29_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t29_nome_site}",
        },
        "cores": st.session_state.t29_cores,
        "navbar": {
            "logos": st.session_state.t29_nav_logos,
            "links": st.session_state.t29_nav_links,
        },
        "hero": {
            "badges":  st.session_state.t29_hero_badges,
            "titulos": st.session_state.t29_hero_titulos,
            "descs":   st.session_state.t29_hero_descs,
            "botoes":  st.session_state.t29_hero_btns,
        },
        "diferenciais": {
            "titulos": st.session_state.t29_diff_titulos,
            "items":   st.session_state.t29_diff_items,
        },
        "impacto": st.session_state.t29_stat_items,
        "cta_final": {
            "titulos": st.session_state.t29_cta_titulos,
            "descs":   st.session_state.t29_cta_descs,
            "botoes":  st.session_state.t29_cta_btns,
        },
        "footer": {
            "copyright": st.session_state.t29_foot_copys,
            "links":     st.session_state.t29_foot_links,
        },
        "observacoes": st.session_state.t29_obs,
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

            st.session_state.t29_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t29_nome_cliente,
                key="t29_nome_cliente_inp", placeholder="Ex: Ana Sustentável",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t29_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t29_email_cliente,
                key="t29_email_cliente_inp", placeholder="Ex: ana@websitesustentavel.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: ecoweb, sustentavel, greentech).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t29_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t29_nome_site,
                key="t29_nome_site_inp",
                placeholder="Ex: ecoweb  →  sttacksite.streamlit.app/?c=ecoweb",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t29_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t29_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t29_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t29_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t29_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t29_cores) > 1 and _del_btn(f"t29_cor_del_{i}"):
                        st.session_state.t29_cores.pop(i); st.rerun()
            if _add_btn("t29_cor_add", "＋ Adicionar cor"):
                st.session_state.t29_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(Emoji | Nome da marca)*")
            for i, item in enumerate(st.session_state.t29_nav_logos):
                c1, c2, c3 = st.columns([2, 7, 1])
                with c1:
                    st.session_state.t29_nav_logos[i]["emoji"] = st.text_input(
                        "Emoji", item["emoji"], key=f"t29_logo_e_{i}", label_visibility="collapsed",
                        help="Um emoji que representa sua marca. Ex: 🌿 🌱 ♻️")
                with c2:
                    st.session_state.t29_nav_logos[i]["texto"] = st.text_input(
                        "Nome", item["texto"], key=f"t29_logo_t_{i}", label_visibility="collapsed",
                        placeholder="Nome da sua marca ou empresa")
                with c3:
                    if len(st.session_state.t29_nav_logos) > 1 and _del_btn(f"t29_logo_del_{i}"):
                        st.session_state.t29_nav_logos.pop(i); st.rerun()
            if _add_btn("t29_logo_add", "＋ Adicionar logo"):
                st.session_state.t29_nav_logos.append({"emoji": "🌿", "texto": "Marca"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Link Ativo:</strong> marque a caixa "Ativo" no link que deve aparecer destacado
                (geralmente o CTA de contato). Links ativos costumam ter visual de botão na navbar.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino | Ativo?)*")
            for i, link in enumerate(st.session_state.t29_nav_links):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t29_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t29_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t29_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t29_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    st.session_state.t29_nav_links[i]["active"] = st.checkbox(
                        "Ativo", link.get("active", False), key=f"t29_navl_a_{i}",
                        help="Marque para destacar este link como botão ativo na navbar.")
                with c4:
                    if len(st.session_state.t29_nav_links) > 1 and _del_btn(f"t29_navl_del_{i}"):
                        st.session_state.t29_nav_links.pop(i); st.rerun()
            if _add_btn("t29_navl_add", "＋ Adicionar link"):
                st.session_state.t29_nav_links.append({"texto": "LINK", "url": "seção de destino", "active": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌿 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título e Descrição:</strong> escreva o texto normalmente.
                Se quiser itálico em alguma palavra ou negrito, descreva na seção Observações —
                ex: "quero a palavra 'rápido' em itálico" ou "quero 'sustentável' em negrito".
            </div>
            """, unsafe_allow_html=True)

            st.caption("Badge  *(pílula verde acima do título — texto curto)*")
            for i, b in enumerate(st.session_state.t29_hero_badges):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_hero_badges[i]["valor"] = st.text_input(
                        "Badge", b["valor"], key=f"t29_h_b_{i}", label_visibility="collapsed",
                        placeholder="Ex: Otimizado para baixo consumo")
                with c2:
                    if len(st.session_state.t29_hero_badges) > 1 and _del_btn(f"t29_h_b_del_{i}"):
                        st.session_state.t29_hero_badges.pop(i); st.rerun()
            if _add_btn("t29_h_b_add", "＋ Adicionar badge"):
                st.session_state.t29_hero_badges.append({"valor": "Novo badge"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t29_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t29_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Seu site pode ser mais rápido e menos poluente.")
                with c2:
                    if len(st.session_state.t29_hero_titulos) > 1 and _del_btn(f"t29_h_t_del_{i}"):
                        st.session_state.t29_hero_titulos.pop(i); st.rerun()
            if _add_btn("t29_h_t_add", "＋ Adicionar título"):
                st.session_state.t29_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t29_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t29_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva sua proposta de valor de forma clara e inspiradora.")
                with c2:
                    if len(st.session_state.t29_hero_descs) > 1 and _del_btn(f"t29_h_d_del_{i}"):
                        st.session_state.t29_hero_descs.pop(i); st.rerun()
            if _add_btn("t29_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t29_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t29_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t29_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t29_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: CERTIFIQUE SEU WEBSITE")
                with c2:
                    st.session_state.t29_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t29_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de contato")
                with c3:
                    if len(st.session_state.t29_hero_btns) > 1 and _del_btn(f"t29_hb_del_{i}"):
                        st.session_state.t29_hero_btns.pop(i); st.rerun()
            if _add_btn("t29_hb_add", "＋ Adicionar botão"):
                st.session_state.t29_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. DIFERENCIAIS (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍃 Diferenciais (Cards)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t29_diff_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_diff_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t29_dt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Por que ser sustentável?")
                with c2:
                    if len(st.session_state.t29_diff_titulos) > 1 and _del_btn(f"t29_dt_del_{i}"):
                        st.session_state.t29_diff_titulos.pop(i); st.rerun()
            if _add_btn("t29_dt_add", "＋ Adicionar título"):
                st.session_state.t29_diff_titulos.append({"valor": "Nossos Diferenciais"}); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t29_diff_items):
                with st.expander(f"Diferencial {i+1}: {item['title']}"):
                    st.session_state.t29_diff_items[i]["icon"] = st.text_input(
                        "Ícone/Emoji", item["icon"], key=f"t29_di_i_{i}",
                        placeholder="Ex: 🍃 🔋 ♻️",
                        help="Um único emoji que represente este diferencial.")
                    st.session_state.t29_diff_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t29_di_t_{i}",
                        placeholder="Ex: Baixa Emissão")
                    st.session_state.t29_diff_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t29_di_d_{i}", height=80,
                        placeholder="Descreva este diferencial em 2-3 frases.")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t29_diff_items[i]["btn_texto"] = st.text_input(
                            "Texto Botão", item["btn_texto"], key=f"t29_di_bt_{i}",
                            placeholder="Ex: SAIBA MAIS")
                    with c2:
                        st.session_state.t29_diff_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t29_di_bu_{i}",
                            placeholder="https://wa.me/... ou link")
                    if len(st.session_state.t29_diff_items) > 1:
                        if st.button("🗑 Remover este diferencial", key=f"t29_di_del_{i}"):
                            st.session_state.t29_diff_items.pop(i); st.rerun()
            if _add_btn("t29_di_add", "＋ Adicionar diferencial"):
                st.session_state.t29_diff_items.append({
                    "icon": "🌱", "title": "Novo Diferencial", "desc": "",
                    "btn_texto": "SAIBA MAIS", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. IMPACTO (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Impacto (Estatísticas)</div>', unsafe_allow_html=True)
            st.caption("Números que mostram seu impacto  *(Valor | Rótulo | Cor)*")
            for i, stat in enumerate(st.session_state.t29_stat_items):
                c1, c2, c3, c4 = st.columns([3, 4, 2, 1])
                with c1:
                    st.session_state.t29_stat_items[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t29_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: -40%")
                with c2:
                    st.session_state.t29_stat_items[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t29_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: NA EMISSÃO DE CO2")
                with c3:
                    st.session_state.t29_stat_items[i]["cor"] = st.color_picker(
                        "Cor", stat["cor"], key=f"t29_st_c_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t29_stat_items) > 1 and _del_btn(f"t29_st_del_{i}"):
                        st.session_state.t29_stat_items.pop(i); st.rerun()
            if _add_btn("t29_st_add", "＋ Adicionar número"):
                st.session_state.t29_stat_items.append({"valor": "0%", "label": "RESULTADO", "cor": "#8eb486"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t29_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_cta_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t29_ct_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pronto para o próximo passo?")
                with c2:
                    if len(st.session_state.t29_cta_titulos) > 1 and _del_btn(f"t29_ct_t_del_{i}"):
                        st.session_state.t29_cta_titulos.pop(i); st.rerun()
            if _add_btn("t29_ct_t_add", "＋ Adicionar título"):
                st.session_state.t29_cta_titulos.append({"valor": "Pronto?"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t29_cta_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_cta_descs[i]["valor"] = st.text_input(
                        "Descrição", d["valor"], key=f"t29_ct_d_{i}", label_visibility="collapsed",
                        placeholder="Ex: Seja parte da mudança positiva no ecossistema digital.")
                with c2:
                    if len(st.session_state.t29_cta_descs) > 1 and _del_btn(f"t29_ct_d_del_{i}"):
                        st.session_state.t29_cta_descs.pop(i); st.rerun()
            if _add_btn("t29_ct_d_add", "＋ Adicionar descrição"):
                st.session_state.t29_cta_descs.append({"valor": ""}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t29_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t29_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t29_ctb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: SOLICITAR ORÇAMENTO VERDE")
                with c2:
                    st.session_state.t29_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t29_ctb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de contato")
                with c3:
                    if len(st.session_state.t29_cta_btns) > 1 and _del_btn(f"t29_ctb_del_{i}"):
                        st.session_state.t29_cta_btns.pop(i); st.rerun()
            if _add_btn("t29_ctb_add", "＋ Adicionar botão"):
                st.session_state.t29_cta_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t29_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t29_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Website Sustentável. Tecnologia com Propósito.")
                with c2:
                    if len(st.session_state.t29_foot_copys) > 1 and _del_btn(f"t29_fcp_del_{i}"):
                        st.session_state.t29_foot_copys.pop(i); st.rerun()
            if _add_btn("t29_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t29_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t29_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t29_foot_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t29_footl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Política de Privacidade")
                with c2:
                    st.session_state.t29_foot_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t29_footl_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t29_foot_links) > 1 and _del_btn(f"t29_footl_del_{i}"):
                        st.session_state.t29_foot_links.pop(i); st.rerun()
            if _add_btn("t29_footl_add", "＋ Adicionar link"):
                st.session_state.t29_foot_links.append({"texto": "LINK", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Este template usa design minimalista sem imagens de fundo</strong> — o visual é
                construído com tipografia, cores e ícones/emojis.<br><br>
                Se quiser adicionar imagens (foto de equipe, parceiros, certificados), descreva na seção
                Observações — ex: "quero uma foto da equipe na seção Diferenciais".<br><br>
                Para logo: tamanho ideal <strong>200 × 60 px</strong> (PNG com fundo transparente).<br>
                Faça upload em <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                e cole a URL nas Observações.<br><br>
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
                Ex: "usar tons ainda mais naturais", "quero a palavra 'rápido' em itálico no título",
                "adicionar seção de clientes/parceiros", "adicionar formulário de contato"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t29_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t29_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t29_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t29_obs) > 1 and _del_btn(f"t29_obs_del_{i}"):
                        st.session_state.t29_obs.pop(i); st.rerun()
            if _add_btn("t29_obs_add", "＋ Adicionar observação"):
                st.session_state.t29_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t29_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t29_email_cliente.strip() or "@" not in st.session_state.t29_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t29_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t29_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t29_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t29_nome_cliente}'*."
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
        page_icon="🌿",
        layout="wide",
        initial_sidebar_bar="collapsed",
    )
    render()
