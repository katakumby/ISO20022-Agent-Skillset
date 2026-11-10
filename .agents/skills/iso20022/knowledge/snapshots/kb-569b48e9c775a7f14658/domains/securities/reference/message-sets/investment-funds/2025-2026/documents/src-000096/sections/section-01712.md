---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.28 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "46.4.5.10.28.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [2402]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.28.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2402 to 2402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2402

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
46.4.5.10.28.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C33 "ReceiversCustodianRule", C34 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2403
     PartyIdentification <PtyId> [1..1] ± 2403
     AccountIdentification <AcctId> [0..1] Text 2403
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2403
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2404
     PartyIdentification <PtyId> [1..1] ± 2404
     AccountIdentification <AcctId> [0..1] Text 2404
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2404
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2405
     PartyIdentification <PtyId> [1..1] ± 2405
     AccountIdentification <AcctId> [0..1] Text 2405
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2405
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2406
     PartyIdentification <PtyId> [1..1] ± 2406
     AccountIdentification <AcctId> [0..1] Text 2406
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2406
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2402 May 2026
```

