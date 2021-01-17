function command_Business_click(event){
	var target = event.target;
	target.classList.add('tagSelected');
}

function command_Business_clear(element){
	element.classList.remove('tagSelected');
}
