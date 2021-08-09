import pytest 

from pgbackup import cli

address = "192.168.0.167"

@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([address])


def test_parser_with_driver(parser):
    """
    The parser will exit if it recieves a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([address, "--driver", "local"])


def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([address, '--driver', 'azure', 'destination'])


def test_parser_with_known_drivers(parser):
    """
    The Parser will not exit if the driver name is knows
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([address, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destination
    """
    args = parser.parse_args([address, '--driver', 'local', '/some/path'])

    assert args.address == address
    assert args.driver == 'local'
    assert args.destination == '/some/path'

