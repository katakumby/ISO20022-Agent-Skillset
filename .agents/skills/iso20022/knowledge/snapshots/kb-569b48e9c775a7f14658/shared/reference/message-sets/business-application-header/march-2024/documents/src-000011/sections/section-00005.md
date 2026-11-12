---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.2 Structure"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.2 Structure

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AppHdr> [1..1]  C5
   CharacterSet <CharSet> [0..1] CodeSet C6 9
   From <Fr> [1..1]  9
{Or     OrganisationIdentification <OrgId> [1..1] ± 9
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 10
   To <To> [1..1]  11
{Or     OrganisationIdentification <OrgId> [1..1] ± 11
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 12
   BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 13
   MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 13
   BusinessService <BizSvc> [0..1] Text 13
   MarketPractice <MktPrctc> [0..1]  14
     Registry <Regy> [1..1] Text 14
     Identification <Id> [1..1] Text 14
   CreationDate <CreDt> [1..1] DateTime 14
   BusinessProcessingDate <BizPrcgDt> [0..1] DateTime 14
   CopyDuplicate <CpyDplct> [0..1] CodeSet 15
   PossibleDuplicate <PssblDplct> [0..1] Indicator 15
   Priority <Prty> [0..1] CodeSet C7 16
   Signature <Sgntr> [0..1] (External Schema) 16
   Related <Rltd> [0..*]  16
     CharacterSet <CharSet> [0..1] CodeSet C6 17
     From <Fr> [1..1]  17
{Or       OrganisationIdentification <OrgId> [1..1] ± 18
Or}       FinancialInstitutionIdentification <FIId> [1..1] ± 19
     To <To> [1..1]  20
{Or       OrganisationIdentification <OrgId> [1..1] ± 20
Or}       FinancialInstitutionIdentification <FIId> [1..1] ± 21
     BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 22
     MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 22
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 7 March 2024
```

