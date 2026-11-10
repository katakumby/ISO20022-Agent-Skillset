---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines", "4.3 Structure of the Signature", "4.2.7 SignedInfo"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.7 SignedInfo

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
32 ISO 20022 Business Application Header Message Usage Guide v3.0  
<ds:KeyInfo Id="Unique -id-to-KeyInfo"> 
 <ds:X509Data> 
  <ds:X509Certificate>MIID1DCCArygAwIB...  </ds:X509Certificate>  
 </ds:X509Data> 
</ds:KeyInfo> 
The X509Certificate contains the certificate that is used to verify the Signature. In case the full 
certification chain is to be present at least the CA root certificate is added as shown in the following 
example. The order of the different certificates is not relevant. 
<ds:KeyInfo Id="Unique -id-to-KeyInfo"> 
 <ds:X509Data> 
  <ds:X509Certificate>MIID1DCCArygAwIB...  </ds:X509Certificate>  
  <ds:X509Certificate>MIIDkDCCAnigUoSI...  </ds:X509Certificate>  
 </ds:X509Data> 
</ds:KeyInfo> 
NOTE Inclusion of the entire certification chain is recommended. Only  when signatures must be 
performed using certified keys by a specific PKI infrastructure, only the signing certificate is sufficient. 
4.2.7 SignedInfo 
The SignedInfo contains the 3 Reference elements. 
• Reference digesting the ISO 20022 Message 
• Reference digesting the BAH 
• Reference digesting the KeyInfo 
The order of the Reference elements in the SignedInfo is not relevant. 
4.2.8 Reference of ISO 20022 Message 
The Reference is identified by the fact that the URI attribute is absent. The absence of the URI 
attribute indicates that the logic for de-referencing this reference is part of the application logic. The 
processing of such Reference is further described in section Process for signing and verifying. 
NOTE Although the Business Message, as illustrated in Figure 1, consists of the BAH and the ISO 
20022 Message, it is not possible to refer easily from the BAH to the ISO 20022 Message. Therefore, 
the option to use the absent URI attribute was selected, since this is possible on one Reference 
element within the SignedInfo . 
The Reference looks like 
<ds:Reference> 
 <ds:Transforms> 
  <ds:Transform Algorithm="http://www.w3.org/2001/10/xml- exc-c14n#"/> 
 </ds:Transforms> 
 <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>  
 <ds:DigestValue>QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=</ds:DigestValue>  
</ds:Reference> 
4.2.9 Reference of BAH 
The Reference of the BAH is identified by the empty URI attribute URI="". 
Such empty URI attribute URI="" refers to the XML element in which the Signature is placed. This 
means that the signing and verifying of the Signature within the BAH happens within the context of 
the BAH. 
The complete BAH is signed except the Signature itself. This is indicated in the first Transform 
algorithm within the Transforms . The second algorithm contains the Exclusive XML canonicalization. 
 
```

