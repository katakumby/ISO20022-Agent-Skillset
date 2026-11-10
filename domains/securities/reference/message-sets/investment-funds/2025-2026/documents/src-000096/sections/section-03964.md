---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.5 ReversedStatus2Choice"]
file_pages: [5261]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.5 ReversedStatus2Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5261 to 5261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5261

```text
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.5  ReversedStatus2Choice
Definition: Reason for the reversed status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5261
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5261
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5261
66.1.50.5.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the reversal status.
Datatype: "Max350Text" on page 5403
66.1.50.5.2  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the reversed status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.5.3  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.6  PendingSettlementStatus3Choice
Definition: Reason for the pending settlement status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5261 May 2026
```

