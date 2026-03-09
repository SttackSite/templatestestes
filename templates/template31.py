import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img31.png"
TEMPLATE_NAME      = "Template 31 — Epiminds Style (Neurotech & AI)"
TEMPLATE_ID        = "template_31"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t31_nome_cliente":  "",
        "t31_email_cliente": "",
        "t31_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t31_cores": [
            {"nome": "Fundo (claro)",    "valor": "#F8F9FF"},
            {"nome": "Roxo (Principal)", "valor": "#6c5ce7"},
            {"nome": "Pêssego (Accent)", "valor": "#ff8a71"},
            {"nome": "Texto Escuro",     "valor": "#1A1A2E"},
            {"nome": "Texto Leve",       "valor": "#64648C"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t31_nav_logos": [{"texto": "epiminds", "ponto_cor": "#ff8a71"}],
        "t31_nav_links": [
            {"texto": "Produtos",         "url": "seção Metodologia"},
            {"texto": "Neurociência",     "url": "seção Metodologia"},
            {"texto": "Casos de Sucesso", "url": "seção Benefícios"},
            {"texto": "Sobre nós",        "url": "seção Rodapé"},
        ],
        "t31_nav_ctas": [{"texto": "Agendar Demo", "url": "https://wa.me/5511999999999"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t31_hero_tags":    [{"valor": "A NOVA ERA DA SAÚDE MENTAL"}],
        "t31_hero_titulos": [{"valor": "Sua mente é o seu maior ativo tecnológico."}],
        "t31_hero_descs":   [{"valor": "Unimos neurociência aplicada e inteligência artificial para decodificar o comportamento humano e potencializar a performance sustentável de líderes e equipes."}],
        "t31_hero_btns":    [{"texto": "QUERO CONHECER A PLATAFORMA", "url": "https://wa.me/5511999999999"}],

        # ── LOGOS (PROVA SOCIAL) ────────────────────────────────────────────
        "t31_logo_labels": [{"valor": "CONFIADO POR GIGANTES DO MERCADO"}],
        "t31_logo_items": [
            {"texto": "MICROSOFT"},
            {"texto": "AMAZON"},
            {"texto": "NUBANK"},
            {"texto": "IFood"},
            {"texto": "GOOGLE"},
        ],

        # ── METODOLOGIA ─────────────────────────────────────────────────────
        "t31_metod_headers": [{"sub": "NOSSA METODOLOGIA", "titulo": "Como hackeamos a alta performance"}],
        "t31_metod_items": [
            {"num": "01", "title": "Mapeamento",     "desc": "Utilizamos biomarcadores para entender o estado atual de estresse, foco e resiliência da sua equipe.", "link_texto": "Saiba mais", "link_url": "https://wa.me/5511999999999"},
            {"num": "02", "title": "Diagnóstico IA", "desc": "Nossa inteligência analisa padrões comportamentais e prevê riscos de burnout com até 3 meses de antecedência.", "link_texto": "Saiba mais", "link_url": "https://wa.me/5511999999999"},
            {"num": "03", "title": "Intervenção",    "desc": "Protocolos de neuroplasticidade personalizados para cada indivíduo, focados em recuperação rápida e foco profundo.", "link_texto": "Saiba mais", "link_url": "https://wa.me/5511999999999"},
        ],

        # ── BENEFÍCIOS ──────────────────────────────────────────────────────
        "t31_bene_headers":  [{"tag": "INSIGHTS EM TEMPO REAL", "titulo": "O Dashboard do cérebro."}],
        "t31_bene_content":  [{"titulo": "Decisões baseadas em dados biológicos, não em suposições.", "desc": "A plataforma integra-se às ferramentas que sua equipe já usa (Slack, Teams, Calendar) para fornecer uma camada de inteligência emocional e cognitiva."}],
        "t31_bene_list": [
            {"item": "Redução de 40% no turnover por burnout"},
            {"item": "Aumento de 25% na capacidade de foco profundo"},
            {"item": "Melhora comprovada no clima organizacional"},
        ],
        "t31_bene_btns": [{"texto": "VER TODOS OS BENEFÍCIOS", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t31_foot_brands": [{"nome": "epiminds.", "desc": "Liderando a fronteira da neurotecnologia aplicada ao trabalho no Brasil e no mundo."}],
        "t31_foot_cols": [
            {
                "titulo": "PRODUTO",
                "links": [
                    {"texto": "Plataforma IA", "url": "https://wa.me/5511999999999"},
                    {"texto": "Treinamentos",  "url": "https://wa.me/5511999999999"},
                    {"texto": "Segurança",     "url": "https://wa.me/5511999999999"},
                    {"texto": "API",           "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "RECURSOS",
                "links": [
                    {"texto": "Whitepapers", "url": "https://wa.me/5511999999999"},
                    {"texto": "Blog",        "url": "https://wa.me/5511999999999"},
                    {"texto": "Neuro-Guia",  "url": "https://wa.me/5511999999999"},
                    {"texto": "Suporte",     "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "contato@meusite.com", "url": "mailto:contato@meusite.com"},
                    {"texto": "LinkedIn",             "url": "https://linkedin.com/"},
                    {"texto": "Instagram",            "url": "https://instagram.com/"},
                ]
            }
        ],
        "t31_foot_copys": [{"valor": "© 2026 NOME DA EMPRESA."}],
        "t31_foot_legal": [
            {"texto": "POLÍTICA DE PRIVACIDADE", "url": "https://wa.me/5511999999999"},
            {"texto": "LGPD",                    "url": "https://wa.me/5511999999999"},
        ],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t31_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t31_nome_cliente,
            "email":     st.session_state.t31_email_cliente,
            "nome_site": st.session_state.t31_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t31_nome_site}",
        },
        "cores": st.session_state.t31_cores,
        "navbar": {
            "logos": st.session_state.t31_nav_logos,
            "links": st.session_state.t31_nav_links,
            "cta":   st.session_state.t31_nav_ctas,
        },
        "hero": {
            "tags":    st.session_state.t31_hero_tags,
            "titulos": st.session_state.t31_hero_titulos,
            "descs":   st.session_state.t31_hero_descs,
            "botoes":  st.session_state.t31_hero_btns,
        },
        "prova_social": {
            "labels": st.session_state.t31_logo_labels,
            "logos":  st.session_state.t31_logo_items,
        },
        "metodologia": {
            "headers": st.session_state.t31_metod_headers,
            "passos":  st.session_state.t31_metod_items,
        },
        "beneficios": {
            "headers": st.session_state.t31_bene_headers,
            "content": st.session_state.t31_bene_content,
            "lista":   st.session_state.t31_bene_list,
            "botoes":  st.session_state.t31_bene_btns,
        },
        "footer": {
            "marca":     st.session_state.t31_foot_brands,
            "colunas":   st.session_state.t31_foot_cols,
            "copyright": st.session_state.t31_foot_copys,
            "legal":     st.session_state.t31_foot_legal,
        },
        "observacoes": st.session_state.t31_obs,
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

            st.session_state.t31_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t31_nome_cliente,
                key="t31_nome_cliente_inp", placeholder="Ex: Ana Neurotech",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t31_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t31_email_cliente,
                key="t31_email_cliente_inp", placeholder="Ex: ana@epiminds.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: epiminds, neurotech, mindai).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t31_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t31_nome_site,
                key="t31_nome_site_inp",
                placeholder="Ex: epiminds  →  sttacksite.streamlit.app/?c=epiminds",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t31_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t31_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t31_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t31_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t31_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_cores) > 1 and _del_btn(f"t31_cor_del_{i}"):
                        st.session_state.t31_cores.pop(i); st.rerun()
            if _add_btn("t31_cor_add", "＋ Adicionar cor"):
                st.session_state.t31_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Logo com ponto decorativo:</strong> o nome da marca aparece seguido de um ponto colorido
                (ex: epiminds<span style="color:#ff8a71">.</span>). Escolha a cor do ponto no seletor ao lado do nome.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Logo  *(Nome da marca | Cor do ponto)*")
            for i, item in enumerate(st.session_state.t31_nav_logos):
                c1, c2, c3 = st.columns([6, 2, 1])
                with c1:
                    st.session_state.t31_nav_logos[i]["texto"] = st.text_input(
                        "Nome", item["texto"], key=f"t31_logo_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: epiminds ou nome da empresa")
                with c2:
                    st.session_state.t31_nav_logos[i]["ponto_cor"] = st.color_picker(
                        "Ponto", item["ponto_cor"], key=f"t31_logo_p_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t31_nav_logos) > 1 and _del_btn(f"t31_logo_del_{i}"):
                        st.session_state.t31_nav_logos.pop(i); st.rerun()
            if _add_btn("t31_logo_add", "＋ Adicionar logo"):
                st.session_state.t31_nav_logos.append({"texto": "marca", "ponto_cor": "#ff8a71"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t31_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t31_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t31_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t31_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t31_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t31_nav_links) > 1 and _del_btn(f"t31_navl_del_{i}"):
                        st.session_state.t31_nav_links.pop(i); st.rerun()
            if _add_btn("t31_navl_add", "＋ Adicionar link"):
                st.session_state.t31_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            st.caption("Botão de destaque CTA na navbar  *(Texto | URL)*")
            for i, cta in enumerate(st.session_state.t31_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t31_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t31_ncta_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Agendar Demo")
                with c2:
                    st.session_state.t31_nav_ctas[i]["url"] = st.text_input(
                        "URL", cta["url"], key=f"t31_ncta_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t31_nav_ctas) > 1 and _del_btn(f"t31_ncta_del_{i}"):
                        st.session_state.t31_nav_ctas.pop(i); st.rerun()
            if _add_btn("t31_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t31_nav_ctas.append({"texto": "DEMO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧠 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> escreva normalmente. Se quiser que parte do título apareça em
                outra cor (ex: em roxo), descreva nas Observações — ex: "quero 'ativo tecnológico' em roxo".
            </div>
            """, unsafe_allow_html=True)

            st.caption("Tag  *(pílula de texto acima do título)*")
            for i, tag in enumerate(st.session_state.t31_hero_tags):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_hero_tags[i]["valor"] = st.text_input(
                        "Tag", tag["valor"], key=f"t31_h_tag_{i}", label_visibility="collapsed",
                        placeholder="Ex: A NOVA ERA DA SAÚDE MENTAL")
                with c2:
                    if len(st.session_state.t31_hero_tags) > 1 and _del_btn(f"t31_h_tag_del_{i}"):
                        st.session_state.t31_hero_tags.pop(i); st.rerun()
            if _add_btn("t31_h_tag_add", "＋ Adicionar tag"):
                st.session_state.t31_hero_tags.append({"valor": "NOVA TAG"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t31_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t31_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Sua mente é o seu maior ativo tecnológico.")
                with c2:
                    if len(st.session_state.t31_hero_titulos) > 1 and _del_btn(f"t31_h_t_del_{i}"):
                        st.session_state.t31_hero_titulos.pop(i); st.rerun()
            if _add_btn("t31_h_t_add", "＋ Adicionar título"):
                st.session_state.t31_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t31_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t31_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva a solução em 2-3 frases.")
                with c2:
                    if len(st.session_state.t31_hero_descs) > 1 and _del_btn(f"t31_h_d_del_{i}"):
                        st.session_state.t31_hero_descs.pop(i); st.rerun()
            if _add_btn("t31_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t31_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t31_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t31_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t31_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: QUERO CONHECER A PLATAFORMA")
                with c2:
                    st.session_state.t31_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t31_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t31_hero_btns) > 1 and _del_btn(f"t31_hb_del_{i}"):
                        st.session_state.t31_hero_btns.pop(i); st.rerun()
            if _add_btn("t31_hb_add", "＋ Adicionar botão"):
                st.session_state.t31_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. LOGOS (PROVA SOCIAL)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 Prova Social (Logos em Texto)</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Logos em texto:</strong> nesta seção as marcas são exibidas como texto tipográfico.
                Se você tiver imagens de logo, solicite via Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Texto da chamada acima das logos")
            for i, l in enumerate(st.session_state.t31_logo_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_logo_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t31_ll_{i}", label_visibility="collapsed",
                        placeholder="Ex: CONFIADO POR GIGANTES DO MERCADO")
                with c2:
                    if len(st.session_state.t31_logo_labels) > 1 and _del_btn(f"t31_ll_del_{i}"):
                        st.session_state.t31_logo_labels.pop(i); st.rerun()
            if _add_btn("t31_ll_add", "＋ Adicionar label"):
                st.session_state.t31_logo_labels.append({"valor": "NOSSOS PARCEIROS"}); st.rerun()

            st.caption("Marcas/clientes  *(nome exibido em tipografia)*")
            for i, item in enumerate(st.session_state.t31_logo_items):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_logo_items[i]["texto"] = st.text_input(
                        "Marca", item["texto"], key=f"t31_li_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: MICROSOFT ou Nome do Cliente")
                with c2:
                    if len(st.session_state.t31_logo_items) > 1 and _del_btn(f"t31_li_del_{i}"):
                        st.session_state.t31_logo_items.pop(i); st.rerun()
            if _add_btn("t31_li_add", "＋ Adicionar marca"):
                st.session_state.t31_logo_items.append({"texto": "NOVA MARCA"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. METODOLOGIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚙️ Metodologia / Processo</div>', unsafe_allow_html=True)

            st.caption("Cabeçalho da seção  *(Sub-título | Título)*")
            for i, h in enumerate(st.session_state.t31_metod_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_metod_headers[i]["sub"] = st.text_input(
                        "Sub-título", h["sub"], key=f"t31_mh_s_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOSSA METODOLOGIA")
                    st.session_state.t31_metod_headers[i]["titulo"] = st.text_input(
                        "Título", h["titulo"], key=f"t31_mh_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Como entregamos resultado")
                with c2:
                    if len(st.session_state.t31_metod_headers) > 1 and _del_btn(f"t31_mh_del_{i}"):
                        st.session_state.t31_metod_headers.pop(i); st.rerun()
            if _add_btn("t31_mh_add", "＋ Adicionar cabeçalho"):
                st.session_state.t31_metod_headers.append({"sub": "SUBTÍTULO", "titulo": "Título"}); st.rerun()

            st.caption("Passos do processo  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t31_metod_items):
                with st.expander(f"Passo {i+1}: {item['title']}"):
                    st.session_state.t31_metod_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t31_mi_n_{i}",
                        placeholder="Ex: 01, 02, 03...")
                    st.session_state.t31_metod_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t31_mi_t_{i}",
                        placeholder="Ex: Diagnóstico")
                    st.session_state.t31_metod_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t31_mi_d_{i}", height=80,
                        placeholder="Descreva este passo em 2-3 frases.")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t31_metod_items[i]["link_texto"] = st.text_input(
                            "Texto do Link", item["link_texto"], key=f"t31_mi_lt_{i}",
                            placeholder="Ex: Saiba mais")
                    with c2:
                        st.session_state.t31_metod_items[i]["link_url"] = st.text_input(
                            "URL do Link", item["link_url"], key=f"t31_mi_lu_{i}",
                            placeholder="https://wa.me/... ou link")
                    if len(st.session_state.t31_metod_items) > 1:
                        if st.button("🗑 Remover este passo", key=f"t31_mi_del_{i}"):
                            st.session_state.t31_metod_items.pop(i); st.rerun()
            if _add_btn("t31_mi_add", "＋ Adicionar passo"):
                st.session_state.t31_metod_items.append({
                    "num": f"0{len(st.session_state.t31_metod_items)+1}",
                    "title": "Novo Passo", "desc": "",
                    "link_texto": "Saiba mais", "link_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. BENEFÍCIOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Benefícios e Resultados</div>', unsafe_allow_html=True)

            st.caption("Cabeçalho  *(Tag | Título do Dashboard)*")
            for i, h in enumerate(st.session_state.t31_bene_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_bene_headers[i]["tag"] = st.text_input(
                        "Tag", h["tag"], key=f"t31_bh_tg_{i}", label_visibility="collapsed",
                        placeholder="Ex: INSIGHTS EM TEMPO REAL")
                    st.session_state.t31_bene_headers[i]["titulo"] = st.text_input(
                        "Título Dashboard", h["titulo"], key=f"t31_bh_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: O Dashboard do cérebro.")
                with c2:
                    if len(st.session_state.t31_bene_headers) > 1 and _del_btn(f"t31_bh_del_{i}"):
                        st.session_state.t31_bene_headers.pop(i); st.rerun()
            if _add_btn("t31_bh_add", "＋ Adicionar cabeçalho"):
                st.session_state.t31_bene_headers.append({"tag": "TAG", "titulo": "Título"}); st.rerun()

            st.caption("Conteúdo textual  *(Título | Descrição)*")
            for i, c in enumerate(st.session_state.t31_bene_content):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_bene_content[i]["titulo"] = st.text_input(
                        "Título", c["titulo"], key=f"t31_bc_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Decisões baseadas em dados")
                    st.session_state.t31_bene_content[i]["desc"] = st.text_area(
                        "Descrição", c["desc"], key=f"t31_bc_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Detalhe o principal benefício da plataforma.")
                with c2:
                    if len(st.session_state.t31_bene_content) > 1 and _del_btn(f"t31_bc_del_{i}"):
                        st.session_state.t31_bene_content.pop(i); st.rerun()
            if _add_btn("t31_bc_add", "＋ Adicionar bloco"):
                st.session_state.t31_bene_content.append({"titulo": "Título", "desc": ""}); st.rerun()

            st.caption("Lista de benefícios  *(um por linha — sem marcador, ele é adicionado automaticamente)*")
            for i, item in enumerate(st.session_state.t31_bene_list):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_bene_list[i]["item"] = st.text_input(
                        "Benefício", item["item"], key=f"t31_bl_i_{i}", label_visibility="collapsed",
                        placeholder="Ex: Redução de 40% no turnover por burnout")
                with c2:
                    if len(st.session_state.t31_bene_list) > 1 and _del_btn(f"t31_bl_del_{i}"):
                        st.session_state.t31_bene_list.pop(i); st.rerun()
            if _add_btn("t31_bl_add", "＋ Adicionar benefício"):
                st.session_state.t31_bene_list.append({"item": ""}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t31_bene_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t31_bene_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t31_bb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VER TODOS OS BENEFÍCIOS")
                with c2:
                    st.session_state.t31_bene_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t31_bb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t31_bene_btns) > 1 and _del_btn(f"t31_bb_del_{i}"):
                        st.session_state.t31_bene_btns.pop(i); st.rerun()
            if _add_btn("t31_bb_add", "＋ Adicionar botão"):
                st.session_state.t31_bene_btns.append({"texto": "VER MAIS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Marca e descrição")
            for i, b in enumerate(st.session_state.t31_foot_brands):
                with st.expander(f"Marca: {b['nome']}"):
                    st.session_state.t31_foot_brands[i]["nome"] = st.text_input(
                        "Nome Marca", b["nome"], key=f"t31_fb_n_{i}",
                        placeholder="Ex: epiminds. ou NOME DA EMPRESA")
                    st.session_state.t31_foot_brands[i]["desc"] = st.text_area(
                        "Descrição", b["desc"], key=f"t31_fb_d_{i}", height=70,
                        placeholder="Ex: Liderando a fronteira da neurotecnologia no Brasil.")
                    if len(st.session_state.t31_foot_brands) > 1:
                        if st.button("🗑 Remover", key=f"t31_fb_del_{i}"):
                            st.session_state.t31_foot_brands.pop(i); st.rerun()
            if _add_btn("t31_fb_add", "＋ Adicionar marca"):
                st.session_state.t31_foot_brands.append({"nome": "MARCA", "desc": ""}); st.rerun()

            st.caption("Colunas de links no rodapé")
            for i, col in enumerate(st.session_state.t31_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t31_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t31_fc_t_{i}",
                        placeholder="Ex: PRODUTO ou CONTATO")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t31_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t31_fcl_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto")
                        with c2:
                            st.session_state.t31_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t31_fcl_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou mailto:")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t31_fcl_del_{i}_{j}"):
                                st.session_state.t31_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t31_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t31_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t31_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t31_fc_del_{i}"):
                            st.session_state.t31_foot_cols.pop(i); st.rerun()
            if _add_btn("t31_fc_add", "＋ Adicionar coluna"):
                st.session_state.t31_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "LINK", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t31_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t31_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DA EMPRESA.")
                with c2:
                    if len(st.session_state.t31_foot_copys) > 1 and _del_btn(f"t31_fcp_del_{i}"):
                        st.session_state.t31_foot_copys.pop(i); st.rerun()
            if _add_btn("t31_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t31_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Links legais  *(Política de Privacidade, LGPD, etc.)*")
            for i, link in enumerate(st.session_state.t31_foot_legal):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t31_foot_legal[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t31_fl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: POLÍTICA DE PRIVACIDADE")
                with c2:
                    st.session_state.t31_foot_legal[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t31_fl_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link da página")
                with c3:
                    if len(st.session_state.t31_foot_legal) > 1 and _del_btn(f"t31_fl_del_{i}"):
                        st.session_state.t31_foot_legal.pop(i); st.rerun()
            if _add_btn("t31_fl_add", "＋ Adicionar link legal"):
                st.session_state.t31_foot_legal.append({"texto": "LINK", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Este template usa design vetorial/tipográfico</strong> — o visual é construído
                com formas, gradientes, tipografia e ícones, sem depender de imagens fotográficas.<br><br>
                Se quiser adicionar imagens (mockup de plataforma, dashboard, equipe), descreva nas
                Observações — ex: "quero um mockup do app no hero".<br><br>
                Para logo: tamanho ideal <strong>200 × 60 px</strong> (PNG com fundo transparente).<br>
                Faça upload em <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                e cole a URL nas Observações.<br><br>
                ❌ <strong>Não conseguiu?</strong> Envie para <strong>sttacksite@gmail.com</strong>
                com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 9. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "usar tons mais frios e tech", "quero 'ativo tecnológico' em roxo no título",
                "adicionar seção de depoimentos", "adicionar mockup de dashboard no hero"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t31_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t31_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t31_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t31_obs) > 1 and _del_btn(f"t31_obs_del_{i}"):
                        st.session_state.t31_obs.pop(i); st.rerun()
            if _add_btn("t31_obs_add", "＋ Adicionar observação"):
                st.session_state.t31_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t31_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t31_email_cliente.strip() or "@" not in st.session_state.t31_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t31_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t31_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t31_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t31_nome_cliente}'*."
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
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
