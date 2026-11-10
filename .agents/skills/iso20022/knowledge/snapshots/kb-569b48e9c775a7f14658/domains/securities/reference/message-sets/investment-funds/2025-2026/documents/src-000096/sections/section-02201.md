---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "50.4.4.9.17.1 SettlementDate <SttlmDt>"]
file_pages: [3097]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.17.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3097 to 3097.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3097

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
3106
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3107
       PartyIdentification <PtyId> [1..1] ± 3107
       AccountIdentification <AcctId> [0..1] Text 3107
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3108
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3108
       PartyIdentification <PtyId> [1..1] ± 3108
       AccountIdentification <AcctId> [0..1] Text 3108
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3108
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3109
       PartyIdentification <PtyId> [1..1] ± 3109
       AccountIdentification <AcctId> [0..1] Text 3109
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3109
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3110
       PartyIdentification <PtyId> [1..1] ± 3110
       AccountIdentification <AcctId> [0..1] Text 3110
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3110
50.4.4.9.17.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
50.4.4.9.17.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3097 May 2026
```

