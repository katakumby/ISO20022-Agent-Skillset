---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.1 CharacterSet <CharSet>"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.14.1 CharacterSet <CharSet>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Related <Rltd> contains the following BusinessApplicationHeader8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CharacterSet <CharSet> [0..1] CodeSet C6 17
   From <Fr> [1..1]  17
{Or     OrganisationIdentification <OrgId> [1..1] ± 18
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 19
   To <To> [1..1]  20
{Or     OrganisationIdentification <OrgId> [1..1] ± 20
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 21
   BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 22
   MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 22
   BusinessService <BizSvc> [0..1] Text 22
   MarketPractice <MktPrctc> [0..1]  23
     Registry <Regy> [1..1] Text 23
     Identification <Id> [1..1] Text 23
   CreationDate <CreDt> [1..1] DateTime 23
   BusinessProcessingDate <BizPrcgDt> [0..1] DateTime 23
   CopyDuplicate <CpyDplct> [0..1] CodeSet 24
   PossibleDuplicate <PssblDplct> [0..1] Indicator 24
   Priority <Prty> [0..1] CodeSet C7 25
   Signature <Sgntr> [0..1] (External Schema) 25
2.4.14.1  CharacterSet <CharSet>
Presence: [0..1]
Definition: Contains the character set of the text-based elements used in the Business Message.
Impacted by: C6 "ValidationByTable"
Datatype: "UnicodeChartsCode" on page 53
Constraints
• ValidationByTable
2.4.14.2  From <Fr>
Presence: [1..1]
Definition: The sending MessagingEndpoint that has created this Business Message for the receiving
MessagingEndpoint that will process this Business Message.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 17 March 2024
```

