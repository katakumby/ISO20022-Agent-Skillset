---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.10 PartyIdentification255Choice"]
file_pages: [454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.10 PartyIdentification255Choice

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 454 to 454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 454

```text
12.1.14.10  PartyIdentification255Choice
Definition: Unique and unambiguous way to identify an organisation using a choice between a BIC or
the name and addres or the country code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 454
Or   NameAndAddress <NmAndAdr> [1..1] ± 454
Or}   Country <Ctry> [1..1] CodeSet   'C5 454
12.1.14.10.1  BIC <BIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by:   'C3 AnyBIC  '
Datatype: AnyBICDec2014Identifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
12.1.14.10.2  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation, using the name and address.
NameAndAddress <NmAndAdr> contains the following elements (see NameAndAddress5 on
page 460 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 460
   Address <Adr> [0..1] ± 460
12.1.14.10.3  Country <Ctry>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation using the country code, using the
country code.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 454
```

