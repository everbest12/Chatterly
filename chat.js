const toggleBtn = document.getElementById("toggleBtn");
const sidebar = document.getElementById("sidebar");

toggleBtn.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});



// setting up the chat
const togglePopup = document.getElementById("togglePopup");
const popupModal = document.getElementById("popupModal");
const closePopup = document.getElementById("closePopup");
togglePopup.addEventListener("click", () => {
    popupModal.classList.toggle("active");
  });
  

togglePopup.addEventListener("click", () => {
  popupModal.style.display = "block";
});

closePopup.addEventListener("click", () => {
  popupModal.style.display = "none";
});

window.addEventListener("click", (event) => {
  if (event.target === popupModal) {
    popupModal.style.display = "none";
  }
});


document.addEventListener("DOMContentLoaded", function () {
    const editIcon = document.getElementById("editToggle");
    const sidebar = document.getElementById("sidebar");
  
    editIcon.addEventListener("click", function () {
      sidebar.classList.toggle("fullscreen");
    });
  });
  