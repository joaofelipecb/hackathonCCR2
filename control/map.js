function control_Map_initialize(DOM,width,height,x,y,z){
	command_Map_initialize(DOM,width,height,x,y,z);
}

function control_Map_render(map){
	command_Map_render(map);
}

function control_Map_drag_start(event){
	command_Map_drag_start(event);
}

function control_Map_drag_stop(event){
	command_Map_drag_stop(event);
}

function control_Map_drag_move(event){
	var map = event.target.map;
	if(map.isDrag == true)
		command_Map_drag_move(event);
}
