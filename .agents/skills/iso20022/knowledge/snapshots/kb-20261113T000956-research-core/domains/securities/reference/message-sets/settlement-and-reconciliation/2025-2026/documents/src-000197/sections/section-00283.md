---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.1 RepoCallAcknowledgementReason <RepoCallAckRsn>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.1 RepoCallAcknowledgementReason <RepoCallAckRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
Constraints
• ReasonRule
If the reason is requested, then it must be in line with the reasons available for the message type
requested.
12.4.6.2.1  RepoCallAcknowledgementReason <RepoCallAckRsn>
Presence: [0..1]
Definition: Specifies additional information on the repurchase agreement call request
acknowledgement.
RepoCallAcknowledgementReason <RepoCallAckRsn> contains one of the following elements (see
"AcknowledgementReason13Choice" on page 1979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1979
Or}   Proprietary <Prtry> [1..1] ± 1980
12.4.6.2.2  CancellationReason <CxlRsn>
Presence: [0..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
CancellationReason <CxlRsn> contains one of the following elements (see
"CancellationReason20Choice" on page 1988 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1988
Or}   Proprietary <Prtry> [1..1] ± 1989
12.4.6.2.3  PendingCancellationReason <PdgCxlRsn>
Presence: [0..1]
Definition: Specifies the reason why the cancellation request is pending.
PendingCancellationReason <PdgCxlRsn> contains one of the following elements (see
"PendingCancellationReasons6Choice" on page 2022 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2023
Or}   Proprietary <Prtry> [1..1] ± 2023
12.4.6.2.4  GeneratedReason <GnrtdRsn>
Presence: [0..1]
Definition: Specifies the reason why the transaction was generated.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 422 March 2026
```

