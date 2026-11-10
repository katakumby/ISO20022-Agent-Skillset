---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.10 AdditionalParameters16", "82.1.19.10.1 PartialSettlement <PrtlSttlm>"]
file_pages: [2983]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.10.1 PartialSettlement <PrtlSttlm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2983 to 2983.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2983

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 2983
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 2983
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 2983
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2983
   PoolIdentification <PoolId> [0..1] Text 2984
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2984
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2984
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2984
82.1.19.10.1  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 3267
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
82.1.19.10.2  PreviousPartialConfirmationIdentification <PrvsPrtlConfId>
Presence: [0..1]
Definition: Identification of the confirmation previously sent to confirm the partial settlement of a
transaction.
Datatype: "Max35Text" on page 3328
82.1.19.10.3  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
82.1.19.10.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2983 August 2026
```

