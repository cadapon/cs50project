import project
import pytest
import sys
import testcli


def test_start_parse(capsys):
    # Test unsupported cmdline option
    with pytest.raises(SystemExit) as e_info:
        project.start_parse("-m")
        captured = capsys.readouterr()
        assert "unrecognized arguments: -m"
    with pytest.raises(SystemExit) as e_info:
        # Test both supported and unsuported cmdline options
        project.start_parse(["-m", "-f"])
        captured = capsys.readouterr()
        assert "unrecognized arguments: -m"
    with pytest.raises(FileNotFoundError) as e_info:
        # Test both supported and unsuported cmdline options
        project.main()
        captured = capsys.readouterr()
        assert "unrecognized arguments: -m"


def test_validate_domain():
    assert project.validate_domain(["stuff.com"]) == ["stuff.com"]
    # Test for spaces in domain name
    with pytest.raises(SystemExit) as e_info:
        project.validate_domain(["space for stuff.com"])
        assert e_info.value.code == 1
    # Test for special characters in domain name
    with pytest.raises(SystemExit) as e_info:
        project.validate_domain(["!specialchar!.com"])
        assert e_info.value.code == 1


def test_domain_lookup():
    assert (
        project.domain_lookup(["yahoo.com"])
        == "Sorry, yahoo.com is already registered!"
    )


if __name__ == "__main__":
    test_start_parse()
