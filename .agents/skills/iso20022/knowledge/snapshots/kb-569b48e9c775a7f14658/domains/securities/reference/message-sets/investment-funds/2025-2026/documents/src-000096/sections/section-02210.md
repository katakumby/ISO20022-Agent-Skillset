---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "50.4.4.9.17.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [3106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.17.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3106 to 3106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3106

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
50.4.4.9.17.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C11 "DeliverersCustodianRule", C12 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3107
     PartyIdentification <PtyId> [1..1] ± 3107
     AccountIdentification <AcctId> [0..1] Text 3107
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3108
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3108
     PartyIdentification <PtyId> [1..1] ± 3108
     AccountIdentification <AcctId> [0..1] Text 3108
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3108
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3109
     PartyIdentification <PtyId> [1..1] ± 3109
     AccountIdentification <AcctId> [0..1] Text 3109
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3109
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3110
     PartyIdentification <PtyId> [1..1] ± 3110
     AccountIdentification <AcctId> [0..1] Text 3110
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3110
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3106 May 2026
```

