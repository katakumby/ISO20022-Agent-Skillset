---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "49.4.5.9.28.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [2860]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.28.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2860 to 2860.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2860

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
49.4.5.9.28.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C33 "ReceiversCustodianRule", C34 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2861
     PartyIdentification <PtyId> [1..1] ± 2861
     AccountIdentification <AcctId> [0..1] Text 2861
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2861
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2862
     PartyIdentification <PtyId> [1..1] ± 2862
     AccountIdentification <AcctId> [0..1] Text 2862
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2862
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2863
     PartyIdentification <PtyId> [1..1] ± 2863
     AccountIdentification <AcctId> [0..1] Text 2863
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2863
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2864
     PartyIdentification <PtyId> [1..1] ± 2864
     AccountIdentification <AcctId> [0..1] Text 2864
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2864
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2860 May 2026
```

