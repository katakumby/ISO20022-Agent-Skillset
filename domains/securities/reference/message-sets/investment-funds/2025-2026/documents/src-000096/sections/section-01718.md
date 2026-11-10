---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "46.4.5.10.28.8 DeliveringSideDetails <DlvrgSdDtls>", "46.4.5.10.28.8.1 DeliverersCustodianDetails <DlvrrsCtdnDtls>"]
file_pages: [2408]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.28.8.1 DeliverersCustodianDetails <DlvrrsCtdnDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2408 to 2408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2408

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
46.4.5.10.28.8.1  DeliverersCustodianDetails <DlvrrsCtdnDtls>
Presence: [0..1]
Definition: Party that acts on behalf of the seller of securities when the seller does not have a direct
relationship with the delivering agent.
DeliverersCustodianDetails <DlvrrsCtdnDtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 2408
   AccountIdentification <AcctId> [0..1] Text 2408
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2409
46.4.5.10.28.8.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
46.4.5.10.28.8.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2408 May 2026
```

