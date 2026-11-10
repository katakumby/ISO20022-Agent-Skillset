---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.11  Business Application A sends a Business Message  to BusinessApplication B with a pre-agreed priority"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.11  Business Application A sends a Business Message  to BusinessApplication B with a pre-agreed priority

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
20 ISO 20022 Business Application Header Message Usage Guide v3.0  
2.11  Business Application A sends a Business Message  
to BusinessApplication B with a pre -agreed priority 
The standard does not define the meaning of the values. The meaning is service/market/business 
area depended and must be pre -agreed within a specific context like the BusinessService, 
MarketPractice, BusinessArea, etc. 
Where required, the BusinessService and/or MarketPractice should be used to identify that specific 
context (i.e. when there may be ambiguity) about the meaning of the value in Priority. 
 
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
PossibleDuplicate  
Priority The priority as defined within the BusinessService 
Signature  
Related  
 
  
```

