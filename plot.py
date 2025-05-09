#!/usr/bin/python3

import pandas as pd
import plotly.express as px


COL_YEAR = "Year"
COL_SPEED_ORIG = "Speed [Gbps]"
COL_SPEED = "Speed (symmetric)"
COL_PRICE = "Price per month [Fr.]"
COL_PRODUCT = "Product"
COL_LINK = "Link"


def main():
    data = pd.read_csv("internet-prices.csv")

    # Convert to string so that plotly treats it as categories (instead of continuous numerical data)
    data[COL_SPEED] = data[COL_SPEED_ORIG].astype(str) + " Gbps"
    print(data)

    # Plot
    fig = px.scatter(
        data,
        x=COL_YEAR,
        y=COL_PRICE,
        color=COL_SPEED,
        text=COL_PRODUCT,
        hover_data=[COL_PRODUCT, COL_SPEED, COL_LINK],
        title="Internet Prices over Time (Switzerland)",
        width=1000,
        height=600,
    )

    fig.update_traces(
        textposition="top center",
        marker_size=12,
    )
    fig.update_layout(
        plot_bgcolor="white",
    )
    fig.update_xaxes(
        gridcolor="lightgrey",
    )
    fig.update_yaxes(
        gridcolor="lightgrey",
    )

    # Add prices below data points
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row[COL_YEAR],
            y=row[COL_PRICE],
            text=f'<a href="{row[COL_LINK]}" target="_blank">{row[COL_PRICE]} Fr.</a>',
            yshift=-20,
            showarrow=False,
        )

    # Add source link
    fig.add_annotation(
        text='<a href="https://github.com/thgoebel/internet-prices" target="_blank">github.com/thgoebel/internet-prices</a>',
        xref="paper",
        yref="paper",
        x=1.05,
        y=-0.11,
        showarrow=False,
        xanchor="center",
        yanchor="bottom",
    )

    # Export
    fig.write_html("internet-prices.html")
    fig.write_image("internet-prices.png")
    fig.show()


if __name__ == "__main__":
    main()
