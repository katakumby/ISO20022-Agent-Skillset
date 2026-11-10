---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>", "72.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.3.4.1 PendingProcessing <PdgPrcg>"]
file_pages: [2500]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3.4.1 PendingProcessing <PdgPrcg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2500 to 2500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2500

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus63Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingProcessing <PdgPrcg> [1..1]  2500
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2501
Or}     Reason <Rsn> [1..*]  2501
       Code <Cd> [1..1]  2501
{Or         Code <Cd> [1..1] CodeSet 2502
Or}         Proprietary <Prtry> [1..1] ± 2503
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2503
Or   CancellationRequested <CxlReqd> [1..1] ± C6 2503
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 2504
Or   Cancelled <Canc> [1..1] ± 2504
Or   Generated <Gnrtd> [1..1]  2504
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2505
Or}     Reason <Rsn> [1..*] ± 2505
Or   Repair <Rpr> [1..1] ± 2505
Or   PendingCancellation <PdgCxl> [1..1]  2505
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2506
Or}     Reason <Rsn> [1..*]  2506
       Code <Cd> [1..1]  2506
{Or         Code <Cd> [1..1] CodeSet 2507
Or}         Proprietary <Prtry> [1..1] ± 2507
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2507
Or}   ModificationRequested <ModReqd> [1..1] ± C6 2508
72.4.3.3.4.1  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Processing of the instruction/request is pending.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2500 August 2026
```

