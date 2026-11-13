---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["4 ANNEX A - Signature Guidelines"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4 ANNEX A - Signature Guidelines

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
28 ISO 20022 Business Application Header Message Usage Guide v3.0  
4 ANNEX A - Signature Guidelines 
4.1  Preface 
It is recommended that implementers create clear guidelines for messaging scenarios and related 
use cases, in which the BAH signature mechanism is employed . Such guidelines can ensure a 
common understanding of the way the signature is structured, and they can constitute a shared 
agreement of how the creator of the signature and all verifiers of the signature must apply the 
signature mechanism. 
 
The guidelines in the remainder of this annex can serve as an illustrative model. Based on the model, 
specific guidelines can be created for each distinct use case in which the BAH signature mechanism 
is to be employed. 
 
The guidelines are pure technical guidelines, which only discuss the formal aspects of the 
construction of the signature. All other aspects of the signature, such as, who can sign and such as 
the message scenarios, which require signing, are not part of this annex. 
4.2  Introduction  
A digital signature is a mathematical scheme for verifying the authenticity of digital messages. A valid 
digital signature, where the prerequisites are satisfied, gives a recipient sufficient confidence that the 
message was created by a known sender (authentication) and that the message was not altered in 
transit (integrity). 
The optional Signature element of the BAH can be employed to contain the digital signature of the 
Business Entity authorised to sign the Business Message, i.e. the ISO 20022 Business A pplication 
Header and the ISO 20022 Message. 
There is no support for signatures covering only a part of the business message. 
The Signature must be structured as per the W3C XML Signatures specification and any additional 
constraints stated for the service and business area within which this BusinessMessage is exchanged. 
This requires that the creator of the Signature and all verifiers of that Signature agree how the 
Signature is structured.
 
4.2.1 Current Signature Guidelines 
 
The Business Application Header Message Usage Guidelines specifies: "Signature contains the digital 
signature of the person authorised to sign this BusinessMessage (based on W3C’s XML Signature 
standard)". 
This means that: 
• The Signature element conforms to the W3C Signature Syntax and 
Processing Recommendation 
• The BusinessMessage is the ISO 20022 Business Application Header and the 
ISO 20022 Message 
• The person authorised to sign is not further specified; this depends on the 
particular context in which the message is sent. 
As a reminder, the terminology of BusinessMessage, ISO 20022 Business Application Header and ISO 
20022 Message is shown in the following picture 
```

