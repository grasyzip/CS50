document.getElementById('myButton').addEventListener('click', () => {
  alert('Botão clicado na extensão do Chrome!');
  chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    chrome.scripting.executeScript({
      target: {tabId: tabs[0].id},
      function: changePageBackground
    });
  });
});

function changePageBackground() {
  document.body.style.backgroundColor = '#f0f0f0';
}