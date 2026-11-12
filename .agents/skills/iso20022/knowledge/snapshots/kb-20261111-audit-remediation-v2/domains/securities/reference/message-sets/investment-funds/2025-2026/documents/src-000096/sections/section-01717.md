---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "46.4.5.10.28.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [2407]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.28.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2407 to 2407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2407

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
46.4.5.10.28.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C12 "DeliverersCustodianRule", C13 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2408
     PartyIdentification <PtyId> [1..1] ± 2408
     AccountIdentification <AcctId> [0..1] Text 2408
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2409
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2409
     PartyIdentification <PtyId> [1..1] ± 2409
     AccountIdentification <AcctId> [0..1] Text 2409
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2409
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2410
     PartyIdentification <PtyId> [1..1] ± 2410
     AccountIdentification <AcctId> [0..1] Text 2410
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2410
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2411
     PartyIdentification <PtyId> [1..1] ± 2411
     AccountIdentification <AcctId> [0..1] Text 2411
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2411
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2407 May 2026
```

