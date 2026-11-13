---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.10 Business Application A suspects Business Application B  has not received the BusinessMessage"]
file_pages: [19]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.10 Business Application A suspects Business Application B  has not received the BusinessMessage

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 19 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
19 ISO 20022 Business Application Header Message Usage Guide v3.0  
2.10  Business Application A suspects Business Application B  
has not received the BusinessMessage 
 
 
PossibleDuplicate is used when the Business Application that sent the message has not received any 
reply (because of technical or other problems). 
It will therefore resend THE SAME BusinessMessage, adding the relevant header elements from the 
original BusinessMessage in the 'Related' MessageElement. 
If the receiver did receive the original BusinessMessage identified in 'Related', then this 
BusinessMessage MUST BE IGNORED. 
If the receiver did NOT receive the original BusinessMessage, then it must treat this BusinessMessage 
as if it was the original BusinessMessage. 
 
 
Following MessageElements must be used: 
 
MessageElement 
Name 
Usage 
CharacterSet  
From Id of BusinessApplication A 
To Id of BusinessApplication B 
BusinessMessageIdentifier Identification of the BusinessMessage A 
MessageDefinitionIdentifier Identification of the MessageDefinition 
BusinessService  
MarketPractice  
CreationDate Date (and time) of the creation of this BusinessApplicationHeader 
(and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate YES 
Priority  
Signature  
Related Copy of the relevant MessageElements of the 
BusinessApplicationHeader of the original BusinessMessage 
sent to Business Application B 
 

```

