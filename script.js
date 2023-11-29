function updateModels() {
    var condition = document.getElementById("condition").value;
    var modelDropdown = document.getElementById("model");

    modelDropdown.innerHTML = "";

    fetch(`images/${condition}`)
        .then(response => response.json())
        .then(models => {
            models.forEach(model => {
                var option = document.createElement("option");
                option.text = model;
                modelDropdown.add(option);
            });
        });
}

updateModels();

document.getElementById("model").addEventListener("change", function () {
    var condition = document.getElementById("condition").value;
    var model = this.value;
    var imagePath = `images/${condition}/${condition}_${model}_Choices.png`;
    document.getElementById("selectedImage").src = imagePath;
});
