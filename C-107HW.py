import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("PixelMath.csv")
print(df.groupby("student_id")["level"].mean())

fig = go.Figure(go.Bar(
    x = df.groupby("student_id")["level"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))
fig.show()