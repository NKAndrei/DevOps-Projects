// ---- plot the values on an existing HTML div element from the json values extracted from the Python API - REF getData
function plotValues(thisElement) {
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

    PLOT = thisElement.parentNode;
    Plotly.newPlot(PLOT, [{
        x: itemArray[1],
        y: itemArray[0]
    }], {
        margin: { t: 0 }
    });
    clearData();
}

// ---- create a new independent plot on the same HTML document
function addPlot() {
    // ---- clear old json data beforehand
    clearData();


    // ---- create new empty plot in the 'getData' div and append
    var mainDiv = document.getElementById('mainDiv');
    var plotDiv = document.getElementById('getData');
    var divClone = plotDiv.cloneNode(true);
    var childPlotlyDiv = divClone.getElementsByClassName("plot-container plotly");
    for (item in childPlotlyDiv) {
        childPlotlyDiv[item].innerHTML = ''
    }
    mainDiv.appendChild(divClone);

}