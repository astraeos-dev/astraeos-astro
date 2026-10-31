"""Positional astronomy in pure Python, ported from libastro, the C core of PyEphem.

The package only needs the Python standard library. LICENSE.txt holds the MIT
notices of libastro and PyEphem, which must travel with it.
scripts/extract_libastro.py regenerates the _*_data.py tables.

Angles are in degrees and times in Julian days, unless a docstring says
otherwise: positions take Terrestrial Time (TT), observations Universal Time.
"""

__version__ = "0.1.0"

from .constellations import NAMES as CONSTELLATION_NAMES, constellation
from .nutation import mean_obliquity, nutation
from .sun import SunObservation, SunPosition, observe_sun, sun_position
from .timescales import delta_t, greenwich_mean_sidereal_time, julian_day

__all__ = [
    "CONSTELLATION_NAMES",
    "__version__",
    "SunObservation",
    "SunPosition",
    "constellation",
    "delta_t",
    "greenwich_mean_sidereal_time",
    "julian_day",
    "mean_obliquity",
    "nutation",
    "observe_sun",
    "sun_position",
]
