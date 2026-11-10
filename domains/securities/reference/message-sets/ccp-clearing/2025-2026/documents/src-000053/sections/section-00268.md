---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.14 SettlementParties <SttlmPties>", "11.4.6.2.14.2 ReceivingSettlementParties <RcvgSttlmPties>", "11.4.6.2.14.2.2 Party1 <Pty1>", "11.4.6.2.14.2.2.2 AccountIdentification <AcctId>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.14.2.2.2 AccountIdentification <AcctId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
PartyIdentification <PtyId> contains one of the following elements (see PartyIdentification254Choice
on page 455 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 455
Or   ProprietaryIdentification <PrtryId> [1..1] ± 456
Or}   NameAndAddress <NmAndAdr> [1..1]  456
     Name <Nm> [1..1] Text 456
     Address <Adr> [1..1] ± 456
11.4.6.2.14.2.2.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: Max35Text on page 493
11.4.6.2.14.2.2.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Specifies the reference of the transaction at the party identified in the sequence.
Datatype: Max35Text on page 493
11.4.6.2.14.2.2.4  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date and optionally the time, at which this transaction was processed by the party identified
in this sequence.
ProcessingDate <PrcgDt> contains one of the following elements (see DateAndDateTime2Choice on
page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
11.4.6.2.14.2.2.5  SubAccount <SubAcct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 357
```

