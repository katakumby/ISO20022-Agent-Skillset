---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.5 PartyIdentificationAndAccount197", "7.1.19.5.4 Nationality <Ntlty>"]
file_pages: [416]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.5.4 Nationality <Ntlty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 416 to 416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 411
   Country <Ctry> [1..1] CodeSet C3 412
   AlternateIdentification <AltrnId> [1..1] Text 412
7.1.19.5.4  Nationality <Ntlty>
Presence: [0..1]
Definition: Nationality of the investor or country of incorporation (for a company).
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.19.5.5  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 557
7.1.19.5.6  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 556
7.1.19.5.7  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 557
7.1.19.5.8  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C1 "AdditonalDetailsGuideline"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 416 March 2026
```

