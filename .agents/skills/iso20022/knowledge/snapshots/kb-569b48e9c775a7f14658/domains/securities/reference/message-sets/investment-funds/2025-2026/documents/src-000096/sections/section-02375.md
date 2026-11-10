---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "52.4.5.10.28.1 SettlementDate <SttlmDt>"]
file_pages: [3341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3341 to 3341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3341

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [1..1]  C13,
C14
3350
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3351
       PartyIdentification <PtyId> [1..1] ± 3351
       AccountIdentification <AcctId> [0..1] Text 3351
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3352
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3352
       PartyIdentification <PtyId> [1..1] ± 3352
       AccountIdentification <AcctId> [0..1] Text 3352
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3352
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3353
       PartyIdentification <PtyId> [1..1] ± 3353
       AccountIdentification <AcctId> [0..1] Text 3353
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3353
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3354
       PartyIdentification <PtyId> [1..1] ± 3354
       AccountIdentification <AcctId> [0..1] Text 3354
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3354
52.4.5.10.28.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
52.4.5.10.28.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3341 May 2026
```

