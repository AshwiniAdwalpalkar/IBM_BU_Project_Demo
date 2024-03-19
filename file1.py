import dash
from dash import html as html
from dash import dcc as dcc


def create_signin_component():
    return html.Div(className="Section",

        
        style={
            "width":"100%",
            "height":"100vh",  
            "position":"relative",
           
                    },
        
        children=[
           html.Div(className="BackgroundImg",
                    style={
                        "position":"absolute",
                        "top":"0",
                        "left":"0",
                        "width":"100%",
                        "height":"100%",
                        "background-color":"#FFEEBB",
                        #"background-image":"url(https://img.freepik.com/free-photo/business-desk-frame-view_23-2148128275.jpg?size=626&ext=jpg&ga=GA1.1.287250440.1706682737&semt=ais)",
                        "background-repeat":"no-repeat",
                        "background-size":"cover",
                        "filter":"blur(4px)",

       
                        
                    }),
            html.Div(className="Container",
                     
                style={
                    "position":"absolute",
                    "top":"50%",
                    "left":"50%",
                    "transform":"translate(-50%,-50%)",
                    "width":"650px",
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
                            html.P("Welcome to Persistent University Chatbot !",style={"text-align":"center","color":"black","font-size":"25px","margin-top":"-1rem"}),
                            html.Img(src="https://img.freepik.com/free-vector/hand-holding-phone-with-conversation-girl-chat-bot-mobile-app-talking-robot-online-flat-vector-illustration-technology-assistance-concept-banner-website-design-landing-page_74855-24649.jpg?w=740&t=st=1708239784~exp=1708240384~hmac=77cc66aef5b6f41f9d698aa8fd80b6f60a818b966ca1d501fed96c4a4a5d1f1f",style={"height":"150px","width":"200px","padding-left":"38px"}),
                            html.P("Sign in to explore a tailored chat experience with PersiChatbot",style={"text-align":"center","color":"black"}),
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
                            html.Div("Sign In",style={"color":"#262626","margin-left":"7rem","font-size":"25px"}),
                            html.Form(
                                children=[
                                    html.Div("Username"),
                                    dcc.Input(id="signup-username", type="text", placeholder="Username",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div("Password"),
                                    dcc.Input(id="signup-password", type="password", placeholder="Password",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div("Email"),
                                    dcc.Input(id="signup-email", type="email", placeholder="Email",style={"display":"block","width":"100%","padding":"10px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px"}),
                                    html.Div(html.Button("Submit", id="signup-button", n_clicks=0,style={"display":"block","width":"50%","padding":"10px","margin-left":"68px","box-sizing":"border-box","margin-bottom":"15px","border":"2px solid #ccc","border-radius":"25px","outline":"none","font-size":"15px","color":"#fff","background":" rgb(206,32,41)"})),                    
                                ],
                            ),
                            html.Div(children=[
                                html.H6("Alrady have an Account?",style={"float":"left","margin-top":"0.1rem","font-size":"15px"}),
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