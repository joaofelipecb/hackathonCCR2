function command_DataDriver_initialize(destination, pattern){
	return new struct_DataDriver(destination, pattern);
}

function command_DataDriver_apply(dataDriver, element){
	var destination = dataDriver.destination;
	var pattern = dataDriver.pattern;
	destination.innerHTML = destination.innerHTML + pattern.replace('$0', element);
}
