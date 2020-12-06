function pollTemperature() {
  var xhttp = new XMLHttpRequest();
  window.setTimeout(pollTemperature, 500);
  xhttp.open("GET", "/api/temperature", true);
  xhttp.timeout = 1000;
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        updateTemperature(this.response);
      }
    }
  }
}

function pollCPU() {
  var xhttp = new XMLHttpRequest();
  window.setTimeout(pollCPU, 500);
  xhttp.open("GET", "/api/cpu", true);
  xhttp.timeout = 1000;
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        updateCPU(this.response);
      }
    }
  }
}

function pollMEM() {
  var xhttp = new XMLHttpRequest();
  window.setTimeout(pollMEM, 500);
  xhttp.open("GET", "/api/memory", true);
  xhttp.timeout = 1000;
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4) {
      if (this.status === 200) {
        updateMEM(this.response);
      }
    }
  }
}

window.setTimeout(pollTemperature, 500);
window.setTimeout(pollCPU, 500);
window.setTimeout(pollMEM, 500);
