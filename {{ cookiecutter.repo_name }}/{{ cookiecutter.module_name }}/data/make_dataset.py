"""Make dataset"""
from {{ cookiecutter.module_name }} import logger


def main():
    """Main"""
    logger.info('your log message')


if __name__ == '__main__':
    main()
