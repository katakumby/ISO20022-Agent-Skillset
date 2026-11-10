---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.3 AlternatePartyIdentification4", "12.1.14.3.3 AlternateIdentification <AltrnId>"]
file_pages: [446]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.3.3 AlternateIdentification <AltrnId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 446 to 446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
Constraints
• Country
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
12.1.14.3.3  AlternateIdentification <AltrnId>
Presence: [1..1]
Definition: Alternate identification for a party.
Datatype: Max35Text on page 493
12.1.14.4  PartyIdentification34Choice
Definition: Unique and unambiguous way to identify an organisation using a choice between a BIC or
the name and addres or the country code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 446
Or   NameAndAddress <NmAndAdr> [1..1] ± 447
Or}   Country <Ctry> [1..1] CodeSet   'C5 447
12.1.14.4.1  BIC <BIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by:   'C4 AnyBIC  '
Datatype: AnyBICIdentifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 446
```

