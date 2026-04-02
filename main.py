import pytest


def run():
    pytest.main(['-rxXs', '--capture=sys', '--capture=fd', '.', '-m', 'swagger', '-rEf'])


if __name__ == "__main__":
    run()
    