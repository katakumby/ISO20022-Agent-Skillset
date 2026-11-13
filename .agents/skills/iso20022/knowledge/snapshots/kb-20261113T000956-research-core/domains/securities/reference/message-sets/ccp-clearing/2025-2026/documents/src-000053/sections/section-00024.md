---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.4 ReceivingParties <RcvgPties>", "2.4.5.4.4.2 Party1 <Pty1>", "2.4.5.4.4.2.5 SubAccount <SubAcct>", "2.4.5.4.4.2.5.1 Identification <Id>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.4.2.5.1 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
SubAccount <SubAcct> contains the following SubAccount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 35
   Name <Nm> [0..1] Text 35
   Characteristic <Chrtc> [0..1] Text 35
2.4.5.4.4.2.5.1  Identification <Id>
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
2.4.5.4.4.2.5.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: Max35Text on page 493
2.4.5.4.4.2.5.3  Characteristic <Chrtc>
Presence: [0..1]
Definition: Specifies additional properties of the account.
Datatype: Max35Text on page 493
2.4.5.4.4.2.6  ContactPerson <CtctPrsn>
Presence: [0..1]
Definition: Contact person and contact information.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 35
```

