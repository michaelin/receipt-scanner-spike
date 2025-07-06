"""Tests for the receipt scanner application."""

import pytest
from receipt_scanner.main import main


def test_main_function_exists():
    """Test that the main function exists and is callable."""
    assert callable(main)


def test_main_runs_without_error(capsys):
    """Test that the main function runs without error."""
    main()
    captured = capsys.readouterr()
    assert "Receipt Scanner Spike" in captured.out
