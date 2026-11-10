---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "41.4.4.8.16.8 DeliveringSideDetails <DlvrgSdDtls>", "41.4.4.8.16.8.1 DeliverersCustodianDetails <DlvrrsCtdnDtls>", "41.4.4.8.16.8.1.3 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [1783]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.16.8.1.3 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1783 to 1783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1783

```text
41.4.4.8.16.8.1.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
41.4.4.8.16.8.2  DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls>
Presence: [0..1]
Definition: Party that the deliverer's custodian uses to effect the delivery of a security, when the
deliverer's custodian does not have a direct relationship with the delivering agent.
DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 1783
   AccountIdentification <AcctId> [0..1] Text 1783
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1783
41.4.4.8.16.8.2.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
41.4.4.8.16.8.2.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
41.4.4.8.16.8.2.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1783 May 2026
```

