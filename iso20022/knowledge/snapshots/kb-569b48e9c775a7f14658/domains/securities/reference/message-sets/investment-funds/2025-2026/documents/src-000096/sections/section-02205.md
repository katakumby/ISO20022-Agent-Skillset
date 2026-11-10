---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.17 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "50.4.4.9.17.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [3101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.17.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3101 to 3101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3101

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
50.4.4.9.17.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C31 "ReceiversCustodianRule", C32 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3102
     PartyIdentification <PtyId> [1..1] ± 3102
     AccountIdentification <AcctId> [0..1] Text 3102
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3102
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3103
     PartyIdentification <PtyId> [1..1] ± 3103
     AccountIdentification <AcctId> [0..1] Text 3103
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3103
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3104
     PartyIdentification <PtyId> [1..1] ± 3104
     AccountIdentification <AcctId> [0..1] Text 3104
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3104
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3105
     PartyIdentification <PtyId> [1..1] ± 3105
     AccountIdentification <AcctId> [0..1] Text 3105
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3105
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3101 May 2026
```

