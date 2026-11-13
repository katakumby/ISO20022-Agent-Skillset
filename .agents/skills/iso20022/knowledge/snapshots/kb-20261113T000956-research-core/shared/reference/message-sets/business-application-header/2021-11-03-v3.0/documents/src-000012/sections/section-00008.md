---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.2 Business Application A  sends a Business Message to  Business Application B"]
file_pages: [9, 10]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.2 Business Application A  sends a Business Message to  Business Application B

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 9 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
9 ISO 20022 Business Application Header Message Usage Guide v3.0  
2.2  Business Application A  
sends a Business Message  to  
Business Application  B 
 
Above is the most common, vanilla scenario, i.e. no special features of this BAH are used. 
 
When there is a 'middle man' between the two Business Applications, it is the function/role of that 
middle man that will determine whether the Business Message from the middle man to Business 
Application B is a new Business Message. 
 
If the middle man only forwards the Business Message, i.e. it does not process the Business Message,  
then only the transport header changes, but the Business Message (with its BAH) remains the same. 
 
 
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
CreationDate Date (and time) of the creation of this 
BusinessApplicationHeader (and BusinessMessage) 
BusinessProcessingDate  
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature  
Related  
 
 

```

## File page 10

```text
10 ISO 20022 Business Application Header Message Usage Guide v3.0  
NOTE In the case of ISO 20022 messages without duplicated BAH elements, the ‘technical middle 
man’ scenario can pose implementation challenges, if the implementer community has chosen not to 
use the BAH. 
If the ‘technical middle man’ were to realise the link between two separate networks (e.g. each with 
its distinct network header), it may be that the non -ISO 20022 mechanisms employed are not  
sufficiently compatible in order for the business elements, otherwise conveyed through the BAH and/or 
the ISO 20022 message to travel from Business Application A to Business Application B. 
In order to avoid such situation, the process outlined in chapter 2.2 can be employed to realise a fully 
ISO 20022-compliant implementation without requiring the mandatory deployment of the BAH. 
If the middle man processes the Business Message, then the middle man is considered a Business 
Application and hence a new Business Message is created and sent to Business Application B (see 
scenario 2.11). 
EXAMPLE 
A Securities Settlement platform serves as technical middle man: 
 
 
Example code for technical middle man 
 
  
 
<AppHdr> 
<Fr>System Member A</Fr> 
<To>System Member B</To> 
… 
<BizSvc>SnR</BizSvc> 
… 
</AppHdr> 
 
 
 
 
```

