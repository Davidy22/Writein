function copy () {
	var copyText = document.getElementById("url");
	copyText.select();
	document.execCommand("Copy");
}

function load() {
	document.getElementById("url").value = document.URL;
}

window.onload = load;
