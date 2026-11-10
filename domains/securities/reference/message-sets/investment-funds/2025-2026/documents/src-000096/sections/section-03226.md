---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.10 Clearing System Member Identification", "66.1.10.2 ClearingSystemMemberIdentification2Choice", "66.1.10.2.23 OtherClearingCodeIdentification <OthrClrCdId>"]
file_pages: [4462]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.10.2.23 OtherClearingCodeIdentification <OthrClrCdId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4462 to 4462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4462

```text
66.1.10.2.23  OtherClearingCodeIdentification <OthrClrCdId>
Presence: [1..1]
Definition: Identification Code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 5403
66.1.11 Commission
66.1.11.1  Commission21
Definition: Amount of money due to a party as compensation for a service.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommissionType <ComssnTp> [1..1]  4462
{Or     Code <Cd> [1..1] CodeSet 4462
Or}     Proprietary <Prtry> [1..1] ± 4463
   CommissionApplied <ComssnApld> [1..1]  4463
{Or     Amount <Amt> [1..1] Amount C1 4463
Or}     Rate <Rate> [1..1] Rate 4463
66.1.11.1.1  CommissionType <ComssnTp>
Presence: [1..1]
Definition: Type of commission.
CommissionType <ComssnTp> contains one of the following CommissionType5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4462
Or}   Proprietary <Prtry> [1..1] ± 4463
66.1.11.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Commission type expressed as a code.
Datatype: "CommissionType6Code" on page 5285
CodeName Name Definition
FEND FrontEndLoad Commission for subscribing to an
investment, paid at the time of the
subscription.
BEND BackEndLoad Commission for redeeming an
investment, when an investor redeems
an investment fund within a certain
period of time.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4462 May 2026
```

