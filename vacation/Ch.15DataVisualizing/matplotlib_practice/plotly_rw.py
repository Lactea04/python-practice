import pandas as pd
import plotly.express as px
import numpy as np
from random_walk import RandomWalk

rnw = RandomWalk(10_000)
rnw.fill_walk()

steps = len(rnw.x_values)
values = np.linspace(0, 1, steps)

df = pd.DataFrame({'x' : rnw.x_values, 'y' : rnw.y_values, 'value' : values, 'title' : "RandomWalk"})

#draw dots
fig = px.scatter(df, x='x', y='y', title='title', color='value', color_continuous_scale='blues')
fig.add_scatter(x=[rnw.x_values[0]], y=[rnw.y_values[0]], mode='markers+text',marker=dict(size=10, color='green', symbol='circle'),
    name='Start', text=['Start'], textposition='top center')
fig.add_scatter(x=[rnw.x_values[-1]], y=[rnw.y_values[-1]], mode='markers+text',marker=dict(size=10, color='red', symbol='circle'), name='End',
    text=['End'], textposition='top center')

fig.update_traces(marker=dict(size=1), selector=dict(mode='marker'))
fig.update_layout(coloraxis_showscale=False)


fig.update_layout(
    xaxis=dict(title='', showticklabels=False),
    yaxis=dict(title='', showticklabels=False)
)
fig.show()
