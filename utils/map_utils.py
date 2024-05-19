import matplotlib
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from staticmap import StaticMap, CircleMarker
import numpy as np

def get_map_categories(df, categories, title='', scale_label=''):
    """
        Given a dataframe with columns 'lat' and 'lng' and a list of categories (column names with boolean values),
        this function returns a matplotlib figure with a map of the points in the dataframe, colored by the categories.
    """
    m = StaticMap(1600, 1000)
    colors = ['yellow', 'blue', 'brown', 'green', 'red', 'black']

    if(len(categories) > len(colors)):
        raise Exception(f'Too many categories {len(categories)}, I only have f{len(colors)} colors!')

    legend_handles = []

    for c, category in enumerate(categories):
        legend_handles.append(mpatches.Patch(color=colors[c], label=category.capitalize()))

        for index, row in df[df[category]].iterrows():
            point = CircleMarker(
                (row['lng'], 
                row['lat']), 
                color=colors[c], 
                width=10)
            m.add_marker(point)

    image = m.render(zoom=12, center=(14.4399466,50.0859818))

    fig, ax = plt.subplots(figsize=(15, 10))
    fig.suptitle(title, verticalalignment='bottom', fontsize=16, y=0.9)
    fig.legend(handles=legend_handles, loc='center right')

    ax.imshow(image)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])

    plt.close()

    return fig

plt.ion()

def get_map_scale(df, color_attribute='', title='', scale_label=''):
    """
        Given a dataframe with columns 'locality_gps_lat' and 'locality_gps_lon' and a name of a column with a numerical value,
        this function returns a matplotlib figure with a map of the points in the dataframe, colored by the numerical value.
    """
    m = StaticMap(1600, 1066)

    color_norm = colors.Normalize(
        vmin=df[color_attribute].min(), 
        vmax=df[color_attribute].max()
    )
    
    color_mapper = cm.ScalarMappable(
        norm=color_norm, 
        cmap='inferno'
    )

    for index, row in df.iterrows():
        point = CircleMarker(
            (row['locality_gps_lon'], 
             row['locality_gps_lat']), 
            color=tuple(np.floor(np.array(color_mapper.to_rgba(row[color_attribute])[:3]) * 255).astype(int)), 
            width=10)
        m.add_marker(point)

    image = m.render(zoom=12)

    fig, ax = matplotlib.pyplot.subplots(figsize=(15, 10))
    fig.suptitle(title, verticalalignment='bottom', fontsize=16, y=0.9)

    plt.colorbar(color_mapper, ax=ax, label=scale_label, fraction=0.03, pad=0.04)
    ax.imshow(image)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])

    return fig

plt.ioff()
