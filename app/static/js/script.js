const button = document.getElementById('toggleButton');
    const popup = document.getElementById('popup');

    button.addEventListener('click', () => {
      if (popup.style.display === 'none' || popup.style.display === '') {
        popup.style.display = 'block';
      } else {
        popup.style.display = 'none';
      }
});
