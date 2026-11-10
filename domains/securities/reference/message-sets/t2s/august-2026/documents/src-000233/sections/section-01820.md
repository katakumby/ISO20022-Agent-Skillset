---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>", "72.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.3.4.1 PendingProcessing <PdgPrcg>", "72.4.3.3.4.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [2501]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3.4.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2501 to 2501.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2501

```text
PendingProcessing <PdgPrcg> contains one of the following PendingProcessingStatus20Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2501
Or}   Reason <Rsn> [1..*]  2501
     Code <Cd> [1..1]  2501
{Or       Code <Cd> [1..1] CodeSet 2502
Or}       Proprietary <Prtry> [1..1] ± 2503
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2503
72.4.3.3.4.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
72.4.3.3.4.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2501
{Or     Code <Cd> [1..1] CodeSet 2502
Or}     Proprietary <Prtry> [1..1] ± 2503
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2503
72.4.3.3.4.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Code <Cd> contains one of the following PendingProcessingReason19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2502
Or}   Proprietary <Prtry> [1..1] ± 2503
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2501 August 2026
```

