let headersList = {
 "Content-Type": "application/json"
}

let bodyContent = JSON.stringify({
  "url" : "https://google.com"
});

let response = await fetch("http://localhost:8000/qr-code", { 
  method: "POST",
  body: bodyContent,
  headers: headersList
});

let data = await response.text();
console.log(data);
