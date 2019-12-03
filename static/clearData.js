// ---- clear the JSON data used in the plots
function clearData() {
    globalJsonArray = [];
}

// ---- clear the data points presented in the HTML plots
function clearGraph(thisElement) {
    Plotly.deleteTraces(thisElement.parentNode, 0);
}