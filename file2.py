from dash import html, dcc
import dash_player as dp


def create_signup_component():
    return html.Div(className="Section",
        style={
            "width":"100%",
            "height":"100vh",  
           # "background":"radial-gradient(circle at 10% 20%, rgba(216, 241, 230, 0.46) 0.1%, rgba(233, 226, 226, 0.28) 90.1%)",  
            "background":"linear-gradient(-20deg, #efd595 0%, #fbfcdb 100%)",
        },
        
        children=[
            html.Div(className="Container",
                     
                style={
                    "position":"absolute",
                    "top":"50%",
                    "left":"50%",
                    "transform":"translate(-50%,-50%)",
                    "width":"700px",
                    "height":"350px",
                    "background":"rgb(255,160,137)",
                    "box-shadow": "0px 0px 5px 0px rgba(0,0,0,1)",
                    "border-radius":"10px",
                    "border":"1px solid rgb(206,32,41)",
                    #"border":"1px solid black",
                },
                children=[
                    html.Div(className="form_content",
                        style={
                            "position":"relative",
                            "width":"50%",
                            "height":"410px",
                            "float":"left",
                            "box-sizing":"border-box",
                            "padding":"40px 30px",
                            "color":"#fff",

                        },
                        children=[
                            html.Img(),
                            html.H3("Welcome to Persistent University Chatbot !"),
                            html.P("Sign in to explore a tailored chat experience with PersiChatbot"),
                        ],
                    
                    ),
                    html.Div(className="login_form",
                        style={
                            "position":"relative",
                            "width":"50%",
                            "height":"420px",
                            "top":"-30px",
                            "float":"left",
                            "box-sizing":"border-box",
                            "box-shadow": "0px 0px 5px 0px rgba(0,0,0,0.5)",
                            "background":"#fff",
                            "padding":"30px",
                            "border-radius":"10px",

                        },

                        children=[
                            html.Div("Sign Up",style={"color":"#262626","margin-left":"7rem","font-size":"25px"}),
                            html.Form(
                                children=[
                                    html.Div("Username"),
                                    dcc.Input(id="signup-username", type="text", placeholder="Username",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div("Password"),
                                    dcc.Input(id="signup-password", type="password", placeholder="Password",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div("Email"),
                                    dcc.Input(id="signup-email", type="email", placeholder="Email",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div(html.Button("Submit", id="signup-button", n_clicks=0,style={"display":"block","width":"50%","padding":"10px","margin-left":"80px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px","color":"#fff","background":" rgb(206,32,41)"})),  
                                    html.Div(id = 'signup-output'),                  
                                ],
                            ),
                            html.Div(children=[
                                html.H6("Already have an Account?",style={"float":"left"}),
                                html.A(
                                "Sign In",
                                href="/signin",
                                style={"color": "blue","float":"right"},
                                ),
                            ], style={"margin-top": "10px"},
                            ),

                                   
                        ],

                    )
                ]

            )
        ]
    )

if __name__ == '__main__':
    app.run_server()
