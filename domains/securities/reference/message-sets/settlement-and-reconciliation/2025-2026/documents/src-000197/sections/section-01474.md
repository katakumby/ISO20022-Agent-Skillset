---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.56 MatchingStatus24Choice", "35.1.29.56.1 Matched <Mtchd>"]
file_pages: [1964]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.56.1 Matched <Mtchd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1964 to 1964.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1964

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
35.1.29.56.1  Matched <Mtchd>
Presence: [1..1]
Definition: Status is matched.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Matched <Mtchd> contains the following elements (see "ProprietaryReason4" on page 1899 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
35.1.29.56.2  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status is unmatched.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1964 March 2026
```

