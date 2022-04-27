from unittest.mock import MagicMock
from pystandalonehtml import cli

def test_cli():
    # Prepare
    cli.docopt = MagicMock(return_value={
        '<input_file.html>':'value1',
        '<output_file.html>':'value2',
    })
    htmlcoverter_mock = cli.make_html_images_inline = MagicMock()

    # Execute
    cli.main()

    # Verify
    htmlcoverter_mock.assert_called_with('value1', 'value2')