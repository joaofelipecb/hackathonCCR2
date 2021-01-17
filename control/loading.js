function control_Loading_initialize(request, hiddenObject, dataObject, callback){
	return command_Loading_initialize(request, hiddenObject, dataObject, callback);
}

function control_Loading_start(loading){
	var request = loading.request;
	var callback = control_Loading_finish.bind(null,loading);
	control_ajax_request(request,callback);
	console.log('loading start');
}

function control_Loading_finish(loading, data){
	var hiddenObject = loading.hiddenObject;
	var dataObject = loading.dataObject;
	var callback = loading.callback;
	console.log(hiddenObject);
	console.log(typeof(hiddenObject));
	if(typeof(hiddenObject) != 'object')
		hiddenObject = [hiddenObject];
	else if(!hiddenObject instanceof Array)
		hiddenObject = [hiddenObject];
	for(i in hiddenObject){
		object = hiddenObject[i]
		if(typeof(object) == 'object'){
			if(object instanceof HTMLElement)
				command_Loading_show(object);
		}
	}
	if(typeof(dataObject) == 'object'){
		if(dataObject instanceof HTMLElement)
			command_Loading_data(dataObject, data);
		else if(dataObject instanceof struct_DataDriver)
			control_DataDriver_apply(dataObject, data);
	}
	if(typeof(callback) == 'object'){
		if(callback instanceof struct_Loading)
			control_Loading_start(callback);
		else if(callback instanceof HTMLElement)
			command_Loading_hide(callback);
	}
	//command_Loading_finish(loading, data);
	console.log('loading finish');
}
