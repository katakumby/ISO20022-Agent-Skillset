---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.14 SettlementParties <SttlmPties>"]
file_pages: [344, 345]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.14 SettlementParties <SttlmPties>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 344 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
11.4.6.2.14  SettlementParties <SttlmPties>
Presence: [0..1]
Definition: Provides details on the parties that are part of the settlement chain.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 344
```

## File page 345

```text
SettlementParties <SttlmPties> contains one of the following SettlementParties38Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DeliveringSettlementParties <DlvrgSttlmPties> [0..1]  C8 346
     Depository <Dpstry> [1..1] ± 348
     Party1 <Pty1> [1..1]  348
       PartyIdentification <PtyId> [1..1] ± 348
       AccountIdentification <AcctId> [0..1] Text 349
       ProcessingIdentification <PrcgId> [0..1] Text 349
       ProcessingDate <PrcgDt> [0..1] ± 349
       SubAccount <SubAcct> [0..1]  349
         Identification <Id> [1..1] ± 350
         Name <Nm> [0..1] Text 350
         Characteristic <Chrtc> [0..1] Text 350
       ContactPerson <CtctPrsn> [0..1] ± 350
     Party2 <Pty2> [0..1]  351
       PartyIdentification <PtyId> [1..1] ± 351
       AccountIdentification <AcctId> [0..1] Text 352
       ProcessingIdentification <PrcgId> [0..1] Text 352
       ProcessingDate <PrcgDt> [0..1] ± 352
       SubAccount <SubAcct> [0..1]  352
         Identification <Id> [1..1] ± 353
         Name <Nm> [0..1] Text 353
         Characteristic <Chrtc> [0..1] Text 353
       ContactPerson <CtctPrsn> [0..1] ± 353
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 354
Or}   ReceivingSettlementParties <RcvgSttlmPties> [0..1]  C9 354
     Depository <Dpstry> [1..1] ± 356
     Party1 <Pty1> [1..1]  356
       PartyIdentification <PtyId> [1..1] ± 356
       AccountIdentification <AcctId> [0..1] Text 357
       ProcessingIdentification <PrcgId> [0..1] Text 357
       ProcessingDate <PrcgDt> [0..1] ± 357
       SubAccount <SubAcct> [0..1]  357
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 345
```

