---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.7.14 SettlementPartiesDetails <SttlmPtiesDtls>", "26.4.7.14.2 SettlementTransactionCondition <SttlmTxCond>"]
file_pages: [578, 579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.7.14.2 SettlementTransactionCondition <SttlmTxCond>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 578 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 578

```text
Definition: Condition under which the order/trade is to be/was executed. This may be required for
settlement through T2S.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition8Choice" on page 5254 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5254
Or}   Proprietary <Prtry> [1..1] ± 5255
26.4.7.14.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be settled. This may be required for settlement
through T2S.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition30Choice" on page 5255 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5255
Or}   Proprietary <Prtry> [1..1] ± 5255
26.4.7.14.3  SecuritiesSettlementSystemIdentification <SctiesSttlmSysId>
Presence: [0..1]
Definition: Identification of a specific system or set of rules and/or processes to be applied at the
settlement place.
Datatype: "Max35Text" on page 5403
26.4.7.14.4  DeliveringSideDetails <DlvrgSdDtls>
Presence: [0..1]
Definition: Chain of delivering settlement parties.
Impacted by: C7 "BookTransferGuideline", C11 "DepositoryGuideline", C26 "Party2PresenceRule", C27
"Party3PresenceRule", C28 "Party4PresenceRule", C29 "Party5PresenceRule", C33
"SettlementChainGuideline"
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 578 May 2026
```

## File page 579

```text
DeliveringSideDetails <DlvrgSdDtls> contains the following SettlementParties131 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 580
   Party1 <Pty1> [0..1] ± 581
   Party2 <Pty2> [0..1] ± 581
   Party3 <Pty3> [0..1] ± 581
   Party4 <Pty4> [0..1] ± 582
   Party5 <Pty5> [0..1] ± 582
Constraints
• BookTransferGuideline
In the case of an own account internal transfer, the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 579 May 2026
```

