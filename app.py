from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("UK Tech Job Market Dashboard"),
    html.P("Dash is working!")
])

if __name__ == "__main__":
    app.run(debug=True)