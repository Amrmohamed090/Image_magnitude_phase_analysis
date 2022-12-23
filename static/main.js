var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);



const image1 = document.getElementById('image1');
var cropper1 = new Cropper(image1, {
        guids : false,
		movable: false,
		zoomable: false,
		minContainerHeight: image1.height,
		minContainerWidth: image1.width,
		minCanvasHeight: image1.height,
		minCanvasWidth: image1.width,
		// viewMode: 3,
		
  crop(event) {
  },
});
const image2 = document.getElementById('image2');
var cropper2 = new Cropper(image2, {
        guids : false,
		movable: false,
		zoomable: false,
		minContainerHeight: image2.height,
		minContainerWidth: image2.width,
		minCanvasHeight: image2.height,
		minCanvasWidth: image2.width,
		
  crop(event) {
  },
});
