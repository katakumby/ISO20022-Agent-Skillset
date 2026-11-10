---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.3 StatusAndReason <StsAndRsn>", "72.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.4.3.4.5 Generated <Gnrtd>", "72.4.3.4.3.4.5.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [2525]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.3.4.5.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2525 to 2525.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2525

```text
Generated <Gnrtd> contains one of the following GeneratedStatus7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2525
Or}   Reason <Rsn> [1..*] ± 2525
72.4.3.4.3.4.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
72.4.3.4.3.4.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the generated status.
Reason <Rsn> contains the following elements (see "GeneratedReason5" on page 3166 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3166
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3166
72.4.3.4.3.4.6  Repair <Rpr>
Presence: [1..1]
Definition: Instruction/Request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RepairStatus12Choice" on page 3188 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3189
Or}   Reason <Rsn> [1..*]  3189
     Code <Cd> [1..1]  3189
{Or       Code <Cd> [1..1] CodeSet 3189
Or}       Proprietary <Prtry> [1..1] ± 3191
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3191
72.4.3.4.3.4.7  PendingCancellation <PdgCxl>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2525 August 2026
```

