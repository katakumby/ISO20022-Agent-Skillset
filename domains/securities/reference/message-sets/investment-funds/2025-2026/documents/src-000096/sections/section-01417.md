---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.29 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "43.4.5.9.29.8 DeliveringSideDetails <DlvrgSdDtls>"]
file_pages: [1987]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.29.8 DeliveringSideDetails <DlvrgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1987 to 1987.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1987

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
43.4.5.9.29.8  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C12 "DeliverersCustodianRule", C13 "DeliverersIntermediary1DetailsRule"
DeliveringSideDetails <DlvrgSdDtls> contains the following DeliveringPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1988
     PartyIdentification <PtyId> [1..1] ± 1988
     AccountIdentification <AcctId> [0..1] Text 1988
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
   DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1989
     PartyIdentification <PtyId> [1..1] ± 1989
     AccountIdentification <AcctId> [0..1] Text 1989
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
   DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1990
     PartyIdentification <PtyId> [1..1] ± 1990
     AccountIdentification <AcctId> [0..1] Text 1990
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1990
   DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1991
     PartyIdentification <PtyId> [1..1] ± 1991
     AccountIdentification <AcctId> [0..1] Text 1991
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1991
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1987 May 2026
```

