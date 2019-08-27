#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dtwr` package."""


import unittest
from click.testing import CliRunner

from dtwr import cli


class TestCLI(unittest.TestCase):
    """Tests for `dtwr` package."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main,
                               '--query tests/query.csv --reference tests/reference.csv'.split())
        assert result.exit_code == 0
        assert '0.1292' in result.output

    def test_help(self):
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output




        
