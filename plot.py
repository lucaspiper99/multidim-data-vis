import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerTuple


def get_marker_size(cylinders):
    return 36 * cylinders - 88


def main():

    df = pd.read_csv('cars.csv', index_col=False)

    mpl.rcParams['toolbar'] = 'None' 
    fig = plt.figure("Exercise 1: Cars Dataset", figsize=(8, 6))
    t = fig.suptitle('Cars Dataset', fontsize=14)
    ax = fig.add_subplot(111, projection='3d')

    originDict = {
        'Europe': 's',
        'Japan': '^',
        'US': 'o'
    }
    origin_labels = []

    for o, m in originDict.items():

        scatter = ax.scatter(
            df[df['origin']==o]['MPG'],
            df[df['origin']==o]['horsepower'],
            df[df['origin']==o]['weigth'],
            alpha=0.8,
            edgecolors='w',
            s=df[df['origin']==o]['cylinders'].apply(get_marker_size),
            marker=m,
            c=df[df['origin']==o]['year'],
            cmap='bone',
            label=o
            )
        
        origin_labels.append(mlines.Line2D(
            [],
            [],
            color=scatter.cmap(0),
            marker=m,
            linestyle='None',
            markersize=10,
            label=o
            ))

    ax.set_xlabel('Miles per Gallon')
    ax.set_ylabel('Horsepower')
    ax.set_zlabel('Weigth')
    legend1 = ax.legend(handles=origin_labels, loc="lower right", title="Origin")
    ax.add_artist(legend1)


    legend_table = []
    for c in [3, 4, 5, 6, 8]:
        p1, = ax.plot([], [], linestyle='None', color=scatter.cmap(0), marker='o', markersize=get_marker_size(c)*.06)
        p2, = ax.plot([], [], linestyle='None', color=scatter.cmap(0), marker='s', markersize=get_marker_size(c)*.06)
        p3, = ax.plot([], [], linestyle='None', color=scatter.cmap(0), marker='^', markersize=get_marker_size(c)*.06)
        legend_table.append((p1, p2, p3))

    ax.legend(
        legend_table,
        ['3', '4', '5', '6', '8'],
        loc="lower left",
        title="Cylinders",
        numpoints=1,
        handler_map={tuple: HandlerTuple(ndivide=None)},
        handlelength=6
        )

    cbar = plt.colorbar(ax.get_children()[2], ax=ax)
    cbar.set_label('Year')
    plt.show()


if __name__ == "__main__":
    main()

