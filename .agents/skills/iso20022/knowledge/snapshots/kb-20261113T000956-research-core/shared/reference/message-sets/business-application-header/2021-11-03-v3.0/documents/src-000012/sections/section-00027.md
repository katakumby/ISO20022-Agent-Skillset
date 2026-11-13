---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines", "4.3 Structure of the Signature", "4.2.10 Reference of KeyInfo"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.10 Reference of KeyInfo

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
33 ISO 20022 Business Application Header Message Usage Guide v3.0  
<Reference URI=""> 
 <Transforms> 
  <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped -signature"/> 
  <Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
 </Transforms> 
 <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>  
 <DigestValue>+OS/MM1NBTiOZWWpvzOWkfRjyP2/F1lg9P+zvC+Gulk=</DigestValue>  
</Reference> 
4.2.10 Reference of KeyInfo 
The reference to the KeyInfo requires that the KeyInfo can be identified with an Id attribute. To 
ensure that such an attribute can be handled correctly when the Signature is enveloped within other 
XML elements, that attribute should contain a unique value within the XML document enclosing the 
Signature. 
NOTE The Signature is XAdES-BES compliant by adding the Reference within the SignedInfo . 
 
 
<ds:Reference URI="#Unique -id-to-KeyInfo"> 
 <ds:Transforms> 
  <ds:Transform Algorithm="http://www.w3.org/2001/10/xml- exc-c14n#"/> 
 </ds:Transforms> 
 <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>  
 <ds:DigestValue>QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=</ds:DigestValue>  
</ds:Reference> 
The optional attribute Type="http://www.w3.org/2000/09/xmldsig#KeyInfo" can be present on 
the Reference element referring to the KeyInfo . There is no obligation to further process this 
attribute. 
 
<ds:Reference URI="#Unique -id-to-KeyInfo" 
Type="http://www.w3.org/2000/09/xmldsig#KeyInfo">  
 <ds:Transforms> 
  <ds:Transform Algorithm="http://www.w3.org/2001/10/xml- exc-c14n#"/> 
 </ds:Transforms> 
 <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>  
 <ds:DigestValue>QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=</ds:DigestValue>  
</ds:Reference> 
4.4  Process for signing and  verifying 
4.2.11 Signing is performed as last step in generating the Business Message 
When an application prepares a Business Message several steps may be needed. Indeed, some 
applications require an approval process where the message may be amended. 
In some cases, some elements of the BAH may be created after the ISO 20022 Message has been 
created. 
In any case, the last step in the creation of the Business Message is calculating the SignatureValue 
within the Signature. The creation of the signature can be implemented within the flow of sending the 
Business Message as long as the process as described in this section is applied. 
4.2.12 Two node-sets 
As illustrated in Figure 1, the Business Message consists of two XML documents. The way in which 
those two documents are created, sent, received and processed depends on the infrastructure used 
by the sender and receiver. It is therefore important that the proces s in creating the Signature is 
independent of the infrastructure used. 
This is achieved by performing the Signature creation and verification using a well -defined XML 
context. Two such contexts are used: 
• The context of the BAH element (AppHdr) 
• The context of the ISO 20022 Message element (for instance Document) 
```

