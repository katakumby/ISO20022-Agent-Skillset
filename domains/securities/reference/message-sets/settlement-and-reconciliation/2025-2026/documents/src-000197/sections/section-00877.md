---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>", "33.4.6.6 Modified <Modfd>"]
file_pages: [1310]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6.6 Modified <Modfd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1310 to 1310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1310

```text
Repaired <Rprd> contains one of the following elements (see "RepairStatus13Choice" on page 1946
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1946
Or}   Reason <Rsn> [1..*]  1946
     Code <Cd> [1..1]  1947
{Or       Code <Cd> [1..1] CodeSet 1947
Or}       Proprietary <Prtry> [1..1] ± 1948
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1949
33.4.6.6  Modified <Modfd>
Presence: [1..1]
Definition: Instruction has been modified.
Modified <Modfd> contains one of the following ModificationStatus6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1310
Or}   Reason <Rsn> [1..*]  1310
     Code <Cd> [1..1]  1311
{Or       Code <Cd> [1..1] CodeSet 1311
Or}       Proprietary <Prtry> [1..1] ± 1311
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1312
33.4.6.6.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
33.4.6.6.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the modification status.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1310 March 2026
```

