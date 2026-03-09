import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img30.png"
TEMPLATE_NAME      = "Template 30 — FORZY Pro Style (Performance & Design)"
TEMPLATE_ID        = "template_30"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t30_nome_cliente":  "",
        "t30_email_cliente": "",
        "t30_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t30_cores": [
            {"nome": "Preto (Principal)",   "valor": "#000000"},
            {"nome": "Branco",              "valor": "#ffffff"},
            {"nome": "Cinza Claro",         "valor": "#f5f5f7"},
            {"nome": "Cinza Médio",         "valor": "#e8e8ed"},
            {"nome": "Texto Secundário",    "valor": "#86868b"},
            {"nome": "Destaque (Accent)",   "valor": "#0066cc"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t30_nav_logos": [{"texto": "FORZY"}],
        "t30_nav_links": [
            {"texto": "SOLUÇÕES",    "url": "seção Serviços",  "active": False},
            {"texto": "ECOSSISTEMA", "url": "seção Serviços",  "active": False},
            {"texto": "RESULTADOS",  "url": "seção Impacto",   "active": False},
            {"texto": "CONTATO",     "url": "seção Rodapé",    "active": True},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t30_hero_labels":  [{"valor": "Performance & Design"}],
        "t30_hero_titulos": [{"valor": "Design que vende. Tecnologia que escala."}],
        "t30_hero_descs":   [{"valor": "Uma consultoria estratégica focada em criar produtos digitais que dominam mercados. Não fazemos apenas sites; construímos ativos de alta performance."}],
        "t30_hero_btns":    [{"texto": "VAMOS CONSTRUIR ALGO NOVO?", "url": "https://wa.me/5511999999999"}],

        # ── SHOWCASE IMAGE ───────────────────────────────────────────────────
        "t30_showcase_imgs": [{"url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600"}],

        # ── SERVIÇOS ────────────────────────────────────────────────────────
        "t30_serv_labels": [{"valor": "O que fazemos"}],
        "t30_serv_items": [
            {"num": "01", "title": "Identidade Visual e Branding",    "desc": "Construímos marcas que são impossíveis de ignorar, unindo psicologia e estética.",                                        "url": "https://wa.me/5511999999999"},
            {"num": "02", "title": "Desenvolvimento Web e Mobile",    "desc": "Sistemas robustos com as tecnologias mais rápidas do mundo para garantir 99.9% de uptime.",                              "url": "https://wa.me/5511999999999"},
            {"num": "03", "title": "Growth Marketing",                "desc": "Estratégias de aquisição baseadas em dados para escalar o seu faturamento de forma previsível.",                         "url": "https://wa.me/5511999999999"},
        ],

        # ── IMPACTO ─────────────────────────────────────────────────────────
        "t30_impact_texts": [{"valor": "A simplicidade é o último grau de sofisticação. Eliminamos o ruído para que sua mensagem brilhe."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t30_foot_titles": [{"valor": "Pronto para elevar o padrão do seu negócio?"}],
        "t30_foot_brands": [{"nome": "FORZY", "desc": "Transformando ideias em interfaces de alto impacto desde 2018."}],
        "t30_foot_cols": [
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "hello@meusite.com.br",   "url": "mailto:hello@meusite.com.br"},
                    {"texto": "+55 11 99999-9999",       "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "FOLLOW",
                "links": [
                    {"texto": "Instagram", "url": "https://instagram.com/"},
                    {"texto": "LinkedIn",  "url": "https://linkedin.com/"},
                    {"texto": "Behance",   "url": "https://behance.net/"},
                ]
            }
        ],
        "t30_foot_copys": [{"valor": "© 2026 NOME DA EMPRESA. TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t30_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t30_nome_cliente,
            "email":     st.session_state.t30_email_cliente,
            "nome_site": st.session_state.t30_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t30_nome_site}",
        },
        "cores": st.session_state.t30_cores,
        "navbar": {
            "logos": st.session_state.t30_nav_logos,
            "links": st.session_state.t30_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t30_hero_labels,
            "titulos": st.session_state.t30_hero_titulos,
            "descs":   st.session_state.t30_hero_descs,
            "botoes":  st.session_state.t30_hero_btns,
        },
        "showcase": st.session_state.t30_showcase_imgs,
        "servicos": {
            "labels": st.session_state.t30_serv_labels,
            "items":  st.session_state.t30_serv_items,
        },
        "impacto": st.session_state.t30_impact_texts,
        "footer": {
            "titulos":   st.session_state.t30_foot_titles,
            "marca":     st.session_state.t30_foot_brands,
            "colunas":   st.session_state.t30_foot_cols,
            "copyright": st.session_state.t30_foot_copys,
        },
        "observacoes": st.session_state.t30_obs,
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

            st.session_state.t30_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t30_nome_cliente,
                key="t30_nome_cliente_inp", placeholder="Ex: Lucas Forzy",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t30_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t30_email_cliente,
                key="t30_email_cliente_inp", placeholder="Ex: lucas@minhaagencia.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: forzy, minhaagencia, designpro).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t30_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t30_nome_site,
                key="t30_nome_site_inp",
                placeholder="Ex: forzy  →  sttacksite.streamlit.app/?c=forzy",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🖤 <strong>Template minimalista:</strong> a paleta padrão é preto e branco com cinzas.
                O campo "Destaque (Accent)" define a cor dos links e elementos interativos.
                Você pode trocar o azul por qualquer cor da sua marca.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t30_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t30_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t30_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t30_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t30_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t30_cores) > 1 and _del_btn(f"t30_cor_del_{i}"):
                        st.session_state.t30_cores.pop(i); st.rerun()
            if _add_btn("t30_cor_add", "＋ Adicionar cor"):
                st.session_state.t30_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(aparece no canto esquerdo — CAIXA ALTA para estilo agência)*")
            for i, item in enumerate(st.session_state.t30_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_nav_logos[i]["texto"] = st.text_input(
                        "Nome", item["texto"], key=f"t30_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: FORZY ou NOME DA AGÊNCIA")
                with c2:
                    if len(st.session_state.t30_nav_logos) > 1 and _del_btn(f"t30_logo_del_{i}"):
                        st.session_state.t30_nav_logos.pop(i); st.rerun()
            if _add_btn("t30_logo_add", "＋ Adicionar logo"):
                st.session_state.t30_nav_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino | Ativo?)*")
            for i, link in enumerate(st.session_state.t30_nav_links):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t30_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t30_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t30_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t30_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    st.session_state.t30_nav_links[i]["active"] = st.checkbox(
                        "Ativo", link.get("active", False), key=f"t30_navl_a_{i}",
                        help="Marque para destacar este link como botão CTA na navbar.")
                with c4:
                    if len(st.session_state.t30_nav_links) > 1 and _del_btn(f"t30_navl_del_{i}"):
                        st.session_state.t30_nav_links.pop(i); st.rerun()
            if _add_btn("t30_navl_add", "＋ Adicionar link"):
                st.session_state.t30_nav_links.append({"texto": "LINK", "url": "seção de destino", "active": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> escreva o texto normalmente.
                Se quiser quebrar o título em duas linhas em pontos específicos, descreva nas Observações —
                ex: "quero quebra de linha após 'vende.'".
            </div>
            """, unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno em cinza acima do título)*")
            for i, l in enumerate(st.session_state.t30_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t30_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Performance & Design")
                with c2:
                    if len(st.session_state.t30_hero_labels) > 1 and _del_btn(f"t30_h_l_del_{i}"):
                        st.session_state.t30_hero_labels.pop(i); st.rerun()
            if _add_btn("t30_h_l_add", "＋ Adicionar label"):
                st.session_state.t30_hero_labels.append({"valor": "Novo label"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t30_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t30_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: Design que vende. Tecnologia que escala.")
                with c2:
                    if len(st.session_state.t30_hero_titulos) > 1 and _del_btn(f"t30_h_t_del_{i}"):
                        st.session_state.t30_hero_titulos.pop(i); st.rerun()
            if _add_btn("t30_h_t_add", "＋ Adicionar título"):
                st.session_state.t30_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t30_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t30_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva sua proposta de valor em 2-3 frases.")
                with c2:
                    if len(st.session_state.t30_hero_descs) > 1 and _del_btn(f"t30_h_d_del_{i}"):
                        st.session_state.t30_hero_descs.pop(i); st.rerun()
            if _add_btn("t30_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t30_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t30_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t30_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t30_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VAMOS CONSTRUIR ALGO NOVO?")
                with c2:
                    st.session_state.t30_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t30_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t30_hero_btns) > 1 and _del_btn(f"t30_hb_del_{i}"):
                        st.session_state.t30_hero_btns.pop(i); st.rerun()
            if _add_btn("t30_hb_add", "＋ Adicionar botão"):
                st.session_state.t30_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. SHOWCASE IMAGE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagem Showcase</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem showcase:</strong> aparece em largura total entre o hero e os serviços.
                Tamanho ideal: <strong>1600 × 700 px</strong> (paisagem larga).
                Use uma imagem de dashboard, projeto, equipe ou portfólio em tons neutros.<br>
                Faça upload em <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                → botão direito → copiar endereço da imagem → cole abaixo.
            </div>
            """, unsafe_allow_html=True)
            st.caption("URL da imagem larga  *(formato paisagem, tons neutros)*")
            for i, img in enumerate(st.session_state.t30_showcase_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_showcase_imgs[i]["url"] = st.text_input(
                        "URL", img["url"], key=f"t30_show_u_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t30_showcase_imgs) > 1 and _del_btn(f"t30_show_del_{i}"):
                        st.session_state.t30_showcase_imgs.pop(i); st.rerun()
            if _add_btn("t30_show_add", "＋ Adicionar imagem"):
                st.session_state.t30_showcase_imgs.append({"url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Serviços</div>', unsafe_allow_html=True)

            st.caption("Label da seção  *(texto pequeno cinza acima dos cards)*")
            for i, l in enumerate(st.session_state.t30_serv_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_serv_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t30_sl_{i}", label_visibility="collapsed",
                        placeholder="Ex: O que fazemos")
                with c2:
                    if len(st.session_state.t30_serv_labels) > 1 and _del_btn(f"t30_sl_del_{i}"):
                        st.session_state.t30_serv_labels.pop(i); st.rerun()
            if _add_btn("t30_sl_add", "＋ Adicionar label"):
                st.session_state.t30_serv_labels.append({"valor": "O que fazemos"}); st.rerun()

            st.caption("Cards de serviço  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t30_serv_items):
                with st.expander(f"Serviço {i+1}: {item['title']}"):
                    st.session_state.t30_serv_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t30_serv_n_{i}",
                        placeholder="Ex: 01, 02, 03...")
                    st.session_state.t30_serv_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t30_serv_t_{i}",
                        placeholder="Ex: Identidade Visual e Branding")
                    st.session_state.t30_serv_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t30_serv_d_{i}", height=80,
                        placeholder="Descreva este serviço em 1-2 frases de forma objetiva.")
                    st.session_state.t30_serv_items[i]["url"] = st.text_input(
                        "URL ao clicar", item["url"], key=f"t30_serv_u_{i}",
                        placeholder="https://wa.me/... ou link de detalhes")
                    if len(st.session_state.t30_serv_items) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t30_serv_del_{i}"):
                            st.session_state.t30_serv_items.pop(i); st.rerun()
            if _add_btn("t30_serv_add_item", "＋ Adicionar serviço"):
                st.session_state.t30_serv_items.append({
                    "num": f"0{len(st.session_state.t30_serv_items)+1}",
                    "title": "Novo Serviço", "desc": "", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. IMPACTO — FRASE DE DESTAQUE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Frase de Impacto</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💬 Esta seção exibe uma frase grande em destaque — uma citação ou manifesto da sua marca.
                Escreva sem aspas; a equipe aplica o estilo tipográfico correto.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Citação ou manifesto da marca")
            for i, t in enumerate(st.session_state.t30_impact_texts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_impact_texts[i]["valor"] = st.text_area(
                        "Citação", t["valor"], key=f"t30_it_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: A simplicidade é o último grau de sofisticação.")
                with c2:
                    if len(st.session_state.t30_impact_texts) > 1 and _del_btn(f"t30_it_del_{i}"):
                        st.session_state.t30_impact_texts.pop(i); st.rerun()
            if _add_btn("t30_it_add", "＋ Adicionar citação"):
                st.session_state.t30_impact_texts.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Título grande do rodapé  *(chamada de ação final)*")
            for i, t in enumerate(st.session_state.t30_foot_titles):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_foot_titles[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t30_ft_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pronto para elevar o padrão do seu negócio?")
                with c2:
                    if len(st.session_state.t30_foot_titles) > 1 and _del_btn(f"t30_ft_del_{i}"):
                        st.session_state.t30_foot_titles.pop(i); st.rerun()
            if _add_btn("t30_ft_add", "＋ Adicionar título"):
                st.session_state.t30_foot_titles.append({"valor": "Pronto?"}); st.rerun()

            st.caption("Marca e descrição  *(nome + frase sobre a empresa)*")
            for i, b in enumerate(st.session_state.t30_foot_brands):
                with st.expander(f"Marca: {b['nome']}"):
                    st.session_state.t30_foot_brands[i]["nome"] = st.text_input(
                        "Nome Marca", b["nome"], key=f"t30_fb_n_{i}",
                        placeholder="Ex: FORZY ou NOME DA EMPRESA")
                    st.session_state.t30_foot_brands[i]["desc"] = st.text_area(
                        "Descrição", b["desc"], key=f"t30_fb_d_{i}", height=70,
                        placeholder="Ex: Transformando ideias em interfaces de alto impacto desde 2020.")
                    if len(st.session_state.t30_foot_brands) > 1:
                        if st.button("🗑 Remover", key=f"t30_fb_del_{i}"):
                            st.session_state.t30_foot_brands.pop(i); st.rerun()
            if _add_btn("t30_fb_add", "＋ Adicionar marca"):
                st.session_state.t30_foot_brands.append({"nome": "MARCA", "desc": ""}); st.rerun()

            st.caption("Colunas de links no rodapé  *(ex: Contato | Redes Sociais)*")
            for i, col in enumerate(st.session_state.t30_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t30_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t30_fc_t_{i}",
                        placeholder="Ex: CONTATO ou FOLLOW")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t30_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t30_fcl_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t30_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t30_fcl_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou mailto:")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t30_fcl_del_{i}_{j}"):
                                st.session_state.t30_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t30_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t30_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t30_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t30_fc_del_{i}"):
                            st.session_state.t30_foot_cols.pop(i); st.rerun()
            if _add_btn("t30_fc_add", "＋ Adicionar coluna"):
                st.session_state.t30_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "LINK", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t30_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t30_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DA EMPRESA. TODOS OS DIREITOS RESERVADOS.")
                with c2:
                    if len(st.session_state.t30_foot_copys) > 1 and _del_btn(f"t30_fcp_del_{i}"):
                        st.session_state.t30_foot_copys.pop(i); st.rerun()
            if _add_btn("t30_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t30_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS — GUIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📐 Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Tamanhos recomendados:</strong><br>
                • Showcase (faixa larga): <strong>1600 × 700 px</strong> (paisagem, tons neutros ou cinza)<br>
                • Logo: <strong>200 × 60 px</strong> (PNG com fundo transparente, preferencialmente escuro)<br><br>
                <strong>Como subir imagens:</strong><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a> (gratuito, sem cadastro).<br>
                2. Faça upload → botão direito na imagem → <em>Copiar endereço da imagem</em>.<br>
                3. Cole no campo correspondente acima.<br><br>
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
                Ex: "manter estética minimalista", "quero quebra de linha no título após 'vende.'",
                "adicionar seção de cases/portfólio", "adicionar e-mail no rodapé com mailto:"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t30_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t30_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_obs) > 1 and _del_btn(f"t30_obs_del_{i}"):
                        st.session_state.t30_obs.pop(i); st.rerun()
            if _add_btn("t30_obs_add", "＋ Adicionar observação"):
                st.session_state.t30_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t30_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t30_email_cliente.strip() or "@" not in st.session_state.t30_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t30_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t30_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t30_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t30_nome_cliente}'*."
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
        page_icon="🔥",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
