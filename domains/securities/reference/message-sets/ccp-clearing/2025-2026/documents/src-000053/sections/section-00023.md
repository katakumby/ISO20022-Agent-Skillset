---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.4 ReceivingParties <RcvgPties>", "2.4.5.4.4.2 Party1 <Pty1>", "2.4.5.4.4.2.2 AccountIdentification <AcctId>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.4.2.2 AccountIdentification <AcctId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

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
2.4.5.4.4.2.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: Max35Text on page 493
2.4.5.4.4.2.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Specifies the reference of the transaction at the party identified in the sequence.
Datatype: Max35Text on page 493
2.4.5.4.4.2.4  ProcessingDate <PrcgDt>
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
2.4.5.4.4.2.5  SubAccount <SubAcct>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 34
```

