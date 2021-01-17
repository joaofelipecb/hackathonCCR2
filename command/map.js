function command_Map_initialize(DOM,width,height,x,y,z){
	var map = new struct_Map(DOM,width,height,x,y,z);
	DOM.map = map;
	DOM.ontouchstart = control_Map_drag_start;
	DOM.ontouchstop = control_Map_drag_stop;
	DOM.ontouchmove = control_Map_drag_move;
	control_Map_render(map);
}

function command_Map_render(map){
	var DOM = map.DOM;
	//var img = DOM.getElementsByTagName('img')[0]
	DOM.style.marginLeft = map.x+'px';
	DOM.style.marginTop = map.y+'px';
	DOM.style.width = (map.width*map.z)+'px';
	DOM.style.height = (map.heightidth*map.z)+'px';
}

function command_Map_drag_start(event){
	event.preventDefault();
	var map = event.target.map;
	var touchLocation = event.targetTouches[0];
	map.isDrag = true;
	map.dragInitX = touchLocation.pageX - map.x;
	map.dragInitY = touchLocation.pageY - map.y;
}

function command_Map_drag_stop(event){
	event.preventDefault();
	var map = event.target.map;
	map.isDrag = false;
}

function command_Map_drag_move(event){
	event.preventDefault();
	var map = event.target.map;
	var touchLocation = event.targetTouches[0];
	map.x = touchLocation.pageX - map.dragInitX;
	map.y = touchLocation.pageY - map.dragInitY;
	command_Map_render(map);
}
