---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.2 ClearingSegment <ClrSgmt>"]
file_pages: [78, 79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.2 ClearingSegment <ClrSgmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 78 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
CodeName Name Definition
AGFS AggregationForSettlement Grouping of receipts/purchases to create
one settlement obligation, and the
grouping of deliveries/sales to create
one settlement obligation.
3.4.5.2  ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Note: This field allows clearing member firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, clearing member firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see
PartyIdentification253Choice on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
3.4.5.3  GuaranteedTrade <GrntedTrad>
Presence: [0..1]
Definition: Indicates if the position is guaranteed or non-guaranteed by the central counterparty, that is
whether the CCP has done the novation and then guarantees the trade, or not.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
3.4.5.4  TradeCounterpartyIdentification <TradCtrPtyId>
Presence: [0..1]
Definition: Whether the trades are guaranteed or not by the central counterparty (this is when the
central counterparty has not done the novation), provide details such as the trade counterparty member
identification or the trade counterparty clearing member identification.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 78
```

## File page 79

```text
TradeCounterpartyIdentification <TradCtrPtyId> contains the following NonGuaranteedTrade4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 80
   TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 80
   DeliveringParties <DlvrgPties> [0..1]  C8 81
     Depository <Dpstry> [1..1] ± 82
     Party1 <Pty1> [1..1]  83
       PartyIdentification <PtyId> [1..1] ± 83
       AccountIdentification <AcctId> [0..1] Text 84
       ProcessingIdentification <PrcgId> [0..1] Text 84
       ProcessingDate <PrcgDt> [0..1] ± 84
       SubAccount <SubAcct> [0..1]  84
         Identification <Id> [1..1] ± 85
         Name <Nm> [0..1] Text 85
         Characteristic <Chrtc> [0..1] Text 85
       ContactPerson <CtctPrsn> [0..1] ± 85
     Party2 <Pty2> [0..1]  86
       PartyIdentification <PtyId> [1..1] ± 86
       AccountIdentification <AcctId> [0..1] Text 87
       ProcessingIdentification <PrcgId> [0..1] Text 87
       ProcessingDate <PrcgDt> [0..1] ± 87
       SubAccount <SubAcct> [0..1]  87
         Identification <Id> [1..1] ± 88
         Name <Nm> [0..1] Text 88
         Characteristic <Chrtc> [0..1] Text 88
       ContactPerson <CtctPrsn> [0..1] ± 88
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 89
   ReceivingParties <RcvgPties> [0..1]  C9 89
     Depository <Dpstry> [1..1] ± 90
     Party1 <Pty1> [1..1]  91
       PartyIdentification <PtyId> [1..1] ± 91
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 79
```

