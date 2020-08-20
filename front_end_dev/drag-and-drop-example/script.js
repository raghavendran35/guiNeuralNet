
//currentTarget 
function onDragStart(event) {
//DataTransfer obj keeps track of info related to current drag
//first param for setData: string telling format of 2nd param
//2nd param: actual data being transferred
  event
  	.dataTransfer
    .setData('text/plain', event.target.id);
  //make a copy of the element being dragged
  const draggableElementCopy = document.getElementById(event.currentTarget.id).cloneNode(true);
  event
  	.currentTarget
    .style
    .backgroundColor = 'yellow';
   console.log(draggableElementCopy)
   const parent = draggableElementCopy.parentElement;
   console.log(parent)
   parent.appendChild(draggableElementCopy);
}

function onDragOver(event) {
	event.preventDefault();
}

function onDrop(event) {
	const id = event
				.dataTransfer
				.getData('text');
	//get draggable element with id
	const draggableElement = document.getElementById(id);
	const dropzone = event.target;
	console.info(dropzone);
	dropzone.appendChild(draggableElement);
	event
		.dataTransfer
		.clearData();
}

//need to do this to consider the case where drag fails
//without this, nothing should be broken, but we should end up seeing
//an extra element
function onDragEnd(event) {
	//get id of element being dragged
	const id = event
				.dataTransfer
				.getData('text');
	//get actual element itself
	const draggableElement = document.getElementById(id);
	console.log("On Drag End handling");
	console.log(draggableElement);
	const parent = draggableElement.parentElement;
	console.log(parent);
	//just to be safe, when drag ends, clear dataTransfer
	//means user sucks at dragging
	event
		.dataTransfer
		.clearData();
	parent.appendChild(draggableElement);
}