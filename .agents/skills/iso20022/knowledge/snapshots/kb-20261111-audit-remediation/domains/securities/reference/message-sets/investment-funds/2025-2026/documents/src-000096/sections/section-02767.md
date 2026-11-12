---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.20 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "55.4.5.19.20.1 SettlementDate <SttlmDt>"]
file_pages: [3900]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.20.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3900 to 3900.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3900

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C10,
C11
3909
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3910
       PartyIdentification <PtyId> [1..1] ± 3910
       AccountIdentification <AcctId> [0..1] Text 3910
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3911
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3911
       PartyIdentification <PtyId> [1..1] ± 3911
       AccountIdentification <AcctId> [0..1] Text 3911
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3911
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3912
       PartyIdentification <PtyId> [1..1] ± 3912
       AccountIdentification <AcctId> [0..1] Text 3912
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3912
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3913
       PartyIdentification <PtyId> [1..1] ± 3913
       AccountIdentification <AcctId> [0..1] Text 3913
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3913
55.4.5.19.20.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
55.4.5.19.20.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3900 May 2026
```

