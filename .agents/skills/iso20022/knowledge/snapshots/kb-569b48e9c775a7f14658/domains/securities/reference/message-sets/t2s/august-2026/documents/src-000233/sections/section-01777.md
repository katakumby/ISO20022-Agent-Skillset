---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.10 TradeDate <TradDt>", "71.4.1.2.10.2 DateTime <DtTm>", "71.4.1.2.10.2.1 FromDateTime <FrDtTm>"]
file_pages: [2440]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.10.2.1 FromDateTime <FrDtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2440 to 2440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2440

```text
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 2440
Or   ToDateTime <ToDtTm> [1..1] DateTime 2440
Or   FromToDateTime <FrToDtTm> [1..1] ± 2440
Or   EqualDateTime <EQDtTm> [1..1] DateTime 2440
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 2440
71.4.1.2.10.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
71.4.1.2.10.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
71.4.1.2.10.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on
page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
71.4.1.2.10.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 3320
71.4.1.2.10.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 3320
71.4.1.2.11  SettlementQuantity <SttlmQty>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2440 August 2026
```

