import holoviews as hv
import panel as pn
import numpy as np

pn.extension(sizing_mode="stretch_width")
hv.extension("bokeh")

CHARTS = (
    "Curve",
    "Scatter",
    "Bars",
    "Area",
    "Image",
    "Contours",
    "HexTiles",
    "QuadMesh",
    "Text",
    "Tiles",
    "Overlay",
    "HLine",
    "VLine",
    "Arrow",
)

default_opts = dict(
    width=50,
    height=50,
    xaxis=None,
    yaxis=None,
    shared_axes=False,
    toolbar=None,
    show_grid=True,
)
for chart in CHARTS:
    hv.opts.defaults(getattr(hv.opts, chart)(**default_opts))
hv.opts.defaults(hv.opts.Layout(shared_axes=False, toolbar=None))

config = dict(sizing_mode="stretch_width", min_width=550)

# COLUMN 1

quick_start_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Quick Start &nbsp🏁</h2>"),
    ),
    pn.widgets.StaticText(
        value="""
        <code>
        import pandas as pd<br>
        import holoviews as hv<br>
        hv.extension("bokeh")<br><br>

        df = pd.DataFrame({"x": [1, 2, 3], "y": [0, 0, 1]})<br>
        curve = hv.Curve(df, kdims="x", vdims="y")<br>
        hv.save(curve, "document.html")
        </code>
    """
    ),
)

help_section = pn.Column(
    pn.widgets.StaticText(value="<h2>Getting Help &nbspℹ️</h2>"),
    pn.widgets.StaticText(
        name="Docs Page",
        value="https://holoviews.org/",
    ),
    pn.widgets.StaticText(
        name="GitHub Repo",
        value="https://github.com/holoviz/holoviews/",
    ),
    pn.widgets.StaticText(
        name="Discourse Forum",
        value="https://discourse.holoviz.org/",
    ),
)

layout_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Layout Plots</h2>"),
        pn.pane.HoloViews(
            (hv.Curve([1, 0, 1]) + hv.Curve([0, 1, 0])),
            width=100,
            align="center",
        ),
    ),
    pn.widgets.StaticText(
        name="Individually", value="<code>(obj1 + obj2).cols(2)</code>", **config
    ),
    pn.widgets.StaticText(
        name="From List", value="<code>hv.Layout([obj1, obj2])</code>", **config
    ),
    pn.widgets.StaticText(
        name="From Dict",
        value="<code>hv.NdLayout({'a': obj1, 'b': obj2})</code>",
        **config
    ),
    pn.widgets.StaticText(
        name="From HoloMap", value="<code>holomap.layout()</code>", **config
    ),
)

overlay_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Overlay Plots</h2>"),
        pn.pane.HoloViews(
            (hv.Curve([1, 0, 1]) * hv.Curve([0, 1, 0])),
            width=50,
            align="center",
        ),
    ),
    pn.widgets.StaticText(
        name="Individually", value="<code>(obj1 * obj2)</code>", **config
    ),
    pn.widgets.StaticText(
        name="From List", value="<code>hv.Overlay([obj1, obj2])</code>", **config
    ),
    pn.widgets.StaticText(
        name="From Dict",
        value="<code>hv.NdOverlay({'a': obj1, 'b': obj2})</code>",
        **config
    ),
    pn.widgets.StaticText(
        name="From HoloMap", value="<code>holomap.overlay()</code>", **config
    ),
)

animate_section = pn.Column(
    pn.widgets.StaticText(value="<h2>Animate Plots</h2>"),
    pn.widgets.StaticText(
        value=(
            """
            <code>
            import pandas as pd<br>
            import holoviews as hv<br>
            df = pd.DataFrame({<Br>
            &nbsp&nbsp&nbsp"x": [1, 2, 3, 4],<br>
            &nbsp&nbsp&nbsp"y": [2, 3, 4, 5],<br>
            &nbsp&nbsp&nbsp"t": [1, 1, 2, 2],<br>
            })<br>
            hv.Dataset(df).to.curve(kdims=["x"], vdims="y")
            </code>
        """
        )
    ),
)

column_1 = pn.Column(
    quick_start_section, help_section, layout_section, overlay_section, animate_section
)

# COLUMN 2

basic_plot_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Basic Plot</h2>"),
        pn.pane.HoloViews(
            hv.Curve([0, 1, 1]),
            width=50,
            align="center",
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Curve([0, 1, 0.5]),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Curve(data, kdims="x", vdims="y", label="C")</code><br>
            Opts: <code>color, line_dash, line_width</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Scatter([0, 1, 0.5]),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Scatter(data, kdims="x", vdims="y", label="S")</code><br>
            Opts: <code>color, marker, size</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Bars([0, 1, 0.5]),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Bars(data, kdims="x", vdims="y", label="B")</code><br>
            Opts: <code>color, fill_alpha, fill_color</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Area(
                {"x": [0, 1, 2], "y": [0, 1, 0.5], "y2": [0, 0.5, 0.25]},
                kdims="x",
                vdims=["y", "y2"],
            ),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Area(data, kdims="x", vdims=["y", "y2"], label="A")</code><br>
            Opts: <code>color, fill_alpha, bar_width</code>
            """,
            **config
        ),
    ),
)

gridded_plot_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Gridded Plot</h2>"),
        pn.pane.HoloViews(
            hv.Image(([0, 1, 0], [0, 1, 2], [[6, 7, 8], [9, 8, 10]])),
            width=50,
            align="center",
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Image(([0, 1, 0], [0, 1, 2], [[6, 7, 8], [9, 8, 10]])),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Image(data, kdims=["x", "y"], vdims="z", label="I")</code><br>
            Opts: <code>cmap, nodata, color_levels</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.QuadMesh(([0, 1, 0], [0, 1, 2], [[6, 7, 8], [9, 8, 10]])),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.QuadMesh(data, kdims=["x", "y"], vdims="z", label="Q")</code><br>
            Opts: <code>cmap, nodata, color_levels</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Contours(([0, 1, 0, 2], [0, 1, 2, 3], [[6, 7, 8], [7, 6, 5]])),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Contours(data, kdims=["x", "y"], vdims="z", label="C")</code><br>
            Opts: <code>cmap, levels, color_levels</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.HexTiles(([0, 1, 0, 2], [0, 1, 2, 3], [[6, 7, 8], [7, 6, 5]])).opts(
                scale=20
            ),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.HexTiles(data, kdims=["x", "y"], vdims="z", label="H")</code><br>
            Opts: <code>cmap, scale, color_levels</code>
            """,
            **config
        ),
    ),
)

reference_plot_section = pn.Column(
    pn.Row(
        pn.widgets.StaticText(value="<h2>Reference Plot</h2>"),
        pn.pane.HoloViews(
            hv.Text(0.5, 0.5, "Ref").opts(color="lightblue"),
            width=50,
            align="center",
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Text(0.5, 0.5, "Labels").opts(text_color="lightblue"),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Labels(data, kdims=["x", "y"], vdims="labels")</code><br>
            Opts: <code>text_font_size, text_align, text_baseline</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.HLine(0.5),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.HLine(y)</code><br>
            Opts: <code>line_color, line_width, line_alpha</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.VLine(0.5),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.VLine(x)</code><br>
            Opts: <code>line_color, line_width, line_alpha</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.Arrow(0.2, 0.2, "Arrow", "v").opts(
                arrow_color="lightblue",
                text_color="lightblue",
                fontsize=3,
            ),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.Arrow(x, y, "Text", "v")</code><br>
            Opts: <code>arrow_color, text_color, font_size</code>
            """,
            **config
        ),
    ),
    pn.Row(
        pn.pane.HoloViews(
            hv.element.tiles.Wikipedia(),
            width=75,
            align="center",
        ),
        pn.widgets.StaticText(
            name="",
            value="""
            <code>hv.element.tiles.Wikipedia()</code><br>
            Opts: <code>level, max_zoom, min_zoom</code>
            """,
            **config
        ),
    ),
)
column_2 = pn.Column(
    basic_plot_section,
    gridded_plot_section,
    reference_plot_section,
)

# COLUMN 3

options_section = pn.Column(
    pn.widgets.StaticText(value="<h2>Customizable Options &nbsp⚙️</h2>"),
    pn.widgets.StaticText(value="Usage: <code>obj.opts(**options)</h4>"),
    pn.widgets.StaticText(
        name="Add Labels",
        value="""<code>title="t", xlabel="x", ylabel="y", clabel="c"</code>""",
        **config
    ),
    pn.widgets.StaticText(
        name="Canvas Size", value="<code>width=300, height=300</code>", **config
    ),
    pn.widgets.StaticText(
        name="Show Legend", value="<code>show_legend=True</code>", **config
    ),
    pn.widgets.StaticText(
        name="Show Grid", value="<code>show_grid=True</code>", **config
    ),
    pn.widgets.StaticText(
        name="Show Colorbar", value="<code>colorbar=True</code>", **config
    ),
    pn.widgets.StaticText(
        name="Show Tooltips", value="""<code>tools=["hover"]</code>""", **config
    ),
    pn.widgets.StaticText(
        name="Active Tools",
        value="""<code>active_tools=["pan", "wheel_zoom"]</code>""",
        **config
    ),
    pn.widgets.StaticText(
        name="Share Axes", value="<code>shared_axes=True</code>", **config
    ),
    pn.widgets.StaticText(
        name="Specify Ticks",
        value="<code>xticks=[-1, 0, 1], yticks=[-1, 0, 1]</code>",
        **config
    ),
    pn.widgets.StaticText(
        name="Enlarge Labels", value="<code>fontscale=2</code>", **config
    ),
    pn.widgets.StaticText(
        name="Hide Toolbar", value="<code>toolbar=False</code>", **config
    ),
    pn.widgets.StaticText(
        name="Hide Axes", value="<code>xaxis=None, yaxis=None</code>", **config
    ),
    pn.widgets.StaticText(
        name="Invert Axes",
        value="<code>invert_xaxis=True, invert_yaxis=True</code>",
        **config
    ),
    pn.widgets.StaticText(
        name="See Options", value="<code>hv.help(obj)</code>", **config
    ),
)

interactivity_section = pn.Column(
    pn.widgets.StaticText(value="<h2>User Interaction &nbsp🤏</h2>"),
    pn.widgets.StaticText(
        value="""
        <code>
        import holoviews as hv<br>
        import numpy as np<br>
        hv.extension("bokeh")<br><br>

        # Create an empty Points element<br>
        points = hv.Points([])<br><br>

        # Create the Tap stream with the points element as the source<br>
        stream = hv.streams.Tap(source=points, x=np.nan, y=np.nan)<br><br>

        # Define what happens on click<br>
        def location(x, y):<br>
        &nbsp&nbsp# Create a plot with a moving dot and label upon click<br>
        &nbsp&nbspreturn hv.Points((x, y), label='x: %0.3f, y: %0.3f' % (x, y))<br><br>

        # Connect the Tap stream to the location callback<br>
        tap_dmap = hv.DynamicMap(location, streams=[stream])<br>
        (points * tap_dmap)
        </code>
    """
    ),
)

column_3 = pn.Column(
    options_section,
    interactivity_section,
)


# TEMPLATE
main_row = pn.Row(column_1, column_2, column_3)
template = pn.template.FastListTemplate(
    main=[main_row],
    logo="https://holoviews.org/_static/logo_horizontal_theme.png",
    title="Cheat Sheet (Bokeh Backend)",
    accent="#2b3e50",
    theme="dark",
)
template.servable()
