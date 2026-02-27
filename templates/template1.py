import streamlit as st
import requests
import json
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
# ⚙️ CONFIGURAÇÕES — EDITE AQUI ANTES DE SUBIR AO STREAMLIT
# ─────────────────────────────────────────────────────────────────────────────
RESEND_API_KEY   = "re_SUA_CHAVE_AQUI"      # ← cole sua chave do Resend
FROM_EMAIL       = "editor@seudominio.com"   # ← domínio verificado no Resend
TO_EMAIL         = "sttacksite@gmail.com"    # ← seu e-mail de destino

TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/site/main/1.png"
TEMPLATE_NAME      = "Template 1 — Agência Digital"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        "t1_client_name":    [{"valor": ""}],
        "t1_client_email":   [{"valor": ""}],
        "t1_page_titles":    [{"valor": "Agência Digital - Transforme seu Negócio"}],
        "t1_page_icons":     [{"valor": "🚀"}],
        "t1_cores": [
            {"nome": "Cor principal (botões, destaques)", "valor": "#0066FF"},
            {"nome": "Cor dos textos",                    "valor": "#1a1a1a"},
            {"nome": "Cor dos subtextos",                 "valor": "#666666"},
        ],
        "t1_logos":     [{"valor": "🚀 AGÊNCIA"}],
        "t1_nav_links": [
            {"texto": "Serviços", "url": "#features"},
            {"texto": "Sobre",    "url": "#cta"},
            {"texto": "Contato",  "url": "#footer"},
        ],
        "t1_nav_ctas":  [{"texto": "Começar", "url": "https://www.google.com/"}],
        "t1_hero_titulos":    [{"parte1": "Transforme seu Negócio com", "destaque": "Estratégia Digital"}],
        "t1_hero_subtitulos": [{"valor": "Soluções completas de marketing digital que aumentam suas vendas e presença online"}],
        "t1_hero_btns": [
            {"texto": "Solicitar Consultoria", "url": "https://www.google.com/", "estilo": "primário"},
            {"texto": "Ver Portfólio",          "url": "https://www.google.com/", "estilo": "secundário"},
        ],
        "t1_stats": [
            {"numero": "500+", "label": "Clientes Satisfeitos"},
            {"numero": "10+",  "label": "Anos de Experiência"},
            {"numero": "300%", "label": "Crescimento Médio"},
        ],
        "t1_secao_titulos": [{"parte1": "Nossos", "destaque": "Serviços"}],
        "t1_secao_descs":   [{"valor": "Oferecemos soluções completas de marketing digital para impulsionar seu negócio"}],
        "t1_cards": [
            {"icone": "📱", "titulo": "Social Media",        "descricao": "Gerenciamento completo de suas redes sociais com estratégia de conteúdo"},
            {"icone": "🎯", "titulo": "Publicidade Digital",  "descricao": "Campanhas otimizadas em Google Ads e Facebook para máximo ROI"},
            {"icone": "📊", "titulo": "Análise de Dados",     "descricao": "Relatórios detalhados e insights para melhorar seu desempenho"},
            {"icone": "🌐", "titulo": "SEO & Conteúdo",       "descricao": "Otimização para buscas e criação de conteúdo de alta qualidade"},
            {"icone": "💻", "titulo": "Web Design",           "descricao": "Websites modernos e responsivos que convertem visitantes em clientes"},
            {"icone": "📧", "titulo": "Email Marketing",      "descricao": "Campanhas de email personalizadas que geram resultados"},
        ],
        "t1_cta_titulos":    [{"valor": "Pronto para Transformar seu Negócio?"}],
        "t1_cta_subtitulos": [{"valor": "Agende uma consultoria gratuita com nossos especialistas"}],
        "t1_cta_btns":       [{"texto": "Agendar Agora", "url": "https://www.google.com/"}],
        "t1_footer_txts":    [{"valor": "© 2026 Agência Digital. Todos os direitos reservados."}],
        "t1_footer_links":   [
            {"texto": "Privacidade", "url": "#"},
            {"texto": "Termos",      "url": "#"},
        ],
        "t1_obs":     [{"valor": ""}],
        "t1_enviado": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _add_btn(key, label="＋ Adicionar"):
    return st.button(label, key=key)

def _del_btn(key):
    return st.button("🗑", key=key, help="Remover")


# ─────────────────────────────────────────────────────────────────────────────
# MONTAGEM DO E-MAIL HTML
# ─────────────────────────────────────────────────────────────────────────────
def _build_email_html():
    ss = st.session_state
    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    client_name  = ss.t1_client_name[0]["valor"]  if ss.t1_client_name  else "—"
    client_email = ss.t1_client_email[0]["valor"] if ss.t1_client_email else "—"

    def section(title, rows_html):
        return f"""
        <div style="margin-bottom:28px;">
          <h3 style="margin:0 0 10px;font-size:14px;font-weight:700;text-transform:uppercase;
                     letter-spacing:1px;color:#0066FF;border-bottom:2px solid #e8f0fe;
                     padding-bottom:6px;">{title}</h3>
          <table style="width:100%;border-collapse:collapse;font-size:14px;">{rows_html}</table>
        </div>"""

    def row(label, value):
        return f"""
        <tr>
          <td style="padding:6px 10px 6px 0;color:#64748b;width:38%;vertical-align:top;
                     font-weight:500;">{label}</td>
          <td style="padding:6px 0;color:#1a1a2e;">{value or "—"}</td>
        </tr>"""

    def color_row(nome, valor):
        return f"""
        <tr>
          <td style="padding:6px 10px 6px 0;color:#64748b;width:38%;vertical-align:top;
                     font-weight:500;">{nome}</td>
          <td style="padding:6px 0;color:#1a1a2e;">
            <span style="display:inline-block;width:16px;height:16px;border-radius:3px;
                         background:{valor};border:1px solid #ccc;vertical-align:middle;
                         margin-right:6px;"></span>{valor}
          </td>
        </tr>"""

    geral_rows = (
        row("Título da aba", "<br>".join(x["valor"] for x in ss.t1_page_titles)) +
        row("Ícone da aba",  "<br>".join(x["valor"] for x in ss.t1_page_icons))
    )
    cores_rows    = "".join(color_row(c["nome"], c["valor"]) for c in ss.t1_cores)
    navbar_rows   = (
        row("Logo / Marca", "<br>".join(x["valor"] for x in ss.t1_logos)) +
        row("Links do menu", "<br>".join(f"{x['texto']} → {x['url']}" for x in ss.t1_nav_links)) +
        row("Botões CTA",    "<br>".join(f"{x['texto']} → {x['url']}" for x in ss.t1_nav_ctas))
    )
    hero_rows     = (
        row("Títulos",    "<br>".join(f"{x['parte1']} <b>{x['destaque']}</b>" for x in ss.t1_hero_titulos)) +
        row("Subtítulos", "<br>".join(x["valor"] for x in ss.t1_hero_subtitulos)) +
        row("Botões",     "<br>".join(f"{x['texto']} [{x['estilo']}] → {x['url']}" for x in ss.t1_hero_btns))
    )
    stats_rows    = "".join(row(x["label"], x["numero"]) for x in ss.t1_stats)
    servicos_rows = (
        row("Título da seção", "<br>".join(f"{x['parte1']} <b>{x['destaque']}</b>" for x in ss.t1_secao_titulos)) +
        row("Descrição",       "<br>".join(x["valor"] for x in ss.t1_secao_descs)) +
        "".join(row(f"Card {i+1} — {c['icone']} {c['titulo']}", c["descricao"]) for i, c in enumerate(ss.t1_cards))
    )
    cta_rows      = (
        row("Títulos",    "<br>".join(x["valor"] for x in ss.t1_cta_titulos)) +
        row("Subtítulos", "<br>".join(x["valor"] for x in ss.t1_cta_subtitulos)) +
        row("Botões",     "<br>".join(f"{x['texto']} → {x['url']}" for x in ss.t1_cta_btns))
    )
    footer_rows   = (
        row("Textos", "<br>".join(x["valor"] for x in ss.t1_footer_txts)) +
        row("Links",  "<br>".join(f"{x['texto']} → {x['url']}" for x in ss.t1_footer_links))
    )
    obs_text      = "<br>".join(x["valor"] for x in ss.t1_obs if x["valor"].strip())
    obs_rows      = row("Observações do cliente", obs_text or "Nenhuma observação")

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6fb;font-family:'Segoe UI',Arial,sans-serif;">
  <div style="max-width:680px;margin:32px auto;background:#fff;border-radius:12px;
              box-shadow:0 2px 16px rgba(0,0,0,.08);overflow:hidden;">
    <div style="background:linear-gradient(135deg,#0066FF,#0044cc);padding:32px 36px;">
      <h1 style="margin:0;color:#fff;font-size:22px;font-weight:700;">✏️ Personalização de Template</h1>
      <p style="margin:6px 0 0;color:rgba(255,255,255,.8);font-size:14px;">
        {TEMPLATE_NAME} — enviado em {now}
      </p>
    </div>
    <div style="padding:24px 36px 0;">
      <div style="background:#f0f7ff;border-radius:8px;padding:16px 20px;margin-bottom:24px;">
        <p style="margin:0;font-size:14px;color:#1a1a2e;">
          <strong>Cliente:</strong> {client_name}<br>
          <strong>E-mail:</strong> {client_email}
        </p>
      </div>
      {section("⚙️ Configuração Geral", geral_rows)}
      {section("🎨 Cores", cores_rows)}
      {section("🔝 Navbar", navbar_rows)}
      {section("🦸 Hero", hero_rows)}
      {section("📊 Estatísticas", stats_rows)}
      {section("🃏 Serviços / Cards", servicos_rows)}
      {section("📣 CTA", cta_rows)}
      {section("🔻 Footer", footer_rows)}
      {section("📝 Observações", obs_rows)}
    </div>
    <div style="padding:20px 36px 28px;text-align:center;">
      <p style="margin:0;font-size:12px;color:#94a3b8;">
        Enviado automaticamente pelo Editor de Templates
      </p>
    </div>
  </div>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────────────────────
# ENVIO VIA RESEND
# ─────────────────────────────────────────────────────────────────────────────
def _send_email():
    client_name  = st.session_state.t1_client_name[0]["valor"]  or "Cliente"
    client_email = st.session_state.t1_client_email[0]["valor"] or ""

    payload = {
        "from":    FROM_EMAIL,
        "to":      [TO_EMAIL],
        "subject": f"[Template 1] Personalização de {client_name} — {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "html":    _build_email_html(),
    }
    if client_email:
        payload["reply_to"] = client_email

    resp = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type":  "application/json",
        },
        data=json.dumps(payload),
        timeout=15,
    )
    return resp.status_code, resp.text


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
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ── DADOS DO CLIENTE ─────────────────────────────────────────────
            st.markdown('<div class="section-label">👤 Seus Dados</div>', unsafe_allow_html=True)

            st.caption("Seu nome")
            for i, item in enumerate(st.session_state.t1_client_name):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_client_name[i]["valor"] = st.text_input(
                        "Nome", item["valor"], key=f"t1_cname_{i}", label_visibility="collapsed",
                        placeholder="Ex: João Silva")
                with c2:
                    if len(st.session_state.t1_client_name) > 1 and _del_btn(f"t1_cname_del_{i}"):
                        st.session_state.t1_client_name.pop(i); st.rerun()
            if _add_btn("t1_cname_add", "＋ Adicionar nome"):
                st.session_state.t1_client_name.append({"valor": ""}); st.rerun()

            st.caption("Seu e-mail (para receber cópia)")
            for i, item in enumerate(st.session_state.t1_client_email):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_client_email[i]["valor"] = st.text_input(
                        "E-mail", item["valor"], key=f"t1_cemail_{i}", label_visibility="collapsed",
                        placeholder="Ex: joao@email.com")
                with c2:
                    if len(st.session_state.t1_client_email) > 1 and _del_btn(f"t1_cemail_del_{i}"):
                        st.session_state.t1_client_email.pop(i); st.rerun()
            if _add_btn("t1_cemail_add", "＋ Adicionar e-mail"):
                st.session_state.t1_client_email.append({"valor": ""}); st.rerun()

            # ── CONFIGURAÇÃO GERAL ───────────────────────────────────────────
            st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)

            st.caption("Título da aba do navegador")
            for i, item in enumerate(st.session_state.t1_page_titles):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_page_titles[i]["valor"] = st.text_input(
                        "Título", item["valor"], key=f"t1_ptitle_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_page_titles) > 1 and _del_btn(f"t1_ptitle_del_{i}"):
                        st.session_state.t1_page_titles.pop(i); st.rerun()
            if _add_btn("t1_ptitle_add", "＋ Adicionar título"):
                st.session_state.t1_page_titles.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Ícone da aba (emoji)")
            for i, item in enumerate(st.session_state.t1_page_icons):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_page_icons[i]["valor"] = st.text_input(
                        "Ícone", item["valor"], key=f"t1_picon_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_page_icons) > 1 and _del_btn(f"t1_picon_del_{i}"):
                        st.session_state.t1_page_icons.pop(i); st.rerun()
            if _add_btn("t1_picon_add", "＋ Adicionar ícone"):
                st.session_state.t1_page_icons.append({"valor": "🌟"}); st.rerun()

            # ── CORES ────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t1_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t1_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t1_cor_nome_{i}", label_visibility="collapsed",
                        placeholder="Nome da cor")
                with c2:
                    st.session_state.t1_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t1_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t1_cores) > 1 and _del_btn(f"t1_cor_del_{i}"):
                        st.session_state.t1_cores.pop(i); st.rerun()
            if _add_btn("t1_cor_add", "＋ Adicionar cor"):
                st.session_state.t1_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ── NAVBAR ───────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, item in enumerate(st.session_state.t1_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t1_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_logos) > 1 and _del_btn(f"t1_logo_del_{i}"):
                        st.session_state.t1_logos.pop(i); st.rerun()
            if _add_btn("t1_logo_add", "＋ Adicionar logo"):
                st.session_state.t1_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t1_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t1_nl_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t1_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t1_nl_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t1_nav_links) > 1 and _del_btn(f"t1_nl_del_{i}"):
                        st.session_state.t1_nav_links.pop(i); st.rerun()
            if _add_btn("t1_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t1_nav_links.append({"texto": "Novo Link", "url": "#"}); st.rerun()

            st.caption("Botões CTA da navbar  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t1_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t1_ncta_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t1_nav_ctas[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t1_ncta_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t1_nav_ctas) > 1 and _del_btn(f"t1_ncta_del_{i}"):
                        st.session_state.t1_nav_ctas.pop(i); st.rerun()
            if _add_btn("t1_ncta_add", "＋ Adicionar botão CTA"):
                st.session_state.t1_nav_ctas.append({"texto": "Novo CTA", "url": "#"}); st.rerun()

            # ── HERO ─────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Títulos do hero  *(Texto normal | Destaque colorido)*")
            for i, t in enumerate(st.session_state.t1_hero_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_hero_titulos[i]["parte1"] = st.text_input(
                        "Parte 1", t["parte1"], key=f"t1_ht_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t1_hero_titulos[i]["destaque"] = st.text_input(
                        "Destaque", t["destaque"], key=f"t1_ht_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque colorido")
                with c3:
                    if len(st.session_state.t1_hero_titulos) > 1 and _del_btn(f"t1_ht_del_{i}"):
                        st.session_state.t1_hero_titulos.pop(i); st.rerun()
            if _add_btn("t1_ht_add", "＋ Adicionar título"):
                st.session_state.t1_hero_titulos.append({"parte1": "Novo Título", "destaque": "Destaque"}); st.rerun()

            st.caption("Subtítulos do hero")
            for i, item in enumerate(st.session_state.t1_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_hero_subtitulos[i]["valor"] = st.text_area(
                        "Subtítulo", item["valor"], key=f"t1_hsub_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_hero_subtitulos) > 1 and _del_btn(f"t1_hsub_del_{i}"):
                        st.session_state.t1_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t1_hsub_add", "＋ Adicionar subtítulo"):
                st.session_state.t1_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botões do hero  *(Texto | URL | Estilo)*")
            for i, btn in enumerate(st.session_state.t1_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t1_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t1_hb_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t1_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t1_hb_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    st.session_state.t1_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"], key=f"t1_hb_style_{i}",
                        index=0 if btn["estilo"] == "primário" else 1, label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t1_hero_btns) > 1 and _del_btn(f"t1_hb_del_{i}"):
                        st.session_state.t1_hero_btns.pop(i); st.rerun()
            if _add_btn("t1_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t1_hero_btns.append({"texto": "Novo Botão", "url": "#", "estilo": "primário"}); st.rerun()

            # ── ESTATÍSTICAS ─────────────────────────────────────────────────
            st.markdown('<div class="section-label">📊 Estatísticas</div>', unsafe_allow_html=True)
            st.caption("Número | Descrição")
            for i, stat in enumerate(st.session_state.t1_stats):
                c1, c2, c3 = st.columns([2, 5, 1])
                with c1:
                    st.session_state.t1_stats[i]["numero"] = st.text_input(
                        "Número", stat["numero"], key=f"t1_st_num_{i}", label_visibility="collapsed",
                        placeholder="Ex: 500+")
                with c2:
                    st.session_state.t1_stats[i]["label"] = st.text_input(
                        "Label", stat["label"], key=f"t1_st_lbl_{i}", label_visibility="collapsed",
                        placeholder="Descrição")
                with c3:
                    if len(st.session_state.t1_stats) > 1 and _del_btn(f"t1_st_del_{i}"):
                        st.session_state.t1_stats.pop(i); st.rerun()
            if _add_btn("t1_st_add", "＋ Adicionar estatística"):
                st.session_state.t1_stats.append({"numero": "0", "label": "Nova Métrica"}); st.rerun()

            # ── SERVIÇOS / CARDS ─────────────────────────────────────────────
            st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto normal | Destaque)*")
            for i, t in enumerate(st.session_state.t1_secao_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_secao_titulos[i]["parte1"] = st.text_input(
                        "Parte 1", t["parte1"], key=f"t1_sect_p1_{i}", label_visibility="collapsed",
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
                        "Descrição", item["valor"], key=f"t1_secd_{i}", height=60, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_secao_descs) > 1 and _del_btn(f"t1_secd_del_{i}"):
                        st.session_state.t1_secao_descs.pop(i); st.rerun()
            if _add_btn("t1_secd_add", "＋ Adicionar descrição"):
                st.session_state.t1_secao_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de serviço")
            for i, card in enumerate(st.session_state.t1_cards):
                with st.expander(f"Card {i+1} — {card['titulo']}"):
                    c1, c2 = st.columns([1, 8])
                    with c1:
                        st.session_state.t1_cards[i]["icone"] = st.text_input(
                            "Ícone", card["icone"], key=f"t1_cd_ico_{i}", label_visibility="collapsed")
                    with c2:
                        st.session_state.t1_cards[i]["titulo"] = st.text_input(
                            "Título", card["titulo"], key=f"t1_cd_tit_{i}", label_visibility="collapsed")
                    st.session_state.t1_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t1_cd_dsc_{i}", height=70,
                        label_visibility="collapsed")
                    if len(st.session_state.t1_cards) > 1:
                        if st.button("🗑 Remover este card", key=f"t1_cd_del_{i}"):
                            st.session_state.t1_cards.pop(i); st.rerun()
            if _add_btn("t1_cd_add", "＋ Adicionar card de serviço"):
                st.session_state.t1_cards.append(
                    {"icone": "⭐", "titulo": "Novo Serviço", "descricao": "Descrição do serviço"}); st.rerun()

            # ── CTA ──────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">📣 Seção CTA</div>', unsafe_allow_html=True)

            st.caption("Títulos do CTA")
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

            st.caption("Subtítulos do CTA")
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

            st.caption("Botões do CTA  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t1_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t1_ctab_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t1_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t1_ctab_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t1_cta_btns) > 1 and _del_btn(f"t1_ctab_del_{i}"):
                        st.session_state.t1_cta_btns.pop(i); st.rerun()
            if _add_btn("t1_ctab_add", "＋ Adicionar botão CTA"):
                st.session_state.t1_cta_btns.append({"texto": "Novo Botão", "url": "#"}); st.rerun()

            # ── FOOTER ───────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🔻 Footer</div>', unsafe_allow_html=True)

            st.caption("Textos do footer")
            for i, item in enumerate(st.session_state.t1_footer_txts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_footer_txts[i]["valor"] = st.text_input(
                        "Texto footer", item["valor"], key=f"t1_ftxt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_footer_txts) > 1 and _del_btn(f"t1_ftxt_del_{i}"):
                        st.session_state.t1_footer_txts.pop(i); st.rerun()
            if _add_btn("t1_ftxt_add", "＋ Adicionar texto ao footer"):
                st.session_state.t1_footer_txts.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Links do footer  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t1_footer_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t1_footer_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t1_fl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t1_footer_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t1_fl_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t1_footer_links) > 1 and _del_btn(f"t1_fl_del_{i}"):
                        st.session_state.t1_footer_links.pop(i); st.rerun()
            if _add_btn("t1_fl_add", "＋ Adicionar link ao footer"):
                st.session_state.t1_footer_links.append({"texto": "Novo Link", "url": "#"}); st.rerun()

            # ── OBSERVAÇÕES ──────────────────────────────────────────────────
            st.markdown('<div class="section-label">📝 Observações</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t1_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t1_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t1_obs_{i}", height=80,
                        placeholder="Ex: quero mudar a fonte, adicionar FAQ, remover botão X...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t1_obs) > 1 and _del_btn(f"t1_obs_del_{i}"):
                        st.session_state.t1_obs.pop(i); st.rerun()
            if _add_btn("t1_obs_add", "＋ Adicionar observação"):
                st.session_state.t1_obs.append({"valor": ""}); st.rerun()

            # ── BOTÃO ENVIAR ─────────────────────────────────────────────────
            st.markdown("---")

            if st.session_state.t1_enviado:
                st.success("✅ Suas informações foram enviadas! Nossa equipe entrará em contato em breve.")
            else:
                if st.button("✅ Finalizar e Enviar para a Equipe", key="t1_send", type="primary"):
                    with st.spinner("Enviando..."):
                        status, body = _send_email()
                    if status in (200, 201):
                        st.session_state.t1_enviado = True
                        st.success("✅ Enviado com sucesso! Nossa equipe aplicará as alterações em breve.")
                        st.balloons()
                        st.rerun()
                    else:
                        st.error(f"❌ Falha ao enviar (status {status}). Tente novamente ou entre em contato diretamente.")
                        st.code(body, language="json")

    # ── PAINEL DIREITO — IMAGEM DO TEMPLATE ──────────────────────────────────
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
