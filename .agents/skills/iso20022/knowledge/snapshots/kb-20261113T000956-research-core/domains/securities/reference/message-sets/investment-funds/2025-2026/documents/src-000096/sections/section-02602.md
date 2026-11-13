---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.9 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "53.4.5.17.9.1 SettlementDate <SttlmDt>"]
file_pages: [3659]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.9.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3659 to 3659.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3659

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C9, C10 3668
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3669
       PartyIdentification <PtyId> [1..1] ± 3669
       AccountIdentification <AcctId> [0..1] Text 3669
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3670
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3670
       PartyIdentification <PtyId> [1..1] ± 3670
       AccountIdentification <AcctId> [0..1] Text 3670
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3670
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3671
       PartyIdentification <PtyId> [1..1] ± 3671
       AccountIdentification <AcctId> [0..1] Text 3671
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3671
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3672
       PartyIdentification <PtyId> [1..1] ± 3672
       AccountIdentification <AcctId> [0..1] Text 3672
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3672
53.4.5.17.9.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
53.4.5.17.9.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3659 May 2026
```

