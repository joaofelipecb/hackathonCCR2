function control_Business_click(event){
	var target = event.target;
	control_Business_clear(target.parentElement);
	command_Business_click(event);
}

function control_Business_clear(parent){
	var elements = parent.getElementsByTagName('div');
	for(element of elements){
		command_Business_clear(element);
	}
}
