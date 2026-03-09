import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img8.png"
TEMPLATE_NAME      = "Template 8 — Patrus Tech (Logística & Inovação)"
TEMPLATE_ID        = "template_8"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t8_nome_cliente":  "",
        "t8_email_cliente": "",
        "t8_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t8_cores": [
            {"nome": "Cor Principal (Laranja)", "valor": "#ff6b00"},
            {"nome": "Cor de Fundo (Dark)",     "valor": "#1a1a1a"},
            {"nome": "Cor de Texto Principal",  "valor": "#333333"},
            {"nome": "Cor Neutra (Gray)",       "valor": "#f4f4f4"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t8_logos": [{"valor": "PATRUS TECH"}],
        "t8_nav_links": [
            {"texto": "SOLUÇÕES",   "url": "seção Ecossistema Digital"},
            {"texto": "TECNOLOGIA", "url": "seção Diferenciais Competitivos"},
            {"texto": "TRACKING",   "url": "seção Nossas Verticais"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t8_hero_bg":      [{"valor": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1600"}],
        "t8_hero_labels":  [{"valor": "Inovação em Movimento"}],
        "t8_hero_titulos": [{"valor": "TECNOLOGIA QUE IMPULSIONA A LOGÍSTICA DO FUTURO."}],
        "t8_hero_descs":   [{"valor": "Dados em tempo real, inteligência artificial e a maior frota conectada do país."}],
        "t8_hero_btns":    [{"texto": "CONHEÇA NOSSAS SOLUÇÕES", "url": "seção Ecossistema Digital"}],

        # ── ECOSSISTEMA DIGITAL ──────────────────────────────────────────────
        "t8_eco_titulos": [{"valor": "ECOSSISTEMA DIGITAL"}],
        "t8_eco_cards": [
            {"titulo": "Telemetria Avançada", "desc": "Monitoramento em tempo real de cada unidade da frota, garantindo segurança e pontualidade.", "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=600", "btn_txt": "SAIBA MAIS", "url": "https://wa.me/5511999999999"},
            {"titulo": "IA de Roteirização",  "desc": "Algoritmos complexos que otimizam rotas para redução de custos e emissão de CO2.",         "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600", "btn_txt": "SAIBA MAIS", "url": "https://wa.me/5511999999999"},
            {"titulo": "Gestão 360°",         "desc": "Painéis de BI exclusivos para clientes com transparência total sobre a operação.",          "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600", "btn_txt": "SAIBA MAIS", "url": "https://wa.me/5511999999999"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t8_stats": [
            {"valor": "+85",  "label": "CIDADES ATENDIDAS"},
            {"valor": "3.5k", "label": "VEÍCULOS CONECTADOS"},
            {"valor": "100%", "label": "RASTREAMENTO"},
        ],

        # ── DIFERENCIAIS ────────────────────────────────────────────────────
        "t8_diff_titulos": [{"valor": "POR QUE A PATRUS TECH?"}],
        "t8_diff_items": [
            {"num": "01", "titulo": "SEGURANÇA DE DADOS",     "desc": "Infraestrutura em nuvem com criptografia de ponta a ponta."},
            {"num": "02", "titulo": "EFICIÊNCIA OPERACIONAL", "desc": "Redução comprovada de 20% no tempo de entrega via otimização digital."},
            {"num": "03", "titulo": "SUSTENTABILIDADE TECH",  "desc": "Uso de tecnologia para monitoramento e compensação de carbono."},
            {"num": "04", "titulo": "SUPORTE ESPECIALIZADO",  "desc": "Equipe de engenharia de dados disponível para integrações via API."},
        ],

        # ── VERTICAIS ───────────────────────────────────────────────────────
        "t8_vert_titulos": [{"valor": "NOSSAS VERTICAIS"}],
        "t8_vert_cards": [
            {"titulo": "LOGÍSTICA 4.0", "desc": "Sistemas integrados de gestão de armazém e transporte.", "btn_txt": "VER SOLUÇÃO", "url": "https://wa.me/5511999999999", "destaque": False},
            {"titulo": "API CONNECT",   "desc": "Integração direta com o seu ERP para automação total.",  "btn_txt": "VER SOLUÇÃO", "url": "https://wa.me/5511999999999", "destaque": True},
            {"titulo": "BI ANALYTICS",  "desc": "Decisões baseadas em dados históricos e preditivos.",    "btn_txt": "VER SOLUÇÃO", "url": "https://wa.me/5511999999999", "destaque": False},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t8_footer_logos": [{"valor": "PATRUS TECH"}],
        "t8_footer_copys": [{"valor": "© 2026 Patrus Transportes. Inovação em cada quilômetro."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t8_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t8_nome_cliente,
            "email":     st.session_state.t8_email_cliente,
            "nome_site": st.session_state.t8_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t8_nome_site}",
        },
        "cores": st.session_state.t8_cores,
        "navbar": {
            "logos": st.session_state.t8_logos,
            "links": st.session_state.t8_nav_links,
        },
        "hero": {
            "bg":      st.session_state.t8_hero_bg,
            "labels":  st.session_state.t8_hero_labels,
            "titulos": st.session_state.t8_hero_titulos,
            "descs":   st.session_state.t8_hero_descs,
            "botoes":  st.session_state.t8_hero_btns,
        },
        "ecossistema": {
            "titulos": st.session_state.t8_eco_titulos,
            "cards":   st.session_state.t8_eco_cards,
        },
        "estatisticas": st.session_state.t8_stats,
        "diferenciais": {
            "titulos": st.session_state.t8_diff_titulos,
            "itens":   st.session_state.t8_diff_items,
        },
        "verticais": {
            "titulos": st.session_state.t8_vert_titulos,
            "cards":   st.session_state.t8_vert_cards,
        },
        "footer": {
            "logos":     st.session_state.t8_footer_logos,
            "copyright": st.session_state.t8_footer_copys,
        },
        "observacoes": st.session_state.t8_obs,
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

            st.session_state.t8_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t8_nome_cliente,
                key="t8_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t8_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t8_email_cliente,
                key="t8_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: patrustech, logistica2026, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t8_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t8_nome_site,
                key="t8_nome_site_inp",
                placeholder="Ex: patrustech  →  sttacksite.streamlit.app/?c=patrustech",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t8_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t8_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t8_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t8_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t8_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t8_cores) > 1 and _del_btn(f"t8_cor_del_{i}"):
                        st.session_state.t8_cores.pop(i); st.rerun()
            if _add_btn("t8_cor_add", "＋ Adicionar cor"):
                st.session_state.t8_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t8_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t8_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: MINHA EMPRESA")
                with c2:
                    if len(st.session_state.t8_logos) > 1 and _del_btn(f"t8_logo_del_{i}"):
                        st.session_state.t8_logos.pop(i); st.rerun()
            if _add_btn("t8_logo_add", "＋ Adicionar logo"):
                st.session_state.t8_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), qualquer link — ou simplesmente descrever
                para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t8_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t8_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t8_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t8_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t8_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t8_nav_links) > 1 and _del_btn(f"t8_nl_del_{i}"):
                        st.session_state.t8_nav_links.pop(i); st.rerun()
            if _add_btn("t8_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t8_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚛 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do Hero:</strong> cole a URL de uma imagem do
                <a href="https://imgur.com" target="_blank">imgur.com</a> (termina em .jpg, .png etc.).
                Tamanho ideal: <strong>1920 × 800 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL da imagem)*")
            for i, bg in enumerate(st.session_state.t8_hero_bg):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_hero_bg[i]["valor"] = st.text_input(
                        "Imagem de fundo", bg["valor"], key=f"t8_h_bg_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t8_hero_bg) > 1 and _del_btn(f"t8_h_bg_del_{i}"):
                        st.session_state.t8_hero_bg.pop(i); st.rerun()

            st.caption("Label  *(texto pequeno acima do título)*")
            for i, label in enumerate(st.session_state.t8_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t8_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Inovação em Movimento")
                with c2:
                    if len(st.session_state.t8_hero_labels) > 1 and _del_btn(f"t8_h_l_del_{i}"):
                        st.session_state.t8_hero_labels.pop(i); st.rerun()
            if _add_btn("t8_h_l_add", "＋ Adicionar label"):
                st.session_state.t8_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título  *(para destacar palavras em laranja, descreva nas Observações)*")
            for i, t in enumerate(st.session_state.t8_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t8_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Título principal em maiúsculas")
                with c2:
                    if len(st.session_state.t8_hero_titulos) > 1 and _del_btn(f"t8_h_t_del_{i}"):
                        st.session_state.t8_hero_titulos.pop(i); st.rerun()
            if _add_btn("t8_h_t_add", "＋ Adicionar título"):
                st.session_state.t8_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t8_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t8_h_d_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Frase que resume sua proposta de valor")
                with c2:
                    if len(st.session_state.t8_hero_descs) > 1 and _del_btn(f"t8_h_d_del_{i}"):
                        st.session_state.t8_hero_descs.pop(i); st.rerun()
            if _add_btn("t8_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t8_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botões  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t8_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t8_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t8_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t8_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t8_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t8_hero_btns) > 1 and _del_btn(f"t8_hb_del_{i}"):
                        st.session_state.t8_hero_btns.pop(i); st.rerun()
            if _add_btn("t8_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t8_hero_btns.append({"texto": "BOTÃO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. ECOSSISTEMA DIGITAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌐 Ecossistema Digital</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(para destacar palavra em laranja, use Observações)*")
            for i, t in enumerate(st.session_state.t8_eco_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_eco_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t8_et_{i}", label_visibility="collapsed",
                        placeholder="Ex: ECOSSISTEMA DIGITAL")
                with c2:
                    if len(st.session_state.t8_eco_titulos) > 1 and _del_btn(f"t8_et_del_{i}"):
                        st.session_state.t8_eco_titulos.pop(i); st.rerun()
            if _add_btn("t8_et_add", "＋ Adicionar título"):
                st.session_state.t8_eco_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos cards:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>600 × 400 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de tecnologia  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t8_eco_cards):
                with st.expander(f"Tecnologia {i+1}: {card['titulo']}"):
                    st.session_state.t8_eco_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t8_ec_t_{i}")
                    st.session_state.t8_eco_cards[i]["img"] = st.text_input(
                        "URL da Imagem", card["img"], key=f"t8_ec_i_{i}",
                        placeholder="https://i.imgur.com/... ou deixe vazio",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t8_eco_cards[i]["desc"] = st.text_area(
                        "Descrição", card["desc"], key=f"t8_ec_d_{i}", height=70,
                        placeholder="Descreva esta tecnologia ou serviço")
                    st.session_state.t8_eco_cards[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", card["btn_txt"], key=f"t8_ec_bt_{i}")
                    st.session_state.t8_eco_cards[i]["url"] = st.text_input(
                        "URL do Botão", card["url"], key=f"t8_ec_u_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t8_eco_cards) > 1:
                        if st.button("🗑 Remover este card", key=f"t8_ec_del_{i}"):
                            st.session_state.t8_eco_cards.pop(i); st.rerun()
            if _add_btn("t8_ec_add", "＋ Adicionar card de tecnologia"):
                st.session_state.t8_eco_cards.append({
                    "titulo": "Nova Tecnologia", "desc": "Descrição da tecnologia.",
                    "img": "", "btn_txt": "SAIBA MAIS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas Operacionais</div>', unsafe_allow_html=True)
            st.caption("Valor | Descrição  *(ex: +85 cidades atendidas)*")
            for i, stat in enumerate(st.session_state.t8_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t8_stats[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t8_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: +85")
                with c2:
                    st.session_state.t8_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t8_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: CIDADES ATENDIDAS")
                with c3:
                    if len(st.session_state.t8_stats) > 1 and _del_btn(f"t8_st_del_{i}"):
                        st.session_state.t8_stats.pop(i); st.rerun()
            if _add_btn("t8_st_add", "＋ Adicionar estatística"):
                st.session_state.t8_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. DIFERENCIAIS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏆 Diferenciais Competitivos</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t8_diff_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_diff_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t8_dt_{i}", label_visibility="collapsed",
                        placeholder="Ex: POR QUE ESCOLHER A GENTE?")
                with c2:
                    if len(st.session_state.t8_diff_titulos) > 1 and _del_btn(f"t8_dt_del_{i}"):
                        st.session_state.t8_diff_titulos.pop(i); st.rerun()
            if _add_btn("t8_dt_add", "＋ Adicionar título"):
                st.session_state.t8_diff_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Itens  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t8_diff_items):
                with st.expander(f"Diferencial {item['num']}: {item['titulo']}"):
                    st.session_state.t8_diff_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t8_di_n_{i}",
                        placeholder="Ex: 01, 02...")
                    st.session_state.t8_diff_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t8_di_t_{i}")
                    st.session_state.t8_diff_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t8_di_d_{i}", height=70,
                        placeholder="Explique este diferencial brevemente")
                    if len(st.session_state.t8_diff_items) > 1:
                        if st.button("🗑 Remover este diferencial", key=f"t8_di_del_{i}"):
                            st.session_state.t8_diff_items.pop(i); st.rerun()
            if _add_btn("t8_di_add", "＋ Adicionar diferencial"):
                st.session_state.t8_diff_items.append({"num": "05", "titulo": "Novo Diferencial", "desc": "Descrição do diferencial."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. VERTICAIS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛣️ Verticais / Serviços</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t8_vert_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_vert_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t8_vt_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOSSAS VERTICAIS ou SERVIÇOS")
                with c2:
                    if len(st.session_state.t8_vert_titulos) > 1 and _del_btn(f"t8_vt_del_{i}"):
                        st.session_state.t8_vert_titulos.pop(i); st.rerun()
            if _add_btn("t8_vt_add", "＋ Adicionar título"):
                st.session_state.t8_vert_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t8_vert_cards):
                with st.expander(f"Vertical {i+1}: {card['titulo']}"):
                    st.session_state.t8_vert_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t8_vc_t_{i}")
                    st.session_state.t8_vert_cards[i]["desc"] = st.text_area(
                        "Descrição", card["desc"], key=f"t8_vc_d_{i}", height=70,
                        placeholder="Descreva este serviço ou solução")
                    st.session_state.t8_vert_cards[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", card["btn_txt"], key=f"t8_vc_bt_{i}")
                    st.session_state.t8_vert_cards[i]["url"] = st.text_input(
                        "URL do Botão", card["url"], key=f"t8_vc_u_{i}",
                        placeholder="https:// ou seção de destino")
                    st.session_state.t8_vert_cards[i]["destaque"] = st.checkbox(
                        "Destaque (borda laranja — serviço em evidência)", value=card["destaque"], key=f"t8_vc_dt_{i}")
                    if len(st.session_state.t8_vert_cards) > 1:
                        if st.button("🗑 Remover esta vertical", key=f"t8_vc_del_{i}"):
                            st.session_state.t8_vert_cards.pop(i); st.rerun()
            if _add_btn("t8_vc_add", "＋ Adicionar vertical"):
                st.session_state.t8_vert_cards.append({
                    "titulo": "Nova Vertical", "desc": "Descrição da vertical.",
                    "btn_txt": "VER SOLUÇÃO", "url": "", "destaque": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t8_footer_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_footer_logos[i]["valor"] = st.text_input(
                        "Logo Rodapé", logo["valor"], key=f"t8_flogo_{i}", label_visibility="collapsed",
                        placeholder="Ex: MINHA EMPRESA")
                with c2:
                    if len(st.session_state.t8_footer_logos) > 1 and _del_btn(f"t8_flogo_del_{i}"):
                        st.session_state.t8_footer_logos.pop(i); st.rerun()
            if _add_btn("t8_flogo_add", "＋ Adicionar logo ao rodapé"):
                st.session_state.t8_footer_logos.append({"valor": "NOVA LOGO"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t8_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_footer_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t8_fcopy_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t8_footer_copys) > 1 and _del_btn(f"t8_fcopy_del_{i}"):
                        st.session_state.t8_footer_copys.pop(i); st.rerun()
            if _add_btn("t8_fcopy_add", "＋ Adicionar linha de copyright"):
                st.session_state.t8_footer_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo correspondente (Hero ou cards do Ecossistema acima).<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero de fundo: <strong>1920 × 800 px</strong><br>
                • Cards do Ecossistema: <strong>600 × 400 px</strong><br>
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
                Ex: "quero mudar a fonte", "destacar palavra X em laranja no título", "adicionar FAQ",
                "colocar vídeo do YouTube", "remover a seção Y", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t8_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t8_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t8_obs) > 1 and _del_btn(f"t8_obs_del_{i}"):
                        st.session_state.t8_obs.pop(i); st.rerun()
            if _add_btn("t8_obs_add", "＋ Adicionar observação"):
                st.session_state.t8_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t8_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t8_email_cliente.strip() or "@" not in st.session_state.t8_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t8_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t8_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t8_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t8_nome_cliente}'*."
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
