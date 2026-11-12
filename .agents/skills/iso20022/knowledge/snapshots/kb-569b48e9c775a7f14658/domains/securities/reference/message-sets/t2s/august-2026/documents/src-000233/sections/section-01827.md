---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.3 StatusAndReason <StsAndRsn>", "72.4.3.3.4 InstructionProcessingStatus <InstrPrcgSts>", "72.4.3.3.4.8 ModificationRequested <ModReqd>"]
file_pages: [2508]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.3.4.8 ModificationRequested <ModReqd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2508 to 2508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2508

```text
72.4.3.3.4.8  ModificationRequested <ModReqd>
Presence: [1..1]
Definition: Modification request from your counterparty for this transaction is pending waiting for your
cancellation request or your consent.
Impacted by: C6 "AdditionalReasonInforrmationRule"
ModificationRequested <ModReqd> contains the following elements (see "ProprietaryReason4" on
page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
72.4.3.3.5  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
72.4.3.3.6  Proprietary <Prtry>
Presence: [0..1]
Definition: Proprietary status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2508 August 2026
```

