---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.4 Message Building Blocks", "6.4.9 IntraPositionDetails <IntraPosDtls>", "6.4.9.7 AvailableDate <AvlblDt>"]
file_pages: [176]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.4.9.7 AvailableDate <AvlblDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 176 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 176

```text
6.4.9.7  AvailableDate <AvlblDt>
Presence: [0..1]
Definition: Date/time securities become available for sale (if securities become unavailable, this
specifies the date/time at which they will become available again).
AvailableDate <AvlblDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
6.4.9.8  CorporateActionEventType <CorpActnEvtTp>
Presence: [0..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType110Choice" on page 1651 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1651
Or}   Proprietary <Prtry> [1..1] ± 1658
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
6.4.9.9  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the securities are moving.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 176 March 2026
```

