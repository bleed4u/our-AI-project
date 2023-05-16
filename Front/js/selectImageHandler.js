var selectImageButton = document.getElementById("selectImageButton");
var imageElement = document.getElementById("imageFromUser")

selectImageButton.addEventListener("click", function() {
    var input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.style.display = "none";
    document.body.appendChild(input);

    input.addEventListener("change", function() {
        var file = input.files[0];
        var reader = new FileReader();
    reader.addEventListener("load", function() {
      imageElement.src = reader.result;
    });
    reader.readAsDataURL(file);
    });

    input.click();
});
