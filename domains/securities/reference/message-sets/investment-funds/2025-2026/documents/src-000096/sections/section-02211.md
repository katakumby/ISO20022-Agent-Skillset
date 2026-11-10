---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "50.4.4.9.17.8 DeliveringSideDetails <DlvrgSdDtls>", "50.4.4.9.17.8.1 DeliverersCustodianDetails <DlvrrsCtdnDtls>"]
file_pages: [3107]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.17.8.1 DeliverersCustodianDetails <DlvrrsCtdnDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3107 to 3107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3107

```text
Constraints
• DeliverersCustodianRule
If DeliverersIntermediary1Details is present, then DeliverersCustodianDetails must be present. If
DeliverersIntermediary1Details is not present then DeliverersCustodianDetails is optional.
On Condition
    /DeliverersIntermediary1Details is present
Following Must be True
    /DeliverersCustodianDetails Must be present
• DeliverersIntermediary1DetailsRule
If DeliverersIntermediary2Details is present, then DeliverersIntermediary1Details must be present. If
DeliverersIntermediary2Details is not present then DeliverersIntermediary1Details is optional.
On Condition
    /DeliverersIntermediary2Details is present
Following Must be True
    /DeliverersIntermediary1Details Must be present
50.4.4.9.17.8.1  DeliverersCustodianDetails <DlvrrsCtdnDtls>
Presence: [0..1]
Definition: Party that acts on behalf of the seller of securities when the seller does not have a direct
relationship with the delivering agent.
DeliverersCustodianDetails <DlvrrsCtdnDtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 3107
   AccountIdentification <AcctId> [0..1] Text 3107
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3108
50.4.4.9.17.8.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.9.17.8.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3107 May 2026
```

