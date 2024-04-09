import json
import numpy as np
import pandas as pd
import plotly.express as px
import os
import webbrowser

#os.remove('__pycache__/re.cpython-311.pyc')
os.system('python textgen.py')
os.system('python layout.py')

india_states = json.load(open("states_india.geojson", "r"))

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

df = pd.read_csv("india_census.csv")
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])
df["DensityScale"] = np.log10(df["Density"])

fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="DensityScale",
    hover_name="State or union territory",
    scope="asia",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})  # Adjust the margin for top-left positioning
fig.update(layout_coloraxis_showscale=False)


# Save the map as HTML file
fig.write_html("india_map.html")

webbrowser.open('index.html', new=2)