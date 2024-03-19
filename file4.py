from dash import html,dcc
def create_forgot_component():
    return html.Div(style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
        children=[
            html.Div(
                style={'text-align': 'center', 'border': '1px solid black', 'padding': '50px'},
                children=[
        html.Div("Username", style={'margin-bottom': '5px'}),
        dcc.Input(id='signin-username', type='text', placeholder='Username'),
        html.Div("Email", style={'margin-top': '10px', 'margin-bottom': '5px'}),
        dcc.Input(id='signin-email', type='email', placeholder='email'),
        html.Div("New_password", style={'margin-top': '10px', 'margin-bottom': '5px'}),
        dcc.Input(id='new_password', type='password', placeholder='new password'),
        html.Div("Confirm_password", style={'margin-top': '10px', 'margin-bottom': '5px'}),
        dcc.Input(id='confirm_password', type='password', placeholder='confirm password'),
        html.Div(html.Button('Submit', id='forgot_password-button', n_clicks=0, style={'margin-top': '10px', 'color': 'green'})),
        html.Div(id='forgot_password-output'),
        html.A('Sign in', href='/signin',style={'margin-left': '5px', 'color': 'blue'})
         ] )])
