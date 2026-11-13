---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "44.4.4.9.16.7 ReceivingSideDetails <RcvgSdDtls>", "44.4.4.9.16.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>"]
file_pages: [2194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.16.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2194 to 2194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2194

```text
On Condition
    /ReceiversIntermediary1Details is present
Following Must be True
    /ReceiversCustodianDetails Must be present
• ReceiversIntermediary1DetailsRule
If ReceiversIntermediary2Details is present, then ReceiversIntermediary1Details must be present. If
ReceiversIntermediary2Details is not present, then ReceiversIntermediary1Details is optional.
On Condition
    /ReceiversIntermediary2Details is present
Following Must be True
    /ReceiversIntermediary1Details Must be present
44.4.4.9.16.7.1  ReceiversCustodianDetails <RcvrsCtdnDtls>
Presence: [0..1]
Definition: Party that acts on behalf of the buyer of securities when the buyer does not have a direct
relationship with the receiving agent.
ReceiversCustodianDetails <RcvrsCtdnDtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 2194
   AccountIdentification <AcctId> [0..1] Text 2194
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2194
44.4.4.9.16.7.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
44.4.4.9.16.7.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
44.4.4.9.16.7.1.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2194 May 2026
```

