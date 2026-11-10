---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.8 Business Application A sends a duplicate  of a previously sent Business Message"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.8 Business Application A sends a duplicate  of a previously sent Business Message

Source: [src-000012](../../../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf). Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
17 ISO 20022 Business Application Header Message Usage Guide v3.0  
2.8  Business Application A sends a duplicate  
of a previously sent Business Message  
 
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
CopyDuplicate DUPL 
PossibleDuplicate  
Priority  
Signature  
Related Copy of the relevant MessageElements of the 
BusinessApplicationHeader of the original BusinessMessage 
sent to Business Application B 
 
EXAMPLE 
Upon request, the Securities Settlement platform resends BusinessMessage1 
 
 
<AppHdr> 
<Fr>Securities Settlement Platform</Fr> 
<To>System Member</To> 
… 
<CpyDplct>DUPL</CpyDplct> 
<Rltd>relevant MessageElements  of original BAH </Rltd> 
… 
</AppHdr> 
<Document> 
 
 
```

