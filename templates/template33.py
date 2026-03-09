import streamlit as st
import json
import urllib.request

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img33.png"
TEMPLATE_NAME      = "Template 33 — Saulo Simon Style (Creative Developer)"
TEMPLATE_ID        = "template_33"
RESEND_API_KEY     = st.secrets.get("RESEND_KEY", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t33_nome_cliente":  "",
        "t33_email_cliente": "",
        "t33_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t33_cores": [
            {"nome": "Fundo (amarelo vibrante)", "valor": "#ffae00"},
            {"nome": "Preto (texto e contraste)", "valor": "#222222"},
            {"nome": "Branco",                   "valor": "#ffffff"},
            {"nome": "Card (amarelo mais claro)", "valor": "#ffc445"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t33_nav_logos": [{"texto": "ss"}],
        "t33_nav_links": [
            {"texto": "Projetos",     "url": "seção Projetos"},
            {"texto": "Experiências", "url": "seção Sobre"},
            {"texto": "Sobre",        "url": "seção Sobre"},
        ],
        "t33_nav_ctas": [{"texto": "Dê o Play", "url": "seção Rodapé"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t33_hero_titulos":    [{"valor": "SEU NOME AQUI"}],
        "t33_hero_subtitulos": [{"valor": "DESENVOLVEDOR CRIATIVO E ESPECIALISTA EM WEB"}],
        "t33_hero_btns":       [{"texto": "VER MEUS PROJETOS", "url": "seção Projetos"}],
        "t33_hero_simulacoes": [{"img_url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200", "texto": "SIMULAÇÃO INTERATIVA 3D"}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t33_proj_headers": [{"valor": "TRABALHOS EM DESTAQUE"}],
        "t33_proj_items": [
            {"tag": "PROJETO 01",  "titulo": "Nome do Projeto 1", "desc": "Descreva brevemente o que é este projeto e o impacto que gerou.", "img_bg": "#222222", "btn_texto": "VER PROJETO", "btn_url": "https://wa.me/5511999999999"},
            {"tag": "PROJETO 02",  "titulo": "Nome do Projeto 2", "desc": "Descreva brevemente o que é este projeto e o impacto que gerou.", "img_bg": "#ffffff", "btn_texto": "VER PROJETO", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── SOBRE ───────────────────────────────────────────────────────────
        "t33_sobre_imgs":    [{"bg_color": "#222222", "border_color": "white"}],
        "t33_sobre_titulos": [{"valor": "QUEM SOU EU?"}],
        "t33_sobre_textos": [
            {"valor": "Sou um desenvolvedor apaixonado por criar experiências digitais que surpreendem. Especialista em tecnologias web modernas e interfaces de alto impacto."},
            {"valor": "Trabalho com agências e marcas para transformar conceitos em produtos digitais onde o usuário é o protagonista."},
        ],
        "t33_sobre_btns": [{"texto": "MEUS SERVIÇOS", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t33_foot_titulos": [{"valor": "VAMOS TRABALHAR JUNTOS?"}],
        "t33_foot_links": [
            {"texto": "INSTAGRAM", "url": "https://instagram.com/"},
            {"texto": "GITHUB",    "url": "https://github.com/"},
            {"texto": "LINKEDIN",  "url": "https://linkedin.com/"},
            {"texto": "E-MAIL",    "url": "mailto:contato@meusite.com"},
        ],
        "t33_foot_copys": [{"valor": "© 2026 SEU NOME — DESENVOLVIDO COM CÓDIGO E PAIXÃO."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t33_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t33_nome_cliente,
            "email":     st.session_state.t33_email_cliente,
            "nome_site": st.session_state.t33_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t33_nome_site}",
        },
        "cores": st.session_state.t33_cores,
        "navbar": {
            "logos": st.session_state.t33_nav_logos,
            "links": st.session_state.t33_nav_links,
            "cta":   st.session_state.t33_nav_ctas,
        },
        "hero": {
            "titulos":    st.session_state.t33_hero_titulos,
            "subtitulos": st.session_state.t33_hero_subtitulos,
            "botoes":     st.session_state.t33_hero_btns,
            "simulacao":  st.session_state.t33_hero_simulacoes,
        },
        "projetos": {
            "headers": st.session_state.t33_proj_headers,
            "items":   st.session_state.t33_proj_items,
        },
        "sobre": {
            "imagem":  st.session_state.t33_sobre_imgs,
            "titulos": st.session_state.t33_sobre_titulos,
            "textos":  st.session_state.t33_sobre_textos,
            "botoes":  st.session_state.t33_sobre_btns,
        },
        "footer": {
            "titulos":   st.session_state.t33_foot_titulos,
            "links":     st.session_state.t33_foot_links,
            "copyright": st.session_state.t33_foot_copys,
        },
        "observacoes": st.session_state.t33_obs,
    }

def _enviar_resend(payload: dict) -> bool:
    try:
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"
        data = json.dumps({
            "from":    "editor@sttacksite.com.br",
            "to":      [DESTINO_EMAIL],
            "subject": f"[Novo Pedido] {TEMPLATE_NAME} — {payload['identificacao']['nome']}",
            "html":    body_html,
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=data,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type":  "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status in (200, 201)
    except Exception:
        return False


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

            st.session_state.t33_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t33_nome_cliente,
                key="t33_nome_cliente_inp", placeholder="Ex: João Dev",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t33_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t33_email_cliente,
                key="t33_email_cliente_inp", placeholder="Ex: joao@devportfolio.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaodev, meuperfil, creativecoder).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t33_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t33_nome_site,
                key="t33_nome_site_inp",
                placeholder="Ex: joaodev  →  sttacksite.streamlit.app/?c=joaodev",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🟡 <strong>Cor de fundo:</strong> o amarelo vibrante é a identidade marcante deste template.
                Você pode trocar por outra cor de marca (laranja, verde néon, azul elétrico...) —
                basta alterar o campo "Fundo" abaixo. O "Card" deve ser um tom ligeiramente mais claro/escuro que o fundo.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t33_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t33_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t33_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t33_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t33_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t33_cores) > 1 and _del_btn(f"t33_cor_del_{i}"):
                        st.session_state.t33_cores.pop(i); st.rerun()
            if _add_btn("t33_cor_add", "＋ Adicionar cor"):
                st.session_state.t33_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(iniciais em caixa bordada — 2-3 letras)*")
            for i, item in enumerate(st.session_state.t33_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_nav_logos[i]["texto"] = st.text_input(
                        "Iniciais", item["texto"], key=f"t33_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: ss ou JP ou MC",
                        help="Use 1-3 letras, de preferência suas iniciais.")
                with c2:
                    if len(st.session_state.t33_nav_logos) > 1 and _del_btn(f"t33_logo_del_{i}"):
                        st.session_state.t33_nav_logos.pop(i); st.rerun()
            if _add_btn("t33_logo_add", "＋ Adicionar logo"):
                st.session_state.t33_nav_logos.append({"texto": "XX"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t33_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t33_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t33_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t33_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t33_nav_links) > 1 and _del_btn(f"t33_navl_del_{i}"):
                        st.session_state.t33_nav_links.pop(i); st.rerun()
            if _add_btn("t33_navl_add", "＋ Adicionar link"):
                st.session_state.t33_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            st.caption("Link destaque  *(estilo play — aparece com sombra e destaque)*")
            for i, cta in enumerate(st.session_state.t33_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t33_ncta_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Dê o Play ou CONTATO")
                with c2:
                    st.session_state.t33_nav_ctas[i]["url"] = st.text_input(
                        "Destino", cta["url"], key=f"t33_ncta_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou seção")
                with c3:
                    if len(st.session_state.t33_nav_ctas) > 1 and _del_btn(f"t33_ncta_del_{i}"):
                        st.session_state.t33_nav_ctas.pop(i); st.rerun()
            if _add_btn("t33_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t33_nav_ctas.append({"texto": "PLAY", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎮 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> o template usa fonte Bungee (estilo gamer/display) em tamanho grande.
                O título é tipicamente o <strong>seu nome</strong> em CAIXA ALTA. Se quiser quebra de linha
                em um ponto específico, descreva nas Observações — ex: "quebrar o título após 'JOÃO'".
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título  *(fonte display grande — geralmente seu nome em CAIXA ALTA)*")
            for i, t in enumerate(st.session_state.t33_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t33_h_t_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: JOÃO SILVA ou SEU NOME")
                with c2:
                    if len(st.session_state.t33_hero_titulos) > 1 and _del_btn(f"t33_h_t_del_{i}"):
                        st.session_state.t33_hero_titulos.pop(i); st.rerun()
            if _add_btn("t33_h_t_add", "＋ Adicionar título"):
                st.session_state.t33_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo  *(sua especialidade ou tagline em CAIXA ALTA)*")
            for i, stt in enumerate(st.session_state.t33_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", stt["valor"], key=f"t33_h_st_{i}", label_visibility="collapsed",
                        placeholder="Ex: DESENVOLVEDOR WEB E DESIGNER CRIATIVO")
                with c2:
                    if len(st.session_state.t33_hero_subtitulos) > 1 and _del_btn(f"t33_h_st_del_{i}"):
                        st.session_state.t33_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t33_h_st_add", "＋ Adicionar subtítulo"):
                st.session_state.t33_hero_subtitulos.append({"valor": "NOVO SUBTÍTULO"}); st.rerun()

            st.caption("Botão central  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t33_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t33_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t33_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VER MEUS PROJETOS")
                with c2:
                    st.session_state.t33_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t33_hb_u_{i}", label_visibility="collapsed",
                        placeholder="seção Projetos ou https://wa.me/...")
                with c3:
                    if len(st.session_state.t33_hero_btns) > 1 and _del_btn(f"t33_hb_del_{i}"):
                        st.session_state.t33_hero_btns.pop(i); st.rerun()
            if _add_btn("t33_hb_add", "＋ Adicionar botão"):
                st.session_state.t33_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            st.caption("Simulação / Imagem de destaque  *(URL da imagem | Texto em overlay)*")
            for i, sim in enumerate(st.session_state.t33_hero_simulacoes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_simulacoes[i]["img_url"] = st.text_input(
                        "URL Imagem", sim["img_url"], key=f"t33_h_s_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... — 1200×800 px ideal")
                    st.session_state.t33_hero_simulacoes[i]["texto"] = st.text_input(
                        "Texto Overlay", sim["texto"], key=f"t33_h_s_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: CLIQUE PARA EXPLORAR ou deixe em branco")
                with c2:
                    if len(st.session_state.t33_hero_simulacoes) > 1 and _del_btn(f"t33_h_s_del_{i}"):
                        st.session_state.t33_hero_simulacoes.pop(i); st.rerun()
            if _add_btn("t33_h_s_add", "＋ Adicionar imagem"):
                st.session_state.t33_hero_simulacoes.append({"img_url": "", "texto": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Trabalhos em Destaque</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, ph in enumerate(st.session_state.t33_proj_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_proj_headers[i]["valor"] = st.text_input(
                        "Título", ph["valor"], key=f"t33_p_h_{i}", label_visibility="collapsed",
                        placeholder="Ex: TRABALHOS EM DESTAQUE")
                with c2:
                    if len(st.session_state.t33_proj_headers) > 1 and _del_btn(f"t33_p_h_del_{i}"):
                        st.session_state.t33_proj_headers.pop(i); st.rerun()
            if _add_btn("t33_p_h_add", "＋ Adicionar título"):
                st.session_state.t33_proj_headers.append({"valor": "PROJETOS"}); st.rerun()

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t33_proj_items):
                with st.expander(f"Projeto {i+1}: {item['titulo']}"):
                    st.session_state.t33_proj_items[i]["tag"] = st.text_input(
                        "Tag/Categoria", item["tag"], key=f"t33_pi_tag_{i}",
                        placeholder="Ex: PROJETO 01 ou WEBDESIGN")
                    st.session_state.t33_proj_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t33_pi_t_{i}",
                        placeholder="Ex: Nome do Projeto")
                    st.session_state.t33_proj_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t33_pi_d_{i}", height=80,
                        placeholder="Descreva o projeto em 1-2 frases.")
                    st.session_state.t33_proj_items[i]["img_bg"] = st.text_input(
                        "Cor de fundo do card (Hex)", item["img_bg"], key=f"t33_pi_bg_{i}",
                        placeholder="Ex: #222222 (escuro) ou #ffffff (claro)",
                        help="Cor de fundo usada no card enquanto não há imagem. Alterne entre escuro e claro para criar contraste visual.")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t33_proj_items[i]["btn_texto"] = st.text_input(
                            "Texto Botão", item["btn_texto"], key=f"t33_pi_bt_{i}",
                            placeholder="Ex: VER PROJETO")
                    with c2:
                        st.session_state.t33_proj_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t33_pi_bu_{i}",
                            placeholder="https://wa.me/... ou link do projeto")
                    if len(st.session_state.t33_proj_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t33_pi_del_{i}"):
                            st.session_state.t33_proj_items.pop(i); st.rerun()
            if _add_btn("t33_pi_add", "＋ Adicionar projeto"):
                st.session_state.t33_proj_items.append({
                    "tag": f"PROJETO 0{len(st.session_state.t33_proj_items)+1}",
                    "titulo": "Novo Projeto", "desc": "",
                    "img_bg": "#222222", "btn_texto": "VER PROJETO", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🙋 Sobre o Profissional</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, stit in enumerate(st.session_state.t33_sobre_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_sobre_titulos[i]["valor"] = st.text_input(
                        "Título", stit["valor"], key=f"t33_s_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: QUEM SOU EU?")
                with c2:
                    if len(st.session_state.t33_sobre_titulos) > 1 and _del_btn(f"t33_s_t_del_{i}"):
                        st.session_state.t33_sobre_titulos.pop(i); st.rerun()
            if _add_btn("t33_s_t_add", "＋ Adicionar título"):
                st.session_state.t33_sobre_titulos.append({"valor": "QUEM SOU?"}); st.rerun()

            st.caption("Parágrafos de bio  *(um parágrafo por campo)*")
            for i, stxt in enumerate(st.session_state.t33_sobre_textos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_sobre_textos[i]["valor"] = st.text_area(
                        "Texto", stxt["valor"], key=f"t33_s_tx_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Conte um pouco sobre você, sua experiência e o que te motiva.")
                with c2:
                    if len(st.session_state.t33_sobre_textos) > 1 and _del_btn(f"t33_s_tx_del_{i}"):
                        st.session_state.t33_sobre_textos.pop(i); st.rerun()
            if _add_btn("t33_s_tx_add", "＋ Adicionar parágrafo"):
                st.session_state.t33_sobre_textos.append({"valor": ""}); st.rerun()

            st.caption("Botão CTA da seção Sobre  *(Texto | URL)*")
            for i, sbtn in enumerate(st.session_state.t33_sobre_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t33_sobre_btns[i]["texto"] = st.text_input(
                        "Texto", sbtn["texto"], key=f"t33_sb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: MEUS SERVIÇOS")
                with c2:
                    st.session_state.t33_sobre_btns[i]["url"] = st.text_input(
                        "URL", sbtn["url"], key=f"t33_sb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t33_sobre_btns) > 1 and _del_btn(f"t33_sb_del_{i}"):
                        st.session_state.t33_sobre_btns.pop(i); st.rerun()
            if _add_btn("t33_sb_add", "＋ Adicionar botão"):
                st.session_state.t33_sobre_btns.append({"texto": "VER MAIS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏁 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Título grande do rodapé  *(chamada de contato)*")
            for i, ft in enumerate(st.session_state.t33_foot_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_foot_titulos[i]["valor"] = st.text_input(
                        "Título", ft["valor"], key=f"t33_f_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VAMOS TRABALHAR JUNTOS? ou ME CHAMA!")
                with c2:
                    if len(st.session_state.t33_foot_titulos) > 1 and _del_btn(f"t33_f_t_del_{i}"):
                        st.session_state.t33_foot_titulos.pop(i); st.rerun()
            if _add_btn("t33_f_t_add", "＋ Adicionar título"):
                st.session_state.t33_foot_titulos.append({"valor": "VAMOS?"}); st.rerun()

            st.caption("Links sociais e de contato  *(Rede | URL ou mailto:email)*")
            for i, flink in enumerate(st.session_state.t33_foot_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_foot_links[i]["texto"] = st.text_input(
                        "Rede", flink["texto"], key=f"t33_fl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: INSTAGRAM ou E-MAIL")
                with c2:
                    st.session_state.t33_foot_links[i]["url"] = st.text_input(
                        "URL", flink["url"], key=f"t33_fl_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/... ou mailto:email@...")
                with c3:
                    if len(st.session_state.t33_foot_links) > 1 and _del_btn(f"t33_fl_del_{i}"):
                        st.session_state.t33_foot_links.pop(i); st.rerun()
            if _add_btn("t33_fl_add", "＋ Adicionar rede social"):
                st.session_state.t33_foot_links.append({"texto": "REDE", "url": ""}); st.rerun()

            st.caption("Copyright")
            for i, fcp in enumerate(st.session_state.t33_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", fcp["valor"], key=f"t33_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 SEU NOME — DESENVOLVIDO COM CÓDIGO E PAIXÃO.")
                with c2:
                    if len(st.session_state.t33_foot_copys) > 1 and _del_btn(f"t33_fcp_del_{i}"):
                        st.session_state.t33_foot_copys.pop(i); st.rerun()
            if _add_btn("t33_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t33_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS — GUIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Tamanhos recomendados:</strong><br>
                • Simulação/destaque no hero: <strong>1200 × 800 px</strong> (paisagem)<br>
                • Foto de perfil (seção Sobre): <strong>400 × 500 px</strong> (retrato)<br>
                • Thumbnails dos projetos: <strong>800 × 500 px</strong><br><br>
                <strong>Como subir imagens:</strong><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a> (gratuito, sem cadastro).<br>
                2. Faça upload → botão direito na imagem → <em>Copiar endereço da imagem</em>.<br>
                3. Cole no campo correspondente acima.<br><br>
                ❌ <strong>Não conseguiu?</strong> Envie para <strong>sttacksite@gmail.com</strong>
                com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 8. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "manter o amarelo vibrante", "quero quebra de linha no título após meu nome",
                "adicionar seção de habilidades/skills", "adicionar seção de depoimentos"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t33_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t33_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_obs) > 1 and _del_btn(f"t33_obs_del_{i}"):
                        st.session_state.t33_obs.pop(i); st.rerun()
            if _add_btn("t33_obs_add", "＋ Adicionar observação"):
                st.session_state.t33_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t33_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t33_email_cliente.strip() or "@" not in st.session_state.t33_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t33_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t33_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso = _enviar_resend(payload)
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t33_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t33_nome_cliente}'*."
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
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
