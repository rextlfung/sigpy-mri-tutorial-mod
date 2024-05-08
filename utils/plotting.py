import matplotlib.pyplot as plt
'''
Plot the middle 3 views of a 3D brain volume

Input arguments:
img: 3D volume of brain (3d array)
title: a title for the image volume (str)
'''
def mid3views(img, title, cmap='gray'):
    # axial
    plt.figure()
    plt.imshow(img[round(img.shape[0]/2),:,:],cmap=cmap,origin='lower')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()

    # coronal
    plt.figure()
    plt.imshow(img[:,round(img.shape[1]/2),:],cmap=cmap,origin='lower')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.colorbar()

    # sagittal
    plt.figure()
    plt.imshow(img[:,:,round(img.shape[2]/2)],cmap=cmap,origin='lower')
    plt.title(title)
    plt.xlabel('y')
    plt.ylabel('z')
    plt.colorbar()

    return None