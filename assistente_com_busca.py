# ============================================================
#   🌐  ASSISTENTE LOCAL (COM BUSCA NA INTERNET)
#   Respostas geradas pelo modelo + ferramenta de web search.
#   Pode consultar fontes externas para dados mais recentes.
# ============================================================

import ollama
import os
from ddgs import DDGS
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
    "[bold cyan]🤖 Assistente Virtual Local (COM BUSCA NA INTERNET) [/bold cyan]\n"
    f"[green]Modelo: {MODELO}[/green]\n"
    "[yellow]Digite 'sair' para encerrar | 'limpar' para nova conversa[/yellow]",
    title="[bold white]Ollama AI[/bold white]", border_style="cyan"
))

def buscar_na_internet(query: str, max_resultados: int = 3) -> str:
    console.print(f"\n[dim]🤖 Buscando na web: '{query}'...[/dim]")
    try:
        with DDGS() as ddgs:
            resultados = list(ddgs.text(query, max_results=max_resultados))
        if not resultados: return "Nenhum resultado encontrado."
        contexto = "Resultados da busca na internet:\n\n"
        for i, r in enumerate(resultados, 1):
            contexto += f"{i}. **{r['title']}**\n{r['body']}\nFonte: {r['href']}\n\n"
        return contexto
    except Exception as e:
        return f"Erro na busca: {e}"

def precisa_buscar(mensagem: str) -> bool:
    gatilhos = ["pesquise", "busque", "notícia", "hoje", "atual", "2026"]
    return any(g in mensagem.lower() for g in gatilhos)

def chat_com_busca(mensagem_usuario: str) -> str:
    mensagem_final = mensagem_usuario
    if precisa_buscar(mensagem_usuario):
        contexto_web = buscar_na_internet(mensagem_usuario)
        mensagem_final = f"Contexto:\n{contexto_web}\n\nPergunta: {mensagem_usuario}"
    historico.append({"role": "user", "content": mensagem_final})
    resposta = ollama.chat(model=MODELO, messages=historico)
    texto_resposta = resposta["message"]["content"]
    historico[-1]["content"] = mensagem_usuario
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
            resposta = chat_com_busca(entrada)
            console.print(Markdown(resposta))
        except (KeyboardInterrupt, SystemExit):
            break

if __name__ == "__main__":
    main()