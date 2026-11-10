---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "47.4.4.8.17.1 SettlementDate <SttlmDt>"]
file_pages: [2617]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.17.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2617 to 2617.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2617

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
2626
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2627
       PartyIdentification <PtyId> [1..1] ± 2627
       AccountIdentification <AcctId> [0..1] Text 2627
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2628
       PartyIdentification <PtyId> [1..1] ± 2628
       AccountIdentification <AcctId> [0..1] Text 2628
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2628
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2629
       PartyIdentification <PtyId> [1..1] ± 2629
       AccountIdentification <AcctId> [0..1] Text 2629
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2629
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2630
       PartyIdentification <PtyId> [1..1] ± 2630
       AccountIdentification <AcctId> [0..1] Text 2630
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2630
47.4.4.8.17.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
47.4.4.8.17.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2617 May 2026
```

