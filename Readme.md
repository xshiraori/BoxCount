## Box-counting 2D images to compute the fractal dimension ##

Implementation of Hausdorff dimension estimation using the box-counting method.

An example of the computation process can be seen below.

![](https://galileounbound.files.wordpress.com/2020/12/image-16.png?w=512)

## Usage and restrictions ##
- The algorithm marks non-white pixels as one and white pixels as zero.
- To be more precise about the result, it only accepts NxN images as input.

**Example usage**,

    from ImageFractalDimension import ImageFractalDimension

	image = ImageFractalDimension('sierpinski_512x512.png', 512)
    print(image.fractal_dim) # result will be printed on the graph so this is just an example to show you the attribute if you want to use the result
    image.graph()

**Output**:

![Imgur](https://i.imgur.com/zJYjLEZ.png)
