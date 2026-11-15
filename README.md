<p align="center"><img src="https://raw.githubusercontent.com/astraeos-dev/astraeos-astro/main/assets/brand/icon.svg" width="128" height="128" alt="astraeos-astro"></p>

# astraeos-astro — the Sun's position in pure Python

> The Sun's position in pure Python, ported from libastro, the C core of [PyEphem](https://rhodesmill.org/pyephem/).

[![PyPI](https://img.shields.io/pypi/v/astraeos-astro?label=version&color=f2b84b)](https://pypi.org/project/astraeos-astro/)
[![Tests](https://github.com/astraeos-dev/astraeos-astro/actions/workflows/tests.yml/badge.svg)](https://github.com/astraeos-dev/astraeos-astro/actions/workflows/tests.yml)
[![MIT licence](https://img.shields.io/github/license/astraeos-dev/astraeos-astro?label=licence)](https://github.com/astraeos-dev/astraeos-astro/blob/main/LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python)

<a href="https://buymeacoffee.com/gregorychau"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="40"></a>

**Install**: `pip install astraeos-astro`. An idea, a problem? [Open a request](https://github.com/astraeos-dev/astraeos-astro/issues/new/choose).

**Active project** · one of the Astraeos projects: [website](https://astraeos-dev.github.io/Gaia/#/astraeos-astro) · [Helios](https://github.com/astraeos-dev/Helios) · [Céleste](https://github.com/astraeos-dev/Celeste_App) · [Océanos](https://github.com/astraeos-dev/Oc-anos)

*Read this in: [English](#english) | [Français](#français)*

---

It needs nothing but the Python standard library, so it installs anywhere Python runs, with no compiler. It matches PyEphem to within a few thousandths of an arcsecond. [Helios](https://github.com/astraeos-dev/Helios), a Home Assistant integration, computes the Sun with it.

## English

### Install

```bash
pip install astraeos-astro
```

Python 3.10 or later.

### Usage

```python
from datetime import datetime, timezone
import astraeos_astro as astro

jd = astro.julian_day(datetime(2024, 6, 21, 12, 0, tzinfo=timezone.utc))
seen = astro.observe_sun(jd, latitude=48.8566, longitude=2.3522, elevation_m=35)
print(f"altitude {seen.altitude:.4f}°, azimuth {seen.azimuth:.4f}°")
# altitude 64.5363°, azimuth 183.9972°

position = seen.position
code = astro.constellation(
    position.astrometric_right_ascension,
    position.astrometric_declination,
    position.jd_tt,
)
print(code, astro.CONSTELLATION_NAMES[code])
# Gem Gemini
```

- Angles are in degrees, longitudes positive east, and times in Julian days.
- `observe_sun` takes Universal Time and applies ΔT itself; `sun_position` takes Terrestrial Time.
- Altitude and azimuth are topocentric (parallax included) and without refraction. Azimuth is 0° north, 90° east.

### What it computes

| Module | Port of | Contents |
| --- | --- | --- |
| `timescales` | `mjd.c`, `deltat.c`, `utc_gst.c` | Julian dates, ΔT, Greenwich mean sidereal time (IAU 1982) |
| `vsop87` | `vsop87.c` | The Earth from VSOP87D (406 terms, as libastro keeps them), FK5 |
| `nutation` | `obliq.c`, `nutation.c` | Mean obliquity, IAU 1980 nutation (106 terms) |
| `frames` | `eq_ecl.c`, `aberration.c`, `precess.c`, `parallax.c`, `aa_hadec.c` | Ecliptic to equator, nutation, aberration, precession, parallax, altitude and azimuth |
| `sun` | `sun.c`, `circum.c` | `sun_position(jd_tt)` and `observe_sun(jd, latitude, longitude, elevation_m)` |
| `constellations` | `constel.c` | IAU boundaries at B1875.0 (Roman's method), all 88 constellations |

### Accuracy against PyEphem 4.2.1

| Value | Largest difference |
| --- | --- |
| Altitude / azimuth | 0.012″ / 0.05″ |
| Apparent right ascension and declination | < 0.001″ |
| Distance | < 10⁻⁷ AU (15 km) |
| ΔT | identical |
| Constellation | identical |

Measured on 3,000 random moments and places from 1900 to 2100. The remaining differences come from PyEphem itself, which stores altitude, azimuth and distance in single precision.

### Data tables

The `_*_data.py` modules hold libastro's tables: VSOP87, nutation, ΔT and constellation boundaries. `scripts/extract_libastro.py` regenerates them from the `libastro` folder of a PyEphem source distribution, byte for byte:

```bash
python scripts/extract_libastro.py path/to/ephem-4.2.1/libastro
```

### Tests

```bash
pip install -e ".[test]"
pytest
```

PyEphem is only the reference the tests compare against; the tests that need it are skipped without it.

### License

MIT. astraeos-astro ports libastro (Elwood Downey) and PyEphem (Brandon Rhodes), both under the MIT license, and Craig Counterman's precession routine. Their notices are in [`src/astraeos_astro/LICENSE.txt`](src/astraeos_astro/LICENSE.txt), which ships with the package.

## Français

**astraeos-astro** calcule la position du soleil en Python pur, à partir d'une traduction de libastro, le cœur en C de [PyEphem](https://rhodesmill.org/pyephem/). Il ne dépend que de la bibliothèque standard de Python et s'installe partout sans compilateur. Il rejoint PyEphem à quelques millièmes de seconde d'arc près. [Helios](https://github.com/astraeos-dev/Helios), une intégration Home Assistant, s'en sert pour calculer le soleil.

```bash
pip install astraeos-astro
```

Python 3.10 ou plus récent.

- Les angles sont en degrés, les longitudes positives vers l'est et les dates en jours juliens.
- `observe_sun` prend le temps universel et applique ΔT lui-même ; `sun_position` prend le temps terrestre.
- La hauteur et l'azimut sont topocentriques (parallaxe comprise) et sans réfraction. L'azimut vaut 0° au nord, 90° à l'est.

L'exemple, le détail des modules et les mesures de précision sont dans la [section en anglais](#english). Les tables de données se régénèrent avec `scripts/extract_libastro.py`, et les tests se lancent avec `pip install -e ".[test]"` puis `pytest`.

Licence MIT. astraeos-astro traduit libastro (Elwood Downey) et PyEphem (Brandon Rhodes), tous deux sous licence MIT, ainsi que la routine de précession de Craig Counterman. Leurs mentions figurent dans [`src/astraeos_astro/LICENSE.txt`](src/astraeos_astro/LICENSE.txt), livré avec le paquet.
