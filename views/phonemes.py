from dash import dcc, html

phoneme_tab = dcc.Tab(label='Tab 1', children=[
            html.Div([
                html.H2("Content for Tab 1"),
                html.P("This is the first tab of the app.")
            ])
        ])