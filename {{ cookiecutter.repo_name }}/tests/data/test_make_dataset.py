import click
from click.testing import CliRunner
from src.data.make_dataset import main

def test_main():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('hello.txt', 'w') as f:
            f.write('Hello World!')
        result = runner.invoke(main, ['hello.txt', 'output_path'])
        assert result.exit_code == 0