---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "44.4.4.9.16.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [2193]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.16.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2193 to 2193.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2193

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
44.4.4.9.16.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C31 "ReceiversCustodianRule", C32 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2194
     PartyIdentification <PtyId> [1..1] ± 2194
     AccountIdentification <AcctId> [0..1] Text 2194
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2194
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2195
     PartyIdentification <PtyId> [1..1] ± 2195
     AccountIdentification <AcctId> [0..1] Text 2195
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2195
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2196
     PartyIdentification <PtyId> [1..1] ± 2196
     AccountIdentification <AcctId> [0..1] Text 2196
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2196
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2197
     PartyIdentification <PtyId> [1..1] ± 2197
     AccountIdentification <AcctId> [0..1] Text 2197
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2197
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2193 May 2026
```

