---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.10 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "53.4.5.16.10.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [3600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.10.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3600 to 3600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3600

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
53.4.5.16.10.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C9 "DeliverersCustodianRule", C10 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3601
     PartyIdentification <PtyId> [1..1] ± 3601
     AccountIdentification <AcctId> [0..1] Text 3601
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3602
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3602
     PartyIdentification <PtyId> [1..1] ± 3602
     AccountIdentification <AcctId> [0..1] Text 3602
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3602
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3603
     PartyIdentification <PtyId> [1..1] ± 3603
     AccountIdentification <AcctId> [0..1] Text 3603
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3603
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3604
     PartyIdentification <PtyId> [1..1] ± 3604
     AccountIdentification <AcctId> [0..1] Text 3604
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3604
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3600 May 2026
```

