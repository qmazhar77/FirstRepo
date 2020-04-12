import logging

logging.basicConfig(filename="C:/Users/junaid/PycharmProjects/Demo/PytestDemo/test2.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG
                    )
logging.debug("This is DEBUG message")
logging.info("This is INFO message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

