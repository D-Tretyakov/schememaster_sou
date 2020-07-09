var select = document.querySelector('#trees');
select.onchange = function(e) {
    var tree_id = select.value[select.value.length-1];
    url_splited = window.location.href.split('/');
    url_splited[url_splited.length - 1] = tree_id;
    window.location.replace(url_splited.join('/'));
}