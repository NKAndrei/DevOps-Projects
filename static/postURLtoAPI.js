function callbackFunction(response) {
    console.log(response);
}

// ---- get a new url from which to extract data and sent it to our Python backend for processing
function sendURL() {
    var urlValue = document.getElementById('inputId').value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(xhttp.responseText)
        }
    }
    xhttp.open('POST', 'http://127.0.0.1:5000/newData', true);
    xhttp.setRequestHeader("Content-type", "application/json");
    jsonURL = "{" + "\"url\"" + ":" + "\"" + urlValue + "\"" + "}";
    xhttp.send(jsonURL);
}