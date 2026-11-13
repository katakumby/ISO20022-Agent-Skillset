---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.4 NonClearingMember <NonClrMmb>"]
file_pages: [17, 18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.4 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 17 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Definition: An account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
DeliveryAccount <DlvryAcct> contains the following elements (see SecuritiesAccount19 on page 375
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
2.4.4 NonClearingMember <NonClrMmb>
Presence: [0..1]
Definition: Provides details about the non clearing member identification and account.
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount227 on page 457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 457
   AlternateIdentification <AltrnId> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C3 457
   ClearingAccount <ClrAcct> [0..1] ± 458
2.4.5 ClearingDetails <ClrDtls>
Presence: [0..1]
Definition: Provides clearing details such as the settlement netting (or not) eligibility code or the clearing
segment.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 17
```

## File page 18

```text
ClearingDetails <ClrDtls> contains the following Clearing8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 19
   ClearingSegment <ClrSgmt> [0..1] ± 20
   GuaranteedTrade <GrntedTrad> [0..1] Indicator 20
   TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  20
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 18
```

