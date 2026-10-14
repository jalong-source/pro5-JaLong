const helloButton = document.querySelector('#hello-button');
const helloMessage = document.querySelector('#hello-message');

helloButton.addEventListener('click', () => {
  helloMessage.textContent = 'Hello World! Chúc nhóm mình xây nhà vui vẻ.';
});
