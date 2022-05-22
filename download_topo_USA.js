// Import the dataset and select the elevation band.
var dataset = ee.Image('NASA/NASADEM_HGT/001');
var elevation = dataset.select('elevation');

// Set elevation visualization properties.
var elevationVis = {
  min: 0,
  max: 2000,
};

var clip = elevation.clip(geometry);

// Set elevation <= 0 as transparent and add to the map.
Map.addLayer(clip.updateMask(elevation.gt(0)), elevationVis, 'Elevation');
Map.setCenter(-102.729859, 41.789314, 2);

Export.image.toDrive({
  image: clip,
  description: 'topography_USA',
  folder: 'Topography',
  region: geometry,
  scale: 1000,
  crs: 'EPSG:4326',
  maxPixels: 1e10});
