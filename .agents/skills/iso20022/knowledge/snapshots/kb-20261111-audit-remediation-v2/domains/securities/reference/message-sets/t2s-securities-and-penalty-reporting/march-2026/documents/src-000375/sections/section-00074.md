---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.3 StatusAndReason <StsAndRsn>", "4.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.3.4.1 PendingProcessing <PdgPrcg>", "4.4.3.3.4.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.3.4.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
PendingProcessing <PdgPrcg> contains one of the following PendingProcessingStatus20Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 105
Or}   Reason <Rsn> [1..*]  105
     Code <Cd> [1..1]  105
{Or       Code <Cd> [1..1] CodeSet 106
Or}       Proprietary <Prtry> [1..1] ± 107
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 107
4.4.3.3.4.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
4.4.3.3.4.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  105
{Or     Code <Cd> [1..1] CodeSet 106
Or}     Proprietary <Prtry> [1..1] ± 107
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 107
4.4.3.3.4.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Code <Cd> contains one of the following PendingProcessingReason19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 106
Or}   Proprietary <Prtry> [1..1] ± 107
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 105 March 2026
```

