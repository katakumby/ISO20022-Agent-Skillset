---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.25 Statement58"]
file_pages: [383]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.25 Statement58

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 383 to 383.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 383

```text
Constraints
• EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event triggers a
securities movement as per the Event Interpretation Grid published by the Securities Market Practice
Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is decided
by the issuer and not by the holders.
7.1.18.25  Statement58
Definition: Characteristics of the report.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [0..1] Text 383
   ReportIdentification <RptId> [0..1] Text 383
   HistoricData <HstrcData> [1..1] Indicator 384
   ActivityIndicator <ActvtyInd> [1..1] Indicator 384
   SubAccountIndicator <SubAcctInd> [1..1] Indicator 384
Constraints
• ReportNumberRule
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
7.1.18.25.1  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the SecuritiesStatementQuery message sent to request this statement.
Datatype: "Max35Text" on page 557
7.1.18.25.2  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a report.
Datatype: "Max35Text" on page 557
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 383 March 2026
```

