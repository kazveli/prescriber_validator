# Validador de Prescritores 🩺🔍
Validador automatizado de registros profissionais de saúde (CRM, CRN, CRP, etc) a partir de uma planilha base.

## Funcionalidades
1. Scraping inteligente pelo Selenium e Requests
2. Lida com Captchas (resolução manual)
3. Salva checkpoints do scraping em JSON 
4. Suporte a múltiplos conselhos (CRM, CRN, CRP, etc)
5. Exportação de planilhada unificada

## Instalação
Baixe o projeto
```bash
git clone https://github.com/kazveli/prescriber_validator.git
```
Crie o ambiente virtual python
```bash
cd prescriber_validator
python -m venv venv
```
Ative o ambiente e instale as dependências
```bash
(Windows) venv\Scripts\Activate.ps1
(Linux) source venv/bin/activate
pip install -r requirements.txt
```

## Utilização
NotImplementedError

## Próximos passos
scraper base (abstrato)
scraper crm < scraper base
factory para escolher qual scraper sera utilizado
loader para carregar e salvar a planilha
driver para gerir o navegador para os scrapers
validator para orquestrar tudo
main para porta de entrada (ainda desfuncinal)


## Contribuindo
NotImplementedError
 