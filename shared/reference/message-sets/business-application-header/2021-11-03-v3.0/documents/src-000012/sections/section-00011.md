---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.5 Business Application A sends a Business Message  with implementation specification"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.5 Business Application A sends a Business Message  with implementation specification

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
13 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
2.5  Business Application  A sends a Business Message  
with implementation specification  
Market practices are a set of rules agreed between parties and specify the business context in which 
business messages are exchanged.  
A market practice specification consists of restrictions of the underlying message definition combined 
with optional extensions of the underlying message definition by using extensions or supplementary 
data of this underlying message.  
MarketPractice is identified by reference via the following sub-elements: 
• Registry 
Name of the implementation specification registry in which the implementation specification of 
the ISO 20022 message is maintained, for example, "MyStandards".  
• Identification 
Identification, which unambiguously identifies, within the implementation specification registry, 
the implementation specification to which the ISO 20022 message is compliant. This can be done 
via a URN. It can also contain a version number or date. 
For instance, "2018-01-01 – Version 2" or "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66". 
 
 
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
MarketPractice The market practice to which the message conforms 
CreationDate Date (and time) of the creation of this BusinessApplicationHeader 
(and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature  
Related  
 

```

