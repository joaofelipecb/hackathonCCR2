function command_Loading_initialize(loadingAnimation, hiddenObject, dataObject){
	return new struct_Loading(loadingAnimation, hiddenObject, dataObject);
}

function command_Loading_finish(loading, data){
	var loadingAnimation = loading.loadingAnimation;
	var hiddenObject = loading.hiddenObject;
	var dataObject = loading.dataObject;
	loadingAnimation.style.display = 'none';
	dataObject.innerHTML = data;
	hiddenObject.style.display = 'block';
}
