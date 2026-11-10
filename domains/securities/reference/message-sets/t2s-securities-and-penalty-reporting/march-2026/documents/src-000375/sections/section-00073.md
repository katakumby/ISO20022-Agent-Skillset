---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.3 StatusAndReason <StsAndRsn>", "4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.3.4.1 PendingProcessing <PdgPrcg>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.3.4.1 PendingProcessing <PdgPrcg>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
InstructionProcessingStatus <InstrPrcgSts> contains one of the following
InstructionProcessingStatus63Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingProcessing <PdgPrcg> [1..1]  104
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 105
Or}     Reason <Rsn> [1..*]  105
       Code <Cd> [1..1]  105
{Or         Code <Cd> [1..1] CodeSet 106
Or}         Proprietary <Prtry> [1..1] ± 107
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 107
Or   CancellationRequested <CxlReqd> [1..1] ± C6 107
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 108
Or   Cancelled <Canc> [1..1] ± 108
Or   Generated <Gnrtd> [1..1]  108
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 109
Or}     Reason <Rsn> [1..*] ± 109
Or   Repair <Rpr> [1..1] ± 109
Or   PendingCancellation <PdgCxl> [1..1]  109
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 110
Or}     Reason <Rsn> [1..*]  110
       Code <Cd> [1..1]  110
{Or         Code <Cd> [1..1] CodeSet 111
Or}         Proprietary <Prtry> [1..1] ± 111
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 111
Or}   ModificationRequested <ModReqd> [1..1] ± C6 112
4.4.3.3.4.1  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Processing of the instruction/request is pending.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 104 March 2026
```

