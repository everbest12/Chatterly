// const toggleBtn = document.getElementById("toggleBtn");
// const sidebar = document.getElementById("sidebar");

// toggleBtn.addEventListener("click", () => {
//   sidebar.classList.toggle("active");
// });




// setting up the chat


  

const toggleBtn = document.getElementById("toggleBtn");
    const sidebar = document.getElementById("sidebar");

    toggleBtn.addEventListener("click", () => {
      sidebar.classList.toggle("active");
    });

    // right sidebar
 // chat.js



// document.addEventListener('DOMContentLoaded', () => {
//   const toggleBtns = document.getElementById('toggleExpand');
//   const leftPanel = document.querySelector('.left');
//   const rightPanel = document.querySelector('.right');

//   let isExpanded = false;

//   toggleBtns.addEventListener('click', () => {
//     isExpanded = !isExpanded;

//     if (isExpanded) {
//       leftPanel.classList.add('expanded-left');
//       rightPanel.classList.add('hide-right');
//     } else {
//       leftPanel.classList.remove('expanded-left');
//       rightPanel.classList.remove('hide-right');
//     }
//   });
// });

document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('toggleExpand');
  const leftPanel = document.getElementById('leftPanel');
  const rightPanel = document.getElementById('rightPanel');

  toggleBtn.addEventListener('click', () => {
    leftPanel.classList.toggle('expanded-left');
    rightPanel.classList.toggle('hide-right');
  });
});

