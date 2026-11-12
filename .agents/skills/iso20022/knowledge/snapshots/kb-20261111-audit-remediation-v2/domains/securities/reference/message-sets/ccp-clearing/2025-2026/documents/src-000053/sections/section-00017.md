---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.3 DeliveringParties <DlvrgPties>", "2.4.5.4.3.3 Party2 <Pty2>"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.3.3 Party2 <Pty2>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

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
2.4.5.4.3.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 1.
Party2 <Pty2> contains the following PartyIdentificationAndAccount229 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 28
   AccountIdentification <AcctId> [0..1] Text 29
   ProcessingIdentification <PrcgId> [0..1] Text 29
   ProcessingDate <PrcgDt> [0..1] ± 29
   SubAccount <SubAcct> [0..1]  29
     Identification <Id> [1..1] ± 30
     Name <Nm> [0..1] Text 30
     Characteristic <Chrtc> [0..1] Text 30
   ContactPerson <CtctPrsn> [0..1] ± 30
2.4.5.4.3.3.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 28
```

