import streamlit as st
import json
import urllib.request

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img35.png"
TEMPLATE_NAME      = "Template 35 — Good Secrets Style (Nutrição Chic)"
TEMPLATE_ID        = "template_35"
RESEND_API_KEY     = st.secrets.get("RESEND_KEY", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t35_nome_cliente":  "",
        "t35_email_cliente": "",
        "t35_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t35_cores": [
            {"nome": "Fundo (off-white quente)",  "valor": "#FDF9F3"},
            {"nome": "Escuro (títulos e texto)",  "valor": "#2D1B14"},
            {"nome": "Texto (marrom suave)",       "valor": "#4A3B33"},
            {"nome": "Acento (bege rosado)",       "valor": "#E8D5C4"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t35_nav_logos": [{"texto": "GOOD SECRETS"}],
        "t35_nav_links": [
            {"texto": "Suplementos", "url": "seção Produtos"},
            {"texto": "Ritual",      "url": "seção Narrativa"},
            {"texto": "Sobre",       "url": "seção Narrativa"},
        ],
        "t35_nav_ctas": [{"texto": "Comprar", "url": "https://wa.me/5511999999999"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t35_hero_labels":  [{"valor": "O SEGREDO DA LONGEVIDADE"}],
        "t35_hero_titulos": [{"valor": "Nutrição consciente para mentes modernas."}],
        "t35_hero_descs":   [{"valor": "Acreditamos que o bem-estar começa de dentro para fora. Criamos suplementos puros, potentes e elegantes para o seu ritual diário."}],
        "t35_hero_btns":    [{"texto": "VER COLEÇÃO", "url": "seção Produtos"}],
        "t35_hero_imgs":    [{"url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=800"}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t35_prod_headers": [{"valor": "Feito para o seu melhor eu."}],
        "t35_prod_items": [
            {"titulo": "FOCO",  "desc": "Clareza cognitiva e energia mental sustentada.", "url": "https://wa.me/5511999999999"},
            {"titulo": "CALMA", "desc": "Equilíbrio para os dias de alta intensidade.",   "url": "https://wa.me/5511999999999"},
            {"titulo": "VITAL", "desc": "Recuperação profunda e suporte imunológico.",    "url": "https://wa.me/5511999999999"},
        ],

        # ── NARRATIVA ───────────────────────────────────────────────────────
        "t35_narr_titulos": [{"valor": "A pureza é a nossa única regra."}],
        "t35_narr_descs":   [{"valor": "Cada ingrediente em nossos suplementos é selecionado com rigor científico e ético. Não usamos enchimentos, não usamos atalhos. Apenas o que seu corpo realmente precisa."}],
        "t35_narr_links":   [{"texto": "Conheça nossa origem →", "url": "https://wa.me/5511999999999"}],
        "t35_narr_imgs":    [{"url": "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=800"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t35_foot_logos": [{"texto": "GOOD SECRETS"}],
        "t35_foot_descs": [{"texto": "Inspirando rituais de saúde desde 2026."}],
        "t35_foot_cols": [
            {
                "titulo": "MENU",
                "links": [
                    {"texto": "Produtos",     "url": "https://wa.me/5511999999999"},
                    {"texto": "Nosso Estudo", "url": "https://wa.me/5511999999999"},
                    {"texto": "Assinatura",   "url": "https://wa.me/5511999999999"},
                    {"texto": "Imprensa",     "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "Instagram", "url": "https://instagram.com/"},
                    {"texto": "E-mail",    "url": "mailto:contato@meusite.com"},
                    {"texto": "Lojas",     "url": "https://wa.me/5511999999999"},
                ]
            }
        ],
        "t35_foot_copys":  [{"valor": "© 2026 GOOD SECRETS BRASIL."}],
        "t35_foot_legals": [{"texto": "PRIVACIDADE & TERMOS", "url": "https://wa.me/5511999999999"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t35_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t35_nome_cliente,
            "email":     st.session_state.t35_email_cliente,
            "nome_site": st.session_state.t35_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t35_nome_site}",
        },
        "cores": st.session_state.t35_cores,
        "navbar": {
            "logos": st.session_state.t35_nav_logos,
            "links": st.session_state.t35_nav_links,
            "cta":   st.session_state.t35_nav_ctas,
        },
        "hero": {
            "labels":  st.session_state.t35_hero_labels,
            "titulos": st.session_state.t35_hero_titulos,
            "descs":   st.session_state.t35_hero_descs,
            "botoes":  st.session_state.t35_hero_btns,
            "imagens": st.session_state.t35_hero_imgs,
        },
        "produtos": {
            "headers": st.session_state.t35_prod_headers,
            "items":   st.session_state.t35_prod_items,
        },
        "narrativa": {
            "titulos": st.session_state.t35_narr_titulos,
            "descs":   st.session_state.t35_narr_descs,
            "links":   st.session_state.t35_narr_links,
            "imagens": st.session_state.t35_narr_imgs,
        },
        "footer": {
            "logos":     st.session_state.t35_foot_logos,
            "descs":     st.session_state.t35_foot_descs,
            "colunas":   st.session_state.t35_foot_cols,
            "copyright": st.session_state.t35_foot_copys,
            "legal":     st.session_state.t35_foot_legals,
        },
        "observacoes": st.session_state.t35_obs,
    }

def _enviar_resend(payload: dict) -> bool:
    try:
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"
        data = json.dumps({
            "from":    "onboarding@resend.dev",
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

            st.session_state.t35_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t35_nome_cliente,
                key="t35_nome_cliente_inp", placeholder="Ex: Ana Nutrição",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t35_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t35_email_cliente,
                key="t35_email_cliente_inp", placeholder="Ex: ana@goodsecrets.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: goodsecrets, meusuplemenos, ritualdebem).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t35_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t35_nome_site,
                key="t35_nome_site_inp",
                placeholder="Ex: goodsecrets  →  sttacksite.streamlit.app/?c=goodsecrets",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🌿 <strong>Paleta quente e natural:</strong> tons de off-white, marrom e bege rosado.
                O "Acento" é usado em fundos de seção e detalhes — mantenha tons pastéis/neutros
                para a estética de bem-estar, ou adapte para as cores da sua marca.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t35_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t35_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t35_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t35_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t35_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t35_cores) > 1 and _del_btn(f"t35_cor_del_{i}"):
                        st.session_state.t35_cores.pop(i); st.rerun()
            if _add_btn("t35_cor_add", "＋ Adicionar cor"):
                st.session_state.t35_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(nome da marca com letras espaçadas — CAIXA ALTA)*")
            for i, item in enumerate(st.session_state.t35_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_nav_logos[i]["texto"] = st.text_input(
                        "Logo", item["texto"], key=f"t35_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: GOOD SECRETS ou NOME DA MARCA")
                with c2:
                    if len(st.session_state.t35_nav_logos) > 1 and _del_btn(f"t35_logo_del_{i}"):
                        st.session_state.t35_nav_logos.pop(i); st.rerun()
            if _add_btn("t35_logo_add", "＋ Adicionar logo"):
                st.session_state.t35_nav_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t35_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t35_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t35_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t35_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t35_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t35_nav_links) > 1 and _del_btn(f"t35_navl_del_{i}"):
                        st.session_state.t35_nav_links.pop(i); st.rerun()
            if _add_btn("t35_navl_add", "＋ Adicionar link"):
                st.session_state.t35_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            st.caption("Botão destaque  *(com sublinhado — geralmente CTA de compra)*")
            for i, cta in enumerate(st.session_state.t35_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t35_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t35_ncta_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Comprar ou PEDIR AGORA")
                with c2:
                    st.session_state.t35_nav_ctas[i]["url"] = st.text_input(
                        "URL", cta["url"], key=f"t35_ncta_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link da loja")
                with c3:
                    if len(st.session_state.t35_nav_ctas) > 1 and _del_btn(f"t35_ncta_del_{i}"):
                        st.session_state.t35_nav_ctas.pop(i); st.rerun()
            if _add_btn("t35_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t35_nav_ctas.append({"texto": "CTA", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> escreva normalmente. Se quiser parte em itálico
                (estilo tipográfico editorial), descreva nas Observações —
                ex: "quero 'mentes modernas.' em itálico".<br>
                <strong>Imagem:</strong> aparece em forma arredondada no topo — ideal com produto em fundo neutro.
                Tamanho ideal: <strong>600 × 800 px</strong> (retrato).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Label  *(texto espaçado em maiúsculas acima do título)*")
            for i, l in enumerate(st.session_state.t35_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t35_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: O SEGREDO DA LONGEVIDADE")
                with c2:
                    if len(st.session_state.t35_hero_labels) > 1 and _del_btn(f"t35_h_l_del_{i}"):
                        st.session_state.t35_hero_labels.pop(i); st.rerun()
            if _add_btn("t35_h_l_add", "＋ Adicionar label"):
                st.session_state.t35_hero_labels.append({"valor": ""}); st.rerun()

            st.caption("Título principal  *(fonte serif leve — editorial e elegante)*")
            for i, t in enumerate(st.session_state.t35_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t35_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Nutrição consciente para mentes modernas.")
                with c2:
                    if len(st.session_state.t35_hero_titulos) > 1 and _del_btn(f"t35_h_t_del_{i}"):
                        st.session_state.t35_hero_titulos.pop(i); st.rerun()
            if _add_btn("t35_h_t_add", "＋ Adicionar título"):
                st.session_state.t35_hero_titulos.append({"valor": ""}); st.rerun()

            st.caption("Descrição  *(parágrafo de apoio abaixo do título)*")
            for i, d in enumerate(st.session_state.t35_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t35_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Criamos suplementos puros para o seu ritual diário.")
                with c2:
                    if len(st.session_state.t35_hero_descs) > 1 and _del_btn(f"t35_h_d_del_{i}"):
                        st.session_state.t35_hero_descs.pop(i); st.rerun()
            if _add_btn("t35_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t35_hero_descs.append({"valor": ""}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t35_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t35_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t35_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VER COLEÇÃO")
                with c2:
                    st.session_state.t35_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t35_hb_u_{i}", label_visibility="collapsed",
                        placeholder="seção Produtos ou https://wa.me/...")
                with c3:
                    if len(st.session_state.t35_hero_btns) > 1 and _del_btn(f"t35_hb_del_{i}"):
                        st.session_state.t35_hero_btns.pop(i); st.rerun()
            if _add_btn("t35_hb_add", "＋ Adicionar botão"):
                st.session_state.t35_hero_btns.append({"texto": "VER MAIS", "url": ""}); st.rerun()

            st.caption("Imagem do hero  *(forma arredondada — 600×800 px, produto em fundo neutro)*")
            for i, img in enumerate(st.session_state.t35_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_hero_imgs[i]["url"] = st.text_input(
                        "URL", img["url"], key=f"t35_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... — 600×800 px ideal")
                with c2:
                    if len(st.session_state.t35_hero_imgs) > 1 and _del_btn(f"t35_h_i_del_{i}"):
                        st.session_state.t35_hero_imgs.pop(i); st.rerun()
            if _add_btn("t35_h_i_add", "＋ Adicionar imagem"):
                st.session_state.t35_hero_imgs.append({"url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💊 Produtos (Cards)</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(aparece sobre fundo de acento — tom bege)*")
            for i, ph in enumerate(st.session_state.t35_prod_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_prod_headers[i]["valor"] = st.text_input(
                        "Título", ph["valor"], key=f"t35_p_h_{i}", label_visibility="collapsed",
                        placeholder="Ex: Feito para o seu melhor eu.")
                with c2:
                    if len(st.session_state.t35_prod_headers) > 1 and _del_btn(f"t35_p_h_del_{i}"):
                        st.session_state.t35_prod_headers.pop(i); st.rerun()
            if _add_btn("t35_p_h_add", "＋ Adicionar título"):
                st.session_state.t35_prod_headers.append({"valor": ""}); st.rerun()

            st.caption("Cards de produto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t35_prod_items):
                with st.expander(f"Produto {i+1}: {item['titulo']}"):
                    st.session_state.t35_prod_items[i]["titulo"] = st.text_input(
                        "Nome do Produto", item["titulo"], key=f"t35_pi_t_{i}",
                        placeholder="Ex: FOCO ou NOME DO SUPLEMENTO")
                    st.session_state.t35_prod_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t35_pi_d_{i}", height=80,
                        placeholder="Ex: Clareza cognitiva e energia mental sustentada.")
                    st.session_state.t35_prod_items[i]["url"] = st.text_input(
                        "URL de Compra", item["url"], key=f"t35_pi_u_{i}",
                        placeholder="https://wa.me/... ou link da loja")
                    if len(st.session_state.t35_prod_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t35_pi_del_{i}"):
                            st.session_state.t35_prod_items.pop(i); st.rerun()
            if _add_btn("t35_pi_add", "＋ Adicionar produto"):
                st.session_state.t35_prod_items.append({"titulo": "NOVO PRODUTO", "desc": "", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. NARRATIVA / SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Narrativa / Sobre a Marca</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📝 Esta seção combina texto à esquerda e imagem à direita. É o espaço para contar a história
                da sua marca, sua filosofia e diferenciais. Ideal para criar conexão emocional com o cliente.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título da narrativa  *(serif leve e elegante)*")
            for i, nt in enumerate(st.session_state.t35_narr_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_narr_titulos[i]["valor"] = st.text_area(
                        "Título", nt["valor"], key=f"t35_n_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: A pureza é a nossa única regra.")
                with c2:
                    if len(st.session_state.t35_narr_titulos) > 1 and _del_btn(f"t35_n_t_del_{i}"):
                        st.session_state.t35_narr_titulos.pop(i); st.rerun()
            if _add_btn("t35_n_t_add", "＋ Adicionar título"):
                st.session_state.t35_narr_titulos.append({"valor": ""}); st.rerun()

            st.caption("Descrição")
            for i, nd in enumerate(st.session_state.t35_narr_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_narr_descs[i]["valor"] = st.text_area(
                        "Descrição", nd["valor"], key=f"t35_n_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Conte a história e os valores da sua marca em 2-3 frases.")
                with c2:
                    if len(st.session_state.t35_narr_descs) > 1 and _del_btn(f"t35_n_d_del_{i}"):
                        st.session_state.t35_narr_descs.pop(i); st.rerun()
            if _add_btn("t35_n_d_add", "＋ Adicionar descrição"):
                st.session_state.t35_narr_descs.append({"valor": ""}); st.rerun()

            st.caption("Link sublinhado  *(Texto | URL — estilo 'saiba mais →')*")
            for i, nl in enumerate(st.session_state.t35_narr_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t35_narr_links[i]["texto"] = st.text_input(
                        "Texto", nl["texto"], key=f"t35_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Conheça nossa origem →")
                with c2:
                    st.session_state.t35_narr_links[i]["url"] = st.text_input(
                        "URL", nl["url"], key=f"t35_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t35_narr_links) > 1 and _del_btn(f"t35_nl_del_{i}"):
                        st.session_state.t35_narr_links.pop(i); st.rerun()
            if _add_btn("t35_nl_add", "＋ Adicionar link"):
                st.session_state.t35_narr_links.append({"texto": "Saiba mais →", "url": ""}); st.rerun()

            st.caption("Imagem lateral  *(800×600 px, produto ou ambiente — fundo claro/neutro)*")
            for i, ni in enumerate(st.session_state.t35_narr_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_narr_imgs[i]["url"] = st.text_input(
                        "URL", ni["url"], key=f"t35_n_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... — 800×600 px ideal")
                with c2:
                    if len(st.session_state.t35_narr_imgs) > 1 and _del_btn(f"t35_n_i_del_{i}"):
                        st.session_state.t35_narr_imgs.pop(i); st.rerun()
            if _add_btn("t35_n_i_add", "＋ Adicionar imagem"):
                st.session_state.t35_narr_imgs.append({"url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, fl in enumerate(st.session_state.t35_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_foot_logos[i]["texto"] = st.text_input(
                        "Logo", fl["texto"], key=f"t35_f_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: GOOD SECRETS ou NOME DA MARCA")
                with c2:
                    if len(st.session_state.t35_foot_logos) > 1 and _del_btn(f"t35_f_l_del_{i}"):
                        st.session_state.t35_foot_logos.pop(i); st.rerun()
            if _add_btn("t35_f_l_add", "＋ Adicionar logo"):
                st.session_state.t35_foot_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Slogan / Descrição curta")
            for i, fd in enumerate(st.session_state.t35_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_foot_descs[i]["texto"] = st.text_input(
                        "Slogan", fd["texto"], key=f"t35_f_d_{i}", label_visibility="collapsed",
                        placeholder="Ex: Inspirando rituais de saúde desde 2026.")
                with c2:
                    if len(st.session_state.t35_foot_descs) > 1 and _del_btn(f"t35_f_d_del_{i}"):
                        st.session_state.t35_foot_descs.pop(i); st.rerun()
            if _add_btn("t35_f_d_add", "＋ Adicionar descrição"):
                st.session_state.t35_foot_descs.append({"texto": ""}); st.rerun()

            st.caption("Colunas de links no rodapé")
            for i, col in enumerate(st.session_state.t35_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t35_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t35_fc_t_{i}",
                        placeholder="Ex: MENU ou CONTATO")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 5, 1])
                        with c1:
                            st.session_state.t35_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t35_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto")
                        with c2:
                            st.session_state.t35_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t35_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https://")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t35_fc_l_del_{i}_{j}"):
                                st.session_state.t35_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t35_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t35_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t35_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t35_fc_del_{i}"):
                            st.session_state.t35_foot_cols.pop(i); st.rerun()
            if _add_btn("t35_fc_add", "＋ Adicionar coluna"):
                st.session_state.t35_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "LINK", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, fcp in enumerate(st.session_state.t35_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", fcp["valor"], key=f"t35_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DA MARCA.")
                with c2:
                    if len(st.session_state.t35_foot_copys) > 1 and _del_btn(f"t35_fcp_del_{i}"):
                        st.session_state.t35_foot_copys.pop(i); st.rerun()
            if _add_btn("t35_fcp_add", "＋ Adicionar linha"):
                st.session_state.t35_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Links legais  *(Privacidade, Termos, etc.)*")
            for i, flg in enumerate(st.session_state.t35_foot_legals):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t35_foot_legals[i]["texto"] = st.text_input(
                        "Texto", flg["texto"], key=f"t35_flg_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: PRIVACIDADE & TERMOS")
                with c2:
                    st.session_state.t35_foot_legals[i]["url"] = st.text_input(
                        "URL", flg["url"], key=f"t35_flg_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t35_foot_legals) > 1 and _del_btn(f"t35_flg_del_{i}"):
                        st.session_state.t35_foot_legals.pop(i); st.rerun()
            if _add_btn("t35_flg_add", "＋ Adicionar link legal"):
                st.session_state.t35_foot_legals.append({"texto": "TERMOS", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS — GUIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Tamanhos recomendados:</strong><br>
                • Hero (produto em forma arredondada): <strong>600 × 800 px</strong>
                (retrato, produto sobre fundo neutro/off-white)<br>
                • Narrativa (imagem lateral): <strong>800 × 600 px</strong>
                (produto, ingredientes ou ambiente clean)<br><br>
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
                Ex: "manter paleta quente e tons naturais", "quero 'mentes modernas.' em itálico no título",
                "adicionar seção de depoimentos", "adicionar seção de ingredientes ou FAQ"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t35_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t35_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t35_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t35_obs) > 1 and _del_btn(f"t35_obs_del_{i}"):
                        st.session_state.t35_obs.pop(i); st.rerun()
            if _add_btn("t35_obs_add", "＋ Adicionar observação"):
                st.session_state.t35_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t35_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t35_email_cliente.strip() or "@" not in st.session_state.t35_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t35_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t35_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso = _enviar_resend(payload)
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t35_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t35_nome_cliente}'*."
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
        page_icon="💊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
