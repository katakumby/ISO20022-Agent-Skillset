---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "49.4.5.9.28.1 SettlementDate <SttlmDt>"]
file_pages: [2856]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.28.1 SettlementDate <SttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2856 to 2856.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2856

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSideDetails <DlvrgSdDtls> [1..1]  C12,
C13
2865
     DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2866
       PartyIdentification <PtyId> [1..1] ± 2866
       AccountIdentification <AcctId> [0..1] Text 2866
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2867
     DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2867
       PartyIdentification <PtyId> [1..1] ± 2867
       AccountIdentification <AcctId> [0..1] Text 2867
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2867
     DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2868
       PartyIdentification <PtyId> [1..1] ± 2868
       AccountIdentification <AcctId> [0..1] Text 2868
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2868
     DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2869
       PartyIdentification <PtyId> [1..1] ± 2869
       AccountIdentification <AcctId> [0..1] Text 2869
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2869
49.4.5.9.28.1  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be delivered or received.
Datatype: "ISODate" on page 5388
49.4.5.9.28.2  SettlementPlace <SttlmPlc>
Presence: [1..1]
Definition: Place where the settlement of the transaction will take place. In the context of investment
funds, the place of settlement is the transfer agent, a Central Securities Depository (CSD) or an
International Central Securities Depository (ICSD).
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2856 May 2026
```

