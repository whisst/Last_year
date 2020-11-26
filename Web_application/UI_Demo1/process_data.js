var data = {
	"dantri":{
		"image":"aaaaaaaaaaa", 
		"title":"bbbbbbbbbbbb"
	},
	"VnExpress":{
		"image":"aaaaaaaaaaa",
		"title":"bbbbbbbbbbb"
	},
	"suc_khoe":{
		"image":"cccccccc",
		"title":"ffffffffffff"
	}
};

let a = JSON.stringify(data, null, 2);
console.log(a);
document.getElementsByClassName("hi").innerHTML = a;