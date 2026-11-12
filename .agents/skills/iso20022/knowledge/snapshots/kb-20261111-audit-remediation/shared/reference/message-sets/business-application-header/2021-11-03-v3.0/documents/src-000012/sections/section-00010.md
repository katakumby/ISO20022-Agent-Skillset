---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.4 Business Application A informs Business Application B of the Business Service within which this BusinessMessage is exchanged"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.4 Business Application A informs Business Application B of the Business Service within which this BusinessMessage is exchanged

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

```text
12 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
Following MessageElements must be used: 
 
 
MessageElement 
Name 
Usage 
CharacterSet Character set 1; Character set 2 
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
Priority  
Signature  
Related  
 
2.4  Business Application A informs Business Application B  
of the Business Service within which this BusinessMessage is  
exchanged  
 
This enables the Receiver to unambiguously relate the BusinessMessage to the BusinessService in 
which it is used. 
Normally this MessageElement is used when this BusinessMessage is used in multiple services. 
It can be the service identified by the service provider or a bilaterally / multilaterally agreed service. 
Following MessageElements must be used: 
 
MessageElement 
Name 
Usage 
CharacterSet  
From Id of BusinessApplication A 
To Id of BusinessApplication B 
BusinessMessageIdentifier Identification of the BusinessMessage A 
MessageDefinitionIdentifier Identification of the MessageDefinition 
BusinessService Identification of the Service within which this Message is 
exchanged 
MarketPractice  
CreationDate Date (and time) of the creation of this BusinessApplicationHeader 
(and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature  
Related  
```

