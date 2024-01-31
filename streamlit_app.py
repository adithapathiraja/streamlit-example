import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def main():
    # Sample DataFrame (replace this with your own data)
    df = pd.DataFrame({
        'Timestamp': pd.date_range(start='2022-01-01', periods=100, freq='D'),
        'Power_Output': [val + 10 * (0.5 - i/100) for i, val in enumerate(range(100))],
        'Solar_Irradiance': [val + 5 * (0.5 - i/100) for i, val in enumerate(range(100))],
        'Date': pd.date_range(start='2022-01-01', periods=100, freq='D').date
    })

    # Create an interactive subplot
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces for power output and solar irradiance
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Power_Output'], name='Power Output (MW)', line=dict(color='blue')), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['Timestamp'], y=df['Solar_Irradiance'], name='Solar Irradiance (Wm^-2)', line=dict(color='orange')), secondary_y=True)

    fig.update_layout(legend=dict(x=0.55, y=1.18, orientation='h'))

    # Update layout
    fig.update_layout(title='<b>Variation of Solar Irradiance and Power Plant Output with time',
                      xaxis_title='Timestamp',
                      yaxis_title='Power Output (MW)',
                      yaxis2_title='Solar Irradiance (Wm^-2)',
                      xaxis_rangeslider_visible=True)

    # Streamlit app
    st.title("Solar Power Plant Dashboard")

    # Introduction column
    st.sidebar.markdown("# Introduction")
    st.sidebar.write("Welcome to the Solar Power Plant Dashboard! This dashboard provides visualizations of power output and solar irradiance over time.")

    # Tabs for visualizations
    tabs = ["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"]
    selected_tab = st.sidebar.radio("Select Tab", tabs)

    if selected_tab == "Tab 1":
        # Visualizations for Tab 1
        st.plotly_chart(fig)

    elif selected_tab == "Tab 2":
        # Visualizations for Tab 2
        st.write("Visualization for Tab 2 goes here.")

    # Repeat the above pattern for other tabs...

if __name__ == "__main__":
    main()
