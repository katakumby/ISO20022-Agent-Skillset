---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.29 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "43.4.5.9.29.1 SettlementDate <SttlmDt>"]
file_pages: [1978]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.29.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1978 to 1978.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1978

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C13
1987
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  1988
       PartyIdentification <PtyId> [1..1] ± 1988
       AccountIdentification <AcctId> [0..1] Text 1988
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  1989
       PartyIdentification <PtyId> [1..1] ± 1989
       AccountIdentification <AcctId> [0..1] Text 1989
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1989
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  1990
       PartyIdentification <PtyId> [1..1] ± 1990
       AccountIdentification <AcctId> [0..1] Text 1990
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1990
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  1991
       PartyIdentification <PtyId> [1..1] ± 1991
       AccountIdentification <AcctId> [0..1] Text 1991
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1991
43.4.5.9.29.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
43.4.5.9.29.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1978 May 2026
```

