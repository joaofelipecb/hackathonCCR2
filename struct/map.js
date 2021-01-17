class struct_Map{
	constructor(DOM,width,height,x,y,z){
		this.DOM = DOM;
		this.x = x;
		this.y = y;
		this.z = z;
		this.width = width;
		this.height = height;
		this.isDrag = false;
		this.dragInitX = 0;
		this.dragInitY = 0;
	}
}