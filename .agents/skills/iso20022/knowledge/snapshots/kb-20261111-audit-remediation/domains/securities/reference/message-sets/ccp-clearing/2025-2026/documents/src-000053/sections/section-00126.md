---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.32 SettlementDetails <SttlmDtls>", "4.4.5.4.32.2 Depository <Dpstry>"]
file_pages: [167, 168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.32.2 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 167 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
SettlementAmount <SttlmAmt> contains the following elements (see AmountAndDirection27 on
page 379 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C1,
  'C7
379
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 380
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount   'C2,
  'C6
380
   ForeignExchangeDetails <FXDtls> [0..1] ± 381
4.4.5.4.32.2  Depository <Dpstry>
Presence: [0..1]
Definition: Place where settlement of the securities takes place.
Depository <Dpstry> contains one of the following elements (see PartyIdentification255Choice on
page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 454
Or   NameAndAddress <NmAndAdr> [1..1] ± 454
Or}   Country <Ctry> [1..1] CodeSet   'C5 454
4.4.5.4.33  ClearingDetails <ClrDtls>
Presence: [0..1]
Definition: Provides clearing details such as the non clearing member identification or the settlement
netting (or not) eligibility code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 167
```

## File page 168

```text
ClearingDetails <ClrDtls> contains the following Clearing8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 169
   ClearingSegment <ClrSgmt> [0..1] ± 170
   GuaranteedTrade <GrntedTrad> [0..1] Indicator 170
   TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  170
     TradeCounterpartyMemberIdentification
<TradCtrPtyMmbId>
[1..1] ± 172
     TradeCounterpartyClearingMemberIdentification
<TradCtrPtyClrMmbId>
[1..1] ± 172
     DeliveringParties <DlvrgPties> [0..1]  C8 173
       Depository <Dpstry> [1..1] ± 174
       Party1 <Pty1> [1..1]  175
         PartyIdentification <PtyId> [1..1] ± 175
         AccountIdentification <AcctId> [0..1] Text 176
         ProcessingIdentification <PrcgId> [0..1] Text 176
         ProcessingDate <PrcgDt> [0..1] ± 176
         SubAccount <SubAcct> [0..1]  176
           Identification <Id> [1..1] ± 177
           Name <Nm> [0..1] Text 177
           Characteristic <Chrtc> [0..1] Text 177
         ContactPerson <CtctPrsn> [0..1] ± 177
       Party2 <Pty2> [0..1]  178
         PartyIdentification <PtyId> [1..1] ± 178
         AccountIdentification <AcctId> [0..1] Text 179
         ProcessingIdentification <PrcgId> [0..1] Text 179
         ProcessingDate <PrcgDt> [0..1] ± 179
         SubAccount <SubAcct> [0..1]  179
           Identification <Id> [1..1] ± 180
           Name <Nm> [0..1] Text 180
           Characteristic <Chrtc> [0..1] Text 180
         ContactPerson <CtctPrsn> [0..1] ± 180
       SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 181
     ReceivingParties <RcvgPties> [0..1]  C9 181
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 168
```

