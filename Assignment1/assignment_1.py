import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr






if __name__ == "__main__":
    path_data = "N21E039.SRTMGL1_NC.nc"
    dset = xr.open_dataset(path_data)
    #pdb.set_trace()

    DEM = np.array(dset.variables["SRTMGL1_DEM"])
    dset.close()

    #pdb.set_trace()

    plt.figure(figsize = (10,8))
    plt.imshow(DEM,cmap = "jet")
    cbar = plt.colorbar(shrink = 0.9)
    cbar.set_label("Elevation (m asl)")
    plt.show()