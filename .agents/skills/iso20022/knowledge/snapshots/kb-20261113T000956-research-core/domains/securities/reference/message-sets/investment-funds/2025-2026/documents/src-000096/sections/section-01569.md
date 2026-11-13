---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "44.4.4.9.16.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [2198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.16.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2198 to 2198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2198

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
44.4.4.9.16.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C11 "DeliverersCustodianRule", C12 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2199
     PartyIdentification <PtyId> [1..1] ± 2199
     AccountIdentification <AcctId> [0..1] Text 2199
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2200
     PartyIdentification <PtyId> [1..1] ± 2200
     AccountIdentification <AcctId> [0..1] Text 2200
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2201
     PartyIdentification <PtyId> [1..1] ± 2201
     AccountIdentification <AcctId> [0..1] Text 2201
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2201
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2202
     PartyIdentification <PtyId> [1..1] ± 2202
     AccountIdentification <AcctId> [0..1] Text 2202
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2202
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2198 May 2026
```

