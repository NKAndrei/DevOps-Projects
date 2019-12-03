// ---- main callback function for all other async functions
function getJsonValue(jsonValues) {
    globalJsonArray.push(jsonValues)
    globalJsonValues = jsonValues
    return jsonValues
}

// ---- a generic function call that triggers the python api to retrieve data
// ---- the uriElement is passed from the html document
// ---- the uriElement defines what api is triggered and what info is returned
function getData(uriElement) {
    const httpRequest = new XMLHttpRequest();
    const url = 'http://127.0.0.1:5000/' + uriElement;
    httpRequest.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            getJsonValue(httpRequest.responseText)
        }
    }
    httpRequest.open("GET", url)
    httpRequest.send()
}