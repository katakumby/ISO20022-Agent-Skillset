---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.18 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "55.4.5.20.18.1 SettlementDate <SttlmDt>"]
file_pages: [3972]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.18.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3972 to 3972.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3972

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [1..1]  C10,
C11
3981
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3982
       PartyIdentification <PtyId> [1..1] ± 3982
       AccountIdentification <AcctId> [0..1] Text 3982
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3983
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3983
       PartyIdentification <PtyId> [1..1] ± 3983
       AccountIdentification <AcctId> [0..1] Text 3983
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3983
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3984
       PartyIdentification <PtyId> [1..1] ± 3984
       AccountIdentification <AcctId> [0..1] Text 3984
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3984
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3985
       PartyIdentification <PtyId> [1..1] ± 3985
       AccountIdentification <AcctId> [0..1] Text 3985
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3985
55.4.5.20.18.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
55.4.5.20.18.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3972 May 2026
```

