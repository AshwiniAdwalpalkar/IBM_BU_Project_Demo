from dash import dcc, html
import sys
sys.path.append('../')

def create_MFA_component():
    return html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
        children= [
            html.Div(
                style={'text-align': 'center', 'border': '1px solid black', 'padding': '50px'},
                children=[
            html.H1("Multi-Factor Authentication"),
            dcc.Input(id = 'mfa-totp-code-input',type='text',placeholder = 'Enter Totp code'),
            html.Div(html.Button('Submit', id='mfa-submit-button', n_clicks=0, style={'margin-top': '10px', 'color': 'green'})),
                    #html.Img(id='qrcode-image',src = 'C:/Users/vishesh_singh/Downloads/MVCauth/MVCauth/View/qrcode.png'),

                html.Div(
                    children=[
                        html.Div(html.Button('generate_QR', id= 'QR-button', n_clicks=0, style={'margin-top': '10px', 'color': 'green'})),
                    ]
                ),
                html.Div(id = 'QR-result-output'),

            html.Div(id ='mfa-result-output')
            
            ])])