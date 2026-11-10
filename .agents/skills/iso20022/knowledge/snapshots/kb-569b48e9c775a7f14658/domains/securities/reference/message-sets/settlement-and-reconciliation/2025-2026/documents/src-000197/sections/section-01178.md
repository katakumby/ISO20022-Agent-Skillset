---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.82 AdditionalParameters30"]
file_pages: [1629]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.82 AdditionalParameters30

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1629 to 1629.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1629

```text
35.1.16.82  AdditionalParameters30
Definition: Specifies additional parameters to the message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreConfirmation <PreConf> [0..1] CodeSet 1629
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1629
   TripartyAgentServiceProviderCollateralTransactionIdentifi
cation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 1629
   ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 1629
35.1.16.82.1  PreConfirmation <PreConf>
Presence: [0..1]
Definition: Specifies whether there exists a pre-confirmation.
Datatype: "PreConfirmation1Code" on page 2111
CodeName Name Definition
PRCA PreConfirmCash Pre-confirmation of the movement of the
cash, pending the movement of
securities.
PRSE PreConfirmSecurities Pre-confirmation of the movement of the
securities, pending the movement of
cash.
35.1.16.82.2  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 2089
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
35.1.16.82.3  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 2192
35.1.16.82.4  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1629 March 2026
```

