<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:msxml="urn:schemas-microsoft-com:xslt">


<xsl:template match="/">

	
	<ol>
		<xsl:for-each select="test/question">
			<!-- <xsl:sort select="rdm:Random(100)" order="descending" /> -->
			<xsl:sort select="@num" order="ascending" />
			<li>
				<xsl:value-of select="text()"/><br />
				<input type="radio" name="{@category}_{@gifting}_{@num}" value="0" />1 
				<input type="radio" name="{@category}_{@gifting}_{@num}" value="1" />2 
				<input type="radio" name="{@category}_{@gifting}_{@num}" value="2" />3 
				<input type="radio" name="{@category}_{@gifting}_{@num}" value="3" />4 
				<input type="radio" name="{@category}_{@gifting}_{@num}" value="4" />5 
			</li>
			<br /><br />
		</xsl:for-each>
	</ol>
	<p align="center">
		<input type="submit" value="See Results" />
	</p>
			
</xsl:template>



</xsl:stylesheet>