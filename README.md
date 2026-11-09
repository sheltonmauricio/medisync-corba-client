# MediSync CORBA Client

Aplicação desktop do MediSync, feita em Python com PySide6. Liga-se ao servidor MediSync via CORBA e disponibiliza fluxos para receção, médicos e administração.

## Requisitos

- Python 3.12 (a imagem Docker usa `python:3.12-slim`).
- Servidor MediSync disponível pela rede nas portas TCP `1050` (Naming Service) e `2809` (serviços).
- Para execução local, os requisitos de sistema do OmniORB e do Qt/PySide6, conforme a plataforma.

## Configuração

Crie `.env` a partir do exemplo:

```sh
cp .env.example .env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Configure as variáveis:

| Variável | Descrição |
| --- | --- |
| `CORBA_NAME_SERVICE_HOST` | IP/DNS do servidor, igual ao `CORBA_PUBLIC_HOST` configurado no servidor. Não use `localhost` nem nome de container quando estiver noutra máquina. |
| `CORBA_NAME_SERVICE_PORT` | Porta do CORBA Naming Service (por omissão, `1050`). |
| `TZ` | Fuso horário da interface (por omissão, `Africa/Maputo`). |

O endereço deve ser alcançável a partir do cliente nas portas `1050` e `2809`.

## Execução local

Crie um ambiente virtual, instale as dependências e inicie a aplicação a partir da pasta do projeto:

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

No Windows PowerShell, ative o ambiente com `.venv\Scripts\Activate.ps1`.

## Execução com Docker Compose

Com Docker e Docker Compose instalados e o `.env` configurado:

```sh
docker compose up --build
```

O container publica a interface gráfica através do noVNC na porta `6080`; abra `http://localhost:6080` no navegador da máquina Docker. Para parar:

```sh
docker compose down
```

## Desenvolvimento

O contrato CORBA está em `idl/hospital.idl`, e os stubs Python usados pela aplicação estão em `generated/`. A interface e os fluxos estão organizados em `src/gui`, `src/services` e `src/application`.
