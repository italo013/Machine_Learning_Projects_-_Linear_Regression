# Importações necessárias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# Gerar dados
np.random.seed(0)
X = np.random.rand(100)
Y = 3*X + np.random.randn(100)

# Inicializar o aplicativo
app = dash.Dash(__name__)

# Definir layout do aplicativo
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(
        id='slope-slider',
        min=-10,
        max=10,
        value=1,
        step=0.1,
        marks={i: '{}'.format(i) for i in range(-10, 11)},
    ),
    html.Br(),
    dcc.Slider(
        id='intercept-slider',
        min=-10,
        max=10,
        value=1,
        step=0.1,
        marks={i: '{}'.format(i) for i in range(-10, 11)},
    )
])

# Callback para atualizar o gráfico
@app.callback(
    Output('graph', 'figure'),
    [Input('slope-slider', 'value'),
     Input('intercept-slider', 'value')]
)
def update_graph(slope, intercept):
    Y_pred = slope*X + intercept
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=X, y=Y, mode='markers', name='Valores originais'))
    fig.add_trace(go.Scatter(x=X, y=Y_pred, mode='lines', name='Linha de Regressão'))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
