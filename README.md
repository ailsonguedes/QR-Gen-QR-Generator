# QR Gen: Gerador de QR Code com React e Flask

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


## Visão Geral do Projeto e Propósito:

Bem-vindo ao **QR Gen**! Esta é uma solução Full-Stack moderna e modular focada na **criação instantânea e dinâmica de QR Codes**.

O projeto atua como um excelente exemplo de **arquitetura de microsserviços simples**, onde a responsabilidade da interface e da lógica de negócios são estritamente separadas. O principal propósito é fornecer uma ferramenta robusta, com alta performance e fácil de escalar, destacando as seguintes áreas:

1. Geração de Imagem Segura: A lógica complexa de geração do código é isolada no Backend (Flask), protegendo a performance do Frontend.

2. Interface Moderna: O Frontend (React/TS) garante uma experiência de usuário fluida e responsiva em qualquer dispositivo.

3. Ambiente Unificado: A orquestração via Docker Compose simplifica o deploy e garante a consistência entre desenvolvimento e produção.

## Tecnologias Utilizadas:

O projeto foi construído utilizando uma **stack moderna e eficiente**, garantindo um desenvolvimento tipado, rápido e com alta performance, encapsulado em contêineres Docker.

| Categoria | Tecnologia | Função Principal |
| :--- | :--- | :--- |
| **Frontend** | **React & TypeScript** | Construção da interface de usuário modular, tipada e reativa. |
| **Tooling** | **Vite** | Empacotamento de alto desempenho e ambiente de desenvolvimento rápido. |
| **Backend (API)** | **Flask** | Framework Python leve e minimalista para processamento e geração da imagem do QR Code.|
| **Servidor WSGI** | **Gunicorn** | Servidor robusto para servir a aplicação Flask em ambiente de produção Docker. |
| **Orquestração** | **Docker Compose** | Gerencia o ciclo de vida, a construção e a comunicação de todos os serviços (Frontend e Backend). |
| **Servidor Web** | **Nginx** | Servidor de alta performance responsável por servir os arquivos estáticos do React no contêiner Frontend. |

## Funcionalidades Principais:

* Geração Dinâmica de QR Code: Cria QR Codes em tempo real para qualquer string de texto ou URL fornecida pelo usuário.

* API RESTful Dedicada: Endpoint HTTP simples no Backend para receber dados e retornar a imagem do QR Code.

* Design Responsivo: Interface construída com foco em Mobile-First, garantindo usabilidade em tablets e smartphones.

* Ambiente Contenerizado: Execução completa da aplicação com apenas um comando (```docker-compose up```).

## Componentes:

| Nome do Serviço | Tecnologia | Porta | Função |
| :--- | :--- | :--- | :--- |
| **Frontend** | **React + Nginx** | ```80``` | Camada de Apresentação. Responsável por capturar a entrada do usuário e exibir o QR Code. |
| **Backend** | **Flask + Gunicorn** | ```5000``` | Camada de API. Processa a requisição, gera a imagem do QR Code e a retorna ao Frontend. |
| **Orchestrator** | **Docker Compose** | N/A | Gerencia a construção, o ciclo de vida e a rede de ambos os contêineres. |

## Como Rodar o Projeto Localmente:

Este projeto utiliza Docker para garantir que o ambiente de execução seja configurado rapidamente e sem conflitos de dependências.

### Pré-requisitos:

Você precisa ter instalado em sua máquina:

1. **Docker**

2. **Docker Compose:** (Geralmente incluído na instalação do Docker Desktop)

### Etapas de Execução:

1. **Clone o Repositório**:
    ```bash
        git clone [link do repositorio]
    ```
2. **Construa e Inicie os Contêineres:**
A partir da pasta raiz do projeto, execute o Docker Compose. Isso irá construir as imagens do Flask e do React e iniciá-las na rede definida.
    ```bash
        cd [pasta do repositorio]
        docker-compose up --build -d
    ```
   (```-d``` executa os serviços em modo detached.)

3. **Acesse a Aplicação**:
O serviço de Frontend (React) estará acessível no seu navegador:
    ```bash
        http://localhost/
    ```

    O Backend (Flask) estará disponível internamente no Docker e externamente em http://localhost:5000/.

## Parar a Aplicação:

### **Para derrubar e remover os contêineres:**

```bash
    docker-compose down
```

## Estrutura de Pastas:

Abaixo está a estrutura de diretórios do repositório:

```
.
├── backend/        # Aplicação Flask (Backend)
│   ├── app.py           # Ponto de entrada da aplicação Flask
│   ├── Pipfile          # Dependências Python (Flask, QR Code Generator)
│   └── Dockerfile       # Instruções de build do container Flask
├── frontend/       # Aplicação React (Frontend)
│   ├── src/             # Código fonte React/TypeScript
│   ├── package.json     # Dependências Node (React, Vite)
│   └── Dockerfile       # Instruções de build do container React/Nginx
├── docker-compose.yml   # Orquestração do Docker (Define os serviços front e back)
└── README.md

```

## Desenvolvimento:

```Frontend```:

* Tecnologia: React, TypeScript, Vite.
* Acesso: O servidor de desenvolvimento é geralmente rodado na porta ```3000``` ou ```5173```. Para desenvolvimento local, você pode iniciar o servidor Node.js diretamente (fora do Docker) e configurar um proxy para o backend.

```Backend```:
* Tecnologia: Flask, Python.
* Dependências: Gerenciadas via Pipenv.
* Comunicação: Os endpoints da API estão em /api/... (Exemplo: /api/generate).

## Contribuição: 

Contribuições são bem-vindas! Se você encontrar um bug ou tiver uma sugestão de recurso, por favor, abra uma Issue ou submeta um Pull Request no repositório.