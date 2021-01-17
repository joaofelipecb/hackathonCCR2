function control_Business_click(event){
	var target = event.target;
	control_Business_clear(target.parentElement);
	command_Business_click(event);
	var loadingAnimation = document.getElementById('loadingAnimation');
	var mapFrame = document.getElementById('mapFrame');
	var mapImage = document.getElementById('mapImage');
	var businessSuggestion = document.getElementById('businessSuggestion');
	var callToAction = document.getElementById('callToAction');
	var business = target.innerHTML;
	var loading = control_Loading_initialize('wsgi.py?route=renderMap&business='+business, [mapFrame, businessSuggestion, callToAction], mapImage, loadingAnimation);
	control_Loading_start(loading);
}

function control_Business_clear(parent){
	var elements = parent.getElementsByTagName('div');
	for(element of elements){
		command_Business_clear(element);
	}
}
