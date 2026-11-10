---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.9 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "53.4.5.17.9.7 ReceivingSideDetails <RcvgSdDtls>", "53.4.5.17.9.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>"]
file_pages: [3664]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.9.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3664 to 3664.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3664

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
53.4.5.17.9.7.1  ReceiversCustodianDetails <RcvrsCtdnDtls>
Presence: [0..1]
Definition: Party that acts on behalf of the buyer of securities when the buyer does not have a direct
relationship with the receiving agent.
ReceiversCustodianDetails <RcvrsCtdnDtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 3664
   AccountIdentification <AcctId> [0..1] Text 3664
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3664
53.4.5.17.9.7.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.17.9.7.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
53.4.5.17.9.7.1.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3664 May 2026
```

