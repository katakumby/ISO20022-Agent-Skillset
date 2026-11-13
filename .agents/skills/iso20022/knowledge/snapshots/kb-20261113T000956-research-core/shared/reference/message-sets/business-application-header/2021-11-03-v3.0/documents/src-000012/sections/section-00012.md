---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000012"]
source_editions: ["Version 3.0 2021-11-03"]
message_ids: []
heading_path: ["2 Scenarios", "2.6 Business Application A sends a Business Message  with instruction of business processing date"]
file_pages: [14, 15]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 2.6 Business Application A sends a Business Message  with instruction of business processing date

Source: [src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md). Locator: one-based file pages 14 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
14 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
EXAMPLE 
 
 
2.6  Business Application A sends a Business Message  
with instruction of business processing date  
The purpose of the timestamp in the BusinessProcessingDate is to indicate which business processing 
date the message refers to. The business processing date may be different from the date provided in 
the CreationDate element. 
A market practice or bilateral agreement should specify how this element should be used. 
EXAMPLE 
1 If a transaction was reported overnight Friday (i.e. after 12:00 am Saturday), the transaction 
would likely be deemed complete on Monday (Business Processing Date), not Saturday 
(effective Processing Date); 
2 After-hours transactions or transfers that are executed on a calendar date different to the 
legal business date; 
3 Extended processing beyond the calendar date – especially to avoid doubt when there are 
time zone changes relative to the UTC Date and Time; 
4 Forward dated requests for migration or scheduled events. 
 
  
<AppHdr> 
<Fr>Securities Settlement Platform</Fr> 
<To>System Member</Fr> 
… 
<MktPrctc> 
<Regy>MyStandards</Regy> 
<Id>urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66</Id> 
</MktPrctc> 
… 
</AppHdr> 
<Document> 
<LqdtyCdtTfr>…..</LqdtyCdtTfr> 
</Document> 

```

## File page 15

```text
15 ISO 20022 Business Application Header Message Usage Guide v3.0  
 
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
BusinessProcessingDate Processing date and time indicated by the sender for the 
receiver of the business message 
CopyDuplicate  
PossibleDuplicate  
Priority  
Signature  
Related  
 
  
<AppHdr> 
<Fr>Securities Settlement Platform</Fr> 
<To>System Member</To> 
… 
<CreDt>2020-09-25T09:00:00Z</CreDt> 
<BizPrcgDt>2020-09-28T09:00:00Z</BizPrcgDt> 
… 
</AppHdr> 
<Document> 
<LqdtyCdtTfr>...</LqdtyCdtTfr> 
</Document> 
```

