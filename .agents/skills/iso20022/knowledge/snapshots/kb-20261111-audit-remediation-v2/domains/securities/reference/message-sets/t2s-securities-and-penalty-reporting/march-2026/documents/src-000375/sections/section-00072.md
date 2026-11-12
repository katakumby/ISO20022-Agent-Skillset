---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.3 StatusAndReason <StsAndRsn>", "4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>"]
file_pages: [103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 103 to 103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 103

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus32Choice" on page 458 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  458
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 459
Or}     Reason <Rsn> [1..*]  459
       Code <Cd> [1..1]  459
{Or         Code <Cd> [1..1] CodeSet 460
Or}         Proprietary <Prtry> [1..1] ± 463
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 463
Or   Failing <Flng> [1..1]  463
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 463
Or}     Reason <Rsn> [1..*]  464
       Code <Cd> [1..1]  464
{Or         Code <Cd> [1..1] CodeSet 464
Or}         Proprietary <Prtry> [1..1] ± 468
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 468
Or}   Proprietary <Prtry> [1..1] ± 468
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
4.4.3.3.4  InstructionProcessingStatus <InstrPrcgSts>
Presence: [0..1]
Definition: Provides the status of an instruction.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 103 March 2026
```

