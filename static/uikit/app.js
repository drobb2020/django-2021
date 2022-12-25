// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });

console.log('Hello devsearch - app')

const alertWrapper = document.getElementById('alert')
const alertClose = document.getElementById('close')

if (alertWrapper) {
  alertClose.addEventListener('click', () => {
    alertWrapper.style.display = 'none'
  })
}
