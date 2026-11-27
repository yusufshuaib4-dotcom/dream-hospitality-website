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

(function(){
 'use strict';
 var form=document.getElementById('brief-form'),summary='',briefUrl='';
 if(form){
  var result=document.getElementById('brief-result'),error=document.getElementById('needs-error'),status=document.getElementById('brief-status');
  var downloadLink=document.getElementById('download-brief'),viewLink=document.getElementById('view-brief');
  function clear(){
   result.hidden=true;summary='';status.textContent='';
   downloadLink.removeAttribute('href');viewLink.removeAttribute('href');
   if(briefUrl){URL.revokeObjectURL(briefUrl);briefUrl='';}
  }
  window.addEventListener('pagehide',function(){
   if(briefUrl){URL.revokeObjectURL(briefUrl);briefUrl='';}
  });
  window.addEventListener('pageshow',function(){
   if(summary&&!briefUrl)prepareDownload();
  });
  function prepareDownload(){
   if(briefUrl)URL.revokeObjectURL(briefUrl);
   // Keep a real link alive until answers change, rather than clicking a temporary link.
   briefUrl=URL.createObjectURL(new Blob(['\ufeff'+summary.replace(/\n/g,'\r\n')+'\r\n'],{type:'text/plain;charset=utf-8'}));
   downloadLink.href=briefUrl;viewLink.href=briefUrl;
  }
  form.addEventListener('input',function(){clear();error.hidden=true;});
  form.addEventListener('change',function(){clear();error.hidden=true;});
  form.addEventListener('submit',function(e){
   e.preventDefault();var data=new FormData(form),needs=data.getAll('needs');
   if(!needs.length){error.hidden=false;form.querySelector('input[name="needs"]').focus();return;}
   error.hidden=true;
   summary=['PROPERTY TECHNOLOGY BRIEF','Property type: '+data.get('propertyType'),'Rooms or units: '+data.get('propertySize'),'Current stage: '+data.get('stage'),'Preferred timing: '+data.get('timing'),'','Areas to improve:',...needs.map(function(n){return '• '+n;}),'','Dream Hospitality software is in development; first modules are planned for 2027.','Prepared on this device. This brief has not been sent.'].join('\n');
   prepareDownload();document.getElementById('brief-text').textContent=summary;result.hidden=false;document.getElementById('brief-title').focus();
  });
  document.getElementById('copy-brief').addEventListener('click',async function(){
   if(!summary)return;
   var copiedSummary=summary;
   try{
    if(!navigator.clipboard)throw new Error('Clipboard unavailable');
    await Promise.race([navigator.clipboard.writeText(copiedSummary),new Promise(function(_,reject){setTimeout(function(){reject(new Error('Clipboard confirmation timed out'));},2000);})]);
    if(summary===copiedSummary)status.textContent='Brief copied. You can paste it into a document or email.';
   }
   catch(e){if(summary===copiedSummary)status.textContent='Copy could not be confirmed. Please select the brief text to copy it, or use Download brief (.txt).';}
  });
  downloadLink.addEventListener('click',function(){
   status.textContent='Download requested. Check your browser downloads. If it does not start, use Open text version to view and save your brief. Nothing has been sent.';
  });
 }
 var enquiry=document.getElementById('enquiry-form');
 if(enquiry){
  var enquiryResult=document.getElementById('enquiry-result'),emailLink=document.getElementById('enquiry-email-link');
  function resetEmail(){enquiryResult.hidden=true;emailLink.removeAttribute('href');}
  enquiry.addEventListener('input',resetEmail);enquiry.addEventListener('change',resetEmail);
  enquiry.addEventListener('submit',function(e){
   e.preventDefault();var d=new FormData(enquiry);var body=['Name: '+d.get('name'),'Email: '+d.get('email'),'Property/company: '+d.get('property'),'Phone: '+(d.get('phone')||'Not provided'),'','Enquiry:',d.get('message'),'','I have read the Privacy Notice and agreed to my details being used to respond to this enquiry.'].join('\n');
   emailLink.href='mailto:'+enquiry.dataset.recipient+'?subject='+encodeURIComponent('Property enquiry – Dream Hospitality')+'&body='+encodeURIComponent(body);enquiryResult.hidden=false;emailLink.focus();
  });
 }
})();
