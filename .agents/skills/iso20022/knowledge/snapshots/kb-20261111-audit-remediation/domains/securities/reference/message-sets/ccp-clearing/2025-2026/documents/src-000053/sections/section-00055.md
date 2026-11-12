---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.4 NonClearingMember <NonClrMmb>"]
file_pages: [75, 76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.4 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 75 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

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
3.4.4 NonClearingMember <NonClrMmb>
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
3.4.5 ClearingDetails <ClrDtls>
Presence: [0..1]
Definition: Provides clearing details such as the non clearing member identification or the settlement
netting (or not) eligibility code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 75
```

## File page 76

```text
ClearingDetails <ClrDtls> contains the following Clearing8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementNettingEligibleCode <SttlmNetgElgblCd> [1..1] CodeSet 77
   ClearingSegment <ClrSgmt> [0..1] ± 78
   GuaranteedTrade <GrntedTrad> [0..1] Indicator 78
   TradeCounterpartyIdentification <TradCtrPtyId> [0..1]  78
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 76
```

