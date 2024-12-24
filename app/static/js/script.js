const button = document.getElementById('toggleButton');
    const popup = document.getElementById('popup');

    button.addEventListener('click', () => {
      if (popup.style.display === 'none' || popup.style.display === '') {
        popup.style.display = 'block'; // Show the pop-up
      } else {
        popup.style.display = 'none'; // Hide the pop-up
      }
});
