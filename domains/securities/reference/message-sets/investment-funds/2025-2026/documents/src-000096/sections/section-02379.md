---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "52.4.5.10.28.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [3345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.28.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3345 to 3345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3345

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
52.4.5.10.28.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C36 "ReceiversCustodianRule", C37 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3346
     PartyIdentification <PtyId> [1..1] ± 3346
     AccountIdentification <AcctId> [0..1] Text 3346
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3346
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3347
     PartyIdentification <PtyId> [1..1] ± 3347
     AccountIdentification <AcctId> [0..1] Text 3347
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3347
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3348
     PartyIdentification <PtyId> [1..1] ± 3348
     AccountIdentification <AcctId> [0..1] Text 3348
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3348
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3349
     PartyIdentification <PtyId> [1..1] ± 3349
     AccountIdentification <AcctId> [0..1] Text 3349
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3349
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3345 May 2026
```

