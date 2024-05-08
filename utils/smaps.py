import numpy as np
import scipy as scp
import sigpy as sp
from tqdm import trange

'''
THIS FUNCTION DOESN'T WORK. It produces really bad sensitivity maps

Estimate 3D sensitivity maps at a lower resolution then upsample back to original resolution

Inputs:
ksp: multicoil 3D k-space data (ndarray: Ncoils x Nz x Ny x Nx). Assume Nz = Ny = Nx
ds_factor: the resolution scale for computing the sensitivity maps at
device: which compute device to use (int). Default = 0 (GPU)

Outputs:
mps: multicoil 3D sensitivity maps in image domain (ndarray: Ncoils x Nz x Ny x Nx)
'''
def compute_smaps(ksp, ds_factor=0.5, device=0):
    Ncoils, Nz, Ny, Nx = ksp.shape

    # Crop out central portion of k-space
    ksp_cropped = ksp[:,
                      round(Nz*1/2*(1 - ds_factor)):round(Nz*1/2*(1 + ds_factor)),
                      round(Ny*1/2*(1 - ds_factor)):round(Ny*1/2*(1 + ds_factor)),
                      round(Nx*1/2*(1 - ds_factor)):round(Nx*1/2*(1 + ds_factor)),]

    # Transform to hybrid space
    mps = np.zeros_like(ksp)
    hybrid_ksp = sp.ifft(ksp_cropped, axes=(1,)) # coil, z, ky, kx

    # compute low res smaps and upsample
    for z in trange(round(Nz*ds_factor)):
        mps_lr = sp.mri.app.EspiritCalib(hybrid_ksp[:,z,:,:],device=device,show_pbar=False).run().get()
        for coil in range(mps.shape[0]):
            mps[coil,z,:,:] = scp.ndimage.zoom(mps_lr[coil,:,:],1/ds_factor)

    return mps