---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "41.4.4.8.16.1 SettlementDate <SttlmDt>"]
file_pages: [1772]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.16.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1772 to 1772.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1772

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C12
1781
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1782
       PartyIdentification <PtyId> [1..1] ± 1782
       AccountIdentification <AcctId> [0..1] Text 1782
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1783
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1783
       PartyIdentification <PtyId> [1..1] ± 1783
       AccountIdentification <AcctId> [0..1] Text 1783
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1783
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1784
       PartyIdentification <PtyId> [1..1] ± 1784
       AccountIdentification <AcctId> [0..1] Text 1784
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1784
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1785
       PartyIdentification <PtyId> [1..1] ± 1785
       AccountIdentification <AcctId> [0..1] Text 1785
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1785
41.4.4.8.16.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
41.4.4.8.16.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1772 May 2026
```

