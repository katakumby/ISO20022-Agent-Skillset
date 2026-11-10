---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "47.4.4.8.17.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [2626]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.17.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2626 to 2626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2626

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
47.4.4.8.17.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C11 "DeliverersCustodianRule", C12 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2627
     PartyIdentification <PtyId> [1..1] ± 2627
     AccountIdentification <AcctId> [0..1] Text 2627
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2628
     PartyIdentification <PtyId> [1..1] ± 2628
     AccountIdentification <AcctId> [0..1] Text 2628
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2629
     PartyIdentification <PtyId> [1..1] ± 2629
     AccountIdentification <AcctId> [0..1] Text 2629
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2629
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2630
     PartyIdentification <PtyId> [1..1] ± 2630
     AccountIdentification <AcctId> [0..1] Text 2630
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2630
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2626 May 2026
```

