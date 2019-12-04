function callbackFunction(response) {
    console.log(response);
}

// ---- get a new url from which to extract data and sent it to our Python backend for processing
function sendURL() {
    var urlValue = document.getElementById('inputId').value;
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callbackFunction(httpRequest.responseText)
        }
    }
    httpRequest.open('POST', 'http://127.0.0.1:5000/newData', true);
    httpRequest.setRequestHeader("Content-type", "application/json");
    jsonURL = "{" + "\"url\"" + ":" + "\"" + urlValue + "\"" + "}";
    httpRequest.send(jsonURL);
}