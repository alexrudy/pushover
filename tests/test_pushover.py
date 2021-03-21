"""Tests for `pushover` package."""
import pushover
from click.testing import CliRunner


def test_command_line_help():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(pushover.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help" in help_result.output
    assert "Show this message and exit." in help_result.output
