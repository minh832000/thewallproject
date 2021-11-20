$.each( $('.post-content'), function( i, l ){
    var content=l.innerText
    l.innerHTML=content
  });