---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.4 ProcessingStatus <PrcgSts>", "13.4.7.4.6 PendingCancellation <PdgCxl>", "13.4.7.4.6.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [445]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.4.6.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 445 to 445.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
PendingCancellation <PdgCxl> contains one of the following PendingStatus81Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 445
Or}   Reason <Rsn> [1..*]  445
     Code <Cd> [1..1]  445
{Or       Code <Cd> [1..1] CodeSet 446
Or}       Proprietary <Prtry> [1..1] ± 446
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
13.4.7.4.6.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
13.4.7.4.6.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  445
{Or     Code <Cd> [1..1] CodeSet 446
Or}     Proprietary <Prtry> [1..1] ± 446
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
13.4.7.4.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following PendingReason77Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 446
Or}   Proprietary <Prtry> [1..1] ± 446
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 445 March 2026
```

