# app.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Inicia o app Dash
app = dash.Dash(__name__)

# Dados de exemplo (financeiros)
categories = ['January', 'February', 'March', 'April', 'May', 'June']
income = [5000, 6000, 7000, 8000, 7500, 7000]
expenses = [3000, 3500, 4000, 4500, 4200, 4000]

# Layout do app
app.layout = html.Div(children=[
    html.H1("Dashboard Financeiro", style={'text-align': 'center'}),
    dcc.Graph(
        id='finance-chart',
        figure={
            'data': [
                go.Bar(
                    x=categories,
                    y=income,
                    name='Receitas',
                    marker={'color': 'green'}
                ),
                go.Bar(
                    x=categories,
                    y=expenses,
                    name='Despesas',
                    marker={'color': 'red'}
                )
            ],
            'layout': go.Layout(
                title="Receitas e Despesas Mensais",
                barmode='group',
                xaxis={'title': 'Meses'},
                yaxis={'title': 'Valor (R$)'},
            )
        }
    ),
])

# Inicia o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
