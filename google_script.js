// Google Script to convert and export money diaries google sheet to valid JSON

// ADD MENU OPTION TO SHEET
function onOpen() {
  var spreadsheet = SpreadsheetApp.getActive();
  var menuItems = [{ name: "generate json", functionName: "getData_" }];
  spreadsheet.addMenu("JSONDATA", menuItems);
  getData_();
}

// STRIP AND STANDARDIZE KEY STRING
function cleanKey(str) {
  var string = str
    .toLowerCase()
    .replace(":", "")
    .replace("my", "")
    .trim()
    .split(" ")
    .join("_");
  return string;
}

// STRIP VALUE TO STRING
function cleanValue(str) {
  var string = str;
  if (isNaN(str)) {
    string = str.replace("\n", "").trim();
  }
  return string;
}

// STRIP AND CONVERT VALUE TO INTEGER
function extractValue(str) {
  var res = str;
  if (isNaN(str) && str) {
    var extracted = str.replace(",", "").match(/\d+/);
    if (extracted) {
      var num = parseInt(extracted[0].replace("$", ""));
      res = Math.round(num);
    } else {
      res = 0;
    }
  }
  return res;
}

// CONVERT DATA TO JSON BLOB & SAVE TO GOOGLE DRIVE
function makeJson(obj) {
  var jsonObject = JSON.stringify(obj, null, 4);
  DriveApp.createFile(
    Utilities.newBlob(jsonObject).setName("moneyDiaries.json")
  );
}

// GET DATA FROM SPREADSHEET;
// iterate through rows and create json object
function getData_() {
  var spreadsheet = SpreadsheetApp.getActiveSheet();
  var data = spreadsheet.getDataRange().getValues();
  var result = [];
  for (var i = 0; i < data.length; i++) {
    var cleanedData = data[i].filter(Boolean);
    var url = cleanedData[0];
    var title = cleanedData[1];

    var obj = {
      url,
      title,
      meta: {},
    };

    for (j = 2; j < cleanedData.length; j++) {
      var isKey = cleanedData[j].length
        ? cleanedData[j][cleanedData[j].length - 1] === ":"
        : false;
      if (isKey) {
        var k = cleanKey(cleanedData[j]);
        var value = cleanedData[j + 1];
        var properties = [
          "occupation",
          "industry",
          "age",
          "location",
          "salary",
          "net_worth",
          "debt",
          "pronouns",
          "gender",
          "rent",
        ];
        var textOnlyStrings = [
          "occupation",
          "industry",
          "location",
          "pronouns",
          "gender",
        ];
        if (properties.indexOf(k) > -1) {
          if (textOnlyStrings.indexOf(k) > -1) {
            obj[k] = cleanValue(value);
          } else {
            obj[k] = extractValue(value);
          }
        } else if (k.indexOf("paycheck") > -1) {
          obj.paycheck = extractValue(value);
        } else {
          obj.meta[k] = extractValue(value);
        }
      }
    }
    result.push(obj);
  }

  return makeJson(result);
}
