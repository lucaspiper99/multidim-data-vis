# Multidimensional  Data Visualization
## Exercise 1: Cars Dataset

### Description

The goal of this exercise is to create a visual representation for all the cars in [this dataset](cars.csv). Besides visualizing all rows, the visualization should also enable the representation of as much variables (columns) as possible, by using Bertin's visual attributes and Mackinlay's importance ordering as a basis (Belleman, 2022). For each of the variables, it was assigned a data type, order of priority and visual attribute, as displayed in the following table:

|   Column   |   Data Type       | Order of Piority | Visual Attribute  |
|------------|-------------------|------------------|-------------------|
| mpg        | quantity-ratio    | 1<sup>st</sup>   | position x        |
| horsepower | quantity-ratio    | 2<sup>nd</sup>   | position y        |
| weight     | quantity-ratio    | 3<sup>rd</sup>   | position z        |
| cylinders  | quantity-ratio    | 4<sup>th</sup>   | area              |
| origin     | nominal           | 5<sup>th</sup>   | shape             |
| year       | quantity-interval | 6<sup>th</sup>   | value             |
| model      | nominal           | 7<sup>th</sup>   | -                 |

In order to tackle this problem, an interactive visualization application was developed using a Python script that takes advantage of the visualization tools from [matplotlib library](https://matplotlib.org/) (Sarkar, 2018).

### How to Run

In order to access the visualization, it's necessary to have Python installed with all the modules specified in the [requirements file](requirements.txt). Afterwards, the visualization can be launched by running `plot.py`.

On Windows:

> `pip install -r requirements.txt`

> `python plot.py`

### How to use

The visualization application also allows for user interaction: within the 3D projection, the camera position can be adjusted, by dragging the mouse pointer.

### References

- Belleman, R. (2022). 1. Introduction \[PowerPoint Slides\]. *Scientific Visualization and Virtual Reality, University of Amsterdam*.
- Sarkar, D. (2018). The Art of Effective Visualization of Multi-dimensional Data. *Towards Data Science*. https://towardsdatascience.com/the-art-of-effective-visualization-of-multi-dimensional-data-6c7202990c57