function command_Loading_initialize(request, hiddenObject, dataObject, callback){
	return new struct_Loading(request, hiddenObject, dataObject, callback);
}

function command_Loading_finish(loading, data){
	var callback = loading.loadingAnimation;
	var hiddenObject = loading.hiddenObject;
	var dataObject = loading.dataObject;
	loadingAnimation.style.display = 'none';
	dataObject.innerHTML = data;
	hiddenObject.style.display = 'block';
}

function command_Loading_hide(element){
	element.style.display = 'none';
}

function command_Loading_show(element){
	element.style.display = 'block';
}

function command_Loading_data(element, data){
	element.innerHTML = data;
}

function command_Loading_refresh(element){
	element.src = element.src;
}
