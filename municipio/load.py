import os

from django.contrib.gis.utils import LayerMapping

from .models import Municipio

# Auto-generated `LayerMapping` dictionary for Municipio model
# Auto-generated `LayerMapping` dictionary for Municipio model
municipio_mapping = {
    'name': 'name',
    'description': 'description',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join('data', 'municipio.geojson'))

def run_municipios(verbose=True):
    lm = LayerMapping(Municipio, shp, municipio_mapping)
    lm.save(strict=True, verbose=True)
