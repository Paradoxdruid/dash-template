"""Pytest tests for {{cookiecutter.project_name}} utils"""

import dash_bootstrap_components as dbc
from dash import html

# from pytest_mock.plugin import MockerFixture

from {{cookiecutter.project_name}}.layout import FOOTER, MODAL, PADDING, SIZING
from {{cookiecutter.project_name}}.utils import generate_layout


def test_generate_layout() -> None:

    EXPECTED = dbc.Container(
        fluid=True,
        children=dbc.Row(
            dbc.Col(
                children=[
                    MODAL,
                    dbc.Row(
                        dbc.Col(
                            dbc.NavbarSimple(
                                id="nav_bar",
                                children=[
                                    dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("More", header=True),
                                            dbc.DropdownMenuItem(
                                                "About",
                                                id="dropdown-button",
                                                n_clicks=0,
                                            ),
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="More",
                                    ),
                                ],
                                brand="{{cookiecutter.project_name}}",
                                brand_href="#",
                                color="primary",
                                dark=True,
                                class_name="pb-3 rounded",
                            )
                        ),
                        class_name="pt-3",
                    ),
                    dbc.Row(
                        dbc.Col(
                            dbc.Col(
                                dbc.Card(
                                    dbc.CardBody(
                                        children=[
                                            html.P(
                                                "{{cookiecutter.description}}",
                                                className="card-text",
                                            ),
                                        ]
                                    )
                                ),
                            ),
                        ),
                    ),
                    dbc.Row(
                        dbc.Col(
                            dbc.Button(
                                "Show me another",
                                color="primary",
                                id="submit-button",
                                class_name="me-1 btn",
                                n_clicks=0,
                            ),
                        ),
                        class_name=PADDING,
                    ),
                    FOOTER,
                ],
                **SIZING,
            ),
            justify="center",
        ),
        style={"min-height": "100vh"},  # fill the whole background
    )

    actual = generate_layout()

    assert repr(actual) == repr(EXPECTED)
