"""Pytest tests for {{cookiecutter.project_name}} app"""

from {{cookiecutter.project_name}}.app import toggle_modal


def test_toggle_modal_callback() -> None:

    output_open = toggle_modal(1, None, True)
    assert output_open is False

    output_closed = toggle_modal(1, None, False)
    assert output_closed is True
