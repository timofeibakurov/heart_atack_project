from flask import render_template, request, config, Flask
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly
import json
import plotly.express as px
import numpy as np
from project_report import app, data




@app.route('/')
def index():
    df = data
    return render_template('index.html', columns=df.columns.values, values=df.values.tolist())
@app.route('/task1')
def task1():
    df = data
    return render_template('task1.html', m_age=df["Age"].median(), std_age=np.std(df['Age']), mean_age=df['Age'].mean(),
                           m_chol=df["Cholesterol"].median(), std_chol=np.std(df['Cholesterol']),
                           mean_chol=df['Cholesterol'].mean(),
                           m_maxhp=df["MaxHR"].median(), std_maxhp=np.std(df['MaxHR']), mean_maxhp=df['MaxHR'].mean())
@app.route('/task2')
def task2():
    df = data
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Number of types of diseases", "A case of a heart attack", "Gender of the respondent"),
        specs=[[{"type": "bar"}, {"type": "pie"}],
               [{"type": "pie"}, {}]],
    )

    fig.add_trace(go.Bar(y=[496, 203, 173, 46], x=['ASY', 'NAP', 'ATA', 'TA']),
                  row=1, col=1)

    fig.add_trace(go.Pie(values=df['HeartDisease'].value_counts(), labels=['True', 'False']),
                  row=1, col=2)

    fig.add_trace(go.Pie(values=df['Sex'].value_counts(), labels=['Male', 'Female'], hole=.3),
                  row=2, col=1)

    fig.update_layout(height=700, showlegend=False)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('task2.html', graphJSON=graphJSON)
@app.route('/task3')
def task3():
    df = data
    fig = px.scatter(df, x="RestingBP", y="Cholesterol", color="HeartDisease",
                     size='RestingBP', hover_data=['Cholesterol'])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('task3.html', graphJSON=graphJSON)
@app.route('/task5')
def task5():
    df = data
    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"type": "bar"}]],
    )
    fig.add_trace(go.Bar(x=df['MaxHR'], y=df['ExerciseAngina']),
                  row=1, col=1)
    fig.update_layout(height=700, showlegend=False)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('task5.html', graphJSON=graphJSON)

@app.route('/task4')
def task4():
    return render_template('task4.html')
