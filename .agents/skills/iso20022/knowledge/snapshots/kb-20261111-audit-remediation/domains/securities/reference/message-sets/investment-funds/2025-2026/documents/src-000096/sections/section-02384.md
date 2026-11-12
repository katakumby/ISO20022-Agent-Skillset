---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "52.4.5.10.28.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [3350]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3350 to 3350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3350

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
52.4.5.10.28.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C13 "DeliverersCustodianRule", C14 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3351
     PartyIdentification <PtyId> [1..1] ± 3351
     AccountIdentification <AcctId> [0..1] Text 3351
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3352
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3352
     PartyIdentification <PtyId> [1..1] ± 3352
     AccountIdentification <AcctId> [0..1] Text 3352
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3352
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3353
     PartyIdentification <PtyId> [1..1] ± 3353
     AccountIdentification <AcctId> [0..1] Text 3353
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3353
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3354
     PartyIdentification <PtyId> [1..1] ± 3354
     AccountIdentification <AcctId> [0..1] Text 3354
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3354
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3350 May 2026
```

