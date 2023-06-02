let selectImageButton = document.getElementById("selectImageButton");
let imageElement = document.getElementById("imageFromUser")

selectImageButton.addEventListener("click", function () {
    let input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.style.display = "none";
    document.body.appendChild(input);

    input.addEventListener("change", function () {
        let file = input.files[0];
        let reader = new FileReader();
        reader.addEventListener("load", function () {
            imageElement.src = reader.result;
        });
        reader.readAsDataURL(file);
        sendData(file);
    });

    input.click();
});

async function sendData(image) {

    const formData = new FormData();

    formData.append('image', image);

    const response = await fetch('../Home/ProcessImage', {
        method: 'POST',
        body: formData
    });

    const result = await response.text();  ///здесь будет какой нибудь текст с разделителем(диагноз|описание)
    let title = result.split("|")[0];
    let description = result.split("|")[1];
    document.getElementById("diagnosisTitle").innerHTML = title;
    document.getElementById("diagnosisDescription").innerHTML = description;
}