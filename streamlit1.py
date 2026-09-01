import numpy as np
import plotly.graph_objects as go
import streamlit as st
from numpy.random import default_rng as rng
from scipy.stats import gaussian_kde

"A chart showing random data"
hist_data = [
    rng(0).standard_normal(200) - 3,
    rng(1).standard_normal(200),
    rng(2).standard_normal(200) + 3,
]
group_labels = ["Group C", "Group B", "Group A"]

fig = go.Figure()
for data, label in zip(hist_data, group_labels):
    kde = gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 200)
    fig.add_trace(go.Scatter(x=x, y=kde(x), mode="lines", fill="tozeroy", name=label))

st.plotly_chart(fig)