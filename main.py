import argparse

def main():
    # Configurando argumentos com argparse
    parser = argparse.ArgumentParser(
        prog = 'Prescriber Validator',
        description = 'Validador de registros profissionais de saúde'
    )
    parser.add_argument('--file', required=True, help='Caminho da planilha')
    parser.add_argument('--cr-type', default=False, help='Tipo de conselho')
    parser.add_argument('--headless', action='store_true', help='Não mostrar navegador em produção')
    args = parser.parse_args()
    
    # Constrói e chama o validador 
    ## criar o objeto validador e executar o metodo .run() dele.

if __name__ == "__main__":
    main()