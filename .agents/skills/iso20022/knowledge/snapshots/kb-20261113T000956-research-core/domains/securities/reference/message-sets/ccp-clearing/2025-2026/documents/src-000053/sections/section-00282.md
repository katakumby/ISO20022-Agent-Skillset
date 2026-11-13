---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.7 SettlementParties <SttlmPties>", "11.4.7.2 ReceivingSettlementParties <RcvgSttlmPties>", "11.4.7.2.1 Depository <Dpstry>"]
file_pages: [371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.7.2.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 371 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 371

```text
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
11.4.7.2.1  Depository <Dpstry>
Presence: [1..1]
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
11.4.7.2.2  Party1 <Pty1>
Presence: [1..1]
Definition: Party that, in a settlement chain interacts with the depository.
Party1 <Pty1> contains the following elements (see PartyIdentificationAndAccount228 on page 441 for
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
11.4.7.2.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 1.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 371
```

