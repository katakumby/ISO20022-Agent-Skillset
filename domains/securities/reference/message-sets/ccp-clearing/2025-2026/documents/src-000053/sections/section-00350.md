---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.1 PartyIdentificationAndAccount228", "12.1.14.1.5 SubAccountDetails <SubAcctDtls>"]
file_pages: [443]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.1.5 SubAccountDetails <SubAcctDtls>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 443 to 443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 443

```text
ProcessingDate <PrcgDt> contains one of the following elements (see DateAndDateTime2Choice on
page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
12.1.14.1.5  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
SubAccountDetails <SubAcctDtls> contains the following SubAccount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 443
   Name <Nm> [0..1] Text 443
   Characteristic <Chrtc> [0..1] Text 443
12.1.14.1.5.1  Identification <Id>
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
12.1.14.1.5.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: Max35Text on page 493
12.1.14.1.5.3  Characteristic <Chrtc>
Presence: [0..1]
Definition: Specifies additional properties of the account.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 443
```

