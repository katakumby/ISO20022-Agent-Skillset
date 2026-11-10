---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "41.4.4.8.16.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [1781]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.16.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1781 to 1781.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1781

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
41.4.4.8.16.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C11 "DeliverersCustodianRule", C12 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1782
     PartyIdentification <PtyId> [1..1] ± 1782
     AccountIdentification <AcctId> [0..1] Text 1782
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1783
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1783
     PartyIdentification <PtyId> [1..1] ± 1783
     AccountIdentification <AcctId> [0..1] Text 1783
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1783
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1784
     PartyIdentification <PtyId> [1..1] ± 1784
     AccountIdentification <AcctId> [0..1] Text 1784
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1784
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1785
     PartyIdentification <PtyId> [1..1] ± 1785
     AccountIdentification <AcctId> [0..1] Text 1785
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1785
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1781 May 2026
```

