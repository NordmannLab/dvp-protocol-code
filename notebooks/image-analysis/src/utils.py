import warnings

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
import spatialdata as sd


def random_sample_by_area(
    gdf: gpd.GeoDataFrame,
    target_area: float,
    exclusion_distance: float | None,
    random_state: int = 42,
):
    """Randomly select shapes from a geopandas dataframe up to a specified area.

    Parameters
    ----------
    gdf
        Shapes to select from
    target_area
        Target area in the units of the shape dataframe (typically square pixels).
    exclusion_distance
        Minimal distance between two adjacent shapes in order to select them in units of the shape dataframe (px).
        Any point of the next shape is guaranteed to have at least `exclusion_distance` from any point in all previous shapes.
        If None, allows for overlapping shapes
    random_state
        Random state to reproducibly select shapes

    Raises
    ------
    warning
        If target area is not reached
    """
    np.random.seed(random_state)
    random_indices = np.random.permutation(len(gdf))

    total_area = 0
    selected_cells = []
    for idx in random_indices:
        row = gdf.iloc[idx]

        # Skip if cells are too close to one another
        if exclusion_distance is not None:
            if any(
                shapely.dwithin(row.geometry, ref.geometry, distance=exclusion_distance)
                for ref in selected_cells
            ):
                continue

        selected_cells.append(row)
        total_area += row.geometry.area

        # Stop if target area is reached
        if total_area > target_area:
            break

    selected_cells = gpd.GeoDataFrame(
        pd.concat(selected_cells, axis=1).T, geometry=gdf.geometry.name
    )

    if selected_cells.geometry.area.sum() < target_area:
        warnings.warn(
            f"Target area was {target_area}, only identified cells with total area of {selected_cells.geometry.area.sum()}"
        )
    return sd.models.ShapesModel.parse(selected_cells)


def largest_polygon_from_multipolygon(geom):
    """Return largest geom from a multipolygon."""
    if not isinstance(geom, (shapely.Polygon, shapely.MultiPolygon)):
        raise ValueError(f"Must be polygon or multipolygon, not {type(geom)}")
    if isinstance(geom, shapely.Polygon):
        return geom

    idx_max = np.argmax([g.area for g in geom.geoms])
    warnings.warn(f"Select {idx_max} for geom")

    return geom.geoms[idx_max]
