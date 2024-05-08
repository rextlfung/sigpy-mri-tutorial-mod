# Rex's modifications made to the SigPy MRI tutorial

This repo is basically a forked-and-modded version of the original SigPy MRI tutorial [repo](https://github.com/mikgroup/sigpy-mri-tutorial).

The new notebooks are:
- [02a](02a.ipynb): Modified from 02-parallel-imaging. Includes 2D and 3D reconstructions of 100x100x100 GRE brain data orginally acquired for the purpose of sensitiviy map estimation
- [02b_mprage](02b_mprage.ipynb): Modified from 02a. Includes 3D reconstruciton of 256x256x192 MP-RAGE brain data. Main purpose was to test how the package performs at scale.
- [03a](03a.ipynb): Modified from 03-building-an-l1-wavelet-reocn-app. Supposed to be for imlementing low-rank constrained reconstruction. TODO!

Impressions:
- Overall, the performance of the package is decent but I can see scalability issues when reconstructing massive datasets like fMRI data.
- Guanhua says to just use BART instead for sensivity map estimation.
- Yongli said the sensitivity map estimation in SigPy worked better than the BART implementation for his project on calculating g-factor.

To run scripts in this library:
1. Clone the repo
2. Start a Python virtual environment and install the packages listed [here](requirements.txt)
3. Run! but make sure the file pathes and GPU IDs are valid for your machine
