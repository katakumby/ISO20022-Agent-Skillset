---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.5 PartyIdentificationAndAccount197", "82.1.20.5.2 LEI <LEI>"]
file_pages: [3062]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.5.2 LEI <LEI>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3062 to 3062.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3062

```text
82.1.20.5.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 3322
82.1.20.5.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 3058 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 3058
   Country <Ctry> [1..1] CodeSet C3 3058
   AlternateIdentification <AltrnId> [1..1] Text 3058
82.1.20.5.4  Nationality <Ntlty>
Presence: [0..1]
Definition: Nationality of the investor or country of incorporation (for a company).
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.20.5.5  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 3328
82.1.20.5.6  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 3326
82.1.20.5.7  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3062 August 2026
```

