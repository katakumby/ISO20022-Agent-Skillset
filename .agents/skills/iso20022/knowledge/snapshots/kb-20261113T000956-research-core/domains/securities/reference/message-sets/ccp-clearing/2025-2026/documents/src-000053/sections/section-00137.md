---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.33 ClearingDetails <ClrDtls>", "4.4.5.4.33.4 TradeCounterpartyIdentification <TradCtrPtyId>", "4.4.5.4.33.4.3 DeliveringParties <DlvrgPties>", "4.4.5.4.33.4.3.3 Party2 <Pty2>", "4.4.5.4.33.4.3.3.5 SubAccount <SubAcct>", "4.4.5.4.33.4.3.3.5.1 Identification <Id>"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.33.4.3.3.5.1 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
SubAccount <SubAcct> contains the following SubAccount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 180
   Name <Nm> [0..1] Text 180
   Characteristic <Chrtc> [0..1] Text 180
4.4.5.4.33.4.3.3.5.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see AccountIdentification26 on page 375 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1]  376
     Identification <Id> [1..1] Text 376
4.4.5.4.33.4.3.3.5.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: Max35Text on page 493
4.4.5.4.33.4.3.3.5.3  Characteristic <Chrtc>
Presence: [0..1]
Definition: Specifies additional properties of the account.
Datatype: Max35Text on page 493
4.4.5.4.33.4.3.3.6  ContactPerson <CtctPrsn>
Presence: [0..1]
Definition: Contact person and contact information.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 180
```

