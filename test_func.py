import project
import pytest
import sys


def test_start_parse():
    with pytest.raises(SystemExit) as e_info:
        project.start_parse()
        assert e_info.value.code == 1


def test_validate_domain():
    assert project.validate_domain(["stuff.com"]) == ["stuff.com"]
    with pytest.raises(SystemExit) as e_info:
        project.validate_domain(["space for stuff.com"])
        assert e_info.value.code == 1
    with pytest.raises(SystemExit) as e_info:
        project.validate_domain(["!specialchar!.com"])
        assert e_info.value.code == 1


def test_domain_lookup():
    assert (
        project.domain_lookup(["yahoo.com"])
        == "Sorry, yahoo.com is already registered!"
    )


if __name__ == "__main__":
    # test_start_parse()
    # test_validate_domain()
    test_domain_lookup()
