"""Pytest tests for bio_falsehoods utils"""

from typing import Dict

import dash_bootstrap_components as dbc
from dash import html
from pytest_mock.plugin import MockerFixture

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
                                brand="Bio-Falsehoods # 1",
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
                            dbc.Card(
                                dbc.CardBody(
                                    children=[
                                        html.H4(
                                            "Myth: Title",
                                            className="card-title",
                                        ),
                                        html.P(
                                            "Reality: Text",
                                            className="card-text",
                                        ),
                                        html.H5("Scientific References:"),
                                        dbc.ListGroup(
                                            children=[
                                                dbc.ListGroupItem(
                                                    "Link 1",
                                                    href="https://test1.com",
                                                ),
                                                dbc.ListGroupItem(
                                                    "Link 2",
                                                    href="https://test2.com",
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ),
                        )
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

