import logging

def who_got_fooled(fool):
    logging.basicConfig(filename='log_file.log', filemode='w', datefmt='%d/%m/%Y %I:%M:%S %p',
                        format='%(asctime)s %(name)-6s %(levelname) s: %(message)s', level=logging.DEBUG)
    logging.info(fool)