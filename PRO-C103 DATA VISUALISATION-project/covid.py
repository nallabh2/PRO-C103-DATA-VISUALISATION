import pandas as pd
import plotly.express as px

contents=pd.read_csv("data.csv")
graph=px.scatter(data_frame=contents,x="date",y="cases",color="country")
graph.show()