---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>", "4.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.4.3.4.7 PendingCancellation <PdgCxl>", "4.4.3.4.3.4.7.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3.4.7.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 130 to 130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 130

```text
Definition: Cancellation request from yourself for this instruction is pending waiting for further
processing.
PendingCancellation <PdgCxl> contains one of the following PendingStatus81Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 130
Or}   Reason <Rsn> [1..*]  130
     Code <Cd> [1..1]  130
{Or       Code <Cd> [1..1] CodeSet 131
Or}       Proprietary <Prtry> [1..1] ± 131
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 131
4.4.3.4.3.4.7.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
4.4.3.4.3.4.7.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason35 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  130
{Or     Code <Cd> [1..1] CodeSet 131
Or}     Proprietary <Prtry> [1..1] ± 131
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 131
4.4.3.4.3.4.7.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 130 March 2026
```

