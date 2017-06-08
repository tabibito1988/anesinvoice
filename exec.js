function init(){
    var spreadsheetid = document.getElementById("spreadsheetid").value();
    console.log(spreadsheetid);
    exec(spreadsheetid);
}

function exec(spreadsheetid){
    console.log("execの中にいるよ");

    location.replace("https://script.google.com/macros/s/AKfycbzxAOTOsx4w___t9hISXqxMadVzJVUysaTWjcZALzhEipc2I2uC/exec?spreadsheetid=" + spreadsheetid);

    console.log(spreadsheetid+"データの抽出ちゅ～");
}