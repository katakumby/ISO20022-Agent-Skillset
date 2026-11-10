---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.4 ReceivingParties <RcvgPties>", "2.4.5.4.4.2 Party1 <Pty1>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.4.2 Party1 <Pty1>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments.
Depository <Dpstry> contains one of the following elements (see PartyIdentification255Choice on
page 454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 454
Or   NameAndAddress <NmAndAdr> [1..1] ± 454
Or}   Country <Ctry> [1..1] CodeSet   'C5 454
2.4.5.4.4.2  Party1 <Pty1>
Presence: [1..1]
Definition: Party that, in a settlement chain interacts with the depository.
Party1 <Pty1> contains the following PartyIdentificationAndAccount229 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 33
   AccountIdentification <AcctId> [0..1] Text 34
   ProcessingIdentification <PrcgId> [0..1] Text 34
   ProcessingDate <PrcgDt> [0..1] ± 34
   SubAccount <SubAcct> [0..1]  34
     Identification <Id> [1..1] ± 35
     Name <Nm> [0..1] Text 35
     Characteristic <Chrtc> [0..1] Text 35
   ContactPerson <CtctPrsn> [0..1] ± 35
2.4.5.4.4.2.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 33
```

