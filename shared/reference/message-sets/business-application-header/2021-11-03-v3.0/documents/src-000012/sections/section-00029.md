---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines", "4.5 Example"]
file_pages: [36, 37]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.5 Example

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 36 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
36 ISO 20022 Business Application Header Message Usage Guide v3.0  
4.5  Example 
An example of a Signature within the BAH that can be verified is as follows: 
 
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig# "> 
 <ds:S ignedInfo>  
  <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml- exc-c14n#"/> 
  <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig -more#rsa- 
sha256"/> 
  <ds:Reference URI="#Unique-id-to-KeyInfo"> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=  
</ds:DigestValue> 
  </ds:Reference> 
  <ds:Reference URI=""> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped- 
signature"/> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> 
+OS/MM1NBTiOZWWpvzOWkfRjyP2/F1lg9P+zvC+Gulk=  
</ds:DigestValue> 
  </ds:Reference> 
  <ds:Reference> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=  
</ds:DigestValue> 
  </ds:Reference> 
 </ds:SignedInfo> 
 <ds:SignatureValue> IKDs7kwX14CxK3AZ1ojJLr35A4eU/98tp/10KFQTtPOwR5WCKyx 
4I05ZV1IljOpEgpkt6xejXhshaEnNBD5B5PII1VN6mviJJjU/njGikNeXzi1Djei2dPEap 
nPX1f26UnQcgYTAqaSVwAnIR7L8/W2UeT8J9z8Rd1OebYV5xE8jVehbgMcAmJwv2rC/c2d 
UkUe2/eBU0APyWGCgKawxGGAPLP3AS4+Mp0ODKlVp08rUzVOF+pFF/1dBknlK/v0dWkDdj 
YvwFRvZhHXue/PYvMNtQBytMUUdB1MiQrNX0jSCE6Y2nljhTXdcrb2lgfgwCclB6xArBRV 
WfMa0kQVQ4Q== 
</ds:SignatureValue> 
 <ds:KeyInfo Id="Unique-id-to-KeyInfo"> 
  <ds: X509Data > 
   <ds:X509Certificate>MIID1DCCArygAwIB </ds:X509Certificate> 
  </ds:X509Data> 
 </ds:KeyInfo> 
</ds:Signature> 
 
```

## File page 37

```text
37 ISO 20022 Business Application Header Message Usage Guide v3.0  
Revision Record 
Revision Date Author Description Sections affected 
1.0 15/04/2010 ISO 20022 
RMG/TSG 
Initial version All 
1.1 30/06/2010 TSG 
secretariat 
corrected typos in some 
examples using T2S and 
added this revision record 
2.1.1.1 and 2.1.6.1 
1.2 20/10/2010 TSG 
secretariat 
Corrected typos, clarified 
scenario 2, updated the 
TOC. 
Replaced 
MessageInstanceIdentifier 
by 
BusinessMessageIdentifier 
in chapter 3 
Added new scenario 2.10 
2.1.2, 3.x, 2.10, TOC 
1.4 20/4/2011 TSG 
secretariat 
corrected typos, added 
1.7, 
corrected scenario 2.4 
1.7, 2.4 
1.5  TSG 
secretariat 
Corrected typo; 
Added an XML Schema 
that formally describes an 
ISO 200222 Business 
Message. 
2.3 Diagram 
1.7 
1.6 8/5/2013 TSG 
secretariat 
Added ANNEX A - 
Signature Guidelines 
4 
1.7 23/5/2013 TSG 
secretariat 
Added last paragraph 
about use of ISO 20022 
XML syntax 
1.1 
1.8 8/4/2016 TSG Added new section on 
BAH deployment options 
2.2 and 2.3 
1.9 15/10/2019 TSG Updated for BAH V2 All 
2.0 22/10/2020 TSG Updated for BAH v2 
Clarification of text, 
diagrams and formatting. 
All 
3.0 03/11/2021 RA Updated for BAH v3 All 
```

