function control_DataDriver_initialize(destination, pattern){
	return command_DataDriver_initialize(destination, pattern);
}

function control_DataDriver_apply(dataDriver, data){
	var list = JSON.parse(data);
	for(element of list){
		command_DataDriver_apply(dataDriver, element);
	}
}
