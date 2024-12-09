var edit_btn = document.getElementById('Edit-btn');
edit_btn.addEventListener('click', (event) => {
    event.preventDefault();
    var content = document.getElementById('Content-edit');
    var save_btn = document.getElementById('Save-btn');
    var mutual = edit_btn.getAttribute('data-mutual'); // Get the value of data-mutual attribute
    
    if (mutual === "1") {
        save_btn.style.opacity = "1";
        save_btn.style.pointerEvents = "all";
        content.style.pointerEvents = "all";
    }
    else{
        console.log("none");
    }

});
