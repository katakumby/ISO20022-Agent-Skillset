---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.2 ClearingSegment <ClrSgmt>"]
file_pages: [20, 21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.2 ClearingSegment <ClrSgmt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 20 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 20

```text
CodeName Name Definition
AGFS AggregationForSettlement Grouping of receipts/purchases to create
one settlement obligation, and the
grouping of deliveries/sales to create
one settlement obligation.
2.4.5.2  ClearingSegment <ClrSgmt>
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
2.4.5.3  GuaranteedTrade <GrntedTrad>
Presence: [0..1]
Definition: Indicates if the position is guaranteed or non-guaranteed by the central counterparty, that is
whether the CCP has done the novation and then guarantees the trade, or not.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
2.4.5.4  TradeCounterpartyIdentification <TradCtrPtyId>
Presence: [0..1]
Definition: Whether the trades are guaranteed or not by the central counterparty (this is when the
central counterparty has not done the novation), provide details such as the trade counterparty member
identification or the trade counterparty clearing member identification.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 20
```

## File page 21

```text
TradeCounterpartyIdentification <TradCtrPtyId> contains the following NonGuaranteedTrade4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 22
   TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 22
   DeliveringParties <DlvrgPties> [0..1]  C8 23
     Depository <Dpstry> [1..1] ± 24
     Party1 <Pty1> [1..1]  25
       PartyIdentification <PtyId> [1..1] ± 25
       AccountIdentification <AcctId> [0..1] Text 26
       ProcessingIdentification <PrcgId> [0..1] Text 26
       ProcessingDate <PrcgDt> [0..1] ± 26
       SubAccount <SubAcct> [0..1]  26
         Identification <Id> [1..1] ± 27
         Name <Nm> [0..1] Text 27
         Characteristic <Chrtc> [0..1] Text 27
       ContactPerson <CtctPrsn> [0..1] ± 27
     Party2 <Pty2> [0..1]  28
       PartyIdentification <PtyId> [1..1] ± 28
       AccountIdentification <AcctId> [0..1] Text 29
       ProcessingIdentification <PrcgId> [0..1] Text 29
       ProcessingDate <PrcgDt> [0..1] ± 29
       SubAccount <SubAcct> [0..1]  29
         Identification <Id> [1..1] ± 30
         Name <Nm> [0..1] Text 30
         Characteristic <Chrtc> [0..1] Text 30
       ContactPerson <CtctPrsn> [0..1] ± 30
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 31
   ReceivingParties <RcvgPties> [0..1]  C9 31
     Depository <Dpstry> [1..1] ± 32
     Party1 <Pty1> [1..1]  33
       PartyIdentification <PtyId> [1..1] ± 33
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 21
```

