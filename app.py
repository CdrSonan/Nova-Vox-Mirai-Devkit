"""
Nova-Vox Mirai Development Kit Dash App
This app serves the Voicebank development kit for Nova-Vox Mirai as a Dash web application.
"""

from dash import Dash, dcc, html

from views.phonemes import phoneme_tab

app = Dash(__name__, title="Nova-Vox Mirai Development Kit", assets_folder='assets')

app.layout = html.Div([
    html.H1("Nova-Vox Mirai Development Kit"),
    dcc.Tabs([
        phoneme_tab,
        dcc.Tab(label='Tab 2', children=[
            html.Div([
                html.H2("Content for Tab 2"),
                html.P("This is the second tab of the app.")
            ])
        ]),
        dcc.Tab(label='Tab 3', children=[
            html.Div([
                html.H2("Content for Tab 3"),
                html.P("This is the third tab of the app.")
            ])
        ])
    ]),
    html.Div(id='tabs-content', style={'margin-top': '20px'}),
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)  # type: ignore
