---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "47.4.4.8.17.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [2621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.17.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2621 to 2621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2621

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
47.4.4.8.17.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C31 "ReceiversCustodianRule", C32 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2622
     PartyIdentification <PtyId> [1..1] ± 2622
     AccountIdentification <AcctId> [0..1] Text 2622
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2622
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2623
     PartyIdentification <PtyId> [1..1] ± 2623
     AccountIdentification <AcctId> [0..1] Text 2623
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2623
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2624
     PartyIdentification <PtyId> [1..1] ± 2624
     AccountIdentification <AcctId> [0..1] Text 2624
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2624
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2625
     PartyIdentification <PtyId> [1..1] ± 2625
     AccountIdentification <AcctId> [0..1] Text 2625
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2625
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2621 May 2026
```

