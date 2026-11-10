---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.8 ModificationProcessingStatus <ModPrcgSts>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.8 ModificationProcessingStatus <ModPrcgSts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
Definition: Provides the status of settlement of a transaction.
Impacted by: C4 "PendingToFailingRule"
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus32Choice" on page 1860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  1861
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1862
Or}     Reason <Rsn> [1..*]  1862
       Code <Cd> [1..1]  1862
{Or         Code <Cd> [1..1] CodeSet 1862
Or}         Proprietary <Prtry> [1..1] ± 1865
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1866
Or   Failing <Flng> [1..1]  1866
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1866
Or}     Reason <Rsn> [1..*]  1866
       Code <Cd> [1..1]  1867
{Or         Code <Cd> [1..1] CodeSet 1867
Or}         Proprietary <Prtry> [1..1] ± 1870
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1871
Or}   Proprietary <Prtry> [1..1] ± 1871
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
13.4.7.8  ModificationProcessingStatus <ModPrcgSts>
Presence: [0..1]
Definition: Provides details on the modification processing status of the transaction.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 449 March 2026
```

