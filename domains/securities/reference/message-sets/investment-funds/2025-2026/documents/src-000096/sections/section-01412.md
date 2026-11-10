---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.29 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "43.4.5.9.29.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [1982]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.29.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1982 to 1982.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1982

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
43.4.5.9.29.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C33 "ReceiversCustodianRule", C34 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1983
     PartyIdentification <PtyId> [1..1] ± 1983
     AccountIdentification <AcctId> [0..1] Text 1983
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1983
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1984
     PartyIdentification <PtyId> [1..1] ± 1984
     AccountIdentification <AcctId> [0..1] Text 1984
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1984
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1985
     PartyIdentification <PtyId> [1..1] ± 1985
     AccountIdentification <AcctId> [0..1] Text 1985
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1985
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1986
     PartyIdentification <PtyId> [1..1] ± 1986
     AccountIdentification <AcctId> [0..1] Text 1986
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1986
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1982 May 2026
```

