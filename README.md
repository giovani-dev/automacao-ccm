# Automação CCM

## 🏗️ Status do Projeto

O foco nestas últimas horas de desenvolvimento esteve inteiramente na **modelagem da arquitetura do projeto** e na **montagem da sua base estrutural**. O trabalho abrangeu desde o setup inicial do ambiente até a definição da base arquitetural para a solução.

> **Aviso Importante:** Até o momento, a solução **ainda não foi testada nem validada**.

A ideia central para resolver o problema proposto está traduzida no código atual. O que está implementado reflete a visão inicial para a solução e a direção que o projeto irá tomar.

---

## 🛠️ Documentação Técnica

### Requisitos e Gerenciamento
Este repositório utiliza o `mise` para o gerenciamento de versões das ferramentas (veja o arquivo `mise.toml`) e o `Poetry` para o gerenciamento das dependências do ecossistema Python.

### Setup Local na Máquina

Para configurar o projeto na sua máquina localmente, execute no terminal:

```bash
# 1. Instale as ferramentas base declaradas no mise.toml
mise install

# 2. Instale as dependências do projeto via Poetry
poetry install --no-interaction
```

### Como Executar

Atualmente, como a fundação do projeto acabou de ser estruturada (sem a implementação final do ponto de entrada), a execução é focada na garantia de qualidade e padronização do código. O ponto de entrada principal, quando implementado, ficará em `src/main.py`.

Para executar as verificações de código e testes:

```bash
# Executar os testes automatizados (assim que implementados)
poetry run pytest -q

# Executar a verificação de tipagem estática
poetry run mypy src

# Executar a análise de qualidade do código
poetry run pylint src

# Verificar a formatação do código
poetry run black --check .
```

### Executando com Docker

Caso deseje rodar a aplicação e suas dependências via containers, o ambiente de desenvolvimento já está preparado:

```bash
# Constrói a imagem Docker de desenvolvimento
docker compose -f docker/docker-compose.yml build

# Sobe os serviços configurados
docker compose -f docker/docker-compose.yml up
```

### Integração Contínua (CI)

O workflow configurado no GitHub Actions utiliza `jdx/mise-action@v2` para o provisionamento das ferramentas a partir do `mise.toml`, executa a instalação via `poetry` e valida automaticamente o projeto rodando todos os linters e testes da aplicação.
