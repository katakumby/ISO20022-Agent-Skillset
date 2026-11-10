---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.5 IndividualPerson32", "66.1.32.5.4 OtherIdentification <OthrId>", "66.1.32.5.4.1 Identification <Id>"]
file_pages: [5077]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.5.4.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5077 to 5077.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5077

```text
Definition: Alternative identification, for example, national registration identification number, passport
number, or an account number used to further identify the beneficial owner, for example, a Central
Provident Fund (CFP) account as required for Singapore.
OtherIdentification <OthrId> contains the following GenericIdentification164 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 5077
   IdentificationType <IdTp> [1..1]  5077
{Or     Code <Cd> [1..1] CodeSet 5077
Or}     Proprietary <Prtry> [1..1] ± 5078
   Issuer <Issr> [0..1] Text 5078
66.1.32.5.4.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 5403
66.1.32.5.4.2  IdentificationType <IdTp>
Presence: [1..1]
Definition: Specifies the nature of the identifier.
IdentificationType <IdTp> contains one of the following OtherIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5077
Or}   Proprietary <Prtry> [1..1] ± 5078
66.1.32.5.4.2.1  Code <Cd>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5077 May 2026
```

