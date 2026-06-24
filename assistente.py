# ============================================================
#   🤖  ASSISTENTE LOCAL
#   Respostas geradas diretamente pelo modelo de linguagem.
#   Sem acesso à internet — tudo vem do conhecimento base.
# ============================================================

import ollama
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from dotenv import load_dotenv

load_dotenv()
MODELO = os.getenv("MODELO", "qwen3:4b")
console = Console()
historico = []

def exibir_banner():
    console.print(Panel.fit(
    "[bold cyan]🤖 Assistente Virtual Local[/bold cyan]\n"
    f"[green]Modelo: {MODELO}[/green]\n"
    "[yellow]Digite 'sair' para encerrar | 'limpar' para nova conversa[/yellow]",
    title="[bold white]Ollama AI[/bold white]", border_style="cyan"
))
    
def chat(mensagem_usuario: str) -> str:
    historico.append({"role": "user", "content": mensagem_usuario})
    resposta = ollama.chat(model=MODELO, messages=historico)
    texto_resposta = resposta["message"]["content"]
    historico.append({"role": "assistant", "content": texto_resposta})
    return texto_resposta

def main():
    exibir_banner()
    while True:
        try:
            console.print("\n[bold green]Você:[/bold green] ", end="")
            entrada = input().strip()
            if not entrada: continue
            if entrada.lower() == 'sair': break
            if entrada.lower() == 'limpar':
                historico.clear(); console.clear(); exibir_banner(); continue
            console.print("\n[bold cyan]🤖 Assistente:[/bold cyan]")
            resposta = chat(entrada)
            console.print(Markdown(resposta))
        except (KeyboardInterrupt, SystemExit):
            break

if __name__ == "__main__":
    main()