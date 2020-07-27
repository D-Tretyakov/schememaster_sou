document.getElementById('app').onchange = debounce(refresh, 200);

function refresh() {
  // console.log('HI');
  if (app.auto_refresh) {
    app.updatePDF();
  }
}