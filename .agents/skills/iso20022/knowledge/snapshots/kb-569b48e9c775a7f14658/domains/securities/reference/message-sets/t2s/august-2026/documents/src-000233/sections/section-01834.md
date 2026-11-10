---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.3 StatusAndReason <StsAndRsn>", "72.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.4.3.4.1 PendingProcessing <PdgPrcg>"]
file_pages: [2520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.3.4.1 PendingProcessing <PdgPrcg>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2520 to 2520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2520

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus63Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingProcessing <PdgPrcg> [1..1]  2520
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2521
Or}     Reason <Rsn> [1..*]  2521
       Code <Cd> [1..1]  2521
{Or         Code <Cd> [1..1] CodeSet 2522
Or}         Proprietary <Prtry> [1..1] ± 2523
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2523
Or   CancellationRequested <CxlReqd> [1..1] ± C6 2523
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 2524
Or   Cancelled <Canc> [1..1] ± 2524
Or   Generated <Gnrtd> [1..1]  2524
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2525
Or}     Reason <Rsn> [1..*] ± 2525
Or   Repair <Rpr> [1..1] ± 2525
Or   PendingCancellation <PdgCxl> [1..1]  2525
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2526
Or}     Reason <Rsn> [1..*]  2526
       Code <Cd> [1..1]  2526
{Or         Code <Cd> [1..1] CodeSet 2527
Or}         Proprietary <Prtry> [1..1] ± 2527
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2527
Or}   ModificationRequested <ModReqd> [1..1] ± C6 2528
72.4.3.4.3.4.1  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Processing of the instruction/request is pending.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2520 August 2026
```

