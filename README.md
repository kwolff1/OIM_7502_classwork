# Altair Visualization Project – Kyle Wolff

I used the Altair Python library to create a series of charts using a bikeshare dataset. Altair makes it really easy to build clean, interactive visuals with just a few lines of code.

---

## What is Altair?

Altair is a Python library for making charts. It’s built on something called Vega-Lite, and it works really well with Pandas. One of the best things about it is that interactivity (like tooltips and zooming) comes built-in without needing extra work.

---

## How to Set It Up

To run the notebook, you just need to install Altair:

```bash
pip install altair
```

And then add this line if your dataset has more than 5,000 rows:

```python
alt.data_transformers.disable_max_rows()
```

---

## What’s in This Project

### Quick Charts:
- Line chart: Bikers by hour
- Bar chart: Average bikers by day
- Heatmap: Bikers by hour and weather

### Advanced Charts:
- Interactive line chart: Bikers vs temperature (with tooltips and zoom)
- Faceted line chart: Bikers by hour, split by season
- Highlightable stacked bar chart: Registered vs casual
- Box plot: Biker count distribution by weather

---

## Why I Picked Altair

I wanted to try a library that wasn’t too common but was still useful. Altair ended up being really smooth to work with and perfect for exploring data quickly. I like that it’s simple but still has all the features I’d need.
