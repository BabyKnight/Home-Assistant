onload=function(){
	setInterval(redirect_to_login, 3000)
};
function redirect_to_login() {
	location.href="/login/";
}
