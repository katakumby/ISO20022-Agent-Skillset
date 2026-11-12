---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.9 PartyIdentificationAndAccount197", "35.1.18.9.4 Nationality <Ntlty>"]
file_pages: [1674]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.9.4 Nationality <Ntlty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1674 to 1674.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1674

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.9.4  Nationality <Ntlty>
Presence: [0..1]
Definition: Nationality of the investor or country of incorporation (for a company).
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.18.9.5  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 2192
35.1.18.9.6  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 2191
35.1.18.9.7  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.9.8  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C5 "AdditonalDetailsGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1674 March 2026
```

