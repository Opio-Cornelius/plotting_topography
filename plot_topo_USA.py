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
#from matplotlib_scalebar.scalebar import ScaleBar

dataset = rs.open('C:/python_work/phd/atm_science/topography_USA.tif')
band = dataset.read(1)

fig = plt.subplots(figsize=(8, 7), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
#plt.gcf().subplots_adjust(hspace=0, wspace=0.25)

img_extent = (-133.10982972349126, -54.35982972349127, 23.66480628870596, 50.583344454973876)
ax = plt.subplot(projection=cartopy.crs.PlateCarree())
plot_trr = ax.imshow(band, cmap='terrain', origin='upper', extent=img_extent, 
                  transform=ccrs.PlateCarree())
ax.coastlines(resolution='10m', color='black', linewidth=0.9)
ax.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
ax.add_feature(lakes_10m, facecolor='none', edgecolor='k')
colorbar_axes = plt.gcf().add_axes([0.2, 0.3, 0.6, 0.03])
cb = plt.colorbar(plot_trr, colorbar_axes, orientation='horizontal', 
                  label='Meters above sea level')
plt.show()
