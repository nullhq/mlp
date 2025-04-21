
async function obtenir_espece_de_iris() {
    let spH = document.getElementById("sepallength").value;
    let spW = document.getElementById("sepalwidth").value;
    let ptH = document.getElementById("petallength").value;
    let ptW = document.getElementById("petalwidth").value;

    if (spH == "" || spW == "" || ptH == "" || ptW == "") {
        alert("Veuillez remplir tous les champs");
        return;
    }

    let reponse_de_api = await fetch("http://127.0.0.1:5000/api", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            spH: spH,
            spW: spW,
            ptH: ptH,
            ptW: ptW
        })
    });
    
    const reponse_de_api_json = await reponse_de_api.json();
    document.getElementById("iris_espece").innerHTML = `Iris ${reponse_de_api_json.specie}`;
    document.getElementById("iris_espece_image").src = `./images/${reponse_de_api_json.specie.toLowerCase()}.jpg`;
}

document.getElementById("predire").addEventListener("click", obtenir_espece_de_iris);