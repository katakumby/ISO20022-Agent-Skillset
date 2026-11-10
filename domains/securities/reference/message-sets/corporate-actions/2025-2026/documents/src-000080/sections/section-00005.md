---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.2 Structure"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AppHdr> [1..1]  C5
   CharacterSet <CharSet> [0..1] CodeSet C6 12
   From <Fr> [1..1]  12
{Or     OrganisationIdentification <OrgId> [1..1] ± 12
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 13
   To <To> [1..1]  13
{Or     OrganisationIdentification <OrgId> [1..1] ± 13
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 13
   BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 14
   MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 14
   BusinessService <BizSvc> [0..1] Text 14
   MarketPractice <MktPrctc> [0..1]  14
     Registry <Regy> [1..1] Text 15
     Identification <Id> [1..1] Text 15
   CreationDate <CreDt> [1..1] DateTime 15
   BusinessProcessingDate <BizPrcgDt> [0..1] DateTime 15
   CopyDuplicate <CpyDplct> [0..1] CodeSet 15
   PossibleDuplicate <PssblDplct> [0..1] Indicator 16
   Priority <Prty> [0..1] CodeSet C7 16
   Signature <Sgntr> [0..1] (External Schema) 17
   Related <Rltd> [0..*]  17
     CharacterSet <CharSet> [0..1] CodeSet C6 18
     From <Fr> [1..1]  18
{Or       OrganisationIdentification <OrgId> [1..1] ± 18
Or}       FinancialInstitutionIdentification <FIId> [1..1] ± 18
     To <To> [1..1]  19
{Or       OrganisationIdentification <OrgId> [1..1] ± 19
Or}       FinancialInstitutionIdentification <FIId> [1..1] ± 19
     BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 20
     MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 20
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 10 February 2026
```

