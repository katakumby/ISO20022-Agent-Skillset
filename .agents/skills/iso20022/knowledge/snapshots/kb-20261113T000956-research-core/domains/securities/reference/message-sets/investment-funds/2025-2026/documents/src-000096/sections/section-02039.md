---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "49.4.5.9.28.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [2865]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.28.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2865 to 2865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2865

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
49.4.5.9.28.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C12 "DeliverersCustodianRule", C13 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2866
     PartyIdentification <PtyId> [1..1] ± 2866
     AccountIdentification <AcctId> [0..1] Text 2866
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2867
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2867
     PartyIdentification <PtyId> [1..1] ± 2867
     AccountIdentification <AcctId> [0..1] Text 2867
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2867
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2868
     PartyIdentification <PtyId> [1..1] ± 2868
     AccountIdentification <AcctId> [0..1] Text 2868
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2868
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2869
     PartyIdentification <PtyId> [1..1] ± 2869
     AccountIdentification <AcctId> [0..1] Text 2869
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2869
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2865 May 2026
```

