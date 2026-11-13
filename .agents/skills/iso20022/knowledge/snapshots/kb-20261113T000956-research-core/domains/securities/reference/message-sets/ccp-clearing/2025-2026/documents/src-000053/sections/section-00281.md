---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.7 SettlementParties <SttlmPties>", "11.4.7.1 DeliveringSettlementParties <DlvrgSttlmPties>", "11.4.7.1.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [370]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.7.1.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 370 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
Party2 <Pty2> contains the following elements (see PartyIdentificationAndAccount228 on page 441 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 442
   AccountIdentification <AcctId> [0..1] Text 442
   ProcessingIdentification <PrcgId> [0..1] Text 442
   ProcessingDate <PrcgDt> [0..1] ± 442
   SubAccountDetails <SubAcctDtls> [0..1]  443
     Identification <Id> [1..1] ± 443
     Name <Nm> [0..1] Text 443
     Characteristic <Chrtc> [0..1] Text 443
   ContactPerson <CtctPrsn> [0..1] ± 444
11.4.7.1.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
11.4.7.2  ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Impacted by: C11 DepositoryGuideline
ReceivingSettlementParties <RcvgSttlmPties> contains the following
ReceivingPartiesAndAccount21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 371
   Party1 <Pty1> [1..1] ± 371
   Party2 <Pty2> [0..1] ± 371
   SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 372
Constraints
• DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 370
```

