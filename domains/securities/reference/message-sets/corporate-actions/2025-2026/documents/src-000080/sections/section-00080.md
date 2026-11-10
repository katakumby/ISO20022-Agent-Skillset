---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.30 ConsentType <CnsntTp>"]
file_pages: [126]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.30 ConsentType <CnsntTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 126 to 126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
3.4.10.30  ConsentType <CnsntTp>
Presence: [0..1]
Definition: Specifies the type of consent announced.
ConsentType <CnsntTp> contains one of the following elements (see "ConsentTypeFormat4Choice"
on page 919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 919
Or}   Proprietary <Prtry> [1..1] ± 920
3.4.10.31  InformationType <InfTp>
Presence: [0..1]
Definition: Specifies the type of information event.
InformationType <InfTp> contains one of the following elements (see
"InformationTypeFormat4Choice" on page 918 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 918
Or}   Proprietary <Prtry> [1..1] ± 918
3.4.10.32  TaxOnNonDistributedProceedsIndicator <TaxOnNonDstrbtdPrcdsInd>
Presence: [0..*]
Definition: Specifies the tax regulation being attributed to the non-distributed proceeds event or to any
other event.
TaxOnNonDistributedProceedsIndicator <TaxOnNonDstrbtdPrcdsInd> contains the following
elements (see "GenericIdentification30" on page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.10.33  DutchAuctionType <DtchAuctnTp>
Presence: [0..1]
Definition: Specifies whether a Dutch auction is modified or unmodified.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 126 February 2026
```

