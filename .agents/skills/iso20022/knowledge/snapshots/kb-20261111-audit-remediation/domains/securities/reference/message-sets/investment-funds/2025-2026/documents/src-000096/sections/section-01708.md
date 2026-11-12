---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "46.4.5.10.28.1 SettlementDate <SttlmDt>"]
file_pages: [2398]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.28.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2398 to 2398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2398

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C13
2407
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2408
       PartyIdentification <PtyId> [1..1] ± 2408
       AccountIdentification <AcctId> [0..1] Text 2408
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2409
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2409
       PartyIdentification <PtyId> [1..1] ± 2409
       AccountIdentification <AcctId> [0..1] Text 2409
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2409
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2410
       PartyIdentification <PtyId> [1..1] ± 2410
       AccountIdentification <AcctId> [0..1] Text 2410
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2410
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2411
       PartyIdentification <PtyId> [1..1] ± 2411
       AccountIdentification <AcctId> [0..1] Text 2411
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2411
46.4.5.10.28.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
46.4.5.10.28.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2398 May 2026
```

