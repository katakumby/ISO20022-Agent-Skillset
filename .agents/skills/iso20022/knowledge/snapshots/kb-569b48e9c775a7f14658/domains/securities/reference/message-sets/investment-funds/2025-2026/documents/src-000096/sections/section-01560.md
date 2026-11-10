---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "44.4.4.9.16.1 SettlementDate <SttlmDt>"]
file_pages: [2189]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.16.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2189 to 2189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2189

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [1..1]  C11,
C12
2198
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2199
       PartyIdentification <PtyId> [1..1] ± 2199
       AccountIdentification <AcctId> [0..1] Text 2199
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2200
       PartyIdentification <PtyId> [1..1] ± 2200
       AccountIdentification <AcctId> [0..1] Text 2200
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2200
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2201
       PartyIdentification <PtyId> [1..1] ± 2201
       AccountIdentification <AcctId> [0..1] Text 2201
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2201
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2202
       PartyIdentification <PtyId> [1..1] ± 2202
       AccountIdentification <AcctId> [0..1] Text 2202
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2202
44.4.4.9.16.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
44.4.4.9.16.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2189 May 2026
```

