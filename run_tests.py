from behave import __main__ as behave_main
import sys

def run_tests():
    args = [
        '--format', 'pretty',  # Formato de saída (pode ser progress, pretty, html, etc.)
        '--no-capture',          # Não capturar saída padrão dos steps
        '--no-capture-stderr',   # Não capturar saída de erro dos steps
        # '--stop',                # Parar no primeiro erro ou falha
        'features'               # Caminho para o diretório de features
    ]
    sys.argv = ['behave'] + args
    behave_main.main()

if __name__ == '__main__':
    run_tests()