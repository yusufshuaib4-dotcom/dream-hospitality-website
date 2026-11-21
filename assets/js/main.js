(function(){
  'use strict';
  var toggle=document.querySelector('.nav-toggle'), links=document.getElementById('nav-links');
  function close(){if(!links||!toggle)return;links.classList.remove('open');toggle.setAttribute('aria-expanded','false');}
  if(toggle&&links){
    toggle.addEventListener('click',function(){var open=links.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));});
    links.addEventListener('click',function(e){if(e.target.closest('a'))close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&links.classList.contains('open')){close();toggle.focus();}});
    document.addEventListener('click',function(e){if(!e.target.closest('.site-header'))close();});
    window.addEventListener('resize',function(){if(window.innerWidth>780)close();});
  }
  var y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();
})();
