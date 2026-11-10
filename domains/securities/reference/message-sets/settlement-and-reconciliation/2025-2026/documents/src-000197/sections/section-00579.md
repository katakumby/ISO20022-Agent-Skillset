---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.18.1 ProcessingStatus <PrcgSts>", "26.4.18.1.3 Repair <Rpr>"]
file_pages: [872]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.18.1.3 Repair <Rpr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 872 to 872.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 872

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
26.4.18.1.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer but is in repair.
Repair <Rpr> contains one of the following elements (see "RepairStatus12Choice" on page 2010 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2011
Or}   Reason <Rsn> [1..*]  2011
     Code <Cd> [1..1]  2011
{Or       Code <Cd> [1..1] CodeSet 2011
Or}       Proprietary <Prtry> [1..1] ± 2013
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2013
26.4.18.1.4  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: A cancellation request from yourself for this instruction is pending waiting for further
processing (only as a response to a SecuritiesTransactionStatusQuery). The pending status on the
processing of a cancellation request must be provided using a
SecuritiesTransactionCancellationRequestStatusAdvice.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 872 March 2026
```

