# 🤖 Assistente Virtual Local com Ollama

Assistente de inteligência artificial 100% local, construído com [Ollama](https://ollama.com/) e Python. Disponível em duas versões: modo offline puro e modo com busca em tempo real na internet via DuckDuckGo, sem dependência de APIs externas pagas, sem vazamento de dados para a nuvem.

---

## ✨ Funcionalidades

- **Chat conversacional com histórico** — mantém o contexto da conversa durante toda a sessão
- **Execução 100% local** — o modelo roda diretamente na sua máquina, sem enviar dados para servidores externos
- **Interface visual rica no terminal** — painéis, cores e renderização de Markdown via `rich`
- **Busca na internet em tempo real** — versão avançada detecta automaticamente perguntas que exigem dados atuais e consulta o DuckDuckGo
- **Configuração via `.env`** — modelo e parâmetros ajustáveis sem alterar o código
- **Comandos de controle integrados** — `sair` encerra o programa, `limpar` reinicia o histórico da conversa

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca | Função |
|---|---|
| `ollama` | SDK oficial para comunicação com o motor de IA local |
| `openai` | Camada de compatibilidade com APIs unificadas |
| `requests` | Gerenciamento de requisições HTTP |
| `beautifulsoup4` | Extração e processamento de dados da web (Web Scraping) |
| `duckduckgo-search` | Busca em tempo real sem necessidade de chaves de API |
| `rich` | Formatação visual, painéis e cores no terminal |
| `gradio` | Construção de interfaces web para interação no navegador |
| `dotenv` | Carregamento seguro de variáveis do arquivo `.env` |
| `colorama` | Suporte a cores ANSI no terminal Windows |

---

## 📋 Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) instalado e em execução
- Git

### Verificar versões

```bash
python --version
pip --version
ollama --version
```

---

## 🚀 Instalação

### 1. Instalar o Ollama

**Windows (PowerShell como Administrador):**
```powershell
irm https://ollama.com/install.ps1 | iex
```

**Linux / macOS:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Baixar um modelo de linguagem

```bash
# Recomendado para a maioria dos computadores (8GB RAM)
ollama pull qwen3:4b

# Alternativa ultra leve
ollama pull llama3.2:3b
```

### 3. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/assistente-ollama.git
cd assistente-ollama
```

### 4. Criar e ativar o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install ollama openai requests beautifulsoup4 duckduckgo-search rich gradio python-dotenv colorama
```

Ou, se o arquivo `requirements.txt` já estiver presente:

```bash
pip install -r requirements.txt
```

### 6. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MODELO=qwen3:4b
TEMPERATURA=0.7
```

---

## 💻 Como Usar

### Versão básica (sem internet)

```bash
python assistente.py
```

O assistente inicia com um painel de boas-vindas e aguarda sua entrada. Responde exclusivamente com o conhecimento base do modelo local.

### Versão avançada (com busca na internet)

```bash
python assistente_com_busca.py
```

Nesta versão, o assistente detecta automaticamente quando uma mensagem contém palavras-gatilho como `pesquise`, `busque`, `notícia`, `hoje`, `atual` ou `2026`, e realiza uma busca no DuckDuckGo antes de formular a resposta.

### Comandos disponíveis durante o chat

| Comando | Ação |
|---|---|
| `sair` | Encerra o assistente |
| `limpar` | Apaga o histórico e reinicia a sessão |
| `Ctrl+C` | Interrompe imediatamente |

---

## 📁 Estrutura de Pastas

```
assistente-ollama/
│
├── venv/                    # Ambiente virtual Python (não versionado)
├── .env                     # Variáveis de configuração local (não versionado)
├── .gitignore               # Arquivos ignorados pelo Git
├── requirements.txt         # Lista de dependências do projeto
├── README.md                # Documentação principal
├── assistente.py            # Assistente básico (offline)
└── assistente_com_busca.py  # Assistente com busca em tempo real
```

---

## 🧠 Modelos Disponíveis

### Leves — 8GB de RAM

| Modelo | Tamanho | Destaque | Comando |
|---|---|---|---|
| llama3.2 | 3B | Balanceado e rápido | `ollama pull llama3.2` |
| qwen3 | 4B | Suporte multilíngue | `ollama pull qwen3:4b` |
| phi4 | 14B | Eficiência lógica (Microsoft) | `ollama pull phi4` |
| gemma3 | 4B | Otimizado pelo Google | `ollama pull gemma3:4b` |
| mistral | 7B | Clássico e confiável | `ollama pull mistral` |

### Médios — 16GB de RAM

| Modelo | Tamanho | Destaque | Comando |
|---|---|---|---|
| qwen3 | 14B | Custo-benefício lógico | `ollama pull qwen3:14b` |
| deepseek-r1 | 14B | Raciocínio passo a passo | `ollama pull deepseek-r1:14b` |
| phi3 | 14B | Nível corporativo compacto | `ollama pull phi3:14b` |

### Pesados — 32GB+ RAM

| Modelo | Tamanho | Destaque | Comando |
|---|---|---|---|
| qwen3 | 32B | Performance top de linha | `ollama pull qwen3:32b` |
| llama3.1 | 70B | Alta escala da Meta | `ollama pull llama3.1:70b` |
| gemma4 | 27B | Multimodal do Google | `ollama pull gemma4:27b` |

---

## 🔧 Configuração do `.gitignore`

```gitignore
venv/
__pycache__/
*.pyc
.env
*.log
```

---

## 📦 Gerar requirements.txt

Após instalar as dependências e com o ambiente virtual ativado:

```bash
pip freeze > requirements.txt
```

---

## 📤 Publicar no GitHub

```bash
git init
git add .
git commit -m "feat: assistente virtual local com Ollama - modulo inicial"
git remote add origin https://github.com/SEU_USUARIO/assistente-ollama.git
git branch -M main
git push -u origin main
```

---

## 👤 Autor

**Leandro Santos Rangel**  
Técnico em Desenvolvimento de Sistemas — Educação Profissional Paulista  
[LinkedIn](https://www.linkedin.com/in/leandro-srgl) • [GitHub](https://github.com/LeandroSRGL)

Desenvolvido como projeto prático de laboratório para estudo de LLMs locais com Ollama.

---

> **Privacidade:** todos os dados e prompts permanecem no seu computador. Nenhuma informação é enviada para servidores externos ao usar os modelos locais.
