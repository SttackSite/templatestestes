import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img3.png"
TEMPLATE_NAME      = "Template 3 — Experiência Absurda (Premium)"
TEMPLATE_ID        = "template_3"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t3_nome_cliente":  "",
        "t3_email_cliente": "",
        "t3_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t3_cores": [
            {"nome": "Cor de destaque (botões, logo)", "valor": "#FF006E"},
            {"nome": "Cor secundária (links, bordas)",  "valor": "#00D9FF"},
            {"nome": "Cor de fundo (gradiente 1)",      "valor": "#0f0f1e"},
            {"nome": "Cor de fundo (gradiente 2)",      "valor": "#1a1a2e"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t3_logos": [{"valor": "PREMIUM"}],
        "t3_nav_links": [
            {"texto": "Recursos", "url": "seção Recursos Incríveis"},
            {"texto": "Galeria",  "url": "seção Números que Falam"},
            {"texto": "Sobre",    "url": "seção Sobre nós"},
            {"texto": "Contato",  "url": "seção de contato ao final da página"},
        ],
        "t3_nav_ctas": [{"texto": "Começar Agora", "url": "https://wa.me/5511999999999"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t3_hero_titulos":    [{"valor": "Experiência Absurda"}],
        "t3_hero_subtitulos": [{"valor": "Design que transforma, cores que inspiram"}],
        "t3_hero_btns": [
            {"texto": "Explorar Agora", "url": "https://wa.me/5511999999999",    "estilo": "primário"},
            {"texto": "Saiba Mais",     "url": "seção Recursos Incríveis", "estilo": "secundário"},
        ],

        # ── RECURSOS (FEATURES) ─────────────────────────────────────────────
        "t3_feat_titulos": [{"valor": "Recursos Incríveis"}],
        "t3_feat_descs":   [{"valor": "Tudo que você precisa para impressionar seus clientes"}],
        "t3_feat_cards": [
            {"icone": "⚡", "titulo": "Ultra Rápido",            "descricao": "Performance otimizada para a melhor experiência do usuário em qualquer dispositivo."},
            {"icone": "🎨", "titulo": "Design Moderno",          "descricao": "Interface visual impressionante com animações suaves e cores dinâmicas."},
            {"icone": "🔧", "titulo": "Totalmente Customizável", "descricao": "Adapte cores, textos e conteúdo facilmente para seu negócio específico."},
            {"icone": "📱", "titulo": "Responsivo",              "descricao": "Funciona perfeitamente em desktop, tablet e mobile com experiência fluida."},
            {"icone": "🚀", "titulo": "Conversão Máxima",        "descricao": "Design estratégico focado em converter visitantes em clientes."},
            {"icone": "✨", "titulo": "Experiência Premium",     "descricao": "Cada detalhe foi pensado para criar uma experiência memorável."},
        ],

        # ── SHOWCASE (NÚMEROS) ───────────────────────────────────────────────
        "t3_show_titulos": [{"valor": "Números que Falam"}],
        "t3_show_descs":   [{"valor": "Resultados comprovados de padrões premium"}],
        "t3_show_cards": [
            {"numero": "300%", "label": "Mais Conversões"},
            {"numero": "50K+", "label": "Clientes Felizes"},
            {"numero": "99%",  "label": "Satisfação"},
            {"numero": "24/7", "label": "Suporte"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t3_ctaf_titulos": [{"valor": "Pronto para Transformar?"}],
        "t3_ctaf_descs":   [{"valor": "Junte-se a milhares de empresas que já estão usando padrões premium para crescer exponencialmente."}],
        "t3_ctaf_btns":    [{"texto": "Começar Sua Jornada", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t3_footer_infos": [{"valor": "Email: contato@premium.com.br | Telefone: (99) 99999-9999"}],
        "t3_footer_addrs": [{"valor": "Endereço: Av. Principal, 1000 - São Paulo, SP"}],
        "t3_footer_copys": [{"valor": "© 2025 Premium padrões. Todos os direitos reservados. Transformando negócios com design excepcional."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t3_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t3_nome_cliente,
            "email":     st.session_state.t3_email_cliente,
            "nome_site": st.session_state.t3_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t3_nome_site}",
        },
        "cores": st.session_state.t3_cores,
        "navbar": {
            "logos": st.session_state.t3_logos,
            "links": st.session_state.t3_nav_links,
            "cta":   st.session_state.t3_nav_ctas,
        },
        "hero": {
            "titulos":    st.session_state.t3_hero_titulos,
            "subtitulos": st.session_state.t3_hero_subtitulos,
            "botoes":     st.session_state.t3_hero_btns,
        },
        "recursos": {
            "titulos":    st.session_state.t3_feat_titulos,
            "descricoes": st.session_state.t3_feat_descs,
            "cards":      st.session_state.t3_feat_cards,
        },
        "showcase": {
            "titulos":    st.session_state.t3_show_titulos,
            "descricoes": st.session_state.t3_show_descs,
            "cards":      st.session_state.t3_show_cards,
        },
        "cta_final": {
            "titulos":    st.session_state.t3_ctaf_titulos,
            "descricoes": st.session_state.t3_ctaf_descs,
            "botoes":     st.session_state.t3_ctaf_btns,
        },
        "footer": {
            "infos":     st.session_state.t3_footer_infos,
            "enderecos": st.session_state.t3_footer_addrs,
            "copyright": st.session_state.t3_footer_copys,
        },
        "observacoes": st.session_state.t3_obs,
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

    # ── Aviso inicial ─────────────────────────────────────────────────────────
    st.markdown("""
    <div class="info-box">
        👋 <strong>Bem-vindo ao editor do seu site!</strong><br>
        Preencha os campos abaixo para personalizar o seu site. Não precisa ser técnico — é só digitar!
        Você também poderá vir aqui e ajustar seu site quantas vezes quiser.<br><br>
        💡 <strong>Tem alguma ideia que não encontrou aqui?</strong> Use o campo <em>Observações</em> no final
        para descrever o que deseja (ex: "quero uma fonte diferente", "adicionar um vídeo", "mudar o layout da seção X").
        Nossa equipe analisa tudo e aplica para você. 😊
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

            st.session_state.t3_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t3_nome_cliente,
                key="t3_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t3_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t3_email_cliente,
                key="t3_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, minhaclinica, premium2026).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t3_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t3_nome_site,
                key="t3_nome_site_inp",
                placeholder="Ex: premium2026  →  sttacksite.streamlit.app/?c=premium2026",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t3_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t3_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t3_cor_nome_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t3_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t3_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t3_cores) > 1 and _del_btn(f"t3_cor_del_{i}"):
                        st.session_state.t3_cores.pop(i); st.rerun()
            if _add_btn("t3_cor_add", "＋ Adicionar cor"):
                st.session_state.t3_cores.append({"nome": "Descreva onde usar esta cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(aparece com gradiente animado no topo)*")
            for i, item in enumerate(st.session_state.t3_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t3_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: MINHA EMPRESA")
                with c2:
                    if len(st.session_state.t3_logos) > 1 and _del_btn(f"t3_logo_del_{i}"):
                        st.session_state.t3_logos.pop(i); st.rerun()
            if _add_btn("t3_logo_add", "＋ Adicionar logo"):
                st.session_state.t3_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto exibido | Para onde leva ao clicar)*")
            for i, link in enumerate(st.session_state.t3_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t3_nl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t3_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t3_nl_url_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...",
                        help="Descreva a seção ou cole um link externo (WhatsApp, Instagram etc.)")
                with c3:
                    if len(st.session_state.t3_nav_links) > 1 and _del_btn(f"t3_nl_del_{i}"):
                        st.session_state.t3_nav_links.pop(i); st.rerun()
            if _add_btn("t3_nl_add", "＋ Adicionar link"):
                st.session_state.t3_nav_links.append({"texto": "Link", "url": "seção de destino"}); st.rerun()

            st.caption("Botão CTA da navbar  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t3_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t3_ncta_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t3_nav_ctas[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t3_ncta_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t3_nav_ctas) > 1 and _del_btn(f"t3_ncta_del_{i}"):
                        st.session_state.t3_nav_ctas.pop(i); st.rerun()
            if _add_btn("t3_ncta_add", "＋ Adicionar CTA navbar"):
                st.session_state.t3_nav_ctas.append({"texto": "CTA", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Título  *(exibido com gradiente animado rosa → cyan → amarelo)*")
            for i, t in enumerate(st.session_state.t3_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t3_ht_{i}", label_visibility="collapsed",
                        placeholder="Título principal do site")
                with c2:
                    if len(st.session_state.t3_hero_titulos) > 1 and _del_btn(f"t3_ht_del_{i}"):
                        st.session_state.t3_hero_titulos.pop(i); st.rerun()
            if _add_btn("t3_ht_add", "＋ Adicionar título"):
                st.session_state.t3_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Subtítulo  *(frase de apoio abaixo do título)*")
            for i, s in enumerate(st.session_state.t3_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_hero_subtitulos[i]["valor"] = st.text_area(
                        "Subtítulo", s["valor"], key=f"t3_hs_{i}", height=60,
                        label_visibility="collapsed",
                        placeholder="Frase curta que explica o que você oferece")
                with c2:
                    if len(st.session_state.t3_hero_subtitulos) > 1 and _del_btn(f"t3_hs_del_{i}"):
                        st.session_state.t3_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t3_hs_add", "＋ Adicionar subtítulo"):
                st.session_state.t3_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botões  *(Texto | URL ou destino | Estilo)*")
            for i, btn in enumerate(st.session_state.t3_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1:
                    st.session_state.t3_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t3_hbtn_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t3_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t3_hbtn_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    st.session_state.t3_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"],
                        index=0 if btn["estilo"] == "primário" else 1,
                        key=f"t3_hbtn_e_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t3_hero_btns) > 1 and _del_btn(f"t3_hbtn_del_{i}"):
                        st.session_state.t3_hero_btns.pop(i); st.rerun()
            if _add_btn("t3_hbtn_add", "＋ Adicionar botão hero"):
                st.session_state.t3_hero_btns.append({"texto": "Botão", "url": "", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. RECURSOS (FEATURES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Recursos</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t3_feat_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_feat_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t3_ft_{i}", label_visibility="collapsed",
                        placeholder="Ex: Recursos Incríveis")
                with c2:
                    if len(st.session_state.t3_feat_titulos) > 1 and _del_btn(f"t3_ft_del_{i}"):
                        st.session_state.t3_feat_titulos.pop(i); st.rerun()
            if _add_btn("t3_ft_add", "＋ Adicionar título"):
                st.session_state.t3_feat_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, d in enumerate(st.session_state.t3_feat_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_feat_descs[i]["valor"] = st.text_input(
                        "Descrição", d["valor"], key=f"t3_fd_{i}", label_visibility="collapsed",
                        placeholder="Frase de apoio abaixo do título")
                with c2:
                    if len(st.session_state.t3_feat_descs) > 1 and _del_btn(f"t3_fd_del_{i}"):
                        st.session_state.t3_feat_descs.pop(i); st.rerun()
            if _add_btn("t3_fd_add", "＋ Adicionar subtítulo"):
                st.session_state.t3_feat_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de recursos  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t3_feat_cards):
                with st.expander(f"Recurso {i+1}: {card['titulo']}"):
                    st.session_state.t3_feat_cards[i]["icone"] = st.text_input(
                        "Ícone/Emoji", card["icone"], key=f"t3_fc_i_{i}",
                        help="Cole um emoji, ex: ⚡ 🎨 🚀")
                    st.session_state.t3_feat_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t3_fc_t_{i}")
                    st.session_state.t3_feat_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t3_fc_d_{i}", height=80,
                        placeholder="Descreva este recurso. Para formatação especial, use as Observações.")
                    if len(st.session_state.t3_feat_cards) > 1:
                        if st.button("🗑 Remover este recurso", key=f"t3_fc_del_{i}"):
                            st.session_state.t3_feat_cards.pop(i); st.rerun()
            if _add_btn("t3_fc_add", "＋ Adicionar recurso"):
                st.session_state.t3_feat_cards.append({"icone": "✨", "titulo": "Novo Recurso", "descricao": "Descrição aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. SHOWCASE (NÚMEROS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números em Destaque</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t3_show_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_show_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t3_st_{i}", label_visibility="collapsed",
                        placeholder="Ex: Números que Falam")
                with c2:
                    if len(st.session_state.t3_show_titulos) > 1 and _del_btn(f"t3_st_del_{i}"):
                        st.session_state.t3_show_titulos.pop(i); st.rerun()
            if _add_btn("t3_st_add", "＋ Adicionar título"):
                st.session_state.t3_show_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, d in enumerate(st.session_state.t3_show_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_show_descs[i]["valor"] = st.text_area(
                        "Subtítulo", d["valor"], key=f"t3_sd_{i}", height=60,
                        label_visibility="collapsed",
                        placeholder="Frase de apoio abaixo do título")
                with c2:
                    if len(st.session_state.t3_show_descs) > 1 and _del_btn(f"t3_sd_del_{i}"):
                        st.session_state.t3_show_descs.pop(i); st.rerun()
            if _add_btn("t3_sd_add", "＋ Adicionar subtítulo"):
                st.session_state.t3_show_descs.append({"valor": "Novo Subtítulo"}); st.rerun()

            st.caption("Números  *(Valor | Rótulo)*")
            for i, card in enumerate(st.session_state.t3_show_cards):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_show_cards[i]["numero"] = st.text_input(
                        "Valor", card["numero"], key=f"t3_sc_n_{i}", label_visibility="collapsed",
                        placeholder="Ex: 300%")
                with c2:
                    st.session_state.t3_show_cards[i]["label"] = st.text_input(
                        "Rótulo", card["label"], key=f"t3_sc_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Mais Conversões")
                with c3:
                    if len(st.session_state.t3_show_cards) > 1 and _del_btn(f"t3_sc_del_{i}"):
                        st.session_state.t3_show_cards.pop(i); st.rerun()
            if _add_btn("t3_sc_add", "＋ Adicionar número"):
                st.session_state.t3_show_cards.append({"numero": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t3_ctaf_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_ctaf_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t3_ctaft_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pronto para Começar?")
                with c2:
                    if len(st.session_state.t3_ctaf_titulos) > 1 and _del_btn(f"t3_ctaft_del_{i}"):
                        st.session_state.t3_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t3_ctaft_add", "＋ Adicionar título"):
                st.session_state.t3_ctaf_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t3_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_ctaf_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t3_ctafd_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase de encerramento e chamada para ação")
                with c2:
                    if len(st.session_state.t3_ctaf_descs) > 1 and _del_btn(f"t3_ctafd_del_{i}"):
                        st.session_state.t3_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t3_ctafd_add", "＋ Adicionar descrição"):
                st.session_state.t3_ctaf_descs.append({"valor": "Nova Descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t3_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_ctaf_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t3_ctafb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t3_ctaf_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t3_ctafb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t3_ctaf_btns) > 1 and _del_btn(f"t3_ctafb_del_{i}"):
                        st.session_state.t3_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t3_ctafb_add", "＋ Adicionar botão"):
                st.session_state.t3_ctaf_btns.append({"texto": "Botão", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Infos de contato  *(telefone, e-mail etc.)*")
            for i, info in enumerate(st.session_state.t3_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_footer_infos[i]["valor"] = st.text_input(
                        "Infos", info["valor"], key=f"t3_finfo_{i}", label_visibility="collapsed",
                        placeholder="Ex: Email: contato@empresa.com | Tel: (11) 99999-9999")
                with c2:
                    if len(st.session_state.t3_footer_infos) > 1 and _del_btn(f"t3_finfo_del_{i}"):
                        st.session_state.t3_footer_infos.pop(i); st.rerun()
            if _add_btn("t3_finfo_add", "＋ Adicionar linha de contato"):
                st.session_state.t3_footer_infos.append({"valor": "Nova info"}); st.rerun()

            st.caption("Endereço")
            for i, addr in enumerate(st.session_state.t3_footer_addrs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_footer_addrs[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t3_faddr_{i}", label_visibility="collapsed",
                        placeholder="Ex: Rua das Flores, 100 - São Paulo, SP")
                with c2:
                    if len(st.session_state.t3_footer_addrs) > 1 and _del_btn(f"t3_faddr_del_{i}"):
                        st.session_state.t3_footer_addrs.pop(i); st.rerun()
            if _add_btn("t3_faddr_add", "＋ Adicionar endereço"):
                st.session_state.t3_footer_addrs.append({"valor": "Novo endereço"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t3_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_footer_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t3_fcopy_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t3_footer_copys) > 1 and _del_btn(f"t3_fcopy_del_{i}"):
                        st.session_state.t3_footer_copys.pop(i); st.rerun()
            if _add_btn("t3_fcopy_add", "＋ Adicionar linha"):
                st.session_state.t3_footer_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole essa URL no campo correspondente nas seções acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
                • Cards / miniaturas: <strong>600 × 400 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, formato PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie diretamente para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>
                e diga onde ela deve ser inserida. Nossa equipe cuida disso para você. 😊
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 9. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "quero mudar a fonte", "adicionar uma seção de FAQ", "colocar vídeo do YouTube",
                "texto em negrito no título", "remover a seção X", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t3_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t3_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t3_obs) > 1 and _del_btn(f"t3_obs_del_{i}"):
                        st.session_state.t3_obs.pop(i); st.rerun()
            if _add_btn("t3_obs_add", "＋ Adicionar observação"):
                st.session_state.t3_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t3_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t3_email_cliente.strip() or "@" not in st.session_state.t3_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t3_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t3_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t3_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t3_nome_cliente}'*."
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
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
