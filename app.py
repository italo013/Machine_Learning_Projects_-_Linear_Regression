# Importando as bibliotecas necessárias
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
from sklearn.linear_model import LinearRegression

# Gerando os dados
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3*x + 7 + np.random.normal(0, 1, 100)  # y = mx + b + noise

# Gerando dados aleatórios para o exemplo
np.random.seed(0)
x1 = np.random.rand(100, 1)
x2 = np.random.rand(100, 1)
y2 = 3*x1 + 2*x2 + np.random.rand(100, 1)

# Modelo de regressão linear múltipla
model = LinearRegression()
model.fit(np.hstack([x1, x2]), y2)


# Inicializando o app Dash
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.Div([
        html.H1("Demonstração de Regressão Linear Simples"),
        html.P("""
            A Regressão Linear é um método para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. 
            No caso da Regressão Linear Simples, temos apenas uma variável independente.
        """),
        html.P("""
            A relação é representada por uma equação da forma y = mx + b.
        """),
        html.P("""
            Onde:
        """),
        html.Ul([
            html.Li("y é a variável dependente;"),
            html.Li("x é a variável independente;"),
            html.Li("m é a inclinação da linha de regressão (representa o efeito de x sobre y);"),
            html.Li("b é a interceptação (representa o valor de y quando x é 0)."),
        ]),
    
    dcc.Graph(id='scatter-plot'),
    
    html.Div(id='regression-formula'),

    html.P("""
            Altere os sliders abaixo para e veja o comportamento da Linha de Regressão:
        """),

    html.Label([
        "Inclinação (m)",
        dcc.Slider(
            id='slope-slider',
            min=-10,
            max=10,
            value=1,
            marks={i: str(i) for i in range(-10, 11)},
            step=0.1
        ),
    ]),
    
    html.Label([
        "Interceptação (b)",
        dcc.Slider(
            id='intercept-slider',
            min=-10,
            max=10,
            value=1,
            marks={i: str(i) for i in range(-10, 11)},
            step=0.1
        ),
    ]),

    html.H1("Demonstração de Regressão Linear Múltipla"),
        html.P("""
            Passando para a regressão linear múltipla, a ideia básica é a mesma, mas a matemática se torna um pouco mais complicada. Agora, em vez de termos apenas um m e um b, temos um coeficiente para cada variável independente e uma interceptação.
        """),
        html.P("""
            A equação da regressão linear é: y = m1*x1 + m2*x2 + b.
        """),
        html.P("""
            Onde:
        """),
        html.Ul([
            html.Li("y é a variável dependente, ou seja, a variável que estamos tentando prever ou estimar;"),
            html.Li("β₀ é o termo de interceptação. Ele representa o valor esperado de Y quando todas as variáveis independentes (Xs) são iguais a zero;"),
            html.Li("β₁, β₂, ..., βₙ são os coeficientes de regressão. Eles representam a mudança esperada na variável dependente (Y) para cada mudança de uma unidade na respectiva variável independente, mantendo todas as outras variáveis independentes constantes;"),
            html.Li("x₁, x₂, ..., xₙ são as variáveis independentes, ou seja, as variáveis que usamos para prever ou estimar Y;"),
            html.Li("ε é o termo de erro, também conhecido como resíduos. Ele representa a diferença entre o valor real e o valor previsto de Y.")
        ]),
    dcc.Graph(id='graph'),
    
    html.Div(id='equation'),
    
    html.Label([
    "Coeficiente m1:",
    dcc.Slider(id='m1-slider', min=-10, max=10, value=3),
    ]),
    html.Label([
        "Coeficiente m2:",
        dcc.Slider(id='m2-slider', min=-10, max=10, value=2),
    ]),
    html.Label([
        "Interceptação b:",
        dcc.Slider(id='b-slider', min=-10, max=10, value=0),
    ]),

    ], style={'width': '100%', 'margin': 'auto'}),

])

# Atualizando o gráfico com os valores dos sliders
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('slope-slider', 'value'),
     Input('intercept-slider', 'value')]
)
def update_graph(slope, intercept):
    y_pred = slope*x + intercept
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Dados'))
    fig.add_trace(go.Scatter(x=x, y=y_pred, mode='lines', name='Linha de Regressão'))
    fig.update_layout(
        title="Demonstração de Regressão Linear Simples",
        xaxis_title="Variável Independente (x)",
        yaxis_title="Variável Dependente (y)",
        autosize=True,
    )
    return fig

# Atualizando a equação de regressão com os valores dos sliders
@app.callback(
    Output('regression-formula', 'children'),
    [Input('slope-slider', 'value'),
     Input('intercept-slider', 'value')]
)
def update_equation(slope, intercept):
    return f'Equação de regressão: y = {slope:.2f}x + {intercept:.2f}'



# Callback para atualizar o gráfico e a equação
@app.callback(
    [Output('graph', 'figure'), Output('equation', 'children')],
    [Input('m1-slider', 'value'), Input('m2-slider', 'value'), Input('b-slider', 'value')]
)
def update_graph2(m1, m2, b):
    # Gerando a superfície de previsão
    x1_range = np.linspace(x1.min(), x1.max(), 100)
    x2_range = np.linspace(x2.min(), x2.max(), 100)
    x1_values, x2_values = np.meshgrid(x1_range, x2_range)
    y_pred = m1*x1_values + m2*x2_values + b

    # Criando o gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x1.squeeze(), y=x2.squeeze(), z=y2.squeeze(), mode='markers', name='Dados'))
    fig.add_trace(go.Surface(x=x1_range, y=x2_range, z=y_pred, opacity=0.7, name='Superfície de Regressão'))

    fig.update_layout(  title="Demonstração de Regressão Linear Múltipla",
                        scene=dict(
                        xaxis_title='X1',
                        yaxis_title='X2',
                        zaxis_title='Y'
    ),
    #width=1000, # Altera a largura do gráfico
    height=800 # Altera a altura do gráfico
    )

    # Criando a equação
    equation = f'Equação de regressão: y = {m1:.2f}*x1 + {m2:.2f}*x2 + {b:.2f}'

    return fig, equation



# Rodando o app
if __name__ == '__main__':
    app.run_server(debug=True)
