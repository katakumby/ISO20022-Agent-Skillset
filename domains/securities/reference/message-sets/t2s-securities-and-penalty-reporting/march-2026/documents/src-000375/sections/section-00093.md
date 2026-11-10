---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>", "4.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.4.3.4.5 Generated <Gnrtd>", "4.4.3.4.3.4.5.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3.4.5.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
Generated <Gnrtd> contains one of the following GeneratedStatus7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 129
Or}   Reason <Rsn> [1..*] ± 129
4.4.3.4.3.4.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 516
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
4.4.3.4.3.4.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the generated status.
Reason <Rsn> contains the following elements (see "GeneratedReason5" on page 475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 475
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 475
4.4.3.4.3.4.6  Repair <Rpr>
Presence: [1..1]
Definition: Instruction/Request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RepairStatus12Choice" on page 484 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 484
Or}   Reason <Rsn> [1..*]  484
     Code <Cd> [1..1]  485
{Or       Code <Cd> [1..1] CodeSet 485
Or}       Proprietary <Prtry> [1..1] ± 486
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 486
4.4.3.4.3.4.7  PendingCancellation <PdgCxl>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 129 March 2026
```

