"""
Example how to use csv grid to convert coordinates into country codes.
"""
import csv
import math

def load_grid(csv_path):
    grid_data = []
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            grid_data.append([cell.strip() for cell in row])

    max_width = max(len(row) for row in grid_data)
    for row in grid_data:
        if len(row) < max_width:
            row += [""] * (max_width - len(row))

    row_count = len(grid_data)
    col_count = max_width
    lon_resolution = 360.0 / col_count
    lat_resolution = 180.0 / row_count

    return {
        "grid": grid_data,
        "row_count": row_count,
        "col_count": col_count,
        "lon_resolution": lon_resolution,
        "lat_resolution": lat_resolution,
    }

def grid_position(lat, lon, grid_info):
    col = int(math.floor((lon + 180.0) / grid_info["lon_resolution"]))
    row = int(math.floor((90.0 - lat) / grid_info["lat_resolution"]))
    row = max(0, min(grid_info["row_count"] - 1, row))
    col = max(0, min(grid_info["col_count"] - 1, col))
    return row, col

def country_code_at(lat, lon, grid_info):
    row, col = grid_position(lat, lon, grid_info)
    return grid_info["grid"][row][col]

grid_info = load_grid("grid1440x720.csv")

print(country_code_at(40.71, -74.01, grid_info))    # United States
print(country_code_at(52.37, 4.90, grid_info))      # Netherlands
print(country_code_at(39.58, 116.46, grid_info))    # China
