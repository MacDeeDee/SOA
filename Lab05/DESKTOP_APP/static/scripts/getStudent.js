function display() {
    var input = document.getElementById("searchBar").value;
    var inputParsed = parseInt(input)
    var tbs = new Object();
    tbs["InputSID"] = inputParsed;
    var tbs2 = JSON.stringify(tbs);
    var webPortal = new XMLHttpRequest();
    webPortal.open("POST", "http://localhost:5000/getbyid", true);
    webPortal.setRequestHeader("Content-Type", "application/json");
    webPortal.onreadystatechange = function () {
        if (webPortal.readyState === 4 && webPortal.status === 200) {
            var received = JSON.parse(webPortal.responseText);
            // console.log(received["personalInfo"]);
            var unpack1 = new Object();
            unpack1 = received["personalInfo"];
            var SID = unpack1["SID"];
            var name = unpack1["name"];
            var gender = unpack1["gender"];
            var DOB = unpack1["DOB"];
            var email = unpack1["email"];
            var unpack2 = unpack1["relative"];

            if (unpack2.length == 2) {
                for (var i = 0; i < unpack2.length; i++) {
                    var temp = new Object();
                    temp = unpack2[i];
                    var unpack3 = new Object();
                    unpack3 = temp["person"];
                    var relRelationship = unpack3["relationship"];
                    var relName = unpack3["name"];
                    var add = unpack3["address"];
                    document.getElementById("relationship" + i).innerHTML = relRelationship;
                    document.getElementById("relName" + i).innerHTML = relName;
                    document.getElementById("add" + i).innerHTML = add;
                    // console.log(temp);
                }
            }

            else if (unpack2.length == 1) {
                for (var i = 0; i < unpack2.length; i++) {
                    var temp = new Object();
                    temp = unpack2[i];
                    var unpack3 = new Object();
                    unpack3 = temp["person"];
                    var relRelationship = unpack3["relationship"];
                    var relName = unpack3["name"];
                    var add = unpack3["address"];
                    document.getElementById("relationship" + i).innerHTML = relRelationship;
                    document.getElementById("relName" + i).innerHTML = relName;
                    document.getElementById("add" + i).innerHTML = add;
                    // console.log(temp);
                }
                document.getElementById("relationship1").innerHTML = "Not available.";
                document.getElementById("relName1").innerHTML = "Not available.";
                document.getElementById("add1").innerHTML = "Not available.";
            }

            else if (unpack2.length == 0){
                for (var i = 0; i < 2; i++) {
                    document.getElementById("relationship" + i).innerHTML = "Not available.";
                    document.getElementById("relName" + i).innerHTML = "Not available.";
                    document.getElementById("add" + i).innerHTML = "Not available.";
                }
            }

            else {
                for (var i = 0; i < 2; i++) {
                    document.getElementById("relationship" + i).innerHTML = "Invalid.";
                    document.getElementById("relName" + i).innerHTML = "Invalid.";
                    document.getElementById("add" + i).innerHTML = "Invalid.";
                }
            }

            document.getElementById("SID").innerHTML = SID;
            document.getElementById("name").innerHTML = name;
            document.getElementById("gender").innerHTML = gender;
            document.getElementById("DOB").innerHTML = DOB;
            document.getElementById("email").innerHTML = email;

        }
    };
    webPortal.send(tbs2);
}

