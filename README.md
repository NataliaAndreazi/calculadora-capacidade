
# Calculadora de Capacidade Produtiva do Time

Este projeto é uma API simples em Python usando FastAPI para calcular a capacidade produtiva de um time, com armazenamento local dos dados em JSON.  

## Como iniciar o desenvolvimento no VS Code
1. Clone o repositório (caso ainda não tenha feito):
```bash

git clone https://github.com/seu-usuario/calculadora-capacidade.git

cd calculadora-capacidade

````

2. Crie e ative o ambiente virtual:
```bash

python3 -m venv venv

source venv/bin/activate # Linux / macOS

.\venv\Scripts\activate # Windows (PowerShell)

```

3. Instale as dependências:
```bash

pip install -r requirements.txt

```

4. Abra o VS Code na pasta do projeto:
```bash

code .

```

5. No VS Code, selecione o interpretador Python do ambiente virtual (geralmente aparece na barra inferior ou use Ctrl+Shift+P e pesquise "Python: Select Interpreter").

## Como rodar o código
Com o ambiente virtual ativado, execute:
```bash

uvicorn main:app --reload

```
O servidor ficará disponível em `http://127.0.0.1:8000`.

## Como testar no navegador
1. Abra o navegador e acesse o Swagger UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Você verá a documentação interativa da API.
3. Para testar a capacidade produtiva, use o endpoint `POST /calcular`.
4. Para ver o histórico salvo, use o endpoint `GET /historico`.

## Como trabalhar com o repositório remoto (GitHub)

### Atualizar seu branch local com a branch `main` remota (rebase)
1. Primeiro, certifique-se de estar na branch `main`:
```bash

git checkout main

```
2. Busque as atualizações do remoto:
```bash

git fetch origin

```
3. Rebase seu branch local para ficar atualizado:
```bash

git rebase origin/main

```
Caso ocorram conflitos, resolva-os manualmente e depois rode:
```bash

git rebase --continue

```

### Enviar suas alterações para o GitHub
1. Adicione arquivos modificados:
```bash

git add .

```
2. Faça commit das mudanças:
```bash

git commit -m "Sua mensagem de commit"

```
3. Envie para o repositório remoto:
```bash

git push origin main

```