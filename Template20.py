import streamlit as st

# Importamos os templates (assumindo que os arquivos estão na mesma pasta)
# Para não carregar 28 imports de uma vez e pesar, podemos usar import_module
import importlib

def main():
    # 1. Configurações iniciais do Hub (Título da aba, etc)
    # Importante: O set_page_config só pode ser chamado UMA VEZ no arquivo principal
    st.set_page_config(layout="wide", page_title="Sttack Templates Hub", page_icon="🚀")

    # 2. Captura o parâmetro da URL (ex: ?t=26)
    query_params = st.query_params
    template_id = query_params.get("t", "home") # "t" de template, padrão é "home"

    # 3. Lógica de Roteamento Dinâmico
    if template_id == "home":
        st.title("🚀 Bem-vindo ao Sttack Templates")
        st.write("Escolha um modelo para editar ou visualizar através da URL.")
        st.info("Exemplo de uso: `...streamlit.app/?t=26` para o Template 26")
        
    else:
        try:
            # Tenta importar o arquivo correspondente ao número na URL
            # Ex: Se ?t=26, ele procura o arquivo Template26.py
            module_name = f"Template{template_id}"
            template_module = importlib.import_module(module_name)
            
            # Chama a função principal do template (que deve se chamar render() em todos)
            # Nota: Como o set_page_config já foi chamado no main, 
            # remova-o de dentro dos arquivos TemplateX.py para não dar erro.
            template_module.render()
            
        except ModuleNotFoundError:
            st.error(f"❌ Erro: O Template '{template_id}' não foi encontrado.")
            st.button("Voltar ao Início", on_click=lambda: st.query_params.clear())
        except Exception as e:
            st.error(f"⚠️ Ocorreu um erro ao carregar o template: {e}")

if __name__ == "__main__":
    main()
