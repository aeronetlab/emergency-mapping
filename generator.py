import numpy as np

def random_augmentation(img, mask):
    #you can add any augmentations you need
    return img, mask

def batch_generator(image, mask, 
                    batch_size=1, 
                    crop_size=0, 
                    patch_size=256,
                    bbox= None,
                    augmentation=False):
    '''
    image: nparray, must have 3 dimension
    mask: nparray, 2 dimensions, same size as image
    batch_size: int, number of images in a batch
    patch_size: int, size of the image returned, patch is square
    crop_size: int, how much pixels should be cropped off the mask
    bbox: None or tuple of 4 ints, (min_y, max_y, min_x, max_x), the data is selected from within the bbox
    augmentation: turn on/off data augmentation. The augmentation function is random_augmentation() above
    
    returns batch of image and mask patches, image is turned to 'channels last' as required by unet
    '''
    if np.ndim(mask) != 2 or np.ndim(image) != 3:
        raise ValueError('image must have 3 dims and mask 2 dims')
    if mask.shape != image.shape[1:]:
        raise ValueError('image and mask shape is different')
 
    im_max = float(np.max(image))
    mask_max = 1.0
    
    #select subimage
    if bbox is not None:
        # check bbox
        if bbox[0] < 0 or bbox [2] < 0 \
            or bbox[1] > mask.shape[0] or bbox[3] > mask.shape[0] \
            or bbox[0] + patch_size > bbox[1] or bbox[2] + patch_size > bbox[3] \
            or patch_size <= 0:
            raise ValueError("Incorrect bbox or patch size")
        img_ = image[:, bbox[0] : bbox[1], bbox[2]:bbox[3]]
        mask_ = mask[bbox[0] : bbox[1], bbox[2]:bbox[3]]
    else:
        img_ = image
        mask_ = mask
    while 1:
        x = []
        y = []
        for i in range (batch_size):
            random_x = np.random.randint(0, mask_.shape[1] - patch_size)
            random_y = np.random.randint(0, mask_.shape[0] - patch_size)
            img_patch = img_[:,
                  random_y : random_y + patch_size, 
                  random_x : random_x + patch_size] / im_max
            
            # transform the image from channels-first (rasterio format) to channels-last (default tensorflow format)
            img_patch = np.moveaxis(img_patch, 0, 2)
            
            mask_patch = mask_[random_y : random_y + patch_size, 
                  random_x : random_x + patch_size] / mask_max
            
            if augmentation:
                img_patch, mask_patch = random_augmentation(img_patch, mask_patch)
                
            # mask is cropped as it may be useful for some convnets that have output size less than input
            if crop_size > 0:
                mask_patch = mask_patch[crop_size : -crop_size, 
                                        crop_size : -crop_size]
            
            mask_patch = np.expand_dims(mask_patch, 2)
            x.append(img_patch)
            y.append(mask_patch)
        yield (np.array(x), np.array(y))
        
