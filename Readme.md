## Box-counting 2D images to compute the fractal dimension ##

Implementation of Hausdorff dimension estimation using the box-counting method.

An example of the computation process can be seen below.

![](https://galileounbound.files.wordpress.com/2020/12/image-16.png?w=512)

## Usage and restrictions ##
- The algorithm marks non-white pixels as one and white pixels as zero.
- To be more precise about the result, it only accepts NxN images as input.

**Example usage**,

    from ImageFractalDimension import ImageFractalDimension
    
    image_name = 'sierpinski_512x512.png'
    image_size = 512
    
	image = ImageFractalDimension(image_name, image_size)
    print(image.fractal_dim)
    image.graph()

**Output**:

![Imgur](https://i.imgur.com/zJYjLEZ.png)
