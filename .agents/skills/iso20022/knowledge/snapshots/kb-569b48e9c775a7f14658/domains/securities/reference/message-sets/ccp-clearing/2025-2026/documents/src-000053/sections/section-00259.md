---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.14 SettlementParties <SttlmPties>", "11.4.6.2.14.1 DeliveringSettlementParties <DlvrgSttlmPties>"]
file_pages: [346, 347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.14.1 DeliveringSettlementParties <DlvrgSttlmPties>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 346 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] ± 358
         Name <Nm> [0..1] Text 358
         Characteristic <Chrtc> [0..1] Text 358
       ContactPerson <CtctPrsn> [0..1] ± 358
     Party2 <Pty2> [0..1]  359
       PartyIdentification <PtyId> [1..1] ± 359
       AccountIdentification <AcctId> [0..1] Text 360
       ProcessingIdentification <PrcgId> [0..1] Text 360
       ProcessingDate <PrcgDt> [0..1] ± 360
       SubAccount <SubAcct> [0..1]  360
         Identification <Id> [1..1] ± 361
         Name <Nm> [0..1] Text 361
         Characteristic <Chrtc> [0..1] Text 361
       ContactPerson <CtctPrsn> [0..1] ± 361
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 362
11.4.6.2.14.1  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Impacted by: C8 DepositoryGuideline
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 346
```

## File page 347

```text
DeliveringSettlementParties <DlvrgSttlmPties> contains the following
DeliveringPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Constraints
• DepositoryGuideline
(Rule)
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 347
```

