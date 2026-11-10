---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["3 Mapping of the BAH to other headers", "3.3 BAH to ebXML/ebMS Header"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.3 BAH to ebXML/ebMS Header

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
26 ISO 20022 Business Application Header Message Usage Guide v3.0  
3.3  BAH to ebXML/ebMS  Header  
 
Business Application Header element ebMS 3.0 
Sending Business Entity 
the Business Entity that created the BusinessMessage 
<eb:From> 
Receiving Business Entity 
the Business Entity that will process the BusinessMessage 
<eb:To> 
character set 
the additionally used character set(s) in the BusinessMessage for Text 
datatypes 
_ 
BusinessService Example: E&I <eb:Service> 
MessageDefinitionIdentifier 
the identification of MessageDefinition 
<eb:Property> 
BusinessMessageIdentifier 
the identification of the BusinessMessage, unique to the 
SendingBusinessEntity 
<eb:MessageId> 
Copy / Duplicate / 
Functionality to indicate this message is a copy / duplicate of another 
BusinessMessage 
_ 
Related Reference 
Reference of the original BusinessMessage 
<eb:RefToMessageId> 
Possible Duplicate 
The BusinessMessage may have been sent before. 
_ 
Priority 
Relative indication of the processing precedence of the message over a 
(set of) BusinessMessages with assigned priorities 
_ 
Signature 
Contains the digital signature of the person authorised to sign this 
BusinessMessage (based on W3C’s XML Signature standard) 
_ 
CreationDate 
Creation date (and time) of the BusinessMessage 
<eb:Timestamp> 
Market Practice 
Set of rules agreed between parties that restricts the usage of the 
messages in order to achieve better STP (Straight Through Processing) 
rates. 
_ 
Business Processing Date 
Processing date and time indicated by the sender for the receiver of the 
business message. 
_ 
BusinessMessage  
  
```

