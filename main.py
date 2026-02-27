import streamlit as st
import importlib.util
import os

# Configuração da página (deve ser a primeira linha de comando Streamlit)
st.set_page_config(
    page_title="Editor de Websites",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Identifica qual template carregar pela URL (ex: ?template=template1)
query_params = st.query_params
template_id = query_params.get("template", "template1") 

def carregar_template(nome_template):
    # Procura o arquivo dentro da pasta 'templates'
    caminho_arquivo = os.path.join("templates", f"{nome_template}.py")
    
    if os.path.exists(caminho_arquivo):
        spec = importlib.util.spec_from_file_location("modulo_template", caminho_arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        return modulo
    else:
        st.error(f"Template '{nome_template}' não encontrado na pasta /templates.")
        return None

# Carrega e executa o template selecionado
template_modulo = carregar_template(template_id)

if template_modulo:
    # Chama a função principal do template
    template_modulo.render()
