import logging, sys

class CallLogger:
    _instance = None
    def __new__(cls, level=logging.DEBUG, log_format='[%(levelname)s](%(filename)s) %(asctime)s: %(message)s'):
        if cls._instance is None:
            cls._instance = super(CallLogger, cls).__new__(cls)

            # Configuração padrão do logger
            cls._instance.logger = logging.getLogger("Logger")
            cls._instance.logger.setLevel(level)
            cls._instance.logger.propagate = False # Evita logs duplicados

            # Configurando handler de console
            output_handler = logging.StreamHandler(sys.stdout)
            output_handler.setFormatter(logging.Formatter(log_format))
            cls._instance.logger.addHandler(output_handler)
            # Configurando handler de arquivo
            file_handler = logging.FileHandler('doc/logs/sys.log', mode='a', encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(log_format))
            cls._instance.logger.addHandler(file_handler)
        return cls._instance
    
    def get(self):
        return self.logger