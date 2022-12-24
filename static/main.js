var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

/* 
var cropped

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
	cropped = this.cropper.crop();
	console.log(cropped)
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
}); */
/* 
var cropper1;
var cropper2;
function readURL1(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
			$('#image1').attr('src', e.target.result)
		};
		reader.readAsDataURL(input.files[0]);
		var image1 = document.getElementById('image1');
		cropper1 = new Cropper(image1, {
		crop: function(e) {
			console.log(e.detail.x);
			console.log(e.detail.y);
		}
		});
		}
}
function readURL2(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
			$('#image2').attr('src', e.target.result)
		};
		reader.readAsDataURL(input.files[0]);
		var image2 = document.getElementById('image2');
		cropper2 = new Cropper(image2, {
			crop: function(e) {
				console.log(e.detail.x);
				console.log(e.detail.y);
			}
			});
			}
	}

 $(document).on('click', '#combine_btn', function (e) {
    e.preventDefault();
	

	post_form(cropper1.getCroppedCanvas().toDataURL()) 

  });
function post_form(formData){
	$.ajax({
		type: 'POST',
		url: 'http://127.0.0.1:5000/',
		
		data: {"fffgf":formData},
			
		
		processData: false,
		
		success: function () {
		 
	  }
		
	  })
}

$("form[name='combine']").on("submit", function(ev) {
	ev.preventDefault(); // Prevent browser default submit.
  
	var formData = new FormData(this);
	cropper1.getCroppedCanvas().toBlob(function (blob) {
		formData.append('croppedImage', blob);
	});
	$.ajax({
	  url: 'http://127.0.0.1:5000/',
	  type: "POST",
	  data: formData,
	  success: function (msg) {
		alert(msg)
	  },
	  cache: false,
	  contentType: false,
	  processData: false
	});
	  
  }); 
 */

  var cropper1;
  var cropper2;
  function readURL1(input) {
	  if (input.files && input.files[0]) {
		  var reader = new FileReader();
		  reader.addEventListener("load", () => {
			document.querySelector("#image1").src = reader.result
		  })
	
		  reader.readAsDataURL(input.files[0]);


		  var image1 = document.getElementById('image1');
		  cropper1 = new Cropper(image1, {
		  crop: function(e) {
			  console.log(e.detail.x);
			  console.log(e.detail.y);
		  }
		  });
		  initCropper1()
		  }
  }
  function readURL2(input) {
	  if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.addEventListener("load", () => {
		  document.querySelector("#image2").src = reader.result
		})
  
		reader.readAsDataURL(input.files[0]);
		  var image2 = document.getElementById('image2');
		  cropper2 = new Cropper(image2, {
			  crop: function(e) {
				  console.log(e.detail.x);
				  console.log(e.detail.y);
			  }
			  });
			  initCropper2()
			  }
	  }
  
function initCropper1(){
	var image = document.getElementById('image1');
	cropper1 = new Cropper(image, {
	  crop: function(e) {
		console.log(e.detail.x);
		console.log(e.detail.y);
	  }
	});

	// On crop button clicked
	
	
	document.getElementById('combine_btn').addEventListener('click', function(){
		var imgurl =  cropper1.getCroppedCanvas().toDataURL();
		var img = document.createElement("img");
		img.src = imgurl;
		document.getElementById("cropped_result1").appendChild(img);


			cropper1.getCroppedCanvas().toBlob(function (blob) {
				  var formData = new FormData();
				  formData.append('croppedImage', blob);
				  // Use `jQuery.ajax` method
				  /* $.ajax("http://localhost:5000/", {
					method: "POST",
					data: formData,
					processData: false,
					contentType: "multipart/form-data",
					success: function () {
					  console.log('Upload success');
					},
					error: function () {
					  console.log('Upload error');
					}
				  }); */
			});
		
	})
}

function initCropper2(){
	var image = document.getElementById('image2');
	var cropper2 = new Cropper(image, {
	  aspectRatio: 1 / 1,
	  crop: function(e) {
		console.log(e.detail.x);
		console.log(e.detail.y);
	  }
	});

	// On crop button clicked
	document.getElementById('combine_btn').addEventListener('click', function(){
		var imgurl =  cropper2.getCroppedCanvas().toDataURL();
		var img = document.createElement("img");
		img.src = imgurl;
		document.getElementById("cropped_result2").appendChild(img);


			cropper.getCroppedCanvas().toBlob(function (blob) {
				  var formData = new FormData();
				  formData.append('croppedImage', blob);
				  // Use `jQuery.ajax` method
				 /*  $.ajax('/path/to/upload', {
					method: "POST",
					data: formData,
					processData: false,
					contentType: false,
					success: function () {
					  console.log('Upload success');
					},
					error: function () {
					  console.log('Upload error');
					}
				  }); */
			});
		
	})
} 
