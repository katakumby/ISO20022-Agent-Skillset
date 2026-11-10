---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.2 ReportGeneralDetails <RptGnlDtls>", "3.4.2.1 QueryReference <QryRef>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.2.1 QueryReference <QryRef>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
Impacted by: C20 "ReportIdentificationRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraPositionReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [0..1] Text 63
   ReportIdentification <RptId> [0..1] Text 63
   QueryType <QryTp> [1..1] CodeSet 63
   ActivityIndicator <ActvtyInd> [1..1] Indicator 63
Constraints
• ReportIdentificationRule
If the report has multiple pages, then the ReportIdentification must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different report identifications. For example, a daily report sent on
day 1 would have ReportIdentification 001, on day 2, 002, etc.
3.4.2.1  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the query message sent to request this statement.
Datatype: "Max35Text" on page 345
3.4.2.2  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 345
3.4.2.3  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 331
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
3.4.2.4  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 63 September 2025
```

