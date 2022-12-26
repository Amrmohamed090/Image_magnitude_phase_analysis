var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let upload1 = document.querySelector('#image_input1')
let upload2 = document.querySelector('#image_input2')
let result1 = document.querySelector('#result1')
let result2 = document.querySelector('#result2')
let submit = document.getElementById("combine_btn")

let image1_x1,image1_x2,image2_x1,image2_x2,image1_y1,image1_y2,image2_y1,image2_y2

upload1.addEventListener('change', e => {
  if (e.target.files.length) {
    // start file reader
    const reader = new FileReader();
    reader.onload = e => {
      if (e.target.result) {
        // create new image
        let img = document.createElement('img');
        img.id = 'image';
        img.src = e.target.result;
        // clean result before
        result1.innerHTML = '';
        // append new image
        result1.appendChild(img)
        // init cropper
        cropper1 = new Cropper(img, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function(e) {

            image1_x1 = e.detail.x
  
            image1_y1 = e.detail.y
   
            image1_x2 = e.detail.width + e.detail.x

            image1_y2 = e.detail.height + e.detail.y
          }
        });
      }
    };
    reader.readAsDataURL(e.target.files[0]);
  }
});

upload2.addEventListener('change', e => {
  if (e.target.files.length) {
    // start file reader
    const reader = new FileReader();
    reader.onload = e => {
      if (e.target.result) {
        // create new image
        let img2 = document.createElement('img');
        img2.id = 'image';
        img2.src = e.target.result;
        // clean result before
        result2.innerHTML = '';
        // append new image
        result2.appendChild(img2)
        // init cropper
        cropper2 = new Cropper(img2, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function(e) {
            image2_x1 = e.detail.x
  
            image2_y1 = e.detail.y
   
            image2_x2 = e.detail.width + e.detail.x

            image2_y2 = e.detail.height + e.detail.y
          }
        });
      }
    };
    reader.readAsDataURL(e.target.files[0]);
  }
});


submit.addEventListener('click', e => {
  e.preventDefault();

  //عشان لو الصورتين الأثنين مش مرفوعين هيطلع ايرور
  try {

    let imgSrc1 = cropper1.getCroppedCanvas().toDataURL();
    let imgSrc2 = cropper2.getCroppedCanvas().toDataURL();
    const option = document.getElementById("image1_info");
    console.log(option.value)

    console.log(imgSrc1)
    console.log(imgSrc2)
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5000/saveImg',
      data: {
        imgdata1: imgSrc1,
        imgdata2: imgSrc2,
        option : option.value,
        img1_x1 : image1_x1,
        img1_x2 : image1_x2,
        img1_y1 : image1_y1,
        img1_y2 : image1_y2,
        img2_x1 : image2_x1,
        img2_x2 : image2_x2,
        img2_y1 : image2_y1,
        img2_y2 : image2_y2
      },
      success: function (res) {
        var responce = JSON.parse(res)
        console.log(responce)
        
        var big_cont = document.getElementById("images_container")

        const cont12 = document.getElementById("cont1")
        cont12.remove()
        var img_1 = document.createElement("div")
        img_1.className = "container"
        img_1.id = "cont1"
        img_1.innerHTML = responce[1]
        big_cont.appendChild(img_1)

      }



    })
  } catch (error) {
    alert("please upload two images")
  }


}
)