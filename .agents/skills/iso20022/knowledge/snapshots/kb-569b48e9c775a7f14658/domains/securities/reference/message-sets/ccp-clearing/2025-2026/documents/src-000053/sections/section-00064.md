---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "3.4.5.4.3 DeliveringParties <DlvrgPties>", "3.4.5.4.3.3 Party2 <Pty2>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.4.3.3 Party2 <Pty2>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

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
3.4.5.4.3.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 1.
Party2 <Pty2> contains the following PartyIdentificationAndAccount229 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 86
   AccountIdentification <AcctId> [0..1] Text 87
   ProcessingIdentification <PrcgId> [0..1] Text 87
   ProcessingDate <PrcgDt> [0..1] ± 87
   SubAccount <SubAcct> [0..1]  87
     Identification <Id> [1..1] ± 88
     Name <Nm> [0..1] Text 88
     Characteristic <Chrtc> [0..1] Text 88
   ContactPerson <CtctPrsn> [0..1] ± 88
3.4.5.4.3.3.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 86
```

