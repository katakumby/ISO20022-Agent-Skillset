---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["3 Mapping of the BAH to other headers", "3.4 BAH to FpML"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.4 BAH to FpML

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
27 ISO 20022 Business Application Header Message Usage Guide v3.0  
3.4  BAH to FpML 
 
Business Application Header element Message Header 
Sending Business Entity 
the Business Entity that created the BusinessMessage 
<sentBy> 
Receiving Business Entity 
the Business Entity that will process the BusinessMessage 
<sendTo> 
character set 
the additionally used character set(s) in the BusinessMessage 
for Text datatypes 
<?xml version="1.0" 
encoding="UTF-8"> 
BusinessService Example: E&I - 
MessageDefinitionIdentifier 
the identification of MessageDefinition 
v5: root element 
v4: xsi:type of Document 
BusinessMessageIdentifier 
the identification of the BusinessMessage, unique to the 
SendingBusinessEntity 
<messageId> 
Copy / Duplicate / 
Functionality to indicate this message is a copy 
/ duplicate of another BusinessMessage 
<copyTo> 
Related Reference 
Reference of the original BusinessMessage 
<inReplyTo> 
Possible Duplicate 
The BusinessMessage may have been sent before. 
 
Priority 
Relative indication of the processing precedence of the 
message over a (set of) BusinessMessages with assigned 
priorities 
_ 
Signature 
Contains the digital signature of the person 
authorised to sign this BusinessMessage 
(based on W3C’s XML Signature standard) 
<dsig:Signature> 
CreationDate 
Creation date (and time) of the Business Message 
<creationTimestamp> 
Market Practice 
Set of rules agreed between parties that restricts the 
usage of the messages in order to achieve better STP 
(Straight Through Processing) rates. 
<implementationSpecification> 
Business Processing Date 
Processing date and time indicated by the sender for the 
receiver of the business message. 
_ 
BusinessMessage  
```

