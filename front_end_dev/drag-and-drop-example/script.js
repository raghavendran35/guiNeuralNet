//Usecases to address:
//User drags box over to dropzone, changes color and is highlighted:
//1. User is able to drag the box successfully into area, duplicate element created
//2. User fails at dragging, element returns back to origin 

//currentTarget is object getting dragged
function onDragStart(event) {
//DataTransfer obj keeps track of info related to current drag
//first param for setData: string telling format of 2nd param
//2nd param: actual data being transferred
  if (event.target.parentElement.className == "dropzone")
  {}
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

//event target is dom that triggered event
//need to make sure we can't affect something with a target
//but note this fires every 350 ms
function allowDrop(event) {
    var t = event.target;
    // Find the drop target
    //console.log(t.classList.contains("target"))
    console.log(t);
    while (t !== null && !t.classList.contains("example-dropzone")) {
        console.log("YEET1");
        console.log(t.classList);
        t = t.parentNode;
        console.log("YEET2");
    }

    // If the target is empty allow the drop.
    if (t && t.childNodes.length == 0) {
        event.preventDefault();
    }
    return false;
}

//one solution to prevent elements in dropzone having elements added to them (readonly)

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
	
	//add element to drop zone
	dropzone.appendChild(draggableElement);
	//now check whether there exists an element in the parent that matches the dragged node	
	//console.log(draggableElementCopy)
    console.log(parent_of_draggable_element)
    parent_of_draggable_element.appendChild(draggableElementCopy);

    //hack to prevent draggable element from being something that can be dragged into another?
    var parentName = draggableElement.parentElement.className;
    var stuff = document.getElementById("dropzone-1");
    //console.log(parentName);
    //console.log(stuff);
    //basically alert issue with dropping draggable element
    if (parentName.startsWith("example-draggable")) {
    	//remove from where it is now
    	//draggableElement.id = "temp_id";
    	draggableElement.parentElement.removeChild(draggableElement);
    	alert("Can't do this, sorry");
    }
	event
		.dataTransfer
		.clearData();    
}

function onDragEnd(event) {
	//get id of element being dragged
	const id = event
				.dataTransfer
				.getData('text');
	event
		.dataTransfer
		.clearData();
}