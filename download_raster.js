var dataset = ee.Image('USGS/GMTED2010');
var elevation = dataset.select('be75');
var elevationVis = {
  min: -100.0,
  max: 6500.0,
  gamma: 3.5,
};

var clip = elevation.clip(geometry);

Map.setCenter(19.671824, 0.109486, 4);
Map.addLayer(clip, elevationVis, 'Elevation');

Export.image.toDrive({
  image: clip,
  description: 'topography_map_Africa',
  folder: 'TROPOMI',
  region: geometry,
  scale: 1000,
  crs: 'EPSG:4326',
  maxPixels: 1e10});
