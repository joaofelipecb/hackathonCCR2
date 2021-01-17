function command_Map_initialize(DOM,x,y,z){
	var map = new struct_Map(DOM,x,y,z);
	DOM.map = map;
	control_Map_render(map);
}

function command_Map_render(map){
	var DOM = map.DOM;
	var img = DOM.getElementsByTagName('img')[0]
	img.style.marginLeft = map.x+'px';
	img.style.marginTop = map.y+'px';
}
