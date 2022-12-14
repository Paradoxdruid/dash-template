"""Utility functions for bio-falsehoods"""

import json
from dataclasses import dataclass
from typing import Dict, List

import dash_bootstrap_components as dbc
from dash import html

from {{cookiecutter.project_name}}.layout import FOOTER, MODAL, SIZING


def generate_layout() -> dbc.Container:
    """Generate a bootstrap layout.

    Returns:
        dbc.Container: layout containing a styled bootstrap card
    """

    navbar = dbc.Row(
        dbc.Col(
            dbc.NavbarSimple(
                id="nav_bar",
                children=[
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("More", header=True),
                            dbc.DropdownMenuItem(
                                "About", id="dropdown-button", n_clicks=0
                            ),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="More",
                    ),
                ],
                brand=f"{{cookiecutter.project_name}}",
                brand_href="#",
                color="primary",
                dark=True,
                class_name="pb-3 rounded",
            )
        ),
        class_name="pt-3",
    )
    card = dbc.Col(
        dbc.Card(
            dbc.CardBody(
                children=[
                    html.P("{{cookiecutter.description}}", className="card-text"),
                ]
            )
        ),
    )

    return dbc.Container(
        fluid=True,
        children=dbc.Row(
            dbc.Col(
                children=[
                    MODAL,
                    navbar,
                    dbc.Row(card),
                    FOOTER,
                ],
                **SIZING,
            ),
            justify="center",
        ),
        style={"min-height": "100vh"},  # fill the whole background
    )
