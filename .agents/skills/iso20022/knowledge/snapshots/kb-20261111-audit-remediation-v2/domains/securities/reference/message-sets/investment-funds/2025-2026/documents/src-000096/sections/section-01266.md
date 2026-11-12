---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.16 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "41.4.4.8.16.7 ReceivingSideDetails <RcvgSdDtls>"]
file_pages: [1776]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.16.7 ReceivingSideDetails <RcvgSdDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1776 to 1776.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1776

```text
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
41.4.4.8.16.7  ReceivingSideDetails <RcvgSdDtls>
Presence: [1..1]
Definition: Chain of parties involved in the settlement of a transaction resulting in the movement of a
security from one account to another.
Impacted by: C31 "ReceiversCustodianRule", C32 "ReceiversIntermediary1DetailsRule"
ReceivingSideDetails <RcvgSdDtls> contains the following ReceivingPartiesAndAccount24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1777
     PartyIdentification <PtyId> [1..1] ± 1777
     AccountIdentification <AcctId> [0..1] Text 1777
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1777
   ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1778
     PartyIdentification <PtyId> [1..1] ± 1778
     AccountIdentification <AcctId> [0..1] Text 1778
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1778
   ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1779
     PartyIdentification <PtyId> [1..1] ± 1779
     AccountIdentification <AcctId> [0..1] Text 1779
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1779
   ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1780
     PartyIdentification <PtyId> [1..1] ± 1780
     AccountIdentification <AcctId> [0..1] Text 1780
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1780
Constraints
• ReceiversCustodianRule
If ReceiversIntermediary1Details is present, then ReceiversCustodianDetails must be present. If
ReceiversIntermediary1Details is not present, then ReceiversCustodianDetails is optional.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1776 May 2026
```

