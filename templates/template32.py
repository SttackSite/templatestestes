import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img32.png"
TEMPLATE_NAME      = "Template 32 — SCENCO Style (Museum & Heritage)"
TEMPLATE_ID        = "template_32"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t32_nome_cliente":  "",
        "t32_email_cliente": "",
        "t32_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t32_cores": [
            {"nome": "Fundo (off-white)",  "valor": "#F5F5F0"},
            {"nome": "Preto (Principal)",  "valor": "#1A1A1A"},
            {"nome": "Azul (Destaque)",    "valor": "#0070FF"},
            {"nome": "Dourado (Acento)",   "valor": "#B58D3D"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t32_nav_logos": [{"texto": "SCENCO"}],
        "t32_nav_links": [
            {"texto": "Exposições", "url": "seção Coleções"},
            {"texto": "Coleções",   "url": "seção Coleções"},
            {"texto": "História",   "url": "seção Mapa"},
        ],
        "t32_nav_ctas": [{"texto": "Explorar →", "url": "seção Mapa"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t32_hero_labels": [{"valor": "Museu Digital do Patrimônio Mundial"}],
        "t32_hero_titulos": [{"valor": "UMA JORNADA PELO TEMPO."}],
        "t32_hero_imgs":   [{"url": "https://images.unsplash.com/photo-1548013146-72479768bbaa?w=1600"}],
        "t32_hero_quotes": [{"valor": "O patrimônio é o nosso legado do passado, o que vivemos hoje e o que transmitimos às gerações futuras."}],

        # ── COLEÇÃO ─────────────────────────────────────────────────────────
        "t32_col_items": [
            {
                "lado": "Esquerda",
                "label": "Arquitetura e Ruínas",
                "titulo": "Templos de Angkor Wat",
                "desc": "Explore a complexidade do maior monumento religioso do mundo, uma obra-prima da civilização Khmer que resistiu aos séculos.",
                "btn_texto": "VER COLEÇÃO COMPLETA",
                "btn_url": "https://wa.me/5511999999999",
                "img_url": "https://images.unsplash.com/photo-1569350080881-22442426302e?w=800",
            },
            {
                "lado": "Direita",
                "label": "Arquitetura e Ruínas",
                "titulo": "A Magia de Mont-Saint-Michel",
                "desc": "Uma abadia gótica situada em uma ilha rochosa no coração de uma baía imensa, desafiando as marés e o horizonte.",
                "btn_texto": "EXPLORAR LOCAL",
                "btn_url": "https://wa.me/5511999999999",
                "img_url": "https://images.unsplash.com/photo-1503917988258-f197e2f4192d?w=800",
            },
        ],

        # ── MAPA GLOBAL ─────────────────────────────────────────────────────
        "t32_map_headers": [{"label": "Mapa Global", "titulo": "Onde a História Vive"}],
        "t32_map_imgs":    [{"url": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=1600", "texto": "CARREGANDO MAPA INTERATIVO..."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t32_foot_brands": [{"nome": "SCENCO", "desc": "O Museu do Patrimônio Mundial é uma iniciativa para preservar a memória cultural através da inovação digital."}],
        "t32_foot_cols": [
            {
                "titulo": "EXPLORAR",
                "links": [
                    {"texto": "África",         "url": "https://wa.me/5511999999999"},
                    {"texto": "Américas",       "url": "https://wa.me/5511999999999"},
                    {"texto": "Ásia e Pacífico","url": "https://wa.me/5511999999999"},
                    {"texto": "Europa",         "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "CRÉDITOS",
                "links": [
                    {"texto": "Curadoria Digital",      "url": "https://wa.me/5511999999999"},
                    {"texto": "Parceiros Tecnológicos", "url": "https://wa.me/5511999999999"},
                    {"texto": "Open Data",              "url": "https://wa.me/5511999999999"},
                ]
            },
            {
                "titulo": "SIGA-NOS",
                "links": [
                    {"texto": "Instagram", "url": "https://instagram.com/"},
                    {"texto": "Twitter",   "url": "https://twitter.com/"},
                    {"texto": "Youtube",   "url": "https://youtube.com/"},
                ]
            }
        ],
        "t32_foot_copys": [{"valor": "NOME DO MUSEU © 2026."}],
        "t32_foot_legal": [
            {"texto": "POLÍTICAS DE PRESERVAÇÃO DIGITAL", "url": "https://wa.me/5511999999999"},
            {"texto": "TERMOS DE USO",                    "url": "https://wa.me/5511999999999"},
        ],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t32_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t32_nome_cliente,
            "email":     st.session_state.t32_email_cliente,
            "nome_site": st.session_state.t32_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t32_nome_site}",
        },
        "cores": st.session_state.t32_cores,
        "navbar": {
            "logos": st.session_state.t32_nav_logos,
            "links": st.session_state.t32_nav_links,
            "cta":   st.session_state.t32_nav_ctas,
        },
        "hero": {
            "labels":  st.session_state.t32_hero_labels,
            "titulos": st.session_state.t32_hero_titulos,
            "imagens": st.session_state.t32_hero_imgs,
            "quotes":  st.session_state.t32_hero_quotes,
        },
        "colecao": st.session_state.t32_col_items,
        "mapa": {
            "headers": st.session_state.t32_map_headers,
            "imagens": st.session_state.t32_map_imgs,
        },
        "footer": {
            "marca":     st.session_state.t32_foot_brands,
            "colunas":   st.session_state.t32_foot_cols,
            "copyright": st.session_state.t32_foot_copys,
            "legal":     st.session_state.t32_foot_legal,
        },
        "observacoes": st.session_state.t32_obs,
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

            st.session_state.t32_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t32_nome_cliente,
                key="t32_nome_cliente_inp", placeholder="Ex: Carlos Scenco",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t32_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t32_email_cliente,
                key="t32_email_cliente_inp", placeholder="Ex: carlos@museu.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: scenco, museudigital, heritage).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t32_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t32_nome_site,
                key="t32_nome_site_inp",
                placeholder="Ex: scenco  →  sttacksite.streamlit.app/?c=scenco",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🥇 <strong>Dourado (Acento):</strong> cor usada em labels, links em destaque e bordas finas.
                Mantenha tons dourados/âmbar para a estética museológica, ou troque pela cor da sua marca.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t32_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t32_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t32_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t32_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t32_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t32_cores) > 1 and _del_btn(f"t32_cor_del_{i}"):
                        st.session_state.t32_cores.pop(i); st.rerun()
            if _add_btn("t32_cor_add", "＋ Adicionar cor"):
                st.session_state.t32_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(canto esquerdo — CAIXA ALTA para estilo institucional)*")
            for i, item in enumerate(st.session_state.t32_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_nav_logos[i]["texto"] = st.text_input(
                        "Nome", item["texto"], key=f"t32_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: SCENCO ou NOME DO MUSEU")
                with c2:
                    if len(st.session_state.t32_nav_logos) > 1 and _del_btn(f"t32_logo_del_{i}"):
                        st.session_state.t32_nav_logos.pop(i); st.rerun()
            if _add_btn("t32_logo_add", "＋ Adicionar logo"):
                st.session_state.t32_nav_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t32_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t32_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t32_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t32_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t32_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t32_nav_links) > 1 and _del_btn(f"t32_navl_del_{i}"):
                        st.session_state.t32_nav_links.pop(i); st.rerun()
            if _add_btn("t32_navl_add", "＋ Adicionar link"):
                st.session_state.t32_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            st.caption("Link de destaque  *(aparece em cor dourada — geralmente o CTA principal)*")
            for i, cta in enumerate(st.session_state.t32_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t32_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t32_ncta_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Explorar →")
                with c2:
                    st.session_state.t32_nav_ctas[i]["url"] = st.text_input(
                        "Destino", cta["url"], key=f"t32_ncta_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t32_nav_ctas) > 1 and _del_btn(f"t32_ncta_del_{i}"):
                        st.session_state.t32_nav_ctas.pop(i); st.rerun()
            if _add_btn("t32_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t32_nav_ctas.append({"texto": "Explorar →", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> escreva o texto normalmente. Se quiser parte em itálico ou
                com fonte serifada (estilo tipográfico museológico), descreva nas Observações —
                ex: "quero a palavra 'Tempo.' em itálico com fonte serifada".<br>
                <strong>Citação:</strong> escreva sem aspas, elas são adicionadas automaticamente no layout.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Label  *(texto em dourado acima do título)*")
            for i, l in enumerate(st.session_state.t32_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t32_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Museu Digital do Patrimônio Mundial")
                with c2:
                    if len(st.session_state.t32_hero_labels) > 1 and _del_btn(f"t32_h_l_del_{i}"):
                        st.session_state.t32_hero_labels.pop(i); st.rerun()
            if _add_btn("t32_h_l_add", "＋ Adicionar label"):
                st.session_state.t32_hero_labels.append({"valor": "NOVO LABEL"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t32_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t32_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: UMA JORNADA PELO TEMPO.")
                with c2:
                    if len(st.session_state.t32_hero_titulos) > 1 and _del_btn(f"t32_h_t_del_{i}"):
                        st.session_state.t32_hero_titulos.pop(i); st.rerun()
            if _add_btn("t32_h_t_add", "＋ Adicionar título"):
                st.session_state.t32_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Imagem principal  *(tela cheia com filtro sépia/escurecido — 1920 × 1080 px)*")
            for i, img in enumerate(st.session_state.t32_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_hero_imgs[i]["url"] = st.text_input(
                        "URL", img["url"], key=f"t32_h_img_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t32_hero_imgs) > 1 and _del_btn(f"t32_h_img_del_{i}"):
                        st.session_state.t32_hero_imgs.pop(i); st.rerun()
            if _add_btn("t32_h_img_add", "＋ Adicionar imagem"):
                st.session_state.t32_hero_imgs.append({"url": ""}); st.rerun()

            st.caption("Citação  *(aparece em itálico abaixo da imagem — sem aspas)*")
            for i, q in enumerate(st.session_state.t32_hero_quotes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_hero_quotes[i]["valor"] = st.text_area(
                        "Citação", q["valor"], key=f"t32_h_q_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: O patrimônio é o nosso legado do passado...")
                with c2:
                    if len(st.session_state.t32_hero_quotes) > 1 and _del_btn(f"t32_h_q_del_{i}"):
                        st.session_state.t32_hero_quotes.pop(i); st.rerun()
            if _add_btn("t32_h_q_add", "＋ Adicionar citação"):
                st.session_state.t32_hero_quotes.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. COLEÇÃO (GRID ASSIMÉTRICO)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Coleções em Destaque</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📐 <strong>Layout assimétrico:</strong> cada item ocupa metade da largura da página.
                O campo "Lado" define se a imagem fica à esquerda ou direita do texto —
                alterne para criar variação visual entre os itens.<br>
                Imagens das coleções: tamanho ideal <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Itens da coleção  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t32_col_items):
                with st.expander(f"Item {i+1}: {item['titulo']}"):
                    st.session_state.t32_col_items[i]["lado"] = st.selectbox(
                        "Posição da imagem", ["Esquerda", "Direita"],
                        index=0 if item["lado"] == "Esquerda" else 1,
                        key=f"t32_ci_l_{i}",
                        help="Define se a imagem aparece à esquerda ou direita do texto.")
                    st.session_state.t32_col_items[i]["label"] = st.text_input(
                        "Label", item["label"], key=f"t32_ci_lb_{i}",
                        placeholder="Ex: Arquitetura e Ruínas")
                    st.session_state.t32_col_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t32_ci_t_{i}",
                        placeholder="Ex: Templos de Angkor Wat")
                    st.session_state.t32_col_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t32_ci_d_{i}", height=80,
                        placeholder="Descreva este patrimônio ou coleção em 2-3 frases.")
                    st.session_state.t32_col_items[i]["img_url"] = st.text_input(
                        "URL da Imagem", item["img_url"], key=f"t32_ci_img_{i}",
                        placeholder="https://i.imgur.com/... — 800×600 px ideal")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t32_col_items[i]["btn_texto"] = st.text_input(
                            "Texto Botão", item["btn_texto"], key=f"t32_ci_bt_{i}",
                            placeholder="Ex: VER COLEÇÃO COMPLETA")
                    with c2:
                        st.session_state.t32_col_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t32_ci_bu_{i}",
                            placeholder="https://wa.me/... ou link")
                    if len(st.session_state.t32_col_items) > 1:
                        if st.button("🗑 Remover este item", key=f"t32_ci_del_{i}"):
                            st.session_state.t32_col_items.pop(i); st.rerun()
            if _add_btn("t32_ci_add", "＋ Adicionar item na coleção"):
                st.session_state.t32_col_items.append({
                    "lado": "Esquerda", "label": "NOVA CATEGORIA",
                    "titulo": "Novo Patrimônio",
                    "desc": "", "btn_texto": "VER MAIS",
                    "btn_url": "",
                    "img_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. MAPA GLOBAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🗺️ Mapa Global</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🗺️ Esta seção exibe um mapa visual com uma imagem de fundo e um texto em overlay.
                Use uma imagem de mapa-múndi ou foto aérea. Tamanho ideal: <strong>1600 × 700 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cabeçalho  *(Label | Título)*")
            for i, h in enumerate(st.session_state.t32_map_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_map_headers[i]["label"] = st.text_input(
                        "Label", h["label"], key=f"t32_ml_{i}", label_visibility="collapsed",
                        placeholder="Ex: Mapa Global")
                    st.session_state.t32_map_headers[i]["titulo"] = st.text_input(
                        "Título", h["titulo"], key=f"t32_mt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Onde a História Vive")
                with c2:
                    if len(st.session_state.t32_map_headers) > 1 and _del_btn(f"t32_mh_del_{i}"):
                        st.session_state.t32_map_headers.pop(i); st.rerun()
            if _add_btn("t32_mh_add", "＋ Adicionar cabeçalho"):
                st.session_state.t32_map_headers.append({"label": "LABEL", "titulo": "Título"}); st.rerun()

            st.caption("Imagem de fundo do mapa  *(URL | Texto em overlay)*")
            for i, m in enumerate(st.session_state.t32_map_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_map_imgs[i]["url"] = st.text_input(
                        "URL Fundo", m["url"], key=f"t32_mi_u_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... — 1600×700 px ideal")
                    st.session_state.t32_map_imgs[i]["texto"] = st.text_input(
                        "Texto Overlay", m["texto"], key=f"t32_mi_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: CARREGANDO MAPA INTERATIVO...")
                with c2:
                    if len(st.session_state.t32_map_imgs) > 1 and _del_btn(f"t32_mi_del_{i}"):
                        st.session_state.t32_map_imgs.pop(i); st.rerun()
            if _add_btn("t32_mi_add", "＋ Adicionar fundo"):
                st.session_state.t32_map_imgs.append({"url": "", "texto": "CARREGANDO..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Marca e descrição")
            for i, b in enumerate(st.session_state.t32_foot_brands):
                with st.expander(f"Marca: {b['nome']}"):
                    st.session_state.t32_foot_brands[i]["nome"] = st.text_input(
                        "Nome", b["nome"], key=f"t32_fb_n_{i}",
                        placeholder="Ex: SCENCO ou NOME DO MUSEU")
                    st.session_state.t32_foot_brands[i]["desc"] = st.text_area(
                        "Descrição", b["desc"], key=f"t32_fb_d_{i}", height=70,
                        placeholder="Ex: Uma iniciativa para preservar a memória cultural.")
                    if len(st.session_state.t32_foot_brands) > 1:
                        if st.button("🗑 Remover", key=f"t32_fb_del_{i}"):
                            st.session_state.t32_foot_brands.pop(i); st.rerun()
            if _add_btn("t32_fb_add", "＋ Adicionar marca"):
                st.session_state.t32_foot_brands.append({"nome": "MARCA", "desc": ""}); st.rerun()

            st.caption("Colunas de links no rodapé")
            for i, col in enumerate(st.session_state.t32_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t32_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t32_fc_t_{i}",
                        placeholder="Ex: EXPLORAR ou CRÉDITOS")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t32_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t32_fcl_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto")
                        with c2:
                            st.session_state.t32_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t32_fcl_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https://")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t32_fcl_del_{i}_{j}"):
                                st.session_state.t32_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t32_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t32_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t32_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t32_fc_del_{i}"):
                            st.session_state.t32_foot_cols.pop(i); st.rerun()
            if _add_btn("t32_fc_add", "＋ Adicionar coluna"):
                st.session_state.t32_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "LINK", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t32_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t32_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOME DO MUSEU © 2026.")
                with c2:
                    if len(st.session_state.t32_foot_copys) > 1 and _del_btn(f"t32_fcp_del_{i}"):
                        st.session_state.t32_foot_copys.pop(i); st.rerun()
            if _add_btn("t32_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t32_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Links legais  *(Termos, Privacidade, etc.)*")
            for i, link in enumerate(st.session_state.t32_foot_legal):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t32_foot_legal[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t32_fl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: TERMOS DE USO")
                with c2:
                    st.session_state.t32_foot_legal[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t32_fl_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link")
                with c3:
                    if len(st.session_state.t32_foot_legal) > 1 and _del_btn(f"t32_fl_del_{i}"):
                        st.session_state.t32_foot_legal.pop(i); st.rerun()
            if _add_btn("t32_fl_add", "＋ Adicionar link legal"):
                st.session_state.t32_foot_legal.append({"texto": "LINK", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS — GUIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📐 Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Tamanhos recomendados:</strong><br>
                • Hero (tela cheia): <strong>1920 × 1080 px</strong> (paisagem, com área central importante)<br>
                • Coleções (grid): <strong>800 × 600 px</strong> (paisagem)<br>
                • Mapa global: <strong>1600 × 700 px</strong> (panorâmica)<br><br>
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
                Ex: "manter estética museológica sóbria", "quero a palavra 'Tempo.' em itálico no título",
                "adicionar seção de eventos/exposições temporárias", "adicionar mapa interativo real"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t32_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t32_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t32_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t32_obs) > 1 and _del_btn(f"t32_obs_del_{i}"):
                        st.session_state.t32_obs.pop(i); st.rerun()
            if _add_btn("t32_obs_add", "＋ Adicionar observação"):
                st.session_state.t32_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t32_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t32_email_cliente.strip() or "@" not in st.session_state.t32_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t32_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t32_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t32_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t32_nome_cliente}'*."
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
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
