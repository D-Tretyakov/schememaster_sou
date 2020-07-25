// If absolute URL from the remote server is provided, configure the CORS
// header on that server.
// var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf';
var url = 'download';
// var nPages = null;
// var pdfDoc = null,
// window.getPDF = getPDF;

// Loaded via <script> tag, create shortcut to access PDF.js exports.
var pdfjsLib = window['pdfjs-dist/build/pdf'];

// The workerSrc property shall be specified.
pdfjsLib.GlobalWorkerOptions.workerSrc = '//mozilla.github.io/pdf.js/build/pdf.worker.js';

// // function getPDF() {
//   // Asynchronous download of PDF
// var loadingTask = pdfjsLib.getDocument(url);
// loadingTask.promise.then(function(pdf) {
//   console.log(pdf.numPages);
//   nPages = pdf.numPages;
//   console.log('PDF loaded');
//   console.log('PIZDA');

  // for (var i = 1; i <= pdf.numPages; i++) {
  //   canvas = document.createElement("canvas");
  //   canvas.id = 'canvas-' + i;
  //   // document.getElementById("pdf-container").appendChild(canvas);
  //   var element = document.getElementById("pdf-container");
  //   element.appendChild(canvas);
  // }
    
//   for (var i = 1; i <= pdf.numPages; i++) {
//       // Fetch the first page
//       var pageNumber = i;
//       pdf.getPage(pageNumber).then(function(page) {
//         console.log('Page loaded');
        
//         var scale = 1.5;
//       var viewport = page.getViewport({scale: scale});
      
//       // Prepare canvas using PDF page dimensions
//       var canvas = document.getElementById('canvas-' + i);
//       var context = canvas.getContext('2d');
//       canvas.height = viewport.height;
//       canvas.width = viewport.width;
      
//       // Render PDF page into canvas context
//       var renderContext = {
//         canvasContext: context,
//         viewport: viewport
//       };
//       var renderTask = page.render(renderContext);
//       renderTask.promise.then(function () {
//         console.log('Page rendered');
//       });
//     });
//   }
  
// }, function (reason) {
//   // PDF loading error
//   console.error(reason);
// });
// // }

var pdfDoc = null,
    pageNum = 1,
    pageRendering = false,
    pageNumPending = null,
    // pagesToRender = []
    scale = 1.25;
    // canvas = document.getElementById('the-canvas'),
    // ctx = canvas.getContext('2d');

/**
 * Get page info from document, resize canvas accordingly, and render page.
 * @param num Page number.
 */
async function renderPage(num) {
  pageRendering = true;
  // Using promise to fetch the page
  pdfDoc.getPage(num).then(function(page) {
    console.log('rendering ' + num);
    var viewport = page.getViewport({scale: scale});
    canvas = document.getElementById('canvas-' + num);
    canvas.height = viewport.height;
    canvas.width = viewport.width;
    console.log('got page ' + num);

    // Render PDF page into canvas context
    var renderContext = {
      canvasContext: canvas.getContext('2d'),
      viewport: viewport
    };
    var renderTask = page.render(renderContext);

    // Wait for rendering to finish
    renderTask.promise.then(function() {
      pageRendering = false;
      if (pageNumPending !== null) {
        // New page rendering is pending
        renderPage(pageNumPending);
        pageNumPending = null;
      }
    });
  });
  return 'Done';
}

// function queueRenderPage(num) {
//   console.log('QUEUE');
//   console.log(pagesToRender);
//   if (pageRendering) {
//     pageNumPending = num;
//     // pagesToRender.push(num);
//   } else {
//     console.log('send to render page ' + num);
//     // var n = pagesToRender.shift();
//     renderPage(num);
//   }
// }

// function onNextPage() {
//   if (pageNum >= pdfDoc.numPages) {
//     return;
//   }
//   pageNum++;
//   queueRenderPage(pageNum);
// }

function getPDF() {
  pdfjsLib.getDocument(url).promise.then(async function(pdfDoc_) {
    pdfDoc = pdfDoc_;
    // document.getElementById('page_count').textContent = pdfDoc.numPages;
    document.getElementById('pdf-container').innerHTML = '';
    for (var i = 1; i <= pdfDoc.numPages; i++) {
      var canvas = document.getElementById('canvas-' + i);
      // if(typeof(canvas) != 'undefined' && canvas != null){
      //   const context = canvas.getContext('2d');
      //   context.clearRect(0, 0, canvas.width, canvas.height);
      // } else{
      canvas = document.createElement("canvas");
      canvas.id = 'canvas-' + i;
      // document.getElementById("pdf-container").appendChild(canvas);
      var element = document.getElementById("pdf-container");
      element.appendChild(canvas);
      // }
      // pagesToRender.push(num);
    }

    for (var i = 1; i <= pdfDoc.numPages; i++) {
      await renderPage(i);
    }
    
    // Initial/first page rendering
    // renderPage(pageNum);
    
    // for (var i = 2; i <= pdfDoc.numPages; i++) {
    //   console.log('SEND');
    //   onNextPage();
    // }

    // pageNum = 1;
  });
}