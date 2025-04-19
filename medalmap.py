import pandas as pd
import plotly.express as px

#  dataset
file_path = "medals_by_countries.csv" 
df = pd.read_csv(file_path)

#  column names
df.columns = df.columns.str.strip()

# Rename for Plotly
if "Country" in df.columns:
    df.rename(columns={"Country": "country"}, inplace=True)

# DataFrame
df_melted = df.melt(
    id_vars="country",
    value_vars=["Gold Medal", "Silver Medal", "Bronze Medal"],
    var_name="Medal Type",
    value_name="Count"
)

# Plot with Plotly
fig = px.choropleth(
    df_melted,
    locations="country",
    locationmode="country names",
    color="Count",
    hover_name="country",
    animation_frame="Medal Type",
    color_continuous_scale="Viridis",
    title="Olympic Medals by Country and Type"
)

fig.update_layout(legend_title_text='Number of Medals')
fig.show()

#Save to HTML
fig.write_html("olympic_medal_map.html")



