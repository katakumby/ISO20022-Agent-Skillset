---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.3 BlockedStatus <BlckdSts>"]
file_pages: [4561]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.3 BlockedStatus <BlckdSts>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4561 to 4561.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4561

```text
• ClosedStatus6Rule
If Closed is present then ClosurePending is not allowed.
On Condition
    /Closed is absent
Following Must be True
    /ClosurePending Must be absent
• EnabledDisabledStatus1Rule
If Enabled is present, then Disabled is not allowed.
On Condition
    /Enabled is present
Following Must be True
    /Disabled Must be absent
• EnabledDisabledStatus2Rule
If Disabled is present, then Enabled is not allowed.
On Condition
    /Disabled is present
Following Must be True
    /Enabled Must be absent
• StatusElementRule
One of the elements (Enabled, Disabled, Pending, PendingOpening, Proforma, Closed,
ClosurePending, Other) must be present.
66.1.24.3.3  BlockedStatus <BlckdSts>
Presence: [0..1]
Definition: Specifies the account is blocked and other factors for the blocked account.
BlockedStatus <BlckdSts> contains one of the following elements (see
"BlockedStatusReason2Choice" on page 5164 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5164
Or}   Reason <Rsn> [1..*]  5165
     TransactionType <TxTp> [1..1]  5165
{Or       Code <Cd> [1..1] CodeSet 5165
Or}       Proprietary <Prtry> [1..1] ± 5167
     Blocked <Blckd> [1..1] Indicator 5167
     Reason <Rsn> [0..*]  5167
{Or       Code <Cd> [1..1] CodeSet 5167
Or}       Proprietary <Prtry> [1..1] ± 5168
     AdditionalInformation <AddtlInf> [1..1] Text 5168
66.1.24.3.4  StatusDate <StsDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4561 May 2026
```

