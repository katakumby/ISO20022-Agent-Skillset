---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.14 SettlementParties <SttlmPties>", "11.4.6.2.14.1 DeliveringSettlementParties <DlvrgSttlmPties>", "11.4.6.2.14.1.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [354, 355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.14.1.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 354 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
ContactPerson <CtctPrsn> contains the following elements (see ContactIdentification2 on page 458
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 459
   GivenName <GvnNm> [0..1] Text 459
   Name <Nm> [1..1] Text 459
   PhoneNumber <PhneNb> [0..1] Text 459
   MobileNumber <MobNb> [0..1] Text 459
   FaxNumber <FaxNb> [0..1] Text 459
   EmailAddress <EmailAdr> [0..1] Text 459
11.4.6.2.14.1.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
11.4.6.2.14.2  ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Impacted by: C9 DepositoryGuideline
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 354
```

## File page 355

```text
ReceivingSettlementParties <RcvgSttlmPties> contains the following
ReceivingPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 356
   Party1 <Pty1> [1..1]  356
     PartyIdentification <PtyId> [1..1] ± 356
     AccountIdentification <AcctId> [0..1] Text 357
     ProcessingIdentification <PrcgId> [0..1] Text 357
     ProcessingDate <PrcgDt> [0..1] ± 357
     SubAccount <SubAcct> [0..1]  357
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
Constraints
• DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 355
```

