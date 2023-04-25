## Box-counting 2D images to compute the fractal dimension ##

## Hausdorff Dimension

"The Hausdorff dimension is a measure of the "roughness" or "complexity" of a geometric object or a set in a metric space. It helps to describe the scaling properties of fractals and irregular shapes. The Hausdorff dimension can be an integer or a non-integer value, depending on the object being measured. It provides a way to quantify the space-filling properties of an object, particularly when the object does not fit well into traditional Euclidean dimensions (such as points, lines, or planes)."


## Implementation of Hausdorff dimension estimation using the box-counting method.

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
