import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img1.png"
TEMPLATE_NAME      = "Template 1 — Agência Digital"
TEMPLATE_ID        = "template_1"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t1_nome_cliente":   "",
        "t1_email_cliente":  "",
        "t1_nome_site":      "",   # aparece como sttacksite.streamlit.app/?c=ESTE_VALOR

        # ── CORES ────────────────────────────────────────────────────────────
        "t1_cores": [
            {"nome": "Cor principal (botões, destaques)", "valor": "#0066FF"},
            {"nome": "Cor dos textos",                    "valor": "#1a1a1a"},
            {"nome": "Cor dos subtextos",                 "valor": "#666666"},
        ],

        # ── NAVBAR ───────────────────────────────────────────────────────────
        "t1_logos": [{"valor": "🚀 AGÊNCIA"}],
        "t1_nav_links": [
            {"texto": "Serviços", "url": "seção Nossos Serviços"},
            {"texto": "Sobre",    "url": "seção Sobre nós"},
            {"texto": "Contato",  "url": "seção de contato ao final da página"},
        ],
        "t1_nav_ctas": [
            {"texto": "✨ Novo",              "cor": "Azul"},
            {"texto": "Transformação Digital", "cor": "Cinza"},
            {"texto": "⭐ Top Rated",          "cor": "Verde"},
        ],

        # ── HERO ─────────────────────────────────────────────────────────────
        "t1_hero_titulos": [
            {"parte1": "Transforme seu Negócio com", "destaque": "Estratégia Digital"},
        ],
        "t1_hero_subtitulos": [
            {"valor": "Soluções completas de marketing digital que aumentam suas vendas e presença online"},
        ],
        "t1_hero_btns": [
            {"texto": "Solicitar Consultoria", "url": "https://wa.me/5511999999999", "estilo": "primário"},
            {"texto": "Ver Portfólio",          "url": "seção Nossos Serviços",       "estilo": "secundário"},
        ],

        # ── ESTATÍSTICAS ─────────────────────────────────────────────────────
        "t1_stats": [
            {"numero": "500+", "label": "Clientes Satisfeitos"},
            {"numero": "10+",  "label": "Anos de Experiência"},
            {"numero": "300%", "label": "Crescimento Médio"},
        ],

        # ── SEÇÃO SERVIÇOS ───────────────────────────────────────────────────
        "t1_secao_titulos": [{"parte1": "Nossos", "destaque": "Serviços"}],
        "t1_secao_descs":   [{"valor": "Oferecemos soluções completas de marketing digital para impulsionar seu negócio"}],
        "t1_cards": [
            {"icone": "📱", "titulo": "Social Media",       "descricao": "Gerenciamento completo de suas redes sociais com estratégia de conteúdo"},
            {"icone": "🎯", "titulo": "Publicidade Digital", "descricao": "Campanhas otimizadas em Google Ads e Facebook para máximo ROI"},
            {"icone": "📊", "titulo": "Análise de Dados",    "descricao": "Relatórios detalhados e insights para melhorar seu desempenho"},
            {"icone": "🌐", "titulo": "SEO & Conteúdo",      "descricao": "Otimização para buscas e criação de conteúdo de alta qualidade"},
            {"icone": "💻", "titulo": "Web Design",          "descricao": "Websites modernos e responsivos que convertem visitantes em clientes"},
            {"icone": "📧", "titulo": "Email Marketing",     "descricao": "Campanhas de email personalizadas que geram resultados"},
        ],

        # ── CTA ──────────────────────────────────────────────────────────────
        "t1_cta_titulos":    [{"valor": "Pronto para Transformar seu Negócio?"}],
        "t1_cta_subtitulos": [{"valor": "Agende uma consultoria gratuita com nossos especialistas"}],
        "t1_cta_btns":       [{"texto": "Agendar Agora", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ───────────────────────────────────────────────────────────
        "t1_footer_txts":  [{"valor": "© 2026 Agência Digital. Todos os direitos reservados."}],
        "t1_footer_links": [
            {"texto": "Privacidade", "url": "página de política de privacidade"},
            {"texto": "Termos",      "url": "página de termos de uso"},
        ],

        # ── OBSERVAÇÕES ──────────────────────────────────────────────────────
        "t1_obs": [{"valor": ""}],
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
    """Monta o dicionário completo para envio."""
    return {
        "template":        TEMPLATE_ID,
        "template_nome":   TEMPLATE_NAME,
        "identificacao": {
            "nome":      st.session_state.t1_nome_cliente,
            "email":     st.session_state.t1_email_cliente,
            "nome_site": st.session_state.t1_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t1_nome_site}",
        },
        "cores":             st.session_state.t1_cores,
        "navbar": {
            "logos":     st.session_state.t1_logos,
            "links":     st.session_state.t1_nav_links,
            "badges":    st.session_state.t1_nav_ctas,
        },
        "hero": {
            "titulos":    st.session_state.t1_hero_titulos,
            "subtitulos": st.session_state.t1_hero_subtitulos,
            "botoes":     st.session_state.t1_hero_btns,
        },
        "estatisticas":     st.session_state.t1_stats,
        "secao_servicos": {
            "titulos":    st.session_state.t1_secao_titulos,
            "descricoes": st.session_state.t1_secao_descs,
            "cards":      st.session_state.t1_cards,
        },
        "cta": {
            "titulos":    st.session_state.t1_cta_titulos,
            "subtitulos": st.session_state.t1_cta_subtitulos,
            "botoes":     st.session_state.t1_cta_btns,
        },
        "footer": {
            "textos": st.session_state.t1_footer_txts,
            "links":  st.session_state.t1_footer_links,
        },
        "observacoes": st.session_state.t1_obs,
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

    # ── CSS do editor ─────────────────────────────────────────────────────────
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
        Preencha os campos abaixo para personalizar o seu site. Não precisa ser técnico — é só digitar!<br><br>
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
            # 0. IDENTIFICAÇÃO (sempre primeiro)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👤 Seus Dados</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin-top:4px">
                Preencha seus dados antes de começar. Usamos essas informações para identificar seu pedido e
                entrar em contato quando o site estiver pronto. 🚀
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t1_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t1_nome_cliente,
                key="t1_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t1_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t1_email_cliente,
                key="t1_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz. É assim que vinculamos seu pedido.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, minhaclinica, fitpro2026).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t1_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t1_nome_site,
                key="t1_nome_site_inp",
                placeholder="Ex: joaosilva  →  sttacksite.streamlit.app/?c=joaosilva",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t1_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t1_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t1_cor_nome_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t1_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t1_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t1_cores) > 1 and _del_btn(f"t1_cor_del_{i}"):
                        st.session_state.t1_cores.pop(i); st.rerun()
            if _add_btn("t1_cor_add", "＋ Adicionar cor"):
                st.session_state.t1_cores.append({"nome": "Descreva onde usar esta cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(aparece no canto superior esquerdo)*")
            for i, item in enumerate(st.session_state.t1_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t1_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: 🚀 Minha Empresa")
                with c2:
                    if len(st.session_state.t1_logos) > 1 and _del_btn(f"t1_logo_del_{i}"):
                        st.session_state.t1_logos.pop(i); st.rerun()
            if _add_btn("t1_logo_add", "＋ Adicionar logo"):
                st.session_state.t1_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto exibido | Para onde leva ao clicar)*")
            for i, link in enumerate(st.session_state.t1_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t1_nl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t1_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t1_nl_url_{i}", label_visibility="collapsed",
                        placeholder="Ex: seção de contato ao final da página",
                        help="Descreva a seção do site ou cole um link externo (https://...)")
                with c3:
                    if len(st.session_state.t1_nav_links) > 1 and _del_btn(f"t1_nl_del_{i}"):
                        st.session_state.t1_nav_links.pop(i); st.rerun()
            if _add_btn("t1_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t1_nav_links.append({"texto": "Nome do link", "url": "seção de destino"}); st.rerun()

            st.caption("Etiquetas / Badges  *(pequenos selos de destaque no topo)*")
            for i, badge in enumerate(st.session_state.t1_nav_ctas):
                c1, c2, c3 = st.columns([5, 3, 1])
                with c1:
                    st.session_state.t1_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", badge["texto"], key=f"t1_ncta_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do badge")
                with c2:
                    st.session_state.t1_nav_ctas[i]["cor"] = st.selectbox(
                        "Cor", ["Azul", "Cinza", "Verde", "Laranja"], key=f"t1_ncta_cor_{i}",
                        index=["Azul", "Cinza", "Verde", "Laranja"].index(badge.get("cor", "Cinza"))
                        if badge.get("cor", "Cinza") in ["Azul", "Cinza", "Verde", "Laranja"] else 1,
                        label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t1_nav_ctas) > 1 and _del_btn(f"t1_ncta_del_{i}"):
                        st.session_state.t1_nav_ctas.pop(i); st.rerun()
            if _add_btn("t1_ncta_add", "＋ Adicionar badge"):
                st.session_state.t1_nav_ctas.append({"texto": "Novo Badge", "cor": "Cinza"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Título principal  *(Texto normal | Parte em destaque colorido)*")
            for i, t in enumerate(st.session_state.t1_hero_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_hero_titulos[i]["parte1"] = st.text_input(
                        "Parte 1", t["parte1"], key=f"t1_ht_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t1_hero_titulos[i]["destaque"] = st.text_input(
                        "Destaque", t["destaque"], key=f"t1_ht_dest_{i}", label_visibility="collapsed",
                        placeholder="Parte em azul/colorido")
                with c3:
                    if len(st.session_state.t1_hero_titulos) > 1 and _del_btn(f"t1_ht_del_{i}"):
                        st.session_state.t1_hero_titulos.pop(i); st.rerun()
            if _add_btn("t1_ht_add", "＋ Adicionar título"):
                st.session_state.t1_hero_titulos.append({"parte1": "Novo Título", "destaque": "Destaque"}); st.rerun()

            st.caption("Subtítulo  *(frase de apoio abaixo do título)*")
            for i, item in enumerate(st.session_state.t1_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_hero_subtitulos[i]["valor"] = st.text_area(
                        "Subtítulo", item["valor"], key=f"t1_hsub_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Frase curta que explica o que você oferece")
                with c2:
                    if len(st.session_state.t1_hero_subtitulos) > 1 and _del_btn(f"t1_hsub_del_{i}"):
                        st.session_state.t1_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t1_hsub_add", "＋ Adicionar subtítulo"):
                st.session_state.t1_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs dos botões:</strong> você pode colocar o que quiser — seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, site externo, ou descrever
                para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Botões do hero  *(Texto | URL ou destino | Estilo)*")
            for i, btn in enumerate(st.session_state.t1_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t1_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t1_hb_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t1_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t1_hb_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    st.session_state.t1_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"], key=f"t1_hb_style_{i}",
                        index=0 if btn["estilo"] == "primário" else 1, label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t1_hero_btns) > 1 and _del_btn(f"t1_hb_del_{i}"):
                        st.session_state.t1_hero_btns.pop(i); st.rerun()
            if _add_btn("t1_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t1_hero_btns.append({"texto": "Novo Botão", "url": "", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas</div>', unsafe_allow_html=True)
            st.caption("Números de destaque exibidos abaixo do hero  *(Valor | Descrição)*")
            for i, stat in enumerate(st.session_state.t1_stats):
                c1, c2, c3 = st.columns([2, 5, 1])
                with c1:
                    st.session_state.t1_stats[i]["numero"] = st.text_input(
                        "Número", stat["numero"], key=f"t1_st_num_{i}", label_visibility="collapsed",
                        placeholder="Ex: 500+")
                with c2:
                    st.session_state.t1_stats[i]["label"] = st.text_input(
                        "Label", stat["label"], key=f"t1_st_lbl_{i}", label_visibility="collapsed",
                        placeholder="Ex: Clientes Satisfeitos")
                with c3:
                    if len(st.session_state.t1_stats) > 1 and _del_btn(f"t1_st_del_{i}"):
                        st.session_state.t1_stats.pop(i); st.rerun()
            if _add_btn("t1_st_add", "＋ Adicionar estatística"):
                st.session_state.t1_stats.append({"numero": "0", "label": "Nova Métrica"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. SERVIÇOS / CARDS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto normal | Destaque colorido)*")
            for i, t in enumerate(st.session_state.t1_secao_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_secao_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t1_sect_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t1_secao_titulos[i]["destaque"] = st.text_input(
                        "Destaque", t["destaque"], key=f"t1_sect_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t1_secao_titulos) > 1 and _del_btn(f"t1_sect_del_{i}"):
                        st.session_state.t1_secao_titulos.pop(i); st.rerun()
            if _add_btn("t1_sect_add", "＋ Adicionar título de seção"):
                st.session_state.t1_secao_titulos.append({"parte1": "Novo", "destaque": "Título"}); st.rerun()

            st.caption("Descrição da seção")
            for i, item in enumerate(st.session_state.t1_secao_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_secao_descs[i]["valor"] = st.text_area(
                        "Descrição", item["valor"], key=f"t1_secd_{i}", height=60, label_visibility="collapsed",
                        placeholder="Frase de apoio abaixo do título da seção")
                with c2:
                    if len(st.session_state.t1_secao_descs) > 1 and _del_btn(f"t1_secd_del_{i}"):
                        st.session_state.t1_secao_descs.pop(i); st.rerun()
            if _add_btn("t1_secd_add", "＋ Adicionar descrição"):
                st.session_state.t1_secao_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de serviço  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t1_cards):
                with st.expander(f"Card {i+1} — {card['titulo']}"):
                    c1, c2 = st.columns([1, 8])
                    with c1:
                        st.session_state.t1_cards[i]["icone"] = st.text_input(
                            "Ícone", card["icone"], key=f"t1_cd_ico_{i}", label_visibility="collapsed",
                            help="Cole um emoji aqui, ex: 📱 🎯 💡")
                    with c2:
                        st.session_state.t1_cards[i]["titulo"] = st.text_input(
                            "Título", card["titulo"], key=f"t1_cd_tit_{i}", label_visibility="collapsed")
                    st.session_state.t1_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t1_cd_dsc_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Descreva brevemente este serviço. Caso queira formatação especial (negrito, itálico, etc), mencione nas Observações.")
                    if len(st.session_state.t1_cards) > 1:
                        if st.button("🗑 Remover este card", key=f"t1_cd_del_{i}"):
                            st.session_state.t1_cards.pop(i); st.rerun()
            if _add_btn("t1_cd_add", "＋ Adicionar card de serviço"):
                st.session_state.t1_cards.append({"icone": "⭐", "titulo": "Novo Serviço", "descricao": "Descrição do serviço"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. CTA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📣 Seção de Chamada para Ação (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, item in enumerate(st.session_state.t1_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_cta_titulos[i]["valor"] = st.text_input(
                        "Título CTA", item["valor"], key=f"t1_ctat_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_cta_titulos) > 1 and _del_btn(f"t1_ctat_del_{i}"):
                        st.session_state.t1_cta_titulos.pop(i); st.rerun()
            if _add_btn("t1_ctat_add", "＋ Adicionar título CTA"):
                st.session_state.t1_cta_titulos.append({"valor": "Novo Título CTA"}); st.rerun()

            st.caption("Subtítulo")
            for i, item in enumerate(st.session_state.t1_cta_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_cta_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo CTA", item["valor"], key=f"t1_ctasub_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_cta_subtitulos) > 1 and _del_btn(f"t1_ctasub_del_{i}"):
                        st.session_state.t1_cta_subtitulos.pop(i); st.rerun()
            if _add_btn("t1_ctasub_add", "＋ Adicionar subtítulo CTA"):
                st.session_state.t1_cta_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t1_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t1_ctab_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t1_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t1_ctab_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t1_cta_btns) > 1 and _del_btn(f"t1_ctab_del_{i}"):
                        st.session_state.t1_cta_btns.pop(i); st.rerun()
            if _add_btn("t1_ctab_add", "＋ Adicionar botão CTA"):
                st.session_state.t1_cta_btns.append({"texto": "Novo Botão", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔻 Rodapé (Footer)</div>', unsafe_allow_html=True)

            st.caption("Texto do rodapé  *(ex: copyright, frase de fechamento)*")
            for i, item in enumerate(st.session_state.t1_footer_txts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_footer_txts[i]["valor"] = st.text_input(
                        "Texto footer", item["valor"], key=f"t1_ftxt_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t1_footer_txts) > 1 and _del_btn(f"t1_ftxt_del_{i}"):
                        st.session_state.t1_footer_txts.pop(i); st.rerun()
            if _add_btn("t1_ftxt_add", "＋ Adicionar texto ao footer"):
                st.session_state.t1_footer_txts.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t1_footer_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_footer_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t1_fl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t1_footer_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t1_fl_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou nome da página")
                with c3:
                    if len(st.session_state.t1_footer_links) > 1 and _del_btn(f"t1_fl_del_{i}"):
                        st.session_state.t1_footer_links.pop(i); st.rerun()
            if _add_btn("t1_fl_add", "＋ Adicionar link ao footer"):
                st.session_state.t1_footer_links.append({"texto": "Novo Link", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a> (gratuito, sem cadastro)
                   e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole essa URL no campo correspondente nas seções acima (ex: logo, banner, foto de perfil).<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
                • Cards / miniaturas: <strong>600 × 400 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, formato PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Sem problema! Envie a imagem diretamente para
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
            for i, item in enumerate(st.session_state.t1_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t1_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_obs) > 1 and _del_btn(f"t1_obs_del_{i}"):
                        st.session_state.t1_obs.pop(i); st.rerun()
            if _add_btn("t1_obs_add", "＋ Adicionar observação"):
                st.session_state.t1_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                payload_preview = _build_json()
                st.json(payload_preview)

            # Validação
            erros = []
            if not st.session_state.t1_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t1_email_cliente.strip() or "@" not in st.session_state.t1_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t1_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            btn_disabled = len(erros) > 0
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t1_send", type="primary",
                         disabled=btn_disabled):
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t1_nome_site}**"
                    )
                    st.balloons()
                else:
                    # fallback: mostra JSON para copiar
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t1_nome_cliente}'*."
                    )
                    st.code(json.dumps(payload, ensure_ascii=False, indent=2), language="json")

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — IMAGEM DO TEMPLATE
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO DIRETA
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
