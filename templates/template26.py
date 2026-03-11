import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img26.png"
TEMPLATE_NAME      = "Template 26 — Dockyard Social Style (Food & Drink Market)"
TEMPLATE_ID        = "template_26"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t26_nome_cliente":  "",
        "t26_email_cliente": "",
        "t26_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t26_cores": [
            {"nome": "Principal (Amarelo Dock)", "valor": "#ffcc00"},
            {"nome": "Escura (Preto Dock)",      "valor": "#111111"},
            {"nome": "Fundo (Branco Dock)",       "valor": "#f4f4f4"},
        ],

        # ── AVISO (ANNOUNCEMENT) ─────────────────────────────────────────────
        "t26_announcements": [{"valor": "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO"}],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t26_nav_logos": [{"valor": "DOCKYARD SOCIAL"}],
        "t26_nav_links": [
            {"texto": "O QUE ROLA", "url": "seção Cards de Destaque"},
            {"texto": "COMIDA",     "url": "seção Cards de Destaque"},
            {"texto": "BEBIDA",     "url": "seção Cards de Destaque"},
            {"texto": "RESERVAR",   "url": "seção Reserva"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t26_hero_titulos": [{"valor": "COMIDA DE RUA. BOAS VIBES. PARA TODOS."}],
        "t26_hero_descs":   [{"valor": "O melhor mercado de comida de rua da cidade, agora na sua tela."}],

        # ── CARDS DE DESTAQUE ────────────────────────────────────────────────
        "t26_card_items": [
            {"img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", "title": "COMIDA",  "subtitle": "10+ VENDEDORES"},
            {"img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600", "title": "BEBIDA",  "subtitle": "CRAFT BEER & COCKTAILS"},
            {"img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600", "title": "EVENTOS", "subtitle": "MÚSICA AO VIVO"},
        ],

        # ── SOBRE ───────────────────────────────────────────────────────────
        "t26_about_titulos": [{"valor": "MAIS QUE UM MERCADO."}],
        "t26_about_descs":   [{"valor": "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos. Nós apoiamos talentos locais, reduzimos o desperdício e garantimos que a única coisa quente por aqui (além da comida) seja a hospitalidade."}],

        # ── CTA (RESERVA) ────────────────────────────────────────────────────
        "t26_cta_titulos": [{"valor": "PRONTO PARA VIVER A EXPERIÊNCIA?"}],
        "t26_cta_descs":   [{"valor": "Garanta seu ingresso agora e venha fazer parte da melhor vibe da cidade."}],
        "t26_cta_btns":    [{"texto": "RESERVAR AGORA", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t26_foot_brand_names": [{"valor": "DOCKYARD."}],
        "t26_foot_addresses":   [{"valor": "AV. PAULISTA, 1000 — SÃO PAULO"}],
        "t26_foot_emails":      [{"valor": "hello@dockyardsocial.com"}],
        "t26_foot_cols": [
            {"titulo": "REDES SOCIAIS", "links": [
                {"texto": "INSTAGRAM", "url": "https://instagram.com/"},
                {"texto": "FACEBOOK",  "url": "https://facebook.com/"},
                {"texto": "TIKTOK",    "url": "https://tiktok.com/"},
            ]},
        ],
        "t26_foot_copys": [{"valor": "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t26_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t26_nome_cliente,
            "email":     st.session_state.t26_email_cliente,
            "nome_site": st.session_state.t26_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t26_nome_site}",
        },
        "cores": st.session_state.t26_cores,
        "barra_aviso": st.session_state.t26_announcements,
        "navbar": {
            "logos": st.session_state.t26_nav_logos,
            "links": st.session_state.t26_nav_links,
        },
        "hero": {
            "titulos": st.session_state.t26_hero_titulos,
            "descs":   st.session_state.t26_hero_descs,
        },
        "cards_destaque": st.session_state.t26_card_items,
        "sobre": {
            "titulos": st.session_state.t26_about_titulos,
            "descs":   st.session_state.t26_about_descs,
        },
        "cta_reserva": {
            "titulos": st.session_state.t26_cta_titulos,
            "descs":   st.session_state.t26_cta_descs,
            "botoes":  st.session_state.t26_cta_btns,
        },
        "footer": {
            "brand_names": st.session_state.t26_foot_brand_names,
            "enderecos":   st.session_state.t26_foot_addresses,
            "emails":      st.session_state.t26_foot_emails,
            "colunas":     st.session_state.t26_foot_cols,
            "copyright":   st.session_state.t26_foot_copys,
        },
        "observacoes": st.session_state.t26_obs,
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

            st.session_state.t26_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t26_nome_cliente,
                key="t26_nome_cliente_inp", placeholder="Ex: Bruno Carvalho",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t26_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t26_email_cliente,
                key="t26_email_cliente_inp", placeholder="Ex: bruno@mercado.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: dockyard, mercadostreet, foodmarket).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t26_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t26_nome_site,
                key="t26_nome_site_inp",
                placeholder="Ex: dockyard  →  sttacksite.streamlit.app/?c=dockyard",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t26_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t26_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t26_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t26_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t26_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t26_cores) > 1 and _del_btn(f"t26_cor_del_{i}"):
                        st.session_state.t26_cores.pop(i); st.rerun()
            if _add_btn("t26_cor_add", "＋ Adicionar cor"):
                st.session_state.t26_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. AVISO (ANNOUNCEMENT)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Barra de Aviso</div>', unsafe_allow_html=True)
            st.caption("Texto da faixa escura no topo — use para horários, promoções ou eventos!")
            for i, item in enumerate(st.session_state.t26_announcements):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_announcements[i]["valor"] = st.text_input(
                        "Aviso", item["valor"], key=f"t26_ann_{i}", label_visibility="collapsed",
                        placeholder="Ex: ABERTO SEX A DOM • DAS 12H ÀS 22H • ENTRADA FRANCA")
                with c2:
                    if len(st.session_state.t26_announcements) > 1 and _del_btn(f"t26_ann_del_{i}"):
                        st.session_state.t26_announcements.pop(i); st.rerun()
            if _add_btn("t26_ann_add", "＋ Adicionar aviso"):
                st.session_state.t26_announcements.append({"valor": "NOVO AVISO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome do mercado  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t26_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t26_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOME DO MERCADO")
                with c2:
                    if len(st.session_state.t26_nav_logos) > 1 and _del_btn(f"t26_logo_del_{i}"):
                        st.session_state.t26_nav_logos.pop(i); st.rerun()
            if _add_btn("t26_logo_add", "＋ Adicionar logo"):
                st.session_state.t26_nav_logos.append({"valor": "MERCADO"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t26_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t26_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t26_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t26_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t26_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t26_nav_links) > 1 and _del_btn(f"t26_nl_del_{i}"):
                        st.session_state.t26_nav_links.pop(i); st.rerun()
            if _add_btn("t26_nl_add", "＋ Adicionar link"):
                st.session_state.t26_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍔 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título em letras enormes:</strong> escreva o texto normalmente.
                Se quiser cada frase em uma linha separada, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(frase de impacto em maiúsculas)*")
            for i, t in enumerate(st.session_state.t26_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t26_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: COMIDA BOA. BOAS VIBES. PARA TODOS.")
                with c2:
                    if len(st.session_state.t26_hero_titulos) > 1 and _del_btn(f"t26_h_t_del_{i}"):
                        st.session_state.t26_hero_titulos.pop(i); st.rerun()
            if _add_btn("t26_h_t_add", "＋ Adicionar título"):
                st.session_state.t26_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Subtítulo  *(frase complementar abaixo do título)*")
            for i, d in enumerate(st.session_state.t26_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_hero_descs[i]["valor"] = st.text_area(
                        "Subtítulo", d["valor"], key=f"t26_h_d_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: O melhor mercado de comida de rua da cidade.")
                with c2:
                    if len(st.session_state.t26_hero_descs) > 1 and _del_btn(f"t26_h_d_del_{i}"):
                        st.session_state.t26_hero_descs.pop(i); st.rerun()
            if _add_btn("t26_h_d_add", "＋ Adicionar subtítulo"):
                st.session_state.t26_hero_descs.append({"valor": "Novo subtítulo."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. CARDS DE DESTAQUE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🃏 Cards de Destaque</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos cards:</strong> tamanho ideal <strong>600 × 400 px</strong>.
                Cole a URL do <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Use fotos de comida, bebida ou ambiente para cada categoria.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards principais  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t26_card_items):
                with st.expander(f"Card {i+1}: {item['title']}"):
                    st.session_state.t26_card_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t26_ci_t_{i}",
                        placeholder="Ex: COMIDA, BEBIDA ou EVENTOS")
                    st.session_state.t26_card_items[i]["subtitle"] = st.text_input(
                        "Subtítulo", item["subtitle"], key=f"t26_ci_s_{i}",
                        placeholder="Ex: 10+ VENDEDORES ou MÚSICA AO VIVO")
                    st.session_state.t26_card_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t26_ci_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Foto do card — 600×400 px ideal")
                    if len(st.session_state.t26_card_items) > 1:
                        if st.button("🗑 Remover este card", key=f"t26_ci_del_{i}"):
                            st.session_state.t26_card_items.pop(i); st.rerun()
            if _add_btn("t26_ci_add", "＋ Adicionar card"):
                st.session_state.t26_card_items.append({
                    "img": "", "title": "NOVO", "subtitle": "DESCRIÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Seção Sobre</div>', unsafe_allow_html=True)

            st.caption("Título  *(afirmação de impacto sobre o espaço)*")
            for i, t in enumerate(st.session_state.t26_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_about_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t26_at_{i}", label_visibility="collapsed",
                        placeholder="Ex: MAIS QUE UM MERCADO.")
                with c2:
                    if len(st.session_state.t26_about_titulos) > 1 and _del_btn(f"t26_at_del_{i}"):
                        st.session_state.t26_about_titulos.pop(i); st.rerun()
            if _add_btn("t26_at_add", "＋ Adicionar título"):
                st.session_state.t26_about_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Descrição  *(história e propósito do espaço)*")
            for i, d in enumerate(st.session_state.t26_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t26_ad_{i}", height=100,
                        label_visibility="collapsed",
                        placeholder="Descreva o espaço, os valores, os fornecedores, o que torna o lugar especial...")
                with c2:
                    if len(st.session_state.t26_about_descs) > 1 and _del_btn(f"t26_ad_del_{i}"):
                        st.session_state.t26_about_descs.pop(i); st.rerun()
            if _add_btn("t26_ad_add", "＋ Adicionar descrição"):
                st.session_state.t26_about_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. CTA (RESERVA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Seção de Reserva</div>', unsafe_allow_html=True)

            st.caption("Título CTA  *(chamada para ação)*")
            for i, t in enumerate(st.session_state.t26_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_cta_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t26_ct_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: PRONTO PARA VIVER A EXPERIÊNCIA?")
                with c2:
                    if len(st.session_state.t26_cta_titulos) > 1 and _del_btn(f"t26_ct_t_del_{i}"):
                        st.session_state.t26_cta_titulos.pop(i); st.rerun()
            if _add_btn("t26_ct_t_add", "＋ Adicionar título"):
                st.session_state.t26_cta_titulos.append({"valor": "NOVO TÍTULO?"}); st.rerun()

            st.caption("Descrição CTA")
            for i, d in enumerate(st.session_state.t26_cta_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_cta_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t26_ct_d_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: Garanta seu ingresso e venha fazer parte da melhor vibe.")
                with c2:
                    if len(st.session_state.t26_cta_descs) > 1 and _del_btn(f"t26_ct_d_del_{i}"):
                        st.session_state.t26_cta_descs.pop(i); st.rerun()
            if _add_btn("t26_ct_d_add", "＋ Adicionar descrição"):
                st.session_state.t26_cta_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão de reserva  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t26_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t26_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t26_ct_b_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: RESERVAR AGORA")
                with c2:
                    st.session_state.t26_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t26_ct_b_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de reserva")
                with c3:
                    if len(st.session_state.t26_cta_btns) > 1 and _del_btn(f"t26_ct_b_del_{i}"):
                        st.session_state.t26_cta_btns.pop(i); st.rerun()
            if _add_btn("t26_ct_b_add", "＋ Adicionar botão"):
                st.session_state.t26_cta_btns.append({"texto": "RESERVAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Nome da marca")
            for i, name in enumerate(st.session_state.t26_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t26_fn_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOME DO MERCADO.")
                with c2:
                    if len(st.session_state.t26_foot_brand_names) > 1 and _del_btn(f"t26_fn_del_{i}"):
                        st.session_state.t26_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t26_fn_add", "＋ Adicionar nome"):
                st.session_state.t26_foot_brand_names.append({"valor": "MERCADO."}); st.rerun()

            st.caption("Endereço físico")
            for i, addr in enumerate(st.session_state.t26_foot_addresses):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_addresses[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t26_fa_{i}", label_visibility="collapsed",
                        placeholder="Ex: RUA EXEMPLO, 100 — BAIRRO, CIDADE")
                with c2:
                    if len(st.session_state.t26_foot_addresses) > 1 and _del_btn(f"t26_fa_del_{i}"):
                        st.session_state.t26_foot_addresses.pop(i); st.rerun()
            if _add_btn("t26_fa_add", "＋ Adicionar endereço"):
                st.session_state.t26_foot_addresses.append({"valor": "Rua, Cidade"}); st.rerun()

            st.caption("E-mail de contato  *(exibido como link clicável)*")
            for i, email in enumerate(st.session_state.t26_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_emails[i]["valor"] = st.text_input(
                        "Email", email["valor"], key=f"t26_fe_{i}", label_visibility="collapsed",
                        placeholder="email@mercado.com",
                        help="Este e-mail será exibido no rodapé como link de contato.")
                with c2:
                    if len(st.session_state.t26_foot_emails) > 1 and _del_btn(f"t26_fe_del_{i}"):
                        st.session_state.t26_foot_emails.pop(i); st.rerun()
            if _add_btn("t26_fe_add", "＋ Adicionar email"):
                st.session_state.t26_foot_emails.append({"valor": "email@mercado.com"}); st.rerun()

            st.caption("Colunas de links  *(redes sociais e outros links)*")
            for i, col in enumerate(st.session_state.t26_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t26_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t26_fc_t_{i}",
                        placeholder="Ex: REDES SOCIAIS ou HORÁRIOS")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t26_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t26_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t26_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t26_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https://instagram.com/...")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t26_fc_l_del_{i}_{j}"):
                                st.session_state.t26_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t26_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t26_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t26_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t26_fc_del_{i}"):
                            st.session_state.t26_foot_cols.pop(i); st.rerun()
            if _add_btn("t26_fc_add", "＋ Adicionar coluna"):
                st.session_state.t26_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t26_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t26_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DO MERCADO. SEMPRE REAL, NUNCA COPIADO.")
                with c2:
                    if len(st.session_state.t26_foot_copys) > 1 and _del_btn(f"t26_fcp_del_{i}"):
                        st.session_state.t26_foot_copys.pop(i); st.rerun()
            if _add_btn("t26_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t26_foot_copys.append({"valor": "© 2026"}); st.rerun()

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
                3. Cole a URL no campo de imagem do card correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Cards de destaque: <strong>600 × 400 px</strong> (paisagem)<br>
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
                Ex: "usar uma paleta mais urbana", "adicionar seção de vendedores/expositores",
                "adicionar mapa de localização", "adicionar horários de funcionamento"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t26_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t26_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_obs) > 1 and _del_btn(f"t26_obs_del_{i}"):
                        st.session_state.t26_obs.pop(i); st.rerun()
            if _add_btn("t26_obs_add", "＋ Adicionar observação"):
                st.session_state.t26_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t26_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t26_email_cliente.strip() or "@" not in st.session_state.t26_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t26_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t26_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t26_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t26_nome_cliente}'*."
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
        page_icon="🍔",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
