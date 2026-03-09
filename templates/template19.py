import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img19.png"
TEMPLATE_NAME      = "Template 19 — Lemonade Style (Social Impact Insurance)"
TEMPLATE_ID        = "template_19"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t19_nome_cliente":  "",
        "t19_email_cliente": "",
        "t19_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t19_cores": [
            {"nome": "Rosa Principal (Pink)",  "valor": "#ff0083"},
            {"nome": "Texto Escuro (Black)",    "valor": "#222222"},
            {"nome": "Fundo Suave (Soft Pink)", "valor": "#fff5f9"},
            {"nome": "Fundo Branco",            "valor": "#ffffff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t19_nav_logos": [{"valor": "Lemonade"}],
        "t19_nav_links": [
            {"texto": "Seguros",  "url": "seção Nossos Serviços"},
            {"texto": "Giveback", "url": "seção Como Funciona"},
            {"texto": "Sobre",    "url": "seção de Confiança"},
        ],

        # ── HERO (GIVEBACK) ─────────────────────────────────────────────────
        "t19_hero_labels":   [{"valor": "Impacto Total do Giveback"}],
        "t19_hero_counters": [{"valor": "$8,231,044"}],
        "t19_hero_titulos":  [{"valor": "Transformamos o lucro não utilizado em doações."}],
        "t19_hero_btns":     [{"texto": "Verifique nossos preços", "url": "https://wa.me/5511999999999"}],

        # ── COMO FUNCIONA ───────────────────────────────────────────────────
        "t19_process_titulos": [{"valor": "Como o Giveback funciona"}],
        "t19_process_items": [
            {"numero": "1", "titulo": "Você escolhe",    "desc": "Ao contratar o seguro, você escolhe uma causa em que acredita — como meio ambiente ou direitos humanos."},
            {"numero": "2", "titulo": "Nós cuidamos",    "desc": "Usamos seu prêmio para pagar sinistros. Somos uma seguradora B-Corp, focada em transparência."},
            {"numero": "3", "titulo": "O resto é doado", "desc": "O dinheiro que sobra no final do ano não vira bônus para executivos. Ele vai direto para a sua causa escolhida."},
        ],

        # ── CAUSAS ──────────────────────────────────────────────────────────
        "t19_cause_titulos": [{"valor": "Algumas das causas que você apoia"}],
        "t19_cause_items": [
            {"nome": "American Red Cross", "emoji": "🏥"},
            {"nome": "Malala Fund",        "emoji": "🎓"},
            {"nome": "Charity: Water",     "emoji": "💧"},
            {"nome": "The Trevor Project", "emoji": "🌈"},
        ],

        # ── CONFIANÇA ───────────────────────────────────────────────────────
        "t19_trust_titulos": [{"valor": "Seguro para o século 21."}],
        "t19_trust_descs":   [{"valor": "A Lemonade foi construída de forma diferente. Ao recebermos uma taxa fixa e doarmos o restante, queremos pagar seus sinistros rapidamente porque não lucramos ao negá-los."}],
        "t19_trust_certs":   [{"valor": "B-Corp Certificada. Focada no Bem Social."}],
        "t19_trust_imgs":    [{"valor": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t19_foot_brand_names": [{"valor": "Lemonade"}],
        "t19_foot_brand_descs": [{"valor": "Seguros de casa, inquilino, pet e vida. Tudo em um só app."}],
        "t19_foot_cols": [
            {"titulo": "PRODUTOS", "links": [{"texto": "Inquilinos", "url": "seção Nossos Serviços"}, {"texto": "Proprietários", "url": "seção Nossos Serviços"}, {"texto": "Vida", "url": "seção Nossos Serviços"}, {"texto": "Pet", "url": "seção Nossos Serviços"}]},
            {"titulo": "EMPRESA",  "links": [{"texto": "Sobre nós", "url": "seção de Confiança"}, {"texto": "Giveback", "url": "seção Como Funciona"}, {"texto": "Carreiras", "url": "https://wa.me/5511999999999"}]},
            {"titulo": "SIGA-NOS", "links": [{"texto": "Instagram", "url": "https://instagram.com/"}, {"texto": "Twitter", "url": "https://twitter.com/"}, {"texto": "TikTok", "url": "https://tiktok.com/"}]},
        ],
        "t19_foot_copys": [{"valor": "© 2026 Lemonade Inc. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t19_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t19_nome_cliente,
            "email":     st.session_state.t19_email_cliente,
            "nome_site": st.session_state.t19_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t19_nome_site}",
        },
        "cores": st.session_state.t19_cores,
        "navbar": {
            "logos": st.session_state.t19_nav_logos,
            "links": st.session_state.t19_nav_links,
        },
        "hero": {
            "labels":   st.session_state.t19_hero_labels,
            "counter":  st.session_state.t19_hero_counters,
            "titulos":  st.session_state.t19_hero_titulos,
            "botoes":   st.session_state.t19_hero_btns,
        },
        "como_funciona": {
            "titulo_secao": st.session_state.t19_process_titulos,
            "passos":       st.session_state.t19_process_items,
        },
        "causas": {
            "titulo_secao": st.session_state.t19_cause_titulos,
            "itens":        st.session_state.t19_cause_items,
        },
        "confianca": {
            "titulos":       st.session_state.t19_trust_titulos,
            "descs":         st.session_state.t19_trust_descs,
            "certificacoes": st.session_state.t19_trust_certs,
            "imagens":       st.session_state.t19_trust_imgs,
        },
        "footer": {
            "brand_names": st.session_state.t19_foot_brand_names,
            "brand_descs": st.session_state.t19_foot_brand_descs,
            "colunas":     st.session_state.t19_foot_cols,
            "copyright":   st.session_state.t19_foot_copys,
        },
        "observacoes": st.session_state.t19_obs,
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
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

            st.session_state.t19_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t19_nome_cliente,
                key="t19_nome_cliente_inp", placeholder="Ex: Carlos Souza",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t19_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t19_email_cliente,
                key="t19_email_cliente_inp", placeholder="Ex: carlos@empresa.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: lemonade, segurosocial, meugiveback).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t19_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t19_nome_site,
                key="t19_nome_site_inp",
                placeholder="Ex: lemonade  →  sttacksite.streamlit.app/?c=lemonade",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t19_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t19_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t19_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t19_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t19_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t19_cores) > 1 and _del_btn(f"t19_cor_del_{i}"):
                        st.session_state.t19_cores.pop(i); st.rerun()
            if _add_btn("t19_cor_add", "＋ Adicionar cor"):
                st.session_state.t19_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, item in enumerate(st.session_state.t19_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t19_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: SuaMarca ou Nome da Empresa")
                with c2:
                    if len(st.session_state.t19_nav_logos) > 1 and _del_btn(f"t19_logo_del_{i}"):
                        st.session_state.t19_nav_logos.pop(i); st.rerun()
            if _add_btn("t19_logo_add", "＋ Adicionar logo"):
                st.session_state.t19_nav_logos.append({"valor": "Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t19_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t19_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t19_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t19_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t19_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t19_nav_links) > 1 and _del_btn(f"t19_nl_del_{i}"):
                        st.session_state.t19_nav_links.pop(i); st.rerun()
            if _add_btn("t19_nl_add", "＋ Adicionar link"):
                st.session_state.t19_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO (GIVEBACK)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍋 Hero (Giveback / Impacto)</div>', unsafe_allow_html=True)

            st.caption("Label superior  *(texto pequeno acima do contador)*")
            for i, l in enumerate(st.session_state.t19_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t19_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Total de Impacto Gerado")
                with c2:
                    if len(st.session_state.t19_hero_labels) > 1 and _del_btn(f"t19_h_l_del_{i}"):
                        st.session_state.t19_hero_labels.pop(i); st.rerun()
            if _add_btn("t19_h_l_add", "＋ Adicionar label"):
                st.session_state.t19_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Contador de impacto  *(número grande em destaque)*")
            for i, c in enumerate(st.session_state.t19_hero_counters):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_hero_counters[i]["valor"] = st.text_input(
                        "Contador", c["valor"], key=f"t19_h_c_{i}", label_visibility="collapsed",
                        placeholder="Ex: R$ 1.200.000 ou 12.500 pessoas")
                with c2:
                    if len(st.session_state.t19_hero_counters) > 1 and _del_btn(f"t19_h_c_del_{i}"):
                        st.session_state.t19_hero_counters.pop(i); st.rerun()
            if _add_btn("t19_h_c_add", "＋ Adicionar contador"):
                st.session_state.t19_hero_counters.append({"valor": "R$ 0"}); st.rerun()

            st.caption("Título principal  *(texto abaixo do contador)*")
            for i, t in enumerate(st.session_state.t19_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t19_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: Transformamos o lucro não utilizado em doações.")
                with c2:
                    if len(st.session_state.t19_hero_titulos) > 1 and _del_btn(f"t19_h_t_del_{i}"):
                        st.session_state.t19_hero_titulos.pop(i); st.rerun()
            if _add_btn("t19_h_t_add", "＋ Adicionar título"):
                st.session_state.t19_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t19_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t19_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t19_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Fale Conosco")
                with c2:
                    st.session_state.t19_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t19_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t19_hero_btns) > 1 and _del_btn(f"t19_hb_del_{i}"):
                        st.session_state.t19_hero_btns.pop(i); st.rerun()
            if _add_btn("t19_hb_add", "＋ Adicionar botão"):
                st.session_state.t19_hero_btns.append({"texto": "VER PREÇOS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. COMO FUNCIONA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚙️ Como Funciona</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t19_process_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_process_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t19_pr_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Como funciona")
                with c2:
                    if len(st.session_state.t19_process_titulos) > 1 and _del_btn(f"t19_pr_t_del_{i}"):
                        st.session_state.t19_process_titulos.pop(i); st.rerun()
            if _add_btn("t19_pr_t_add", "＋ Adicionar título"):
                st.session_state.t19_process_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Passos do processo  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t19_process_items):
                with st.expander(f"Passo {i+1}: {item['titulo']}"):
                    st.session_state.t19_process_items[i]["numero"] = st.text_input(
                        "Número / Ícone", item["numero"], key=f"t19_pi_n_{i}",
                        placeholder="Ex: 1, 2, 3 ou um emoji")
                    st.session_state.t19_process_items[i]["titulo"] = st.text_input(
                        "Título do Passo", item["titulo"], key=f"t19_pi_t_{i}",
                        placeholder="Ex: Você contrata")
                    st.session_state.t19_process_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t19_pi_d_{i}", height=80,
                        placeholder="Descreva este passo em 1 a 3 frases")
                    if len(st.session_state.t19_process_items) > 1:
                        if st.button("🗑 Remover este passo", key=f"t19_pi_del_{i}"):
                            st.session_state.t19_process_items.pop(i); st.rerun()
            if _add_btn("t19_pi_add", "＋ Adicionar passo"):
                st.session_state.t19_process_items.append({
                    "numero": str(len(st.session_state.t19_process_items) + 1),
                    "titulo": "Novo Passo", "desc": "Descreva este passo aqui."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. CAUSAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Causas / Parceiros Apoiados</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t19_cause_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_cause_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t19_cs_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Causas que apoiamos")
                with c2:
                    if len(st.session_state.t19_cause_titulos) > 1 and _del_btn(f"t19_cs_t_del_{i}"):
                        st.session_state.t19_cause_titulos.pop(i); st.rerun()
            if _add_btn("t19_cs_t_add", "＋ Adicionar título"):
                st.session_state.t19_cause_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de causa / parceiro  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t19_cause_items):
                with st.expander(f"Causa {i+1}: {item['nome']}"):
                    st.session_state.t19_cause_items[i]["emoji"] = st.text_input(
                        "Emoji / Ícone", item["emoji"], key=f"t19_ci_e_{i}",
                        help="Cole um emoji para representar esta causa",
                        placeholder="Ex: 🏥 🎓 💧 🌳")
                    st.session_state.t19_cause_items[i]["nome"] = st.text_input(
                        "Nome da Causa / Parceiro", item["nome"], key=f"t19_ci_n_{i}",
                        placeholder="Ex: Cruz Vermelha Brasileira")
                    if len(st.session_state.t19_cause_items) > 1:
                        if st.button("🗑 Remover esta causa", key=f"t19_ci_del_{i}"):
                            st.session_state.t19_cause_items.pop(i); st.rerun()
            if _add_btn("t19_ci_add", "＋ Adicionar causa"):
                st.session_state.t19_cause_items.append({"nome": "Nova Causa", "emoji": "🌟"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. CONFIANÇA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛡️ Seção de Confiança</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t19_trust_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_trust_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t19_tr_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Solução para o século 21.")
                with c2:
                    if len(st.session_state.t19_trust_titulos) > 1 and _del_btn(f"t19_tr_t_del_{i}"):
                        st.session_state.t19_trust_titulos.pop(i); st.rerun()
            if _add_btn("t19_tr_t_add", "＋ Adicionar título"):
                st.session_state.t19_trust_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(texto de credibilidade)*")
            for i, d in enumerate(st.session_state.t19_trust_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_trust_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t19_tr_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Explique por que sua empresa é diferente e confiável")
                with c2:
                    if len(st.session_state.t19_trust_descs) > 1 and _del_btn(f"t19_tr_d_del_{i}"):
                        st.session_state.t19_trust_descs.pop(i); st.rerun()
            if _add_btn("t19_tr_d_add", "＋ Adicionar descrição"):
                st.session_state.t19_trust_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Certificação / Selo  *(ex: B-Corp, ISO, ANVISA)*")
            for i, c in enumerate(st.session_state.t19_trust_certs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_trust_certs[i]["valor"] = st.text_input(
                        "Certificação", c["valor"], key=f"t19_tr_c_{i}", label_visibility="collapsed",
                        placeholder="Ex: Empresa certificada. Foco no bem social.")
                with c2:
                    if len(st.session_state.t19_trust_certs) > 1 and _del_btn(f"t19_tr_c_del_{i}"):
                        st.session_state.t19_trust_certs.pop(i); st.rerun()
            if _add_btn("t19_tr_c_add", "＋ Adicionar certificação"):
                st.session_state.t19_trust_certs.append({"valor": "Nova Certificação."}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem lateral:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem lateral  *(URL)*")
            for i, img in enumerate(st.session_state.t19_trust_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_trust_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t19_tr_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t19_trust_imgs) > 1 and _del_btn(f"t19_tr_i_del_{i}"):
                        st.session_state.t19_trust_imgs.pop(i); st.rerun()
            if _add_btn("t19_tr_i_add", "＋ Adicionar imagem"):
                st.session_state.t19_trust_imgs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(destacado em cor principal)*")
            for i, name in enumerate(st.session_state.t19_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t19_fn_{i}", label_visibility="collapsed",
                        placeholder="Ex: SuaMarca")
                with c2:
                    if len(st.session_state.t19_foot_brand_names) > 1 and _del_btn(f"t19_fn_del_{i}"):
                        st.session_state.t19_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t19_fn_add", "＋ Adicionar nome"):
                st.session_state.t19_foot_brand_names.append({"valor": "Marca"}); st.rerun()

            st.caption("Descrição da marca  *(texto abaixo do logo)*")
            for i, desc in enumerate(st.session_state.t19_foot_brand_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_foot_brand_descs[i]["valor"] = st.text_area(
                        "Descrição", desc["valor"], key=f"t19_fd_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Breve descrição da empresa para o rodapé")
                with c2:
                    if len(st.session_state.t19_foot_brand_descs) > 1 and _del_btn(f"t19_fd_del_{i}"):
                        st.session_state.t19_foot_brand_descs.pop(i); st.rerun()
            if _add_btn("t19_fd_add", "＋ Adicionar descrição"):
                st.session_state.t19_foot_brand_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Colunas de links  *(clique para expandir e editar cada uma)*")
            for i, col in enumerate(st.session_state.t19_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t19_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t19_fc_t_{i}",
                        placeholder="Ex: PRODUTOS, EMPRESA, SIGA-NOS")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t19_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t19_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t19_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t19_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou seção")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t19_fc_l_del_{i}_{j}"):
                                st.session_state.t19_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t19_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t19_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t19_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t19_fc_del_{i}"):
                            st.session_state.t19_foot_cols.pop(i); st.rerun()
            if _add_btn("t19_fc_add", "＋ Adicionar coluna"):
                st.session_state.t19_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t19_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t19_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t19_foot_copys) > 1 and _del_btn(f"t19_fcp_del_{i}"):
                        st.session_state.t19_foot_copys.pop(i); st.rerun()
            if _add_btn("t19_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t19_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem lateral da seção Confiança acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Imagem lateral (seção Confiança): <strong>800 × 600 px</strong><br>
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
                Ex: "mudar o rosa para um tom mais neon", "adicionar seção de depoimentos",
                "adicionar FAQ", "adicionar seção de preços/planos", "remover seção Causas"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t19_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t19_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t19_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t19_obs) > 1 and _del_btn(f"t19_obs_del_{i}"):
                        st.session_state.t19_obs.pop(i); st.rerun()
            if _add_btn("t19_obs_add", "＋ Adicionar observação"):
                st.session_state.t19_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t19_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t19_email_cliente.strip() or "@" not in st.session_state.t19_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t19_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t19_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t19_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t19_nome_cliente}'*."
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
        page_icon="🍋",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
