# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:35:39 2022

@author: opio
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import rasterio as rs
from matplotlib_scalebar.scalebar import ScaleBar

dataset = rs.open('C:/python_work/phd/paper3/trial/topography_map_Africa.tif')
band = dataset.read(1)

fig = plt.subplots(figsize=(8, 4), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
#plt.gcf().subplots_adjust(hspace=0, wspace=0.25)

img_extent = (-18.228303408101194, 53.0949387793988, -20.092435328999994, 16.1140338569136)
ax = plt.subplot(projection=cartopy.crs.PlateCarree())
plot_trr = ax.imshow(band, cmap='terrain', origin='upper', extent=img_extent, 
                  transform=ccrs.PlateCarree())
ax.coastlines(resolution='10m', color='black', linewidth=0.9)
ax.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax.add_feature(lakes_10m, facecolor='none', edgecolor='k')
#colorbar_axes_tro = plt.gcf().add_axes([0.41, 0.06, 0.205, 0.04])
cb = plt.colorbar(plot_trr, orientation='vertical', 
                  label='Meters above sea level', shrink=.8)
plt.show()
