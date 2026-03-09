import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img7.png"
TEMPLATE_NAME      = "Template 7 — Elite Portfolio (Premium)"
TEMPLATE_ID        = "template_7"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t7_nome_cliente":  "",
        "t7_email_cliente": "",
        "t7_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t7_cores": [
            {"nome": "Cor Principal (Ciano)",    "valor": "#64c8ff"},
            {"nome": "Cor Secundária (Azul)",    "valor": "#0099ff"},
            {"nome": "Cor de Fundo (Deep Blue)", "valor": "#0a0e27"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t7_logos": [{"valor": "ELITE"}],
        "t7_nav_links": [
            {"texto": "Sobre",     "url": "seção Sobre"},
            {"texto": "Expertise", "url": "seção Expertise"},
            {"texto": "Trabalhos", "url": "seção Trabalhos em Destaque"},
            {"texto": "Contato",   "url": "seção de contato ao final da página"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t7_hero_labels":  [{"valor": "Bem-vindo"}],
        "t7_hero_titulos": [{"valor": "Transformando Visões em Realidade"}],
        "t7_hero_descs":   [{"valor": "Especialista em criar soluções de impacto com design sofisticado e estratégia de negócio."}],
        "t7_hero_btns": [
            {"texto": "Iniciar Projeto",    "url": "https://wa.me/5511999999999", "estilo": "primário"},
            {"texto": "Explorar Trabalhos", "url": "seção Trabalhos em Destaque", "estilo": "secundário"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t7_stats": [
            {"numero": "150+", "label": "Projetos Entregues"},
            {"numero": "98%",  "label": "Satisfação Clientes"},
            {"numero": "12+",  "label": "Anos Experiência"},
            {"numero": "50M+", "label": "Impacto Gerado"},
        ],

        # ── EXPERTISE ───────────────────────────────────────────────────────
        "t7_exp_titulos": [{"valor": "Expertise"}],
        "t7_exp_items": [
            {"num": "01", "titulo": "Estratégia Digital", "desc": "Desenvolvimento de estratégias robustas que transformam objetivos em resultados mensuráveis e crescimento sustentável."},
            {"num": "02", "titulo": "Design Premium",     "desc": "Criação de interfaces sofisticadas que combinam estética com funcionalidade, elevando a experiência do usuário."},
            {"num": "03", "titulo": "Desenvolvimento",    "desc": "Implementação de soluções técnicas escaláveis e performáticas usando tecnologias de ponta do mercado."},
            {"num": "04", "titulo": "Consultoria",        "desc": "Orientação estratégica para empresas que buscam inovação, transformação digital e posicionamento de mercado."},
        ],

        # ── TRABALHOS ───────────────────────────────────────────────────────
        "t7_work_titulos": [{"valor": "Trabalhos em Destaque"}],
        "t7_work_items": [
            {"emoji": "🚀", "titulo": "Plataforma SaaS",    "desc": "Solução completa de gestão empresarial com impacto em 10K+ usuários.",  "url": "https://wa.me/5511999999999"},
            {"emoji": "💎", "titulo": "Marca Luxury",       "desc": "Rebranding completo para marca premium com presença global.",            "url": "https://wa.me/5511999999999"},
            {"emoji": "📊", "titulo": "Analytics Platform", "desc": "Dashboard inteligente para análise de dados em tempo real.",             "url": "https://wa.me/5511999999999"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t7_ctaf_titulos": [{"valor": "Pronto para Crescer?"}],
        "t7_ctaf_descs":   [{"valor": "Vamos transformar sua visão em uma solução que gera resultados reais e impacto mensurável."}],
        "t7_ctaf_btns":    [{"texto": "Conversar Agora", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t7_footer_infos": [{"valor": "Email: contato@elite.com | Telefone: +55 (99) 99999-9999"}],
        "t7_footer_links": [{"valor": "LinkedIn: linkedin.com/in/seu-perfil | Portfólio: seu-site.com"}],
        "t7_footer_copys": [{"valor": "© 2026 Elite Portfolio. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t7_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t7_nome_cliente,
            "email":     st.session_state.t7_email_cliente,
            "nome_site": st.session_state.t7_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t7_nome_site}",
        },
        "cores": st.session_state.t7_cores,
        "navbar": {
            "logos": st.session_state.t7_logos,
            "links": st.session_state.t7_nav_links,
        },
        "hero": {
            "labels":   st.session_state.t7_hero_labels,
            "titulos":  st.session_state.t7_hero_titulos,
            "descs":    st.session_state.t7_hero_descs,
            "botoes":   st.session_state.t7_hero_btns,
        },
        "estatisticas": st.session_state.t7_stats,
        "expertise": {
            "titulos": st.session_state.t7_exp_titulos,
            "itens":   st.session_state.t7_exp_items,
        },
        "trabalhos": {
            "titulos": st.session_state.t7_work_titulos,
            "itens":   st.session_state.t7_work_items,
        },
        "cta_final": {
            "titulos":    st.session_state.t7_ctaf_titulos,
            "descricoes": st.session_state.t7_ctaf_descs,
            "botoes":     st.session_state.t7_ctaf_btns,
        },
        "footer": {
            "infos":     st.session_state.t7_footer_infos,
            "links":     st.session_state.t7_footer_links,
            "copyright": st.session_state.t7_footer_copys,
        },
        "observacoes": st.session_state.t7_obs,
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

            st.session_state.t7_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t7_nome_cliente,
                key="t7_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t7_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t7_email_cliente,
                key="t7_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, eliteportfolio, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t7_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t7_nome_site,
                key="t7_nome_site_inp",
                placeholder="Ex: eliteportfolio  →  sttacksite.streamlit.app/?c=eliteportfolio",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t7_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t7_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t7_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t7_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t7_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t7_cores) > 1 and _del_btn(f"t7_cor_del_{i}"):
                        st.session_state.t7_cores.pop(i); st.rerun()
            if _add_btn("t7_cor_add", "＋ Adicionar cor"):
                st.session_state.t7_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t7_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t7_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: ELITE ou Seu Nome")
                with c2:
                    if len(st.session_state.t7_logos) > 1 and _del_btn(f"t7_logo_del_{i}"):
                        st.session_state.t7_logos.pop(i); st.rerun()
            if _add_btn("t7_logo_add", "＋ Adicionar logo"):
                st.session_state.t7_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t7_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t7_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t7_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t7_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t7_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t7_nav_links) > 1 and _del_btn(f"t7_nl_del_{i}"):
                        st.session_state.t7_nav_links.pop(i); st.rerun()
            if _add_btn("t7_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t7_nav_links.append({"texto": "Link", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Hero (Apresentação)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno de boas-vindas acima do título)*")
            for i, label in enumerate(st.session_state.t7_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t7_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Bem-vindo, Olá ou seu nome")
                with c2:
                    if len(st.session_state.t7_hero_labels) > 1 and _del_btn(f"t7_h_l_del_{i}"):
                        st.session_state.t7_hero_labels.pop(i); st.rerun()
            if _add_btn("t7_h_l_add", "＋ Adicionar label"):
                st.session_state.t7_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título  *(para destacar uma palavra em gradiente, descreva nas Observações)*")
            for i, t in enumerate(st.session_state.t7_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t7_h_t_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: Transformando Visões em Realidade")
                with c2:
                    if len(st.session_state.t7_hero_titulos) > 1 and _del_btn(f"t7_h_t_del_{i}"):
                        st.session_state.t7_hero_titulos.pop(i); st.rerun()
            if _add_btn("t7_h_t_add", "＋ Adicionar título"):
                st.session_state.t7_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(frase de apresentação profissional)*")
            for i, d in enumerate(st.session_state.t7_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t7_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Descreva sua especialidade e proposta de valor")
                with c2:
                    if len(st.session_state.t7_hero_descs) > 1 and _del_btn(f"t7_h_d_del_{i}"):
                        st.session_state.t7_hero_descs.pop(i); st.rerun()
            if _add_btn("t7_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t7_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botões  *(Texto | URL ou destino | Estilo)*")
            for i, btn in enumerate(st.session_state.t7_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t7_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t7_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t7_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t7_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    st.session_state.t7_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"],
                        index=0 if btn["estilo"] == "primário" else 1,
                        key=f"t7_hb_e_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t7_hero_btns) > 1 and _del_btn(f"t7_hb_del_{i}"):
                        st.session_state.t7_hero_btns.pop(i); st.rerun()
            if _add_btn("t7_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t7_hero_btns.append({"texto": "Novo Botão", "url": "", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas</div>', unsafe_allow_html=True)
            st.caption("Número | Descrição  *(ex: 150+ projetos entregues)*")
            for i, stat in enumerate(st.session_state.t7_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t7_stats[i]["numero"] = st.text_input(
                        "Valor", stat["numero"], key=f"t7_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: 150+")
                with c2:
                    st.session_state.t7_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t7_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Projetos Entregues")
                with c3:
                    if len(st.session_state.t7_stats) > 1 and _del_btn(f"t7_st_del_{i}"):
                        st.session_state.t7_stats.pop(i); st.rerun()
            if _add_btn("t7_st_add", "＋ Adicionar estatística"):
                st.session_state.t7_stats.append({"numero": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. EXPERTISE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧠 Expertise & Serviços</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t7_exp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_exp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t7_et_{i}", label_visibility="collapsed",
                        placeholder="Ex: Expertise ou Serviços")
                with c2:
                    if len(st.session_state.t7_exp_titulos) > 1 and _del_btn(f"t7_et_del_{i}"):
                        st.session_state.t7_exp_titulos.pop(i); st.rerun()
            if _add_btn("t7_et_add", "＋ Adicionar título"):
                st.session_state.t7_exp_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Itens  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t7_exp_items):
                with st.expander(f"Expertise {item['num']}: {item['titulo']}"):
                    st.session_state.t7_exp_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t7_ei_n_{i}",
                        placeholder="Ex: 01, 02...")
                    st.session_state.t7_exp_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t7_ei_t_{i}",
                        placeholder="Nome do serviço ou área de expertise")
                    st.session_state.t7_exp_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t7_ei_d_{i}", height=80,
                        placeholder="Descreva este serviço ou área de atuação")
                    if len(st.session_state.t7_exp_items) > 1:
                        if st.button("🗑 Remover este item", key=f"t7_ei_del_{i}"):
                            st.session_state.t7_exp_items.pop(i); st.rerun()
            if _add_btn("t7_ei_add", "＋ Adicionar item de expertise"):
                st.session_state.t7_exp_items.append({"num": "05", "titulo": "Nova Expertise", "desc": "Descrição da expertise."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. TRABALHOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💼 Trabalhos em Destaque</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t7_work_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_work_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t7_wt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Trabalhos em Destaque ou Portfólio")
                with c2:
                    if len(st.session_state.t7_work_titulos) > 1 and _del_btn(f"t7_wt_del_{i}"):
                        st.session_state.t7_work_titulos.pop(i); st.rerun()
            if _add_btn("t7_wt_add", "＋ Adicionar título"):
                st.session_state.t7_work_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de trabalho  *(clique para expandir e editar cada um)*")
            for i, work in enumerate(st.session_state.t7_work_items):
                with st.expander(f"Trabalho {i+1}: {work['titulo']}"):
                    st.session_state.t7_work_items[i]["emoji"] = st.text_input(
                        "Emoji / Ícone", work["emoji"], key=f"t7_wi_e_{i}",
                        help="Cole um emoji, ex: 🚀 💎 📊 🎨")
                    st.session_state.t7_work_items[i]["titulo"] = st.text_input(
                        "Título", work["titulo"], key=f"t7_wi_t_{i}",
                        placeholder="Nome do projeto ou trabalho")
                    st.session_state.t7_work_items[i]["desc"] = st.text_area(
                        "Descrição", work["desc"], key=f"t7_wi_d_{i}", height=70,
                        placeholder="Cole aqui o texto do depoimento, sem aspas.")
                    st.session_state.t7_work_items[i]["url"] = st.text_input(
                        "URL do trabalho", work["url"], key=f"t7_wi_u_{i}",
                        placeholder="https:// ou descreva o destino",
                        help="Link para o projeto, case ou portfólio completo.")
                    if len(st.session_state.t7_work_items) > 1:
                        if st.button("🗑 Remover este trabalho", key=f"t7_wi_del_{i}"):
                            st.session_state.t7_work_items.pop(i); st.rerun()
            if _add_btn("t7_wi_add", "＋ Adicionar trabalho"):
                st.session_state.t7_work_items.append({"emoji": "✨", "titulo": "Novo Trabalho", "desc": "Descrição do trabalho.", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏁 Chamada Final (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t7_ctaf_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_ctaf_titulos[i]["valor"] = st.text_input(
                        "Título CTA", t["valor"], key=f"t7_ctaft_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pronto para Crescer?")
                with c2:
                    if len(st.session_state.t7_ctaf_titulos) > 1 and _del_btn(f"t7_ctaft_del_{i}"):
                        st.session_state.t7_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t7_ctaft_add", "＋ Adicionar título CTA"):
                st.session_state.t7_ctaf_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t7_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_ctaf_descs[i]["valor"] = st.text_area(
                        "Descrição CTA", d["valor"], key=f"t7_ctafd_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase de encerramento convidando o visitante a entrar em contato")
                with c2:
                    if len(st.session_state.t7_ctaf_descs) > 1 and _del_btn(f"t7_ctafd_del_{i}"):
                        st.session_state.t7_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t7_ctafd_add", "＋ Adicionar descrição CTA"):
                st.session_state.t7_ctaf_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t7_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t7_ctaf_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t7_ctafb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t7_ctaf_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t7_ctafb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t7_ctaf_btns) > 1 and _del_btn(f"t7_ctafb_del_{i}"):
                        st.session_state.t7_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t7_ctafb_add", "＋ Adicionar botão CTA"):
                st.session_state.t7_ctaf_btns.append({"texto": "Novo Botão", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Informações de contato  *(ex: Email | Telefone)*")
            for i, info in enumerate(st.session_state.t7_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_infos[i]["valor"] = st.text_input(
                        "Infos", info["valor"], key=f"t7_finfo_{i}", label_visibility="collapsed",
                        placeholder="Ex: Email: contato@email.com | Tel: (11) 99999-9999")
                with c2:
                    if len(st.session_state.t7_footer_infos) > 1 and _del_btn(f"t7_finfo_del_{i}"):
                        st.session_state.t7_footer_infos.pop(i); st.rerun()
            if _add_btn("t7_finfo_add", "＋ Adicionar linha de contato"):
                st.session_state.t7_footer_infos.append({"valor": "Novo contato"}); st.rerun()

            st.caption("Links sociais  *(ex: LinkedIn | Instagram | Portfólio)*")
            for i, link in enumerate(st.session_state.t7_footer_links):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_links[i]["valor"] = st.text_input(
                        "Links Sociais", link["valor"], key=f"t7_flink_{i}", label_visibility="collapsed",
                        placeholder="Ex: LinkedIn: linkedin.com/in/seuperfil")
                with c2:
                    if len(st.session_state.t7_footer_links) > 1 and _del_btn(f"t7_flink_del_{i}"):
                        st.session_state.t7_footer_links.pop(i); st.rerun()
            if _add_btn("t7_flink_add", "＋ Adicionar linha de links sociais"):
                st.session_state.t7_footer_links.append({"valor": "Nova rede social"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t7_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_footer_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t7_fcopy_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Seu Nome. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t7_footer_copys) > 1 and _del_btn(f"t7_fcopy_del_{i}"):
                        st.session_state.t7_footer_copys.pop(i); st.rerun()
            if _add_btn("t7_fcopy_add", "＋ Adicionar linha de copyright"):
                st.session_state.t7_footer_copys.append({"valor": "Novo texto"}); st.rerun()

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
                3. Cole essa URL no campo correspondente nas seções acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Foto de perfil / hero: <strong>800 × 800 px</strong> (quadrada)<br>
                • Banner: <strong>1920 × 800 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, formato PNG)<br><br>
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
                Ex: "quero mudar a fonte", "adicionar uma seção de depoimentos", "colocar vídeo do YouTube",
                "destacar a palavra X em gradiente", "remover a seção Y", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t7_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t7_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t7_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t7_obs) > 1 and _del_btn(f"t7_obs_del_{i}"):
                        st.session_state.t7_obs.pop(i); st.rerun()
            if _add_btn("t7_obs_add", "＋ Adicionar observação"):
                st.session_state.t7_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t7_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t7_email_cliente.strip() or "@" not in st.session_state.t7_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t7_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t7_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t7_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t7_nome_cliente}'*."
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
