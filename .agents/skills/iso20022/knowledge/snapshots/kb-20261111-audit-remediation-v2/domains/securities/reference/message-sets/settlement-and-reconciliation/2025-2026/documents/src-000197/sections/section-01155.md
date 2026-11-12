---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.64 AdditionalParameters29", "35.1.16.64.1 PreConfirmation <PreConf>"]
file_pages: [1602]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.64.1 PreConfirmation <PreConf>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1602 to 1602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1602

```text
The PartialSettlement field should be used as follows:
- with code PAIN in the first message(s) (there may be more than one) confirming the partial
settlement of an instruction.
- with code PARC in the very last message sent to confirm the settlement of the remaining part.
For more details, see the relevant market practice document on www.smpg.info.
35.1.16.64.1  PreConfirmation <PreConf>
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
35.1.16.64.2  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 2089
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
35.1.16.64.3  PreviousPartialConfirmationIdentification <PrvsPrtlConfId>
Presence: [0..1]
Definition: Identification of the confirmation previously sent to confirm the partial settlement of a
transaction.
Datatype: "Max35Text" on page 2192
35.1.16.64.4  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1602 March 2026
```

