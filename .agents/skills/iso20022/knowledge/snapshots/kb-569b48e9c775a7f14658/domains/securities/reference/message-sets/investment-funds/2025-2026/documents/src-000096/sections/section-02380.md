---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "52.4.5.10.28.7 ReceivingSideDetails <RcvgSdDtls>", "52.4.5.10.28.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>"]
file_pages: [3346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28.7.1 ReceiversCustodianDetails <RcvrsCtdnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3346 to 3346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3346

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
52.4.5.10.28.7.1  ReceiversCustodianDetails <RcvrsCtdnDtls>
Presence: [0..1]
Definition: Party that acts on behalf of the buyer of securities when the buyer does not have a direct
relationship with the receiving agent.
ReceiversCustodianDetails <RcvrsCtdnDtls> contains the following
PartyIdentificationAndAccount235 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 3346
   AccountIdentification <AcctId> [0..1] Text 3346
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3346
52.4.5.10.28.7.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
52.4.5.10.28.7.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
52.4.5.10.28.7.1.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3346 May 2026
```

