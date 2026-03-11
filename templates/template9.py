import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img9.png"
TEMPLATE_NAME      = "Template 9 — WIS (Learntech & Consultoria)"
TEMPLATE_ID        = "template_9"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t9_nome_cliente":  "",
        "t9_email_cliente": "",
        "t9_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t9_cores": [
            {"nome": "Cor Principal (Azul)",     "valor": "#0055ff"},
            {"nome": "Cor de Destaque (Laranja)", "valor": "#ff6600"},
            {"nome": "Cor Escura (Dark)",         "valor": "#1e1e1e"},
            {"nome": "Cor de Fundo (Light)",      "valor": "#f8faff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t9_logos": [{"valor": "WIS."}],
        "t9_nav_links": [
            {"texto": "SOLUÇÕES",   "url": "seção Soluções Corporativas"},
            {"texto": "QUEM SOMOS", "url": "seção Manifesto e Metodologia"},
            {"texto": "BLOG",       "url": "https://wa.me/5511999999999"},
            {"texto": "CONTATO",    "url": "seção de contato ao final da página"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t9_hero_badges":  [{"valor": "Learntech & Consultoria"}],
        "t9_hero_titulos": [{"valor": "Prepare sua empresa para o próximo nível da aprendizagem."}],
        "t9_hero_descs":   [{"valor": "Desenvolvemos soluções de aprendizagem corporativa personalizadas com foco em Cultura e Performance."}],
        "t9_hero_btns":    [{"texto": "FALE COM ESPECIALISTAS", "url": "seção Soluções Corporativas"}],

        # ── SOLUÇÕES ────────────────────────────────────────────────────────
        "t9_sol_labels":  [{"valor": "NOSSAS SOLUÇÕES"}],
        "t9_sol_titulos": [{"valor": "Como podemos ajudar seu negócio?"}],
        "t9_sol_cards": [
            {"icon": "🚀", "titulo": "Learning Campaigns",     "desc": "Campanhas de aprendizagem engajadoras para mudanças de cultura e novos processos.", "card_link_txt": "Saiba mais →", "url": "https://wa.me/5511999999999"},
            {"icon": "🤝", "titulo": "Design de Comunidades",  "desc": "Criamos ecossistemas internos onde o conhecimento flui de forma orgânica e contínua.", "card_link_txt": "Saiba mais →", "url": "https://wa.me/5511999999999"},
            {"icon": "📈", "titulo": "Upskilling & Reskilling", "desc": "Programas intensivos de desenvolvimento de novas competências para o futuro.", "card_link_txt": "Saiba mais →", "url": "https://wa.me/5511999999999"},
        ],

        # ── NÚMEROS (STATS) ─────────────────────────────────────────────────
        "t9_stats": [
            {"valor": "+12",   "label": "Anos de Mercado"},
            {"valor": "+900",  "label": "Projetos Entregues"},
            {"valor": "+100k", "label": "Pessoas Impactadas"},
            {"valor": "+50",   "label": "Grandes Empresas"},
        ],

        # ── MANIFESTO / METODOLOGIA ─────────────────────────────────────────
        "t9_man_badges":  [{"valor": "Nossa Metodologia"}],
        "t9_man_titulos": [{"valor": "Aprendizagem aplicada que gera resultado real."}],
        "t9_man_descs":   [{"valor": "Não acreditamos em treinamentos passivos. Nossa abordagem foca na prática, utilizando tecnologia e inovação para resolver desafios reais de liderança, cultura e vendas."}],
        "t9_man_imgs":    [{"valor": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800"}],
        "t9_man_btns":    [{"texto": "CONHEÇA NOSSA HISTÓRIA", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t9_foot_titulos":  [{"valor": "WIS."}],
        "t9_foot_locais":   [{"valor": "São Paulo | Vitória | Florianópolis"}],
        "t9_foot_contatos": [{"valor": "contato@wis.digital\n(11) 5555-5555"}],
        "t9_foot_sociais": [
            {"nome": "Linkedin",  "url": "https://wa.me/5511999999999"},
            {"nome": "Instagram", "url": "https://wa.me/5511999999999"},
            {"nome": "Spotify",   "url": "https://wa.me/5511999999999"},
        ],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t9_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t9_nome_cliente,
            "email":     st.session_state.t9_email_cliente,
            "nome_site": st.session_state.t9_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t9_nome_site}",
        },
        "cores": st.session_state.t9_cores,
        "navbar": {
            "logos": st.session_state.t9_logos,
            "links": st.session_state.t9_nav_links,
        },
        "hero": {
            "badges":  st.session_state.t9_hero_badges,
            "titulos": st.session_state.t9_hero_titulos,
            "descs":   st.session_state.t9_hero_descs,
            "botoes":  st.session_state.t9_hero_btns,
        },
        "solucoes": {
            "labels":  st.session_state.t9_sol_labels,
            "titulos": st.session_state.t9_sol_titulos,
            "cards":   st.session_state.t9_sol_cards,
        },
        "estatisticas": st.session_state.t9_stats,
        "manifesto": {
            "badges":  st.session_state.t9_man_badges,
            "titulos": st.session_state.t9_man_titulos,
            "descs":   st.session_state.t9_man_descs,
            "imagens": st.session_state.t9_man_imgs,
            "botoes":  st.session_state.t9_man_btns,
        },
        "footer": {
            "logos":    st.session_state.t9_foot_titulos,
            "locais":   st.session_state.t9_foot_locais,
            "contatos": st.session_state.t9_foot_contatos,
            "sociais":  st.session_state.t9_foot_sociais,
        },
        "observacoes": st.session_state.t9_obs,
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

            st.session_state.t9_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t9_nome_cliente,
                key="t9_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t9_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t9_email_cliente,
                key="t9_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: wisdigital, minhaconsultoria, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t9_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t9_nome_site,
                key="t9_nome_site_inp",
                placeholder="Ex: wisdigital  →  sttacksite.streamlit.app/?c=wisdigital",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t9_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t9_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t9_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t9_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t9_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_cores) > 1 and _del_btn(f"t9_cor_del_{i}"):
                        st.session_state.t9_cores.pop(i); st.rerun()
            if _add_btn("t9_cor_add", "＋ Adicionar cor"):
                st.session_state.t9_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t9_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t9_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: WIS. ou Minha Empresa")
                with c2:
                    if len(st.session_state.t9_logos) > 1 and _del_btn(f"t9_logo_del_{i}"):
                        st.session_state.t9_logos.pop(i); st.rerun()
            if _add_btn("t9_logo_add", "＋ Adicionar logo"):
                st.session_state.t9_logos.append({"valor": "NOVA LOGO"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos links:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o link deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t9_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t9_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t9_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t9_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t9_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t9_nav_links) > 1 and _del_btn(f"t9_nl_del_{i}"):
                        st.session_state.t9_nav_links.pop(i); st.rerun()
            if _add_btn("t9_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t9_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Badge  *(etiqueta colorida acima do título)*")
            for i, badge in enumerate(st.session_state.t9_hero_badges):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_hero_badges[i]["valor"] = st.text_input(
                        "Badge", badge["valor"], key=f"t9_h_b_{i}", label_visibility="collapsed",
                        placeholder="Ex: Learntech & Consultoria")
                with c2:
                    if len(st.session_state.t9_hero_badges) > 1 and _del_btn(f"t9_h_b_del_{i}"):
                        st.session_state.t9_hero_badges.pop(i); st.rerun()
            if _add_btn("t9_h_b_add", "＋ Adicionar badge"):
                st.session_state.t9_hero_badges.append({"valor": "Nova Badge"}); st.rerun()

            st.caption("Título  *(para destacar palavras em azul, descreva nas Observações)*")
            for i, t in enumerate(st.session_state.t9_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t9_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Título principal da página")
                with c2:
                    if len(st.session_state.t9_hero_titulos) > 1 and _del_btn(f"t9_h_t_del_{i}"):
                        st.session_state.t9_hero_titulos.pop(i); st.rerun()
            if _add_btn("t9_h_t_add", "＋ Adicionar título"):
                st.session_state.t9_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(para negrito em alguma palavra, descreva nas Observações)*")
            for i, d in enumerate(st.session_state.t9_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t9_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que apresenta sua empresa e proposta de valor")
                with c2:
                    if len(st.session_state.t9_hero_descs) > 1 and _del_btn(f"t9_h_d_del_{i}"):
                        st.session_state.t9_hero_descs.pop(i); st.rerun()
            if _add_btn("t9_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t9_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botões  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t9_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t9_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t9_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t9_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t9_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t9_hero_btns) > 1 and _del_btn(f"t9_hb_del_{i}"):
                        st.session_state.t9_hero_btns.pop(i); st.rerun()
            if _add_btn("t9_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t9_hero_btns.append({"texto": "NOVO BOTÃO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. SOLUÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Soluções Corporativas</div>', unsafe_allow_html=True)

            st.caption("Rótulo da seção  *(texto pequeno acima do título)*")
            for i, l in enumerate(st.session_state.t9_sol_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_sol_labels[i]["valor"] = st.text_input(
                        "Rótulo", l["valor"], key=f"t9_sl_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOSSAS SOLUÇÕES")
                with c2:
                    if len(st.session_state.t9_sol_labels) > 1 and _del_btn(f"t9_sl_del_{i}"):
                        st.session_state.t9_sol_labels.pop(i); st.rerun()
            if _add_btn("t9_sl_add", "＋ Adicionar rótulo"):
                st.session_state.t9_sol_labels.append({"valor": "NOVO RÓTULO"}); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t9_sol_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_sol_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t9_solt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Como podemos ajudar seu negócio?")
                with c2:
                    if len(st.session_state.t9_sol_titulos) > 1 and _del_btn(f"t9_solt_del_{i}"):
                        st.session_state.t9_sol_titulos.pop(i); st.rerun()
            if _add_btn("t9_solt_add", "＋ Adicionar título"):
                st.session_state.t9_sol_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de solução  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t9_sol_cards):
                with st.expander(f"Solução {i+1}: {card['titulo']}"):
                    st.session_state.t9_sol_cards[i]["icon"] = st.text_input(
                        "Ícone / Emoji", card["icon"], key=f"t9_sc_i_{i}",
                        help="Cole um emoji, ex: 🚀 🤝 📈 💡")
                    st.session_state.t9_sol_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t9_sc_t_{i}",
                        placeholder="Nome da solução ou serviço")
                    st.session_state.t9_sol_cards[i]["desc"] = st.text_area(
                        "Descrição", card["desc"], key=f"t9_sc_d_{i}", height=80,
                        placeholder="Cole aqui o texto do depoimento, sem aspas.")
                    st.session_state.t9_sol_cards[i]["card_link_txt"] = st.text_input(
                        "Texto do link", card["card_link_txt"], key=f"t9_sc_lt_{i}",
                        placeholder="Ex: Saiba mais →")
                    st.session_state.t9_sol_cards[i]["url"] = st.text_input(
                        "URL do link", card["url"], key=f"t9_sc_u_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t9_sol_cards) > 1:
                        if st.button("🗑 Remover esta solução", key=f"t9_sc_del_{i}"):
                            st.session_state.t9_sol_cards.pop(i); st.rerun()
            if _add_btn("t9_sc_add", "＋ Adicionar solução"):
                st.session_state.t9_sol_cards.append({
                    "icon": "💡", "titulo": "Nova Solução", "desc": "Descrição da solução.",
                    "card_link_txt": "Saiba mais →", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. NÚMEROS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Prova Social (Números)</div>', unsafe_allow_html=True)
            st.caption("Valor | Descrição  *(ex: +100k pessoas impactadas)*")
            for i, stat in enumerate(st.session_state.t9_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t9_stats[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t9_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: +900")
                with c2:
                    st.session_state.t9_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t9_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Projetos Entregues")
                with c3:
                    if len(st.session_state.t9_stats) > 1 and _del_btn(f"t9_st_del_{i}"):
                        st.session_state.t9_stats.pop(i); st.rerun()
            if _add_btn("t9_st_add", "＋ Adicionar estatística"):
                st.session_state.t9_stats.append({"valor": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. MANIFESTO / METODOLOGIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Manifesto & Metodologia</div>', unsafe_allow_html=True)

            st.caption("Badge  *(etiqueta da seção)*")
            for i, b in enumerate(st.session_state.t9_man_badges):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_man_badges[i]["valor"] = st.text_input(
                        "Badge", b["valor"], key=f"t9_mb_{i}", label_visibility="collapsed",
                        placeholder="Ex: Nossa Metodologia")
                with c2:
                    if len(st.session_state.t9_man_badges) > 1 and _del_btn(f"t9_mb_del_{i}"):
                        st.session_state.t9_man_badges.pop(i); st.rerun()
            if _add_btn("t9_mb_add", "＋ Adicionar badge"):
                st.session_state.t9_man_badges.append({"valor": "Nova Badge"}); st.rerun()

            st.caption("Título")
            for i, t in enumerate(st.session_state.t9_man_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_man_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t9_mt_{i}", label_visibility="collapsed",
                        placeholder="Frase que resume sua filosofia ou metodologia")
                with c2:
                    if len(st.session_state.t9_man_titulos) > 1 and _del_btn(f"t9_mt_del_{i}"):
                        st.session_state.t9_man_titulos.pop(i); st.rerun()
            if _add_btn("t9_mt_add", "＋ Adicionar título"):
                st.session_state.t9_man_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(para negrito em palavras específicas, use Observações)*")
            for i, d in enumerate(st.session_state.t9_man_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_man_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t9_md_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Texto explicando sua abordagem, diferencial ou história")
                with c2:
                    if len(st.session_state.t9_man_descs) > 1 and _del_btn(f"t9_md_del_{i}"):
                        st.session_state.t9_man_descs.pop(i); st.rerun()
            if _add_btn("t9_md_add", "＋ Adicionar descrição"):
                st.session_state.t9_man_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem lateral do Manifesto:</strong> cole a URL de uma foto do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem  *(URL da foto ao lado do texto)*")
            for i, img in enumerate(st.session_state.t9_man_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_man_imgs[i]["valor"] = st.text_input(
                        "URL Imagem", img["valor"], key=f"t9_mi_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t9_man_imgs) > 1 and _del_btn(f"t9_mi_del_{i}"):
                        st.session_state.t9_man_imgs.pop(i); st.rerun()
            if _add_btn("t9_mi_add", "＋ Adicionar imagem"):
                st.session_state.t9_man_imgs.append({"valor": ""}); st.rerun()

            st.caption("Botões  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t9_man_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t9_man_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t9_mbtn_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t9_man_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t9_mbtn_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t9_man_btns) > 1 and _del_btn(f"t9_mbtn_del_{i}"):
                        st.session_state.t9_man_btns.pop(i); st.rerun()
            if _add_btn("t9_mbtn_add", "＋ Adicionar botão"):
                st.session_state.t9_man_btns.append({"texto": "SAIBA MAIS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé & Contato</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, t in enumerate(st.session_state.t9_foot_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_foot_titulos[i]["valor"] = st.text_input(
                        "Logo Footer", t["valor"], key=f"t9_ft_{i}", label_visibility="collapsed",
                        placeholder="Ex: WIS. ou Minha Empresa")
                with c2:
                    if len(st.session_state.t9_foot_titulos) > 1 and _del_btn(f"t9_ft_del_{i}"):
                        st.session_state.t9_foot_titulos.pop(i); st.rerun()
            if _add_btn("t9_ft_add", "＋ Adicionar logo"):
                st.session_state.t9_foot_titulos.append({"valor": "NOVA LOGO"}); st.rerun()

            st.caption("Localidades  *(ex: São Paulo | Vitória | Florianópolis)*")
            for i, l in enumerate(st.session_state.t9_foot_locais):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_foot_locais[i]["valor"] = st.text_input(
                        "Locais", l["valor"], key=f"t9_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: São Paulo | Rio de Janeiro")
                with c2:
                    if len(st.session_state.t9_foot_locais) > 1 and _del_btn(f"t9_fl_del_{i}"):
                        st.session_state.t9_foot_locais.pop(i); st.rerun()
            if _add_btn("t9_fl_add", "＋ Adicionar localidade"):
                st.session_state.t9_foot_locais.append({"valor": "Nova Cidade"}); st.rerun()

            st.caption("Dados de contato  *(email, telefone, endereço...)*")
            for i, c in enumerate(st.session_state.t9_foot_contatos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_foot_contatos[i]["valor"] = st.text_area(
                        "Contato", c["valor"], key=f"t9_fc_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: contato@empresa.com.br&#10;(11) 99999-9999")
                with c2:
                    if len(st.session_state.t9_foot_contatos) > 1 and _del_btn(f"t9_fc_del_{i}"):
                        st.session_state.t9_foot_contatos.pop(i); st.rerun()
            if _add_btn("t9_fc_add", "＋ Adicionar dado de contato"):
                st.session_state.t9_foot_contatos.append({"valor": "novo@email.com"}); st.rerun()

            st.caption("Redes sociais  *(Nome | URL)*")
            for i, soc in enumerate(st.session_state.t9_foot_sociais):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t9_foot_sociais[i]["nome"] = st.text_input(
                        "Rede", soc["nome"], key=f"t9_fs_n_{i}", label_visibility="collapsed",
                        placeholder="Ex: LinkedIn")
                with c2:
                    st.session_state.t9_foot_sociais[i]["url"] = st.text_input(
                        "URL", soc["url"], key=f"t9_fs_u_{i}", label_visibility="collapsed",
                        placeholder="https://linkedin.com/in/...")
                with c3:
                    if len(st.session_state.t9_foot_sociais) > 1 and _del_btn(f"t9_fs_del_{i}"):
                        st.session_state.t9_foot_sociais.pop(i); st.rerun()
            if _add_btn("t9_fs_add", "＋ Adicionar rede social"):
                st.session_state.t9_foot_sociais.append({"nome": "Nova Rede", "url": ""}); st.rerun()

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
                3. Cole a URL no campo de imagem da seção Manifesto acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Foto do Manifesto/lateral: <strong>800 × 600 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
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
                Ex: "quero mudar a fonte", "destacar palavra X em azul no título do hero", "adicionar FAQ",
                "colocar vídeo do YouTube", "negrito na palavra Y", "remover seção Z", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t9_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t9_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t9_obs) > 1 and _del_btn(f"t9_obs_del_{i}"):
                        st.session_state.t9_obs.pop(i); st.rerun()
            if _add_btn("t9_obs_add", "＋ Adicionar observação"):
                st.session_state.t9_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t9_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t9_email_cliente.strip() or "@" not in st.session_state.t9_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t9_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t9_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t9_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t9_nome_cliente}'*."
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
