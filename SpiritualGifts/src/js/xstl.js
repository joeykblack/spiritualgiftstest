function loadXMLDoc(dname)
	{
	if (window.XMLHttpRequest)
	  {
	  xhttp=new XMLHttpRequest();
	  }
	else
	  {
	  xhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xhttp.open("GET",dname,false);
	if (window.ActiveXObject || "ActiveXObject" in window)
	{
		try { xhttp.responseType = 'msxml-document'; } catch(e){}
	}
	xhttp.send("");
	return xhttp.responseXML;
	}

	
function displayResult(lang)
	{
	xml=loadXMLDoc("xml/test-" + lang + ".xml");
	xsl=loadXMLDoc("xsl/test.xsl");
	// code for IE
	if (window.ActiveXObject || "ActiveXObject" in window)
	  {
	  ex=xml.transformNode(xsl);
	  document.getElementById("test").innerHTML=ex;
	  }
	// code for Mozilla, Firefox, Opera, etc.
	else if (document.implementation && document.implementation.createDocument)
	  {
	  xsltProcessor=new XSLTProcessor();
	  xsltProcessor.importStylesheet(xsl);
	  resultDocument = xsltProcessor.transformToFragment(xml,document);
	  document.getElementById("test").appendChild(resultDocument);
	  }
	}