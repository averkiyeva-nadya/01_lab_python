import sys

from toolkit.__main__ import main


def test_cli_calc_ok():
    sys.argv = ["toolkit", "calc", "2+3*4"]

    code = main()

    assert code == 0


def test_cli_calc_division_by_zero():
    sys.argv = ["toolkit", "calc", "1/0"]

    code = main()

    assert code == 2


def test_cli_calc_empty():
    sys.argv = ["toolkit", "calc", " "]

    code = main()

    assert code == 2


def test_cli_convert_ok():
    sys.argv = [
        "toolkit",
        "convert",
        "1000",
        "--from",
        "mm",
        "--to",
        "m"
    ]

    code = main()

    assert code == 0


def test_cli_convert_incompatible():
    sys.argv = [
        "toolkit",
        "convert",
        "1",
        "--from",
        "kg",
        "--to",
        "m"
    ]

    code = main()

    assert code == 2


def test_cli_convert_unknown_unit():
    sys.argv = [
        "toolkit",
        "convert",
        "1",
        "--from",
        "xyz",
        "--to",
        "m"
    ]

    code = main()

    assert code == 2


def test_cli_no_command():
    sys.argv = ["toolkit"]

    code = main()

    assert code == 2

