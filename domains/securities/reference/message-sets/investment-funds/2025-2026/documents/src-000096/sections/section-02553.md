---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.10 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "53.4.5.16.10.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [3595]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.10.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3595 to 3595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3595

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
53.4.5.16.10.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C33 "ReceiversCustodianRule", C34 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3596
     PartyIdentification <PtyId> [1..1] ± 3596
     AccountIdentification <AcctId> [0..1] Text 3596
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3596
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3597
     PartyIdentification <PtyId> [1..1] ± 3597
     AccountIdentification <AcctId> [0..1] Text 3597
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3597
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3598
     PartyIdentification <PtyId> [1..1] ± 3598
     AccountIdentification <AcctId> [0..1] Text 3598
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3598
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3599
     PartyIdentification <PtyId> [1..1] ± 3599
     AccountIdentification <AcctId> [0..1] Text 3599
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3599
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3595 May 2026
```

