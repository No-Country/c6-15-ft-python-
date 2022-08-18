function toggleText1() {
            var points1 = document.getElementById("points1");
            var showMoreText1 = document.getElementById("moreText1");
            var buttonText1 = document.getElementById("textButton1");
	    if (points1.style.display === "none") {
                showMoreText1.style.display = "none";
                points1.style.display = "inline";
                buttonText1.innerHTML = "Leer más";
            }
            else if (points1.style.display != "none") {
                showMoreText1.style.display = "inline";
                points1.style.display = "none";
                buttonText1.innerHTML = "Leer menos";
            };
}
function toggleText2() {
            var points2 = document.getElementById("points2");
            var showMoreText2 = document.getElementById("moreText2");
            var buttonText2 = document.getElementById("textButton2");
	    if (points2.style.display === "none") {
                showMoreText2.style.display = "none";
                points2.style.display = "inline";
                buttonText2.innerHTML = "Leer más";
            }
            else if (points2.style.display != "none") {
                showMoreText2.style.display = "inline";
                points2.style.display = "none";
                buttonText2.innerHTML = "Leer menos";
            };
}
function toggleText3() {
            var points3 = document.getElementById("points3");
            var showMoreText3 = document.getElementById("moreText3");
            var buttonText3 = document.getElementById("textButton3");
	    if (points3.style.display === "none") {
                showMoreText3.style.display = "none";
                points3.style.display = "inline";
                buttonText3.innerHTML = "Leer más";
            }
            else if (points3.style.display != "none") {
                showMoreText3.style.display = "inline";
                points3.style.display = "none";
                buttonText3.innerHTML = "Leer menos";
            };
}
function toggleText4() {
        var points4 = document.getElementById("points4");
        var showMoreText4 = document.getElementById("moreText4");
        var buttonText4 = document.getElementById("textButton4");
        if (points4.style.display === "none") {
	        showMoreText4.style.display = "none";
                points4.style.display = "inline";
                buttonText4.innerHTML = "Leer más";
            }
        else if (points4.style.display != "none") {
                showMoreText4.style.display = "inline";
                points4.style.display = "none";
                buttonText4.innerHTML = "Leer menos";
            };
	}
function toggleText5() {
        var points5 = document.getElementById("points5");
        var showMoreText5 = document.getElementById("moreText5");
        var buttonText5 = document.getElementById("textButton5");

        if (points5.style.display === "none") {
	        showMoreText5.style.display = "none";
                points5.style.display = "inline";
                buttonText5.innerHTML = "Leer más";
            }
        else {
                showMoreText5.style.display = "inline";
                points5.style.display = "none";
                buttonText5.innerHTML = "Leer menos";
	       }
	};
function toggleText() {
  
            // Get all the elements from the page
            var points = document.getElementById("points");
            var showMoreText = document.getElementById("moreText");
            var buttonText =
                document.getElementById("textButton");
            if (points.style.display === "none") {
                showMoreText.style.display = "none";
                points.style.display = "inline";
                buttonText.innerHTML = "Show More";
            }
            else {
                showMoreText.style.display = "inline";
                points.style.display = "none";
                buttonText.innerHTML = "Show Less";
            }
        }
