---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.3 StatusAndReason <StsAndRsn>", "4.4.3.4.3.4 InstructionProcessingStatus <InstrPrcgSts>", "4.4.3.4.3.4.8 ModificationRequested <ModReqd>"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.3.4.8 ModificationRequested <ModReqd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
4.4.3.4.3.4.8  ModificationRequested <ModReqd>
Presence: [1..1]
Definition: Modification request from your counterparty for this transaction is pending waiting for your
cancellation request or your consent.
Impacted by: C6 "AdditionalReasonInforrmationRule"
ModificationRequested <ModReqd> contains the following elements (see "ProprietaryReason4" on
page 470 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 470
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
4.4.3.4.3.5  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 470 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 470
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
4.4.3.4.3.6  Proprietary <Prtry>
Presence: [0..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 469
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 469
   ProprietaryReason <PrtryRsn> [0..*] ± C6 469
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 132 March 2026
```

