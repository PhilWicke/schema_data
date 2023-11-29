document.addEventListener("DOMContentLoaded", function () {
    const mainImage = document.getElementById("mainImage");
    const conditionSelector = document.getElementById("conditionSelector");
    const modelSelector = document.getElementById("modelSelector");

    const imageFolder = "images/";

    function updateImage() {
        const condition = conditionSelector.value;
        const model = modelSelector.value;
        const imagePath = `${imageFolder}${condition}_${model}_Choices.png`;
        mainImage.src = imagePath;
    }

    function populateModelOptions() {
        const condition = conditionSelector.value;
        const models = getModelsForCondition(condition);

        modelSelector.innerHTML = ""; // Clear previous options

        models.forEach((model) => {
            const option = document.createElement("option");
            option.value = model;
            option.text = model;
            modelSelector.add(option);
        });

        updateImage(); // Update the image when the models are populated
    }

    function getModelsForCondition(condition) {
        const modelSet = new Set();

        // Fetch models based on the condition
        fetch(`${imageFolder}${condition}/`)
            .then(response => response.text())
            .then(data => {
                const parser = new DOMParser();
                const htmlDoc = parser.parseFromString(data, "text/html");
                const files = Array.from(htmlDoc.querySelectorAll("a"))
                    .map(link => link.getAttribute("href"))
                    .filter(file => file.endsWith("_Choices.png"));

                files.forEach(file => {
                    const model = file.split("_")[1];
                    modelSet.add(model);
                });

                // Trigger the model options update
                populateModelOptions();
            });

        return Array.from(modelSet);
    }

    conditionSelector.addEventListener("change", populateModelOptions);
    modelSelector.addEventListener("change", updateImage);
});
