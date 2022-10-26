var html = document.documentElement.outerHTML

console.log(html);
console.log(get_doctype());

function get_doctype(){
  let doctype = "";
  if(document.doctype){
    doctype += "<!DOCTYPE HTML";
    if(document.doctype.publicId){
      doctype += ' PUBLIC "'+document.doctype.publicId+'"';
    }
    if(document.doctype.systemId){
      doctype += ' "'+document.doctype.systemId+'"';
    }
    doctype += ">";
  }
  return doctype;
}