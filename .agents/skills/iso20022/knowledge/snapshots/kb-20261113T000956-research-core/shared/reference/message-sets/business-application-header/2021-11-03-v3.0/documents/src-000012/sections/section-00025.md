---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines", "4.3 Structure of the Signature"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.3 Structure of the Signature

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
31 ISO 20022 Business Application Header Message Usage Guide v3.0  
o Algorithms used 
o KeyInfo 
o Structure of Reference elements 
• The process used for signing and verifying 
 
4.3  Structure of the  Signature 
4.2.4 Overview 
This section describes the structure of the Signature signing the Business Message. The elements used 
within the Signature of the BAH are discussed. An example of a Signature used in the BAH can be 
found in Example on section Example. 
The next section describes the processing of signing and verifying the Signature of a Business 
Message. 
4.2.5 Algorithms used 
Security algorithms are selected to be widely available but yet strong enough to offer sufficient 
security. It is possible that algorithms need to be updated to a stronger version, for example SHA3 for 
the digest algorithm. Applications should take this into account. 
The following section shows an illustrative selection of algorithms:  
• The signing algorithm is RSA based on the SHA-256 digest on the 
information signed 
• The digest algorithm is SHA-256 
• The canonicalization algorithm is the Exclusive XML Canonicalization. This 
algorithm is applied prior to digesting the XML. Using the canonicalization 
allows applications to use XML processing and parsing on the XML data 
without breaking the signature. The Exclusive Canonicalization algorithm is 
chosen to avoid any impact of enveloping elements when sending or 
receiving Business Messages. 
This is shown in the following table: 
 
Purpose Element  Algorithm attribute value  
PKI sign algorithm  SignMethod  http://www.w3.org/2001/04/xmldsig-
more#rsa - sha256 
Digest algorithm  DigestMethod  http://www.w3.org/2001/04/xmlenc#sha256  
Canonicaliza tio n 
algorithm  
CanonicalizationMethod  http://www.w3.org/2001/10/xml-exc-c14n# 
4.2.6 KeyInfo 
The KeyInfo must contain the X509v3 certificate containing the validation key. Optionally, it can also 
contain the certificates that are part of the ce rtification chain. This depends on the allowed PKI 
infrastructures used within the business context. For instance, when between sender and receiver 
always the same PKI infrastructure is used, then it can be better to use the CA root certificate from 
the environment than to check that the correct CA root certificate is used within the KeyInfo . 
NOTE It is recommended not to use any other elements within the KeyInfo . 
The KeyInfo itself is signed and must contain the Id attribute. This attribute should contain a unique 
value. 
The KeyInfo looks like: 
```

