---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.20 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "55.4.5.19.20.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [3904]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.20.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3904 to 3904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3904

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
55.4.5.19.20.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C32 "ReceiversCustodianRule", C33 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3905
     PartyIdentification <PtyId> [1..1] ± 3905
     AccountIdentification <AcctId> [0..1] Text 3905
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3905
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3906
     PartyIdentification <PtyId> [1..1] ± 3906
     AccountIdentification <AcctId> [0..1] Text 3906
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3906
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3907
     PartyIdentification <PtyId> [1..1] ± 3907
     AccountIdentification <AcctId> [0..1] Text 3907
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3907
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3908
     PartyIdentification <PtyId> [1..1] ± 3908
     AccountIdentification <AcctId> [0..1] Text 3908
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3908
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3904 May 2026
```

