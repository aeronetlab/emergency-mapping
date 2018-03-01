def batch_generator(batch_size=1, image, mask, crop_size=0, patch_size=256, rotation=True):
    '''
    image: nparray, must have 3 dimension
    mask: nparray, 2 dimensions, same size as image
    patch_size: int, patch is square
    '''
    while 1:
        random_x = np.random.randint(0, mask.shape[1] - img_size)
        random_y = np.random.randint(0, mask.shape[0] - img_size)
        img_patch = img[:,
              random_x : random_x + patch_size, 
              random_y : random_y + patch_size].astype(float)
        mask_patch = mask[random_x : random_x + patch_size, 
              random_y : random_y + patch_size].astype(float)
        
        #if rotation:
            #angle = np.random.random(3) # 0, 90, 180, 270
            #
        # mask is cropped as it may be useful for some convnets that have outpud size less than input
        y = y[:, 
              crop_size : -crop_size, 
              crop_size : -crop_size]
        
        yield (x, y)
        
