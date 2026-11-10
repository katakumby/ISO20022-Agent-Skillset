---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines", "4.2 Introduction", "4.2.3 Scope of this documents Signature Guidelines"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.3 Scope of this documents Signature Guidelines

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
30 ISO 20022 Business Application Header Message Usage Guide v3.0  
The message that is to be signed is made available. The first step in the signing process is to 
canonicalize the message. This is a transformation that constructs the canonical form of the XML that 
is being signed. By doing so, the input of the digest algorithm is robust enough to be independent on 
the parsing technology used. 
The calculated digest is placed into the DigestValue (a sub-element of SignedInfo). The exact mapping 
is made clear in the picture below. The SignedInfo element itself is canonicalized, and as last step the 
SignedInfo itself is signed using the signing algorithm. The result is placed in SignatureValue. The 
diagram shows a private key used for this purpose. 
The message and its signature are then sent to the receiver. The verification of the Signature follows 
the reverse process. First, the SignatureValue is verified to be correct. The input to the verification 
algorithm is the canonicalized SignedInfo, the certificate containing the certified public key and the 
SignatureValue containing the result of the signing operation. In case the verification succeeds, the 
SignedInfo is authentic and signed by the signer. The verification process continues and checks if the 
digest within the SignedInfo matches the Message that is covered by the digest. This is done by  
canonicalizing the Message and then digest the canonicalized Message. The verification is ok if the 
calculated digest is equal to the digest within the SignedInfo. 
The Signature elements used are illustrated in the following picture: 
Figure 3 - XML Signature elements 
 
As shown, the SignedInfo contains one or more Reference elements. Each Reference identifies an 
XML resource that is to be signed. The example in the picture shows a KeyInfo element with as content 
a KeyValue. Using a Public Key Infrastructure 
4.2.3 Scope of this documents Signature Guidelines 
This document does not introduce any change in business requirements related to the signature within 
the Business Application Header. 
This document proposes the approach to implement the current signature guidelines. In particular, it 
addresses the following 
• The structure of the Signature 

```

