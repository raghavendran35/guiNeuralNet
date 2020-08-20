//Usecases to address:
//User drags box over to dropzone, changes color and is highlighted:
//1. User is able to drag the box successfully into area, duplicate element created
//2. User fails at dragging, element returns back to origin 

//currentTarget is object getting dragged
function onDragStart(event) {
//DataTransfer obj keeps track of info related to current drag
//first param for setData: string telling format of 2nd param
//2nd param: actual data being transferred
  event
  	.dataTransfer
    .setData('text/plain', event.target.id);
  //don't change background color for now
  //event
  //	.currentTarget
  //  .style
  //  .backgroundColor = 'yellow';
}

//override 
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
    //make a copy of the element being dragged
    const draggableElementCopy = draggableElement.cloneNode(true);
    //get parent of draggable element
    const parent_of_draggable_element = draggableElement.parentElement;	
	console.info(dropzone);
	//add element to drop zone
	dropzone.appendChild(draggableElement);
	event
		.dataTransfer
		.clearData();
	//now check whether there exists an element in the parent that matches the dragged node	
	console.log(draggableElementCopy)
    console.log(parent_of_draggable_element)
    parent_of_draggable_element.appendChild(draggableElementCopy);	
}

//need to do this to consider the case where drag fails
//without this, nothing should be broken, but we should end up seeing
//an extra element
function onDragEnd(event) {
	//get id of element being dragged
	const id = event
				.dataTransfer
				.getData('text');
	event
		.dataTransfer
		.clearData();
}