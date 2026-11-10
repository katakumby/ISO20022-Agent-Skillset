---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.4 ProcessingStatus <PrcgSts>", "13.4.7.4.3 Rejected <Rjctd>"]
file_pages: [443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.4.3 Rejected <Rjctd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 443 to 443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 443

```text
PendingProcessing <PdgPrcg> contains one of the following elements (see
"PendingProcessingStatus22Choice" on page 2020 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2020
Or}   Reason <Rsn> [1..*]  2020
     Code <Cd> [1..1]  2020
{Or       Code <Cd> [1..1] CodeSet 2021
Or}       Proprietary <Prtry> [1..1] ± 2022
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2022
13.4.7.4.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/Request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus38Choice" on page 1874
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1874
Or}   Reason <Rsn> [1..*]  1874
     Code <Cd> [1..1]  1874
{Or       Code <Cd> [1..1] CodeSet 1875
Or}       Proprietary <Prtry> [1..1] ± 1876
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1877
13.4.7.4.4  Repair <Rpr>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but is in repair.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 443 March 2026
```

