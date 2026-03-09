import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img10.png"
TEMPLATE_NAME      = "Template 10 — GetResponse Style (Marketing & Automação)"
TEMPLATE_ID        = "template_10"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t10_nome_cliente":  "",
        "t10_email_cliente": "",
        "t10_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t10_cores": [
            {"nome": "Cor Principal (Azul)",     "valor": "#0066FF"},
            {"nome": "Cor de Destaque (Amarelo)", "valor": "#FFD60A"},
            {"nome": "Cor Escura (Texto)",        "valor": "#1a1a1a"},
            {"nome": "Cor de Fundo (Branco)",     "valor": "#ffffff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t10_logos": [{"valor": "GetResponse"}],
        "t10_nav_links": [
            {"texto": "Produto",  "url": "seção Ferramentas Poderosas"},
            {"texto": "Recursos", "url": "seção Estatísticas"},
            {"texto": "Preços",   "url": "seção Chamada para Ação"},
            {"texto": "Sobre",    "url": "seção de contato ao final da página"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t10_hero_labels":  [{"valor": "Email Marketing & Automação"}],
        "t10_hero_titulos": [{"valor": "Não é você, é o algoritmo"}],
        "t10_hero_descs":   [{"valor": "Plataforma de email marketing, automação e landing pages com IA integrada. Crie, teste e venda mais rápido."}],
        "t10_hero_visuals": [{"valor": "📧"}],
        "t10_hero_btns": [
            {"texto": "Comece Grátis", "url": "https://wa.me/5511999999999", "tipo": "Primário"},
            {"texto": "Saiba Mais",    "url": "seção Ferramentas Poderosas", "tipo": "Secundário"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t10_stats": [
            {"valor": "99%",   "label": "Taxa de Entregabilidade para 160+ países"},
            {"valor": "+150",  "label": "Integrações Disponíveis"},
            {"valor": "350K+", "label": "Clientes ao Redor do Mundo"},
            {"valor": "24/7",  "label": "Suporte de Sucesso do Cliente"},
        ],

        # ── FEATURES ────────────────────────────────────────────────────────
        "t10_feat_titulos": [{"valor": "Ferramentas Poderosas para Seu Negócio"}],
        "t10_feat_cards": [
            {"icon": "📧", "titulo": "Email Marketing", "desc": "Envie newsletters ilimitadas com IA que cria linhas de assunto e personaliza conteúdo para seu público."},
            {"icon": "🤖", "titulo": "Automação com IA", "desc": "Crie jornadas automáticas que identificam o melhor momento para contatar seus clientes."},
            {"icon": "🌐", "titulo": "Landing Pages",   "desc": "Publique landing pages ilimitadas com IA que escreve o texto e escolhe o layout ideal."},
        ],

        # ── DEPOIMENTO ──────────────────────────────────────────────────────
        "t10_test_texts":   [{"valor": "Geramos resultados incríveis em vendas com apenas 10 e-mails usando esta plataforma. A automação e a IA mudaram nosso negócio."}],
        "t10_test_authors": [{"valor": "João Silva - CEO da Tech Company"}],

        # ── CTA ─────────────────────────────────────────────────────────────
        "t10_cta_titulos":      [{"valor": "Junte-se a 350.000+ Empresas"}],
        "t10_cta_placeholders": [{"valor": "Seu endereço de e-mail"}],
        "t10_cta_btns":         [{"texto": "Começar Grátis", "url": "https://wa.me/5511999999999"}],
        "t10_cta_notes":        [{"valor": "Teste gratuito de 14 dias | Não precisa de cartão | Cancele a qualquer momento"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t10_foot_cols": [
            {"titulo": "Produto",  "links": [{"texto": "Email Marketing", "url": "https://wa.me/5511999999999"}, {"texto": "Automação", "url": "https://wa.me/5511999999999"}, {"texto": "Landing Pages", "url": "https://wa.me/5511999999999"}, {"texto": "Formulários", "url": "https://wa.me/5511999999999"}]},
            {"titulo": "Recursos", "links": [{"texto": "Blog", "url": "https://wa.me/5511999999999"}, {"texto": "Webinars", "url": "https://wa.me/5511999999999"}, {"texto": "Templates", "url": "https://wa.me/5511999999999"}, {"texto": "Integrações", "url": "https://wa.me/5511999999999"}]},
            {"titulo": "Empresa",  "links": [{"texto": "Sobre Nós", "url": "https://wa.me/5511999999999"}, {"texto": "Carreiras", "url": "https://wa.me/5511999999999"}, {"texto": "Imprensa", "url": "https://wa.me/5511999999999"}, {"texto": "Contato", "url": "https://wa.me/5511999999999"}]},
            {"titulo": "Legal",    "links": [{"texto": "Privacidade", "url": "https://wa.me/5511999999999"}, {"texto": "Termos", "url": "https://wa.me/5511999999999"}, {"texto": "Cookies", "url": "https://wa.me/5511999999999"}, {"texto": "Suporte", "url": "https://wa.me/5511999999999"}]},
        ],
        "t10_foot_copys": [{"valor": "© 2026 GetResponse. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t10_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t10_nome_cliente,
            "email":     st.session_state.t10_email_cliente,
            "nome_site": st.session_state.t10_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t10_nome_site}",
        },
        "cores": st.session_state.t10_cores,
        "navbar": {
            "logos": st.session_state.t10_logos,
            "links": st.session_state.t10_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t10_hero_labels,
            "titulos": st.session_state.t10_hero_titulos,
            "descs":   st.session_state.t10_hero_descs,
            "visuals": st.session_state.t10_hero_visuals,
            "botoes":  st.session_state.t10_hero_btns,
        },
        "estatisticas": st.session_state.t10_stats,
        "features": {
            "titulos": st.session_state.t10_feat_titulos,
            "cards":   st.session_state.t10_feat_cards,
        },
        "depoimento": {
            "textos":  st.session_state.t10_test_texts,
            "autores": st.session_state.t10_test_authors,
        },
        "cta": {
            "titulos":      st.session_state.t10_cta_titulos,
            "placeholders": st.session_state.t10_cta_placeholders,
            "botoes":       st.session_state.t10_cta_btns,
            "notas":        st.session_state.t10_cta_notes,
        },
        "footer": {
            "colunas":   st.session_state.t10_foot_cols,
            "copyright": st.session_state.t10_foot_copys,
        },
        "observacoes": st.session_state.t10_obs,
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

            st.session_state.t10_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t10_nome_cliente,
                key="t10_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t10_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t10_email_cliente,
                key="t10_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: minhaempresa, getresponse2026, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t10_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t10_nome_site,
                key="t10_nome_site_inp",
                placeholder="Ex: minhaempresa  →  sttacksite.streamlit.app/?c=minhaempresa",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t10_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t10_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t10_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t10_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t10_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t10_cores) > 1 and _del_btn(f"t10_cor_del_{i}"):
                        st.session_state.t10_cores.pop(i); st.rerun()
            if _add_btn("t10_cor_add", "＋ Adicionar cor"):
                st.session_state.t10_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t10_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t10_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: Minha Empresa")
                with c2:
                    if len(st.session_state.t10_logos) > 1 and _del_btn(f"t10_logo_del_{i}"):
                        st.session_state.t10_logos.pop(i); st.rerun()
            if _add_btn("t10_logo_add", "＋ Adicionar logo"):
                st.session_state.t10_logos.append({"valor": "NOVA LOGO"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos links:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), qualquer link — ou simplesmente descrever
                para qual seção o link deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t10_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t10_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t10_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t10_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t10_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t10_nav_links) > 1 and _del_btn(f"t10_nl_del_{i}"):
                        st.session_state.t10_nav_links.pop(i); st.rerun()
            if _add_btn("t10_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t10_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📧 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno acima do título)*")
            for i, label in enumerate(st.session_state.t10_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t10_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Email Marketing & Automação")
                with c2:
                    if len(st.session_state.t10_hero_labels) > 1 and _del_btn(f"t10_h_l_del_{i}"):
                        st.session_state.t10_hero_labels.pop(i); st.rerun()
            if _add_btn("t10_h_l_add", "＋ Adicionar label"):
                st.session_state.t10_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal  *(frase de impacto curta)*")
            for i, t in enumerate(st.session_state.t10_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t10_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase de impacto do Hero")
                with c2:
                    if len(st.session_state.t10_hero_titulos) > 1 and _del_btn(f"t10_h_t_del_{i}"):
                        st.session_state.t10_hero_titulos.pop(i); st.rerun()
            if _add_btn("t10_h_t_add", "＋ Adicionar título"):
                st.session_state.t10_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t10_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t10_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que resume sua plataforma ou serviço")
                with c2:
                    if len(st.session_state.t10_hero_descs) > 1 and _del_btn(f"t10_h_d_del_{i}"):
                        st.session_state.t10_hero_descs.pop(i); st.rerun()
            if _add_btn("t10_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t10_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Emoji visual  *(círculo decorativo à direita do hero)*")
            for i, v in enumerate(st.session_state.t10_hero_visuals):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_visuals[i]["valor"] = st.text_input(
                        "Emoji Visual", v["valor"], key=f"t10_h_v_{i}", label_visibility="collapsed",
                        help="Cole um emoji grande que represente seu produto, ex: 📧 🚀 💡 📊")
                with c2:
                    if len(st.session_state.t10_hero_visuals) > 1 and _del_btn(f"t10_h_v_del_{i}"):
                        st.session_state.t10_hero_visuals.pop(i); st.rerun()
            if _add_btn("t10_h_v_add", "＋ Adicionar emoji visual"):
                st.session_state.t10_hero_visuals.append({"valor": "🚀"}); st.rerun()

            st.caption("Botões  *(clique para expandir e editar cada um)*")
            for i, btn in enumerate(st.session_state.t10_hero_btns):
                with st.expander(f"Botão {i+1}: {btn['texto']}"):
                    st.session_state.t10_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t10_hb_t_{i}",
                        placeholder="Texto do botão")
                    st.session_state.t10_hero_btns[i]["url"] = st.text_input(
                        "URL ou destino", btn["url"], key=f"t10_hb_u_{i}",
                        placeholder="https:// ou seção")
                    st.session_state.t10_hero_btns[i]["tipo"] = st.selectbox(
                        "Tipo / Estilo", ["Primário", "Secundário"],
                        index=0 if btn["tipo"] == "Primário" else 1,
                        key=f"t10_hb_tp_{i}")
                    if len(st.session_state.t10_hero_btns) > 1:
                        if st.button("🗑 Remover este botão", key=f"t10_hb_del_{i}"):
                            st.session_state.t10_hero_btns.pop(i); st.rerun()
            if _add_btn("t10_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t10_hero_btns.append({"texto": "NOVO BOTÃO", "url": "", "tipo": "Primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas / Prova Social</div>', unsafe_allow_html=True)
            st.caption("Valor | Descrição  *(ex: 99% taxa de entregabilidade)*")
            for i, stat in enumerate(st.session_state.t10_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t10_stats[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t10_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: 99%")
                with c2:
                    st.session_state.t10_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t10_st_l_{i}", label_visibility="collapsed",
                        placeholder="Descrição do número")
                with c3:
                    if len(st.session_state.t10_stats) > 1 and _del_btn(f"t10_st_del_{i}"):
                        st.session_state.t10_stats.pop(i); st.rerun()
            if _add_btn("t10_st_add", "＋ Adicionar estatística"):
                st.session_state.t10_stats.append({"valor": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. FEATURES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Funcionalidades / Features</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t10_feat_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_feat_titulos[i]["valor"] = st.text_input(
                        "Título Seção", t["valor"], key=f"t10_featt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Ferramentas Poderosas para Seu Negócio")
                with c2:
                    if len(st.session_state.t10_feat_titulos) > 1 and _del_btn(f"t10_featt_del_{i}"):
                        st.session_state.t10_feat_titulos.pop(i); st.rerun()
            if _add_btn("t10_featt_add", "＋ Adicionar título"):
                st.session_state.t10_feat_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t10_feat_cards):
                with st.expander(f"Feature {i+1}: {card['titulo']}"):
                    st.session_state.t10_feat_cards[i]["icon"] = st.text_input(
                        "Emoji Ícone", card["icon"], key=f"t10_fcard_i_{i}",
                        help="Cole um emoji, ex: 📧 🤖 🌐 📊")
                    st.session_state.t10_feat_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t10_fcard_t_{i}",
                        placeholder="Nome da funcionalidade")
                    st.session_state.t10_feat_cards[i]["desc"] = st.text_area(
                        "Descrição", card["desc"], key=f"t10_fcard_d_{i}", height=80,
                        placeholder="Cole aqui o texto do depoimento, sem aspas.")
                    if len(st.session_state.t10_feat_cards) > 1:
                        if st.button("🗑 Remover esta feature", key=f"t10_fcard_del_{i}"):
                            st.session_state.t10_feat_cards.pop(i); st.rerun()
            if _add_btn("t10_fcard_add", "＋ Adicionar funcionalidade"):
                st.session_state.t10_feat_cards.append({"icon": "🚀", "titulo": "Nova Feature", "desc": "Descrição da feature."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. DEPOIMENTO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimento de Cliente</div>', unsafe_allow_html=True)

            st.caption("Texto do depoimento")
            for i, text in enumerate(st.session_state.t10_test_texts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_test_texts[i]["valor"] = st.text_area(
                        "Depoimento", text["valor"], key=f"t10_tt_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Cole aqui o texto do depoimento, sem aspas.")
                with c2:
                    if len(st.session_state.t10_test_texts) > 1 and _del_btn(f"t10_tt_del_{i}"):
                        st.session_state.t10_test_texts.pop(i); st.rerun()
            if _add_btn("t10_tt_add", "＋ Adicionar depoimento"):
                st.session_state.t10_test_texts.append({"valor": "Novo depoimento."}); st.rerun()

            st.caption("Autor e cargo")
            for i, author in enumerate(st.session_state.t10_test_authors):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_test_authors[i]["valor"] = st.text_input(
                        "Autor", author["valor"], key=f"t10_ta_{i}", label_visibility="collapsed",
                        placeholder="Ex: João Silva — CEO da Tech Company")
                with c2:
                    if len(st.session_state.t10_test_authors) > 1 and _del_btn(f"t10_ta_del_{i}"):
                        st.session_state.t10_test_authors.pop(i); st.rerun()
            if _add_btn("t10_ta_add", "＋ Adicionar autor"):
                st.session_state.t10_test_authors.append({"valor": "Nome — Cargo"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. CTA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada para Ação (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t10_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_titulos[i]["valor"] = st.text_input(
                        "Título CTA", t["valor"], key=f"t10_ctat_{i}", label_visibility="collapsed",
                        placeholder="Ex: Junte-se a 350.000+ Empresas")
                with c2:
                    if len(st.session_state.t10_cta_titulos) > 1 and _del_btn(f"t10_ctat_del_{i}"):
                        st.session_state.t10_cta_titulos.pop(i); st.rerun()
            if _add_btn("t10_ctat_add", "＋ Adicionar título CTA"):
                st.session_state.t10_cta_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Placeholder do campo de captação  *(texto dentro do campo de e-mail)*")
            for i, p in enumerate(st.session_state.t10_cta_placeholders):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_placeholders[i]["valor"] = st.text_input(
                        "Placeholder", p["valor"], key=f"t10_ctap_{i}", label_visibility="collapsed",
                        placeholder="Ex: Seu endereço de e-mail")
                with c2:
                    if len(st.session_state.t10_cta_placeholders) > 1 and _del_btn(f"t10_ctap_del_{i}"):
                        st.session_state.t10_cta_placeholders.pop(i); st.rerun()
            if _add_btn("t10_ctap_add", "＋ Adicionar placeholder"):
                st.session_state.t10_cta_placeholders.append({"valor": "Seu e-mail"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t10_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t10_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t10_ctab_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t10_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t10_ctab_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t10_cta_btns) > 1 and _del_btn(f"t10_ctab_del_{i}"):
                        st.session_state.t10_cta_btns.pop(i); st.rerun()
            if _add_btn("t10_ctab_add", "＋ Adicionar botão CTA"):
                st.session_state.t10_cta_btns.append({"texto": "Novo Botão", "url": ""}); st.rerun()

            st.caption("Nota de rodapé do CTA  *(ex: termos, garantias)*")
            for i, n in enumerate(st.session_state.t10_cta_notes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_notes[i]["valor"] = st.text_input(
                        "Nota", n["valor"], key=f"t10_ctan_{i}", label_visibility="collapsed",
                        placeholder="Ex: Teste grátis 14 dias | Sem cartão | Cancele quando quiser")
                with c2:
                    if len(st.session_state.t10_cta_notes) > 1 and _del_btn(f"t10_ctan_del_{i}"):
                        st.session_state.t10_cta_notes.pop(i); st.rerun()
            if _add_btn("t10_ctan_add", "＋ Adicionar nota"):
                st.session_state.t10_cta_notes.append({"valor": "Nova nota"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Dinâmico</div>', unsafe_allow_html=True)
            st.caption("Colunas de links  *(clique para expandir e editar cada uma)*")
            for i, col in enumerate(st.session_state.t10_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t10_foot_cols[i]["titulo"] = st.text_input(
                        "Título da Coluna", col["titulo"], key=f"t10_fcol_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t10_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t10_fcol_lt_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t10_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t10_fcol_lu_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou seção")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t10_fcol_ld_{i}_{j}"):
                                st.session_state.t10_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t10_fcol_la_{i}", "＋ Adicionar link"):
                        st.session_state.t10_foot_cols[i]["links"].append({"texto": "Novo Link", "url": ""}); st.rerun()
                    if len(st.session_state.t10_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t10_fcol_del_{i}"):
                            st.session_state.t10_foot_cols.pop(i); st.rerun()
            if _add_btn("t10_foot_col_add", "＋ Adicionar coluna ao rodapé"):
                st.session_state.t10_foot_cols.append({"titulo": "Nova Coluna", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t10_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t10_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t10_foot_copys) > 1 and _del_btn(f"t10_fcp_del_{i}"):
                        st.session_state.t10_foot_copys.pop(i); st.rerun()
            if _add_btn("t10_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t10_foot_copys.append({"valor": "© 2026"}); st.rerun()

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
                3. Cole a URL no campo de imagem correspondente.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
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
                Ex: "quero mudar a fonte", "alterar o emoji visual do hero", "adicionar FAQ",
                "colocar vídeo do YouTube", "remover seção Y", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t10_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t10_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_obs) > 1 and _del_btn(f"t10_obs_del_{i}"):
                        st.session_state.t10_obs.pop(i); st.rerun()
            if _add_btn("t10_obs_add", "＋ Adicionar observação"):
                st.session_state.t10_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t10_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t10_email_cliente.strip() or "@" not in st.session_state.t10_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t10_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t10_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t10_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t10_nome_cliente}'*."
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
