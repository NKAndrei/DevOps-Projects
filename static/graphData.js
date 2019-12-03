function plotValues() {
    var itemArray = []

    // ---- check is the array is empty
    if (globalJsonValues != undefined) {
        console.log(globalJsonArray)
    } else {
        console.log("is empty")
    }

    // ---- parse the array of json values into an array of javascript objects for iteration
    for (var i = 0; i < globalJsonArray.length; i++) {
        itemArray[i] = []
        var stringObject = JSON.parse(globalJsonArray[i])
        var jsonObject = JSON.parse(stringObject)
        var key = Object.keys(jsonObject)
        for (item in jsonObject[key[0]]) {
            itemArray[i].push(jsonObject[key[0]][item])
        }

    }
    console.log(itemArray[0])
    console.log(itemArray[1])



    // ---- get html element and create a graph from the parsed json array
    TESTER = document.getElementById('tester');
    Plotly.plot(TESTER, [{
        x: itemArray[1],
        y: itemArray[0]
    }], {
        margin: { t: 0 }
    });
}

function addPlot(newPlotName) {
    var plotDiv = document.getElementById('plotDiv');
    var newPlot = document.createElement("div");
    newPlot.setAttribute("id", newPlotName);
    plotDiv.appendChild(newPlot);
}