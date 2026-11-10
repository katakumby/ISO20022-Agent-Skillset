---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.8 GenericIdentification81", "66.1.23.8.1 Identification <Id>"]
file_pages: [4544]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.8.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4544 to 4544.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4544

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4544
   IdentificationType <IdTp> [1..1]  4544
{Or     Code <Cd> [1..1] CodeSet 4544
Or}     Proprietary <Prtry> [1..1] ± 4545
66.1.23.8.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party, such as a tax or social security identifier.
Datatype: "Max35Text" on page 5403
66.1.23.8.2  IdentificationType <IdTp>
Presence: [1..1]
Definition: Type of identification.
IdentificationType <IdTp> contains one of the following OtherIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4544
Or}   Proprietary <Prtry> [1..1] ± 4545
66.1.23.8.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification expressed as a code.
Datatype: "PartyIdentificationType7Code" on page 5336
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
IDCD IdentityCardNumber Number assigned by a national authority
to an identity card.
NRIN NationalRegistrationIdentificationNumber National registration identification
number. In Singapore this is known as
the NRIC.
OTHR Other Another type of identification type.
PASS PassportNumber Number assigned by a passport
authority to a passport.
POCD PostOfficeCardNumber Post office card number as assigned by
a national post office.
SOCS SocialSecurityNumber Number assigned by a social security
agency.
SRSA SRSAccountNumber Supplementary retirement scheme
account number.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4544 May 2026
```

